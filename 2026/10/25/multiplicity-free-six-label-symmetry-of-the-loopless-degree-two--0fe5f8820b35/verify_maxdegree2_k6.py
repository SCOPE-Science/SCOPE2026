#!/usr/bin/env python3
"""Exact finite checks for the loopless six-label maximum-degree-two graph complex.
Python 3 standard library only. Run: python3 verify_maxdegree2_k6.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial

N = 6
EDGES = list(combinations(range(N), 2))
NE = len(EDGES)
EDGE_INDEX = {p: i for i, p in enumerate(EDGES)}
INC = [sum(1 << j for j, (a, b) in enumerate(EDGES) if v in (a, b)) for v in range(N)]

def bits(x):
    while x:
        low = x & -x
        yield low.bit_length()-1
        x -= low

def admissible(x):
    return all((x & q).bit_count() <= 2 for q in INC)

def admissible_alt(x):
    degrees = [0] * N
    for j in bits(x):
        a, b = EDGES[j]
        degrees[a] += 1
        degrees[b] += 1
    return max(degrees) <= 2

for x in range(1 << NE):
    assert admissible(x) == admissible_alt(x)
FACES = [x for x in range(1 << NE) if admissible(x)]
ACTIVE = set(FACES)
assert len(FACES) == 1858
assert Counter(x.bit_count()-1 for x in FACES if x) == {0:15,1:105,2:395,3:735,4:537,5:70}
facets = Counter(x.bit_count()-1 for x in FACES if x and not any((x | (1 << i)) in ACTIVE for i in range(NE) if not (x >> i & 1)))
assert facets == {4:117,5:70}

# Lexicographic vertex-toggle matching, including the augmented empty face.
remaining = set(FACES)
matching = []
for j in range(NE):
    for a in sorted(remaining):
        if a & (1 << j):
            continue
        b = a | (1 << j)
        if b in remaining:
            remaining.remove(a)
            remaining.remove(b)
            matching.append((a, b))
assert matching[0] == (0, 1)
assert len(matching) == 897
assert Counter(x.bit_count()-1 for x in remaining) == {3:14,4:50}

# Topological sort of the ordinary (nonempty) Forman gradient graph.
# The augmented pair (empty, singleton) is excluded, leaving one critical vertex.
nonempty = set(FACES) - {0}
matched = set(matching[1:])
indeg = {x: 0 for x in nonempty}
adj = {x: [] for x in nonempty}
incidences = 0
for upper in nonempty:
    for j in bits(upper):
        lower = upper ^ (1 << j)
        if not lower:
            continue
        incidences += 1
        if (lower, upper) in matched:
            u, v = lower, upper
        else:
            u, v = upper, lower
        adj[u].append(v)
        indeg[v] += 1
q = deque(x for x in sorted(nonempty) if indeg[x] == 0)
visited = 0
while q:
    x = q.popleft()
    visited += 1
    for y in adj[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
assert visited == len(nonempty) == 1857
assert incidences == 7440

# Algebraic Morse cancellation on augmented oriented simplex chains over Z.
D = {}
for x in FACES:
    d = {}
    for pos, j in enumerate(bits(x)):
        d[x ^ (1 << j)] = (-1) ** pos
    D[x] = d
current = set(FACES)
for lower, upper in matching:
    pivot = D[upper].get(lower, 0)
    assert abs(pivot) == 1
    for c in sorted(current):
        if c == upper or c.bit_count() != upper.bit_count():
            continue
        t = D[c].pop(lower, 0)
        if not t:
            continue
        for z, coeff in D[upper].items():
            if z == lower:
                continue
            new = D[c].get(z, 0) - t * coeff * pivot
            if new:
                D[c][z] = new
            else:
                D[c].pop(z, None)
    current.remove(lower)
    current.remove(upper)
    del D[lower]
    del D[upper]
assert current == remaining
row_cells = sorted(x for x in current if x.bit_count() == 4)
col_cells = sorted(x for x in current if x.bit_count() == 5)
B = [[D[c].get(r, 0) for c in col_cells] for r in row_cells]
assert len(B) == 14 and all(len(row) == 50 for row in B)
assert sum(v != 0 for row in B for v in row) == 122
assert max(abs(v) for row in B for v in row) == 3
PIVOT_COLUMNS = [1,2,4,7,9,10,11,12,14,18,20,21,24,37]

def det_bareiss(M):
    A = [row[:] for row in M]
    n = len(A)
    previous = 1
    sign = 1
    for k in range(n-1):
        if A[k][k] == 0:
            r = next((i for i in range(k+1, n) if A[i][k]), None)
            if r is None:
                return 0
            A[k], A[r] = A[r], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = A[i][j] * pivot - A[i][k] * A[k][j]
                assert num % previous == 0
                A[i][j] = num // previous
            A[i][k] = 0
        previous = pivot
    return sign * A[n-1][n-1]

determinant = det_bareiss([[row[j] for j in PIVOT_COLUMNS] for row in B])
assert determinant == -1

# Independent simplicial boundary rank calculation over finite fields.
by_size = {r: sorted(x for x in FACES if x.bit_count() == r) for r in range(7)}

def rank_mod2(r):
    row_id = {x: i for i, x in enumerate(by_size[r-1])}
    basis = {}
    for x in by_size[r]:
        vec = 0
        for j in bits(x):
            vec ^= 1 << row_id[x ^ (1 << j)]
        while vec:
            lead = vec.bit_length()-1
            if lead not in basis:
                basis[lead] = vec
                break
            vec ^= basis[lead]
    return len(basis)

def rank_modp(r, p):
    row_id = {x: i for i, x in enumerate(by_size[r-1])}
    basis = {}
    for x in by_size[r]:
        v = {row_id[x ^ (1 << j)]: (1 if pos % 2 == 0 else p-1) for pos, j in enumerate(bits(x))}
        while v:
            j = min(v)
            if j not in basis:
                inverse = pow(v[j], -1, p)
                basis[j] = {i:(co*inverse)%p for i,co in v.items()}
                break
            factor = v[j]
            for i, val in basis[j].items():
                new = (v.get(i, 0) - factor*val) % p
                if new:
                    v[i] = new
                else:
                    v.pop(i, None)
    return len(basis)

EXPECTED_RANKS = [1,14,91,304,431,70]
assert [rank_mod2(r) for r in range(1,7)] == EXPECTED_RANKS
assert [rank_modp(r,3) for r in range(1,7)] == EXPECTED_RANKS

# Conjugacy-class rational homology trace from oriented simplicial Lefschetz counts.
def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    for p in range(min(n, max_part or n), 0, -1):
        for q in partitions(n-p, p):
            yield (p,)+q

def representative(mu):
    g = list(range(sum(mu)))
    offset = 0
    for length in mu:
        for i in range(length):
            g[offset+i] = offset+(i+1)%length
        offset += length
    return tuple(g)

def edge_orbits(mu):
    g = representative(mu)
    action = [EDGE_INDEX[tuple(sorted((g[a],g[b])))] for a,b in EDGES]
    seen = set()
    out = []
    for j in range(NE):
        if j in seen:
            continue
        orbit = []
        k = j
        while k not in seen:
            seen.add(k)
            orbit.append(k)
            k = action[k]
        out.append(orbit)
    return out

def character_orbits(mu):
    orbits = edge_orbits(mu)
    total = 0
    for selection in range(1 << len(orbits)):
        degrees = [0]*N
        valid = True
        for i, orbit in enumerate(orbits):
            if not (selection >> i & 1):
                continue
            for j in orbit:
                a,b = EDGES[j]
                degrees[a] += 1
                degrees[b] += 1
                if degrees[a] > 2 or degrees[b] > 2:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            total += -1 if selection.bit_count() % 2 else 1
    return -total

def character_direct(mu):
    g = representative(mu)
    action = [EDGE_INDEX[tuple(sorted((g[a],g[b])))] for a,b in EDGES]
    value = 0
    for x in FACES:
        y = sum(1 << action[j] for j in bits(x))
        if x != y:
            continue
        chosen = list(bits(x))
        img = [action[j] for j in chosen]
        inversions = sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))
        value += (-1) ** (len(chosen)-1+inversions)
    return int(value)

PARTS = list(partitions(N))
CHAR = [character_orbits(mu) for mu in PARTS]
assert CHAR == [2,1,0,0,0,0,0,8,4,0,36]
assert CHAR == [character_direct(mu) for mu in PARTS]

def class_size(mu):
    cc = Counter(mu)
    z = 1
    for a,b in cc.items():
        z *= a**b * factorial(b)
    return factorial(sum(mu)) // z

@lru_cache(None)
def tabloid_fixed(alpha,mu):
    if any(v<0 for v in alpha) or sum(alpha)!=sum(mu):
        return 0
    table = {tuple(alpha): 1}
    for cycle in mu:
        next_table = defaultdict(int)
        for remaining, count in table.items():
            for j, x in enumerate(remaining):
                if x >= cycle:
                    nxt = list(remaining)
                    nxt[j] -= cycle
                    next_table[tuple(nxt)] += count
        table = next_table
    return table.get((0,)*len(alpha),0)

@lru_cache(None)
def specht_char(lam,mu):
    # Jacobi-Trudi determinant interpreted via Young permutation characters.
    ell = len(lam)
    result = 0
    for perm in permutations(range(ell)):
        alpha = tuple(lam[i]-i+perm[i] for i in range(ell))
        inversion_parity = sum(perm[i]>perm[j] for i in range(ell) for j in range(i+1,ell))%2
        result += (-1 if inversion_parity else 1)*tabloid_fixed(alpha,mu)
    return result

MULTIPLICITIES = {}
for lam in PARTS:
    numerator = sum(class_size(mu)*c*specht_char(lam,mu) for mu,c in zip(PARTS,CHAR))
    assert numerator % factorial(N) == 0
    multiplicity = numerator//factorial(N)
    assert multiplicity >= 0
    if multiplicity:
        MULTIPLICITIES[lam] = multiplicity
assert MULTIPLICITIES == {(6,):1,(4,2):1,(3,2,1):1,(2,2,2):1,(2,1,1,1,1):1}
assert sum(m*specht_char(lam,(1,)*6) for lam,m in MULTIPLICITIES.items()) == 36
print('face_vector=15,105,395,735,537,70')
print('facet_counts: dimension_4=117, dimension_5=70')
print('ordinary_Hasse_incidences=',incidences,'acyclic_vertices=',visited)
print('critical_cells: vertex=1, dimension_3=14, dimension_4=50')
print('integer_Morse_boundary_shape=14x50; unit_minor_determinant=',determinant)
print('simplicial_boundary_ranks_mod_2_and_3=',EXPECTED_RANKS)
print('S6_conjugacy_types=',PARTS)
print('H4_character=',CHAR)
print('irreducible_multiplicities=',MULTIPLICITIES)
print('VERIFY_OK')
