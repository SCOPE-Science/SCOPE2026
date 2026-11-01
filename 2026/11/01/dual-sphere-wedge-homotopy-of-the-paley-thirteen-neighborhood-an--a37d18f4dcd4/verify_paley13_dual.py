#!/usr/bin/env python3
"""Exact standalone check of neighborhood/dominance homotopy of Paley(13)."""
from collections import Counter, deque

P = 13
FULL = (1 << P) - 1
SQUARES = {pow(x, 2, P) for x in range(1, P)}
assert SQUARES == {1, 3, 4, 9, 10, 12}


def mask_of(iterable):
    return sum(1 << x for x in iterable)


def mapped(s, mult):
    return mask_of((mult * i) % P for i in range(P) if (s >> i) & 1)


neigh = [mask_of(j for j in range(P) if j != i and (j-i) % P in SQUARES)
         for i in range(P)]
closed = [n | (1 << i) for i, n in enumerate(neigh)]
comp_neigh = [(FULL ^ neigh[i]) & ~(1 << i) for i in range(P)]
assert all(x.bit_count() == 6 for x in neigh)
for i in range(P):
    for j in range(i+1, P):
        assert (neigh[i] & neigh[j]).bit_count() == (2 if (neigh[i] >> j) & 1 else 3)
for i in range(P):
    assert mapped(neigh[i], 2) == comp_neigh[(2*i) % P]

# Enumerate by definitions, with no imported graph or triangulation.
N = {s for s in range(1, FULL+1) if any(s & nb == s for nb in neigh)}
D = {s for s in range(1, FULL+1) if not any(s & nb == nb for nb in closed)}
assert len(N) == 598 and len(D) == 7592
assert all((s in D) == (not any((FULL ^ s) & nb == (FULL ^ s)
                                    for nb in comp_neigh))
           for s in range(1, FULL+1))  # D = Alexander dual of N(complement)
# Exact duality, including the empty face and full ground set.
for s in range(FULL+1):
    inside_d = not any((s & nb) == nb for nb in closed)
    inside_nbar_dual = not any(((FULL ^ s) & nb) == (FULL ^ s)
                               for nb in comp_neigh)
    assert inside_d == inside_nbar_dual


def check_complex(name, faces, f_expected, crit_expected, expected_hom_degree):
    hist = Counter(s.bit_count()-1 for s in faces)
    assert [hist[d] for d in range(len(f_expected))] == list(f_expected)
    assert all(((s ^ (1 << i)) in faces) for s in faces
               for i in range(P) if (s >> i) & 1 and s.bit_count() > 1)

    # Repeated lexicographic vertex-toggling matching.
    left = set(faces)
    pairs = []
    stages = []
    for v in range(P):
        before = len(pairs)
        for low in sorted(left):
            high = low | (1 << v)
            if not (low >> v) & 1 and low in left and high in left:
                left.remove(low)
                left.remove(high)
                pairs.append((low, high))
        stages.append(len(pairs) - before)
    assert Counter(s.bit_count()-1 for s in left) == Counter(crit_expected)
    assert len(pairs) * 2 + len(left) == len(faces)
    assert all((hi ^ lo).bit_count() == 1 and (lo & hi) == lo for lo, hi in pairs)

    # Directed Hasse graph: every unmatched edge high -> low; matching low -> high.
    id_of = {s: idx for idx, s in enumerate(sorted(faces))}
    edges_out = [[] for _ in faces]
    indegree = [0] * len(faces)
    paired = set(pairs)
    for s in faces:
        for v in range(P):
            if not (s >> v) & 1:
                continue
            low = s ^ (1 << v)
            if low == 0 or low not in faces:
                continue
            a, b = (low, s) if (low, s) in paired else (s, low)
            edges_out[id_of[a]].append(id_of[b])
            indegree[id_of[b]] += 1
    total_hasse = sum(map(len, edges_out))
    work = deque(i for i, a in enumerate(indegree) if a == 0)
    visited = 0
    while work:
        i = work.popleft()
        visited += 1
        for j in edges_out[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                work.append(j)
    assert visited == len(faces), 'matched Hasse digraph contains directed cycle'

    # Independently compute mod-two simplicial boundary ranks.
    by_dim = {d: sorted(s for s in faces if s.bit_count() == d+1)
              for d in hist}
    ranks = {0: 0}
    for d in sorted(by_dim):
        if d == 0:
            continue
        low_position = {s: i for i, s in enumerate(by_dim[d-1])}
        pivot = {}
        for face in by_dim[d]:
            b = 0
            for v in range(P):
                if (face >> v) & 1:
                    b ^= 1 << low_position[face ^ (1 << v)]
            while b:
                j = b.bit_length()-1
                if j not in pivot:
                    pivot[j] = b
                    break
                b ^= pivot[j]
        ranks[d] = len(pivot)
    reduced_betti = {}
    for d in sorted(by_dim):
        betti = hist[d] - ranks.get(d, 0) - ranks.get(d+1, 0)
        if d == 0:
            betti -= 1
        if betti:
            reduced_betti[d] = betti
    assert reduced_betti == {expected_hom_degree: 25}, reduced_betti

    print(name, 'faces',len(faces),'f_vector',str(f_expected),
          'matching_pairs',len(pairs),'critical_cells',dict(crit_expected),
          'directed_Hasse_edges',total_hasse,'acyclic',visited == len(faces),
          'mod2_Betti',reduced_betti)
    print(name, 'matching_phase_pairs',stages)
    return pairs

N_pairs = check_complex('Neighborhood',N,(13,78,221,195,78,13),{0:1,2:25},2)
D_pairs = check_complex('Dominance',D,(13,78,286,715,1287,1716,1703,1209,520,65),{0:1,8:25},8)
assert all(len([v for v in range(P) if (adj >> v) & 1]) == 6 for adj in neigh)
assert sum((-1)**(s.bit_count()-1) for s in N) == 26
assert sum((-1)**(s.bit_count()-1) for s in D) == 26
print('Paley13 strongly regular (13,6,2,3); multiplier two gives complement.')
print('All 8192 vertex subsets checked for Alexander duality.')
print('The Morse CW complexes have one 0-cell and 25 cells only in dimension 2 or 8.')
print('Integral homotopy: Neighborhood = wedge_25(S^2), Dominance = wedge_25(S^8).')
print('PALEY13_DUAL_COMPLEXES_EXACT_MORSE_VERIFIED')
