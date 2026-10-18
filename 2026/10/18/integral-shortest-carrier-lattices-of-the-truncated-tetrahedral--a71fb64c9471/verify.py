#!/usr/bin/env python3
"""Exact, reproducible matching-complex carrier census for the truncated tetrahedron.
Run: python3 verify.py ; requires SymPy 1.14.0. Integer arithmetic throughout.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd, prod
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

# The truncated tetrahedral graph is the graph of directed K_4 half-edges.
V = [(a, b) for a in range(4) for b in range(4) if a != b]
vid = {v: i for i, v in enumerate(V)}
E = sorted(set(tuple(sorted((vid[x], vid[y]))) for x, y in (
    [((a, b), (a, c)) for a in range(4)
     for b, c in combinations([d for d in range(4) if d != a], 2)]
    + [((a, b), (b, a)) for a, b in combinations(range(4), 2)])))
assert len(V) == 12 and len(E) == 18

# Every simplex is a tuple of disjoint graph-edge indices.
faces_by_size = {k: [] for k in range(1, 7)}
for k in range(1, 7):
    for face in combinations(range(len(E)), k):
        if len({v for e in face for v in E[e]}) == 2 * k:
            faces_by_size[k].append(face)
assert tuple(len(faces_by_size[k]) for k in range(1, 7)) == (18,117,332,390,144,8)
F = set().union(*[set(l) for l in faces_by_size.values()])
assert len(F) == 1009

# Lexicographic acyclic matching on the *nonaugmented* face poset.
unmatched = set(F)
matching = []
for v in range(18):
    for face in sorted(unmatched, key=lambda x: (len(x), x)):
        if v in face:
            continue
        upper = tuple(sorted((*face, v)))
        if upper in unmatched:
            unmatched.remove(face)
            unmatched.remove(upper)
            matching.append((face, upper))
assert len(matching) == 493
assert Counter(len(f) - 1 for f in unmatched) == {0: 1, 3: 22}
matched = {(f, g) for f, g in matching}

# Exact directed Hasse graph: matched incidences lower->upper, others upper->lower.
forward = defaultdict(list)
indeg = {f: 0 for f in F}
incidences = 0
for upper in F:
    for j in range(len(upper)):
        lower = upper[:j] + upper[j+1:]
        if not lower:
            continue
        incidences += 1
        src, dst = (lower, upper) if (lower, upper) in matched else (upper, lower)
        forward[src].append(dst)
        indeg[dst] += 1
queue = deque(f for f, d in indeg.items() if d == 0)
seen = 0
while queue:
    f = queue.popleft()
    seen += 1
    for g in forward[f]:
        indeg[g] -= 1
        if indeg[g] == 0:
            queue.append(g)
assert seen == len(F) and incidences == 3558
# Forman gives a CW complex with one 0-cell and 22 3-cells, hence wedge 22 S^3.

# Enumerate all spanning 4-path P3-factors. A path is two incident graph edges.
paths = []
for a, b in combinations(range(18), 2):
    verts = frozenset(E[a] + E[b])
    if len(verts) == 3:
        paths.append((a, b, verts))
assert len(paths) == 36
carriers = sorted({tuple(sorted((a,b) for a,b,_ in four)) for four in combinations(paths, 4)
                   if len(set().union(*(p[2] for p in four))) == 12})
assert len(carriers) == 111
assert len({frozenset(e for pair in c for e in pair) for c in carriers}) == 111

# Full symmetry from the four distinguished triangular 3-cycles: Aut(G) = S_4.
autmaps = []
for pi in permutations(range(4)):
    vertex_map = {vid[(a,b)]: vid[(pi[a],pi[b])] for a,b in V}
    autmaps.append({i: E.index(tuple(sorted((vertex_map[a],vertex_map[b]))))
                    for i,(a,b) in enumerate(E)})
assert len(autmaps) == 24
remaining = set(carriers)
orbits = []
while remaining:
    rep = min(remaining)
    orb = {tuple(sorted(tuple(sorted((emap[a], emap[b]))) for a,b in rep))
           for emap in autmaps}
    assert orb <= set(carriers)
    orbits.append(sorted(orb))
    remaining -= orb
assert tuple(map(len, orbits)) == (12,12,24,3,24,6,24,6)

# Integral Morse reduction: cancel each matched (3,4)-pair by its signed boundary.
# The remaining matched upper 3-cells project to 0; critical 3-cells survive.
lower3 = {f: g for f,g in matching if len(f)==4}
critical3 = sorted(f for f in unmatched if len(f)==4)
upper3 = {g for f,g in matching if len(g)==4}
assert len(lower3)==136 and len(upper3)==232 and len(critical3)==22
critindex = {f:i for i,f in enumerate(critical3)}

@lru_cache(None)
def projection(face):
    """Integer coordinates of a 3-simplex in the reduced 22-cell Morse complex."""
    if face in critindex:
        return {critindex[face]:1}
    if face in upper3:
        return {}
    upper = lower3[face]
    p = next(j for j in range(5) if upper[:j]+upper[j+1:] == face)
    out = defaultdict(int)
    for j in range(5):
        if j == p:
            continue
        other = upper[:j] + upper[j+1:]
        coeff = -1 if (1+j-p)%2 else 1
        for coordinate, val in projection(other).items():
            out[coordinate] += coeff*val
    return {i:v for i,v in out.items() if v}

def boundary(chain):
    out = defaultdict(int)
    for face, x in chain.items():
        for j in range(len(face)):
            lower = face[:j]+face[j+1:]
            if lower:
                out[lower] += (-1 if j%2 else 1)*x
    return {face:x for face,x in out.items() if x}

def mapped(chain):
    out = [0]*22
    for face, x in chain.items():
        for j, val in projection(face).items():
            out[j] += x*val
    return out

# Check the proposed integer Morse projection annihilates every C4 boundary.
for f in faces_by_size[5]:
    assert mapped(boundary({f:1})) == [0]*22

def sign_of_sort(sequence):
    return -1 if sum(sequence[i]>sequence[j] for i in range(len(sequence))
                     for j in range(i+1,len(sequence)))%2 else 1

def sphere_cycle(factor):
    """Alternating oriented fundamental chain of (S^0)^{*4}."""
    ans = defaultdict(int)
    for choices in product((0,1), repeat=4):
        picked = tuple(factor[i][choices[i]] for i in range(4))
        coeff = (-1 if (4-sum(choices))%2 else 1)*sign_of_sort(picked)
        ans[tuple(sorted(picked))] += coeff
    return {f:x for f,x in ans.items() if x}

coords = []
for factor in carriers:
    z = sphere_cycle(factor)
    assert len(z)==16 and all(f in F for f in z)
    assert not boundary(z)
    col = mapped(z)
    assert gcd(*[abs(int(x)) for x in col]) == 1
    coords.append(col)
X = Matrix(22,111,lambda i,j:coords[j][i])

def smith_data(A):
    s = smith_normal_form(A, domain=ZZ)
    ds = [abs(int(s[j,j])) for j in range(min(s.shape)) if s[j,j]]
    return len(ds), prod(ds), tuple(x for x in ds if x>1)
assert smith_data(X) == (22,1,())

ranks = []
for orb in orbits:
    sub = X[:,[carriers.index(c) for c in orb]]
    ranks.append(smith_data(sub))
assert [r for r,_,_ in ranks] == [8,11,14,3,13,6,16,6]
assert all(index==1 for _,index,_ in ranks)

# Check exactly the natural two-/three-orbit generation threshold and exception.
pair_generators = []
triple_generators = []
for t in (2,3):
    for ids in combinations(range(8),t):
        indices = sorted({carriers.index(c) for j in ids for c in orbits[j]})
        rank, index, factors = smith_data(X[:,indices])
        if rank==22:
            (pair_generators if t==2 else triple_generators).append((ids,index,factors))
assert pair_generators == [((1,6),1,()),((2,6),1,()),((5,6),1,()),((6,7),1,())]
assert len(triple_generators)==19
assert [(ids,index,fac) for ids,index,fac in triple_generators if index != 1] == [((3,4,6),2,(2,))]

# One explicit unimodular selection proves that 22 actual geometric carriers are a basis.
unit_indices=[99,36,47,97,94,110,84,1,53,74,11,33,16,32,96,37,22,68,61,30,65,86]
assert int(X[:,unit_indices].det(method='domain-ge')) == 1

print('VERIFY_OK_TRUNCATED_TETRA_SHORTEST_CARRIERS')
print('GRAPH',len(V),len(E),'FACES',tuple(len(faces_by_size[k]) for k in range(1,7)))
print('MORSE',len(matching),'critical',Counter(len(f)-1 for f in unmatched),'DAG_INCIDENCES',incidences)
print('SPANNING_P3_FACTORS',len(carriers),'S4_ORBITS',tuple(len(o) for o in orbits))
print('ALL_111_CYCLES_PRIMITIVE',True,'ALL_CARRIER_SMITH',(22,1))
print('ORBIT_RANKS',tuple(x[0] for x in ranks),'ORBIT_SATURATION_INDEX',tuple(x[1] for x in ranks))
print('TWO_ORBIT_INTEGRAL_GENERATORS',[x[0] for x in pair_generators])
print('THREE_ORBIT_SPANNING_UNIONS',len(triple_generators),'UNIQUE_INDEX_TWO',((3,4,6),2,(2,)))
print('EXPLICIT_22_CLASS_BASIS_DETERMINANT',1)
