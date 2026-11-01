"""Standalone exact verification of the nine-point affine cap-complex theorem.

Python 3 standard library only. Builds all faces, checks acyclic matching,
integer cycle/cocycle and full affine symmetry character from definitions.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product

POINTS = tuple(product(range(3), repeat=2))
LINES = set()
for i, (x, y) in enumerate(POINTS):
    for j, (a, b) in enumerate(POINTS):
        if j <= i:
            continue
        d = ((a-x) % 3, (b-y) % 3)
        k = POINTS.index(((x+2*d[0]) % 3, (y+2*d[1]) % 3))
        LINES.add(tuple(sorted((i, j, k))))
assert len(LINES) == 12 and all(len(L) == 3 for L in LINES)
assert all(sum(i in L for L in LINES) == 4 for i in range(9))

FACES = tuple(tuple(S for S in combinations(range(9), k)
                    if all(not set(L).issubset(S) for L in LINES))
              for k in range(1, 10))
assert list(map(len, FACES)) == [9, 36, 72, 54, 0, 0, 0, 0, 0]
FACE_SET = set(frozenset(S) for level in FACES for S in level)
assert len(FACE_SET) == 171

# A staged, disjoint matching with successive coordinate toggles.
ORDER = (5, 4, 7, 2, 6, 0, 8, 1, 3)
remaining = set(FACE_SET)
matched = []
for v in ORDER:
    for small in sorted(remaining, key=lambda S: (len(S), tuple(sorted(S)))):
        large = small | {v}
        if v not in small and large in remaining:
            matched.append((small, large))
            remaining.remove(small)
            remaining.remove(large)
assert len(matched) == 79
assert Counter(len(S)-1 for S in remaining) == Counter({0: 1, 2: 1, 3: 11})
assert remaining & {frozenset((5,))} == {frozenset((5,))}

# Directed face Hasse graph: unmatched covering edges point downward;
# matched covering edges point upward. A topological sort proves acyclicity.
paired = {(a, b) for a, b in matched}
indeg = {S: 0 for S in FACE_SET}
nexts = defaultdict(list)
cover_count = 0
for large in FACE_SET:
    for v in large:
        small = large - {v}
        if not small:
            continue
        cover_count += 1
        if (small, large) in paired:
            src, dst = small, large
        else:
            src, dst = large, small
        nexts[src].append(dst)
        indeg[dst] += 1
Q = deque(S for S, k in indeg.items() if k == 0)
visited = 0
while Q:
    S = Q.popleft()
    visited += 1
    for T in nexts[S]:
        indeg[T] -= 1
        if indeg[T] == 0:
            Q.append(T)
assert visited == len(FACE_SET), 'discrete Morse matching contains a cycle'

# The integral 2-cycle z and integral 2-cocycle c.
Z = {(0, 1, 3): -1, (0, 1, 6): 1, (0, 2, 3): 1,
     (0, 2, 6): -1, (1, 2, 3): -1, (1, 2, 6): 1}
C = {(0, 1, 4): 1, (0, 2, 5): -1, (0, 4, 5): -1,
     (0, 4, 6): -1, (0, 6, 7): 1, (1, 2, 3): 1,
     (1, 3, 4): -1, (1, 3, 6): -1, (1, 6, 7): 1,
     (2, 3, 5): 1, (2, 5, 6): -1, (2, 6, 7): 1}
assert all(S in FACES[2] for S in Z) and all(S in FACES[2] for S in C)
edge_bd = Counter()
for S, coeff in Z.items():
    for i in range(3):
        edge_bd[S[:i]+S[i+1:]] += coeff*(-1)**i
assert all(x == 0 for x in edge_bd.values()), 'z not a cycle'
for S in FACES[3]:
    delta = sum((-1)**i*C.get(S[:i]+S[i+1:], 0) for i in range(4))
    assert delta == 0, (S, delta)
PAIR = sum(C.get(S, 0)*n for S, n in Z.items())
assert PAIR == -1

def sign(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i+1, len(seq))) % 2 else 1

def trace_chains(permutation):
    traces = []
    for faces in FACES[:4]:
        tr = 0
        for S in faces:
            img = [permutation[i] for i in S]
            if set(img) == set(S):
                tr += sign(img)
        traces.append(tr)
    return tuple(traces)

# Generate all of AGL(2,3), check its 432 distinct permutations, and
# derive the trace on the unique H2 line by the exact integer pairing.
profiles = Counter()
perms = set()
for a, b, c, d in product(range(3), repeat=4):
    det = (a*d-b*c) % 3
    if det == 0:
        continue
    for u, v in product(range(3), repeat=2):
        permutation = tuple(POINTS.index(((a*x+b*y+u) % 3,
                                            (c*x+d*y+v) % 3))
                            for x, y in POINTS)
        perms.add(permutation)
        assert all(tuple(sorted(permutation[i] for i in L)) in LINES for L in LINES)
        paired_g = 0
        for S, val in Z.items():
            mapped = [permutation[i] for i in S]
            paired_g += val*sign(mapped)*C.get(tuple(sorted(mapped)), 0)
        epsilon = paired_g // PAIR
        assert paired_g == PAIR*epsilon
        assert epsilon == (1 if det == 1 else -1), (det, epsilon)
        traces = trace_chains(permutation)
        chi3 = 1 + epsilon - sum((-1)**k*t for k, t in enumerate(traces))
        profiles[(det, traces, epsilon, chi3)] += 1
assert len(perms) == 432
EXPECTED = {
    (1,(0,0,0,0),1,2):8,
    (1,(0,0,3,0),1,-1):48,
    (1,(1,-4,0,6),1,3):9,
    (1,(1,-1,0,0),1,0):72,
    (1,(1,0,0,-2),1,-1):54,
    (1,(3,3,0,0),1,2):24,
    (1,(9,36,72,54),1,11):1,
    (2,(0,0,0,0),-1,0):72,
    (2,(1,0,0,0),-1,-1):108,
    (2,(3,0,-6,0),-1,3):36,
}
assert profiles == EXPECTED
assert sum(m*key[-1] for key, m in profiles.items()) == 0
assert sum(m*key[-2] for key, m in profiles.items()) == 0
print('FACE_VECTOR 9 36 72 54; LINES 12; FACES_TOTAL 171')
print('MORSE_MATCHED_PAIRS 79; CRITICAL_BY_DIM 0:1 2:1 3:11')
print('HASSE_EDGES', cover_count, 'TOPOLOGICAL_SORT', visited)
print('INTEGRAL_CYCLE_COCYCLE_PAIRING', PAIR)
print('AFFINE_AUTOMORPHISMS', len(perms), 'CHARACTER_PROFILES', len(profiles))
for key, count in sorted(profiles.items()):
    print('PROFILE', key, count)
print('AVERAGE_REDUCED_CHARACTERS_ZERO')
print('VERIFY_OK')
