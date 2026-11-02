#!/usr/bin/env python3
"""Reproduce the folded-five-cube independence complex and its finite homology character."""
from itertools import permutations
from collections import Counter, defaultdict, deque

N = 16
EDGE_STEPS = (1, 2, 4, 8, 15)
PIVOTS = (2, 10, 0, 14, 6, 5, 3, 8, 7, 11, 15, 1, 12, 13, 9, 4)


def adjacent(u, v):
    return (u ^ v) in EDGE_STEPS


def independent_masks():
    out = []
    for mask in range(1 << N):
        vertices = [j for j in range(N) if mask & (1 << j)]
        if all(not adjacent(a, b) for i, a in enumerate(vertices)
               for b in vertices[i + 1:]):
            out.append(mask)
    return out


def verify_matching(all_faces):
    remaining = set(all_faces)
    pairs = []
    for v in PIVOTS:
        bit = 1 << v
        for face in sorted(tuple(remaining)):
            if face & bit:
                continue
            upper = face | bit
            if face in remaining and upper in remaining:
                remaining.remove(face)
                remaining.remove(upper)
                pairs.append((face, upper))
    assert len(pairs) == 192
    assert len(remaining) == 9
    assert all(face.bit_count() == 4 for face in remaining)
    assert (0, (1 << PIVOTS[0])) in pairs
    # Ordinary Morse matching: leave the vertex matched to the empty face critical.
    pairs.remove((0, (1 << PIVOTS[0])))
    paired = set(pairs)
    nonempty = set(all_faces) - {0}
    assert len(nonempty) == 392
    arcs = defaultdict(list)
    indegree = {s: 0 for s in nonempty}
    covering = 0
    for upper in nonempty:
        for i in range(N):
            if not (upper & (1 << i)):
                continue
            lower = upper ^ (1 << i)
            if not lower:
                continue
            covering += 1
            a, b = (lower, upper) if (lower, upper) in paired else (upper, lower)
            arcs[a].append(b)
            indegree[b] += 1
    queue = deque(v for v, degree in indegree.items() if degree == 0)
    seen = 0
    while queue:
        v = queue.popleft()
        seen += 1
        for w in arcs[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    assert seen == len(nonempty), 'The matching is not acyclic'
    unmatched = nonempty - {f for pair in pairs for f in pair}
    assert len(unmatched) == 10
    assert Counter(f.bit_count() - 1 for f in unmatched) == {0: 1, 3: 9}
    return covering


def permutation_sign(array):
    return -1 if sum(array[i] > array[j]
                     for i in range(len(array)) for j in range(i+1, len(array))) % 2 else 1


def quotient_action(x, p):
    # Representative of x in F_2^5/<11111>: (x_0,...,x_3,0).
    out = 0
    for i in range(4):
        if x & (1 << i):
            out ^= (1 << p[i])
    if out & 16:
        out ^= 31  # return to the representative with fifth coordinate zero
    return out & 15


def lefschetz_trace(g, nonempty_faces):
    L = 0
    for face in nonempty_faces:
        vertices = [i for i in range(N) if face & (1 << i)]
        transported = [g[i] for i in vertices]
        target = sum(1 << j for j in transported)
        if target == face:
            L += (-1 if len(vertices) % 2 == 0 else 1) * permutation_sign(transported)
    # Only H_0=Q, H_3=Q^9, so L=1-Tr(H_3).
    return 1 - L


def predicted_trace(t, p):
    sign = permutation_sign(p)
    fixed = [i for i in range(5) if p[i] == i]
    # The five nontrivial characters of the translation group are
    # chi_i(t)=(-1)^(sum of all five coordinates of t except i).
    orbit = sum((-1)**(t.bit_count() - ((t >> i) & 1)) for i in fixed)
    return sign * (len(fixed) - 1 + orbit)


def verify_symmetry(nonempty_faces):
    distribution = Counter()
    translation_sum = 0
    all_sum = 0
    tested = 0
    vertex_maps = set()
    for p in permutations(range(5)):
        permuted = [quotient_action(x, p) for x in range(N)]
        for t in range(16):
            g = tuple(z ^ t for z in permuted)
            assert len(set(g)) == 16
            # Every one of the 40 edges remains an edge.
            assert all(adjacent(g[x],g[x ^ d]) for x in range(N) for d in EDGE_STEPS)
            vertex_maps.add(g)
            observed = lefschetz_trace(g, nonempty_faces)
            expected = predicted_trace(t, p)
            assert observed == expected, (t, p, observed, expected)
            distribution[observed] += 1
            all_sum += observed
            if p == (0,1,2,3,4):
                translation_sum += observed
            tested += 1
    assert len(vertex_maps) == tested == 1920
    assert all_sum == 0  # The full quotient has no positive rational homology.
    assert translation_sum == 16*4  # The translation quotient has four 3-classes.
    assert distribution == {-5:20, -3:60, -1:884, 1:865, 3:80, 5:10, 9:1}
    return distribution


def main():
    all_faces = independent_masks()
    counts = Counter(face.bit_count() for face in all_faces)
    assert counts == {0:1,1:16,2:80,3:160,4:120,5:16}
    covering = verify_matching(all_faces)
    distribution = verify_symmetry([f for f in all_faces if f])
    print('F_VECTOR=16,80,160,120,16')
    print('NONEMPTY_FACES=392; ACYCLIC_MATCHED_PAIRS=191; CRITICAL_CELLS=0:1,3:9')
    print('HASSE_COVERINGS=' + str(covering))
    print('AUTOMORPHISMS=1920; CHARACTER_DISTRIBUTION=' + str(sorted(distribution.items())))
    print('TRANSLATION_INVARIANTS=4; FULL_GROUP_INVARIANTS=0')
    print('CLEBSCH_WD5_NINE_SPHERES_CHARACTER_OK')


if __name__ == '__main__':
    main()
