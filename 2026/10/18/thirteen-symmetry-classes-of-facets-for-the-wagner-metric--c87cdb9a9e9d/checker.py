"""Exact finite certificate for the facet-orbit classification of the Wagner graph.
Run: python3 checker.py. No third-party dependencies.
"""
from collections import Counter
from itertools import product

N = 8
E = tuple(sorted({tuple(sorted((i,(i+1)%N))) for i in range(N)} |
                 {tuple(sorted((i,(i+4)%N))) for i in range(N//2)}))
assert len(E) == 12
EXPECTED = {
    '01010101': (2, 1, 8), '00101101': (8, 1, 10),
    '00010101': (16, 1, 7), '00100101': (16, 1, 9),
    '00101011': (16, 1, 8), '01210121': (4, 2, 8),
    '00100121': (16, 2, 9), '00121121': (16, 2, 10),
    '01011211': (16, 2, 9), '01110121': (16, 2, 7),
    '00101121': (32, 2, 10), '00110121': (32, 2, 8),
    '01101121': (32, 2, 9),
}

def normalized(f):
    low = min(f)
    return tuple(v-low for v in f)

def tight_edges(f):
    return tuple((u,v) for u,v in E if abs(f[u]-f[v]) == 1)

def rank_connectivity(f):
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for a,b in tight_edges(f):
        ra,rb = root(a),root(b)
        parent[ra] = rb
    return len({root(i) for i in range(N)}) == 1

def candidate(f):
    return all(abs(f[u]-f[v]) <= 1 for u,v in E) and rank_connectivity(f)

def orbit(f):
    out = set()
    for s in (-1,1):
        for t in range(N):
            for sign in (-1,1):
                g=[0]*N
                for i,val in enumerate(f):
                    g[(s*i+t)%N] = sign*val
                out.add(normalized(g))
    return out

# Exhaustive finite enumeration of every possible normalized integral vertex.
facets = {f for f in product(range(3),repeat=N) if min(f)==0 and candidate(f)}
assert len(facets)==222
assert Counter(max(f) for f in facets)=={1:58,2:164}
assert Counter(len(tight_edges(f)) for f in facets)=={7:32,8:54,9:80,10:56}

# Separate normalization: enumerate all possible integral potentials with f(0)=0.
# The graph has diameter two, so range [-2,2] exhausts them.
independent = {normalized((0,)+g) for g in product(range(-2,3),repeat=N-1)
               if candidate((0,)+g)}
assert independent == facets

seen=set()
for label,(expected_size,height,edges) in EXPECTED.items():
    f=tuple(int(c) for c in label)
    assert f in facets and max(f)==height and len(tight_edges(f))==edges
    o=orbit(f)
    assert len(o)==expected_size
    assert o<=facets and not(o&seen)
    seen|=o
assert len(EXPECTED)==13 and seen==facets
assert sum(v[0] for v in EXPECTED.values()) == 222
print('PASS: 222 facets, 13 symmetry orbits, independently normalized exhaustive certificate')
print('height:',dict(sorted(Counter(max(f) for f in facets).items())))
print('tight-edge spectrum:',dict(sorted(Counter(map(lambda f: len(tight_edges(f)), facets)).items())))
