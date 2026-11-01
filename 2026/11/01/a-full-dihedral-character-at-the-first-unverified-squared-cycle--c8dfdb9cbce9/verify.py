"""Exact reproducible certificate for a squared-cycle cut complex.

Requires only Python 3 standard library. All integer computations are exact.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from math import comb

N = 21
K = 16
U = (1 << N) - 1


def vertices(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def boundary(mask):
    return [(mask ^ (1 << i), -1 if j % 2 else 1)
            for j, i in enumerate(vertices(mask))]


def graph():
    return tuple(sum(1 << j for j in range(N)
                     if 0 < min((i - j) % N, (j - i) % N) <= 2)
                 for i in range(N))


ADJ = graph()


def connected(mask):
    seen = mask & -mask
    while True:
        nxt = seen
        rem = seen
        while rem:
            low = rem & -rem
            rem -= low
            nxt |= ADJ[low.bit_length() - 1] & mask
        if nxt == seen:
            return seen == mask
        seen = nxt


def make_complex():
    facets = set()
    for subset in combinations(range(N), N - K):
        f = sum(1 << j for j in subset)
        if not connected(U ^ f):
            facets.add(f)
    faces = {0}
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return facets, faces


def morse_matching(faces):
    active = set(faces)
    pairs = []
    for pivot in range(N):
        bit = 1 << pivot
        for low in sorted(active):
            if low == 0 or low & bit or low | bit not in active:
                continue
            high = low | bit
            active.remove(low)
            active.remove(high)
            pairs.append((low, high))
    assert 0 in active and 1 in active
    return active - {0}, pairs


def check_matching_acyclic(faces, pairs):
    paired = {(low, high) for low, high in pairs}
    out = {x: [] for x in faces if x != 0}
    indeg = {x: 0 for x in out}
    arcs = 0
    for high in out:
        for low, _ in boundary(high):
            if low == 0:
                continue
            src, dst = (low, high) if (low, high) in paired else (high, low)
            out[src].append(dst)
            indeg[dst] += 1
            arcs += 1
    q = deque(x for x, v in indeg.items() if v == 0)
    removed = 0
    while q:
        x = q.popleft()
        removed += 1
        for y in out[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    assert removed == len(out), (removed, len(out))
    return arcs


def morse_boundary(critical, pairs):
    c3 = sorted(x for x in critical if x.bit_count() == 4)
    c4 = sorted(x for x in critical if x.bit_count() == 5)
    idx = {x: j for j, x in enumerate(c3)}
    down3up4 = {a: b for a, b in pairs if a.bit_count() == 4}
    upper3 = {b for a, b in pairs if b.bit_count() == 4}

    @lru_cache(None)
    def normal(y):
        if y in idx:
            return ((idx[y], 1),)
        if y in upper3:
            return ()
        assert y in down3up4, vertices(y)
        z = down3up4[y]
        incidence = dict(boundary(z))[y]
        ans = Counter()
        for face, sign in boundary(z):
            if face == y:
                continue
            for j, coefficient in normal(face):
                ans[j] -= incidence * sign * coefficient
        return tuple(sorted((j, v) for j, v in ans.items() if v))

    matrix = []
    for x in c4:
        column = Counter()
        for face, sign in boundary(x):
            for j, coefficient in normal(face):
                column[j] += sign * coefficient
        matrix.append({j: v for j, v in column.items() if v})
    return c3, c4, matrix, normal


def signed_action(mask, shift, reflect):
    old = vertices(mask)
    images = tuple((shift - v if reflect else shift + v) % N for v in old)
    inversions = sum(images[i] > images[j]
                     for i in range(len(images))
                     for j in range(i + 1, len(images)))
    newmask = sum(1 << v for v in images)
    return newmask, -1 if inversions % 2 else 1


def reduced_lefschetz(faces, shift, reflect):
    # Empty face contributes -1 to reduced Lefschetz number.
    total = -1
    for face in faces:
        if face == 0:
            continue
        image, sign = signed_action(face, shift, reflect)
        if image == face:
            total += (1 if face.bit_count() % 2 else -1) * sign
    return total


def lift_cycle(critical, pairs):
    c3 = sorted(f for f in critical if f.bit_count() == 4)
    z = {c3[0]: 1}
    # Reverse the elimination to lift a critical 3-cell to a simplicial cycle.
    for low, high in reversed(pairs):
        if low.bit_count() != 3:
            continue
        current_coeff = sum(coef * dict(boundary(cell)).get(low, 0)
                            for cell, coef in z.items())
        if current_coeff:
            incidence = dict(boundary(high))[low]
            assert current_coeff % incidence == 0
            z[high] = z.get(high, 0) - current_coeff // incidence
            if z[high] == 0:
                del z[high]
    bdy = Counter()
    for cell, coef in z.items():
        for face, sign in boundary(cell):
            bdy[face] += coef * sign
    assert all(v == 0 for v in bdy.values())
    return z


def rank_gf2(vectors):
    pivots = {}
    for vec in vectors:
        while vec:
            lead = vec.bit_length() - 1
            if lead in pivots:
                vec ^= pivots[lead]
            else:
                pivots[lead] = vec
                break
    return len(pivots)


def main():
    facets, faces = make_complex()
    fv = Counter(x.bit_count() - 1 for x in faces)
    assert len(facets) == 2520
    assert fv == {-1: 1, 0: 21, 1: 210, 2: 1330, 3: 3024, 4: 2520}
    critical, pairs = morse_matching(faces)
    ccritical = Counter(x.bit_count() - 1 for x in critical)
    assert ccritical == {0: 1, 3: 14, 4: 650}, ccritical
    assert len(pairs) == (len(faces) - 1 - sum(ccritical.values())) // 2
    arcs = check_matching_acyclic(faces, pairs)
    c3, c4, matrix, normal = morse_boundary(critical, pairs)
    assert (len(c3), len(c4)) == (14, 650)
    nonzero_cols = [(vertices(c4[t]), col) for t, col in enumerate(matrix) if col]
    assert len(nonzero_cols) == 13
    for i, (support, col) in enumerate(nonzero_cols):
        assert support == (i + 2, i + 3, i + 4, 19, 20)
        assert col == {i: 1, 13: -1}
    # The displayed 13 columns have an identity upper 13 x 13 minor.
    # Therefore the integral rank is 13 and the image is primitive.
    assert sum(1 for col in matrix if col) == 13

    z = lift_cycle(critical, pairs)
    assert len(z) == 8
    assert all(abs(v) == 1 for v in z.values())
    def cocycle(cell):
        return sum(v for _j, v in normal(cell))
    assert sum(coef * cocycle(cell) for cell, coef in z.items()) == 1
    # Direct cocycle check in the original complex, not only the Morse complex.
    for facet in facets:
        assert sum(sign * cocycle(face) for face, sign in boundary(facet)) == 0

    traces = Counter()
    for reflect in (False, True):
        for shift in range(N):
            transported_z_pairing = 0
            for cell, coef in z.items():
                image, sign = signed_action(cell, shift, reflect)
                transported_z_pairing += coef * sign * cocycle(image)
            assert transported_z_pairing == 1
            lef = reduced_lefschetz(faces, shift, reflect)
            char4 = lef + 1  # reduced L = -char(H3) + char(H4)
            if reflect:
                assert char4 == -7
                label = 'reflection'
            elif shift == 0:
                assert char4 == 637
                label = 'identity'
            elif shift in (7, 14):
                assert char4 == 7
                label = 'order-three rotation'
            else:
                assert char4 == 0
                label = 'other rotation'
            traces[(label, char4)] += 1

    # Direct full-chain mod-2 computation as a separate homology check.
    f2 = sorted(x for x in faces if x.bit_count() == 3)
    f3 = sorted(x for x in faces if x.bit_count() == 4)
    f4 = sorted(x for x in faces if x.bit_count() == 5)
    id2 = {x: j for j, x in enumerate(f2)}
    id3 = {x: j for j, x in enumerate(f3)}
    d3 = [sum(1 << id2[y] for y, _ in boundary(x)) for x in f3]
    d4 = [sum(1 << id3[y] for y, _ in boundary(x)) for x in f4]
    rank3 = rank_gf2(d3)
    rank4 = rank_gf2(d4)
    assert rank3 == len(f3) - rank4 - 1  # beta3=1
    assert rank4 == len(f4) - 637
    assert (rank3, rank4) == (1140, 1883), (rank3, rank4)
    assert (637 + 2 * 7 + 21 * -7) // 42 == 12
    assert (637 + 2 * 7 + 21 * -7) % 42 == 0
    print('SQUARED_CYCLE_21_16_EXACT_OK')
    print('facets=2520 augmented_faces=7106 f_vector=(21,210,1330,3024,2520)')
    print(f'matching_pairs={len(pairs)} critical=(one0,fourteen3,sixhundredfifty4) directed_hasse_arcs={arcs}')
    print('integral_Morse_boundary_14x650=13_columns(e_i-e_13), others_zero; 13_unit_pivots')
    print(f'primitive_integral_3_cycle_terms={len(z)} cocycle_pairing=1 all_facets_cocycle_closed')
    print(f'full_chain_GF2_ranks_d3_d4=({rank3},{rank4})')
    print('D21_H3_character=+1_for_all_42_elements')
    for (name, value), count in sorted(traces.items()):
        print(f'D21_H4_character_{name.replace(" ", "_")}={value}; count={count}')
    print('D21_quotient_reduced_rational_Betti_3=1_Betti_4=12')


if __name__ == '__main__':
    main()
