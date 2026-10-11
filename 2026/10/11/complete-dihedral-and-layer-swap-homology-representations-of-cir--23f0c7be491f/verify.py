"""Exact finite consistency checks for the dihedral action on prism independence complexes.

Only Python 3 standard library is required.  The general theorem is proved in RESULT.md;
finite enumeration here independently tests its chain-level formulas and the homology input.
"""
from itertools import product
from functools import lru_cache
from math import gcd


def degree(n):
    if n % 4 == 0:
        return n // 2 - 1
    if n % 4 == 1:
        return (n - 3) // 2
    if n % 4 == 2:
        return (n - 2) // 2
    return (n - 1) // 2


def predicted_character(n, k=0, reflection=False, layer_swap=False):
    k %= n
    if n % 2:
        return (-1) ** ((n + 1) // 4) if reflection else 1
    if n % 4 == 2:
        base = (-1) ** (k + int(layer_swap))
        return base * ((-1) ** ((n - 2) // 4)) if reflection else base
    delta = (-1) ** (n // 4 + 1)
    if reflection:
        return (-delta) if layer_swap else delta
    w = (2, 0, -2, 0)[k % 4]
    return w + (-1 if layer_swap else 1)


def permutation(n, k, reflection, layer_swap):
    return tuple(((k - (v % n) if reflection else k + (v % n)) % n)
                 + n * ((v // n) ^ int(layer_swap)) for v in range(2 * n))


def faces(n):
    # Encode independent sets by a three-symbol cyclic word: vacant, upper, lower.
    for states in product((0, 1, 2), repeat=n):
        if all(not (states[j] != 0 and states[j] == states[(j + 1) % n])
               for j in range(n)):
            yield tuple(sorted(j + n * (state - 1) for j, state in enumerate(states) if state))


def trace_direct(n, k, reflection, layer_swap):
    pi = permutation(n, k, reflection, layer_swap)
    total = 0
    for face in faces(n):
        if tuple(sorted(pi[x] for x in face)) != face:
            continue
        unvisited = set(face)
        cycles = 0
        while unvisited:
            cycles += 1
            x = min(unvisited)
            while x in unvisited:
                unvisited.remove(x)
                x = pi[x]
        total += -1 if cycles % 2 == 0 else 1  # Includes the empty face.
    return total


def graph_edges(n):
    edges = set()
    for a in (0, 1):
        for j in range(n):
            edges.add(tuple(sorted((a * n + j, a * n + (j + 1) % n))))
    for j in range(n):
        edges.add((j, j + n))
    return edges


def eval_independence_minus_one(adjs):
    @lru_cache(None)
    def run(mask):
        if not mask:
            return 1
        # Branch on a maximum-degree vertex in the remaining induced graph.
        candidates = mask
        chosen, max_degree = -1, -1
        while candidates:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            candidates ^= bit
            d = (adjs[v] & mask).bit_count()
            if d > max_degree:
                chosen, max_degree = v, d
        bit = 1 << chosen
        return run(mask ^ bit) - run(mask & ~(bit | adjs[chosen]))
    return run((1 << len(adjs)) - 1)


def trace_orbit(n, k, reflection, layer_swap):
    pi = permutation(n, k, reflection, layer_swap)
    orbits, origin = [], {}
    for v in range(2 * n):
        if v in origin:
            continue
        current, orbit = v, []
        while current not in origin:
            origin[current] = len(orbits)
            orbit.append(current)
            current = pi[current]
        assert current == v
        orbits.append(orbit)
    adjs = [0] * len(orbits)
    for a, b in graph_edges(n):
        i, j = origin[a], origin[b]
        adjs[i] |= 1 << j
        adjs[j] |= 1 << i
    good = [i for i in range(len(orbits)) if not (adjs[i] >> i) & 1]
    H = [sum(1 << l for l, j in enumerate(good) if (adjs[i] >> j) & 1)
         for i in good]
    return -eval_independence_minus_one(H)


def mod2_rank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            i = x.bit_length() - 1
            if i not in pivots:
                pivots[i] = x
                break
            x ^= pivots[i]
    return len(pivots)


def mod2_betti(n):
    all_faces = list(faces(n))
    levels = [[()]]
    for k in range(1, n + 1):
        levels.append([f for f in all_faces if len(f) == k])
    if sum(map(len, levels)) != len(all_faces):
        raise AssertionError('Incomplete levels')
    ranks = [0] * len(levels)
    for k in range(1, len(levels)):
        target = {f: i for i, f in enumerate(levels[k - 1])}
        columns = []
        for f in levels[k]:
            bits = 0
            for i in range(len(f)):
                bits ^= 1 << target[f[:i] + f[i + 1:]]
            columns.append(bits)
        ranks[k] = mod2_rank(columns)
    return {k - 1: len(levels[k]) - ranks[k] - (ranks[k + 1] if k + 1 < len(levels) else 0)
            for k in range(len(levels)) if len(levels[k]) - ranks[k] -
            (ranks[k + 1] if k + 1 < len(levels) else 0)}


def matrix_evidence():
    T = ((1, -1, -1), (1, 0, -1), (1, -1, 0))
    def prod(A, B):
        return tuple(tuple(sum(A[i][h] * B[h][j] for h in range(3))
                           for j in range(3)) for i in range(3))
    I = tuple(tuple(int(i == j) for j in range(3)) for i in range(3))
    T2 = prod(T, T)
    assert tuple(sum((T2[i][j] + I[i][j]) for j in range(3))
                 for i in range(3)) == (0, 0, 0)
    assert tuple(sum((1, -1, -1)[i] * (T2[i][j] + I[i][j])
                     for i in range(3)) for j in range(3)) == (0, 0, 0)
    A = I
    for m in range(1, 81):
        A = prod(A, T)
        period = (1, -1, 1, 3)[(m - 1) % 4]
        assert sum(A[i][i] for i in range(3)) == period, (m, A)


def main():
    matrix_evidence()
    face_checks = orbit_checks = 0
    for n in range(3, 11):
        group_elements = [(k, bool(s), bool(t)) for k in range(n)
                          for s in range(2) for t in range(2)]
        for k, reflection, layer_swap in group_elements:
            expected = (-1) ** degree(n) * predicted_character(n, k, reflection, layer_swap)
            actual = trace_direct(n, k, reflection, layer_swap)
            assert actual == expected, ('direct', n, k, reflection, layer_swap, actual, expected)
            face_checks += 1
    for n in range(3, 25):
        for k in range(n):
            for s in (False, True):
                for t in (False, True):
                    expected = (-1) ** degree(n) * predicted_character(n, k, s, t)
                    result = trace_orbit(n, k, s, t)
                    assert result == expected, ('orbit', n, k, s, t, result, expected)
                    orbit_checks += 1
    for n in range(3, 12):
        ranks = mod2_betti(n)
        expected = {degree(n): (3 if n % 4 == 0 else 1)}
        assert ranks == expected, ('homology', n, ranks, expected)
    print('VERIFY_OK: direct_signed_traces=%d, orbit_signed_traces=%d, mod2_homology_widths=9, transfer_periods=80' %
          (face_checks, orbit_checks))


if __name__ == '__main__':
    main()
