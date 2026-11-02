"""Exact 3- and 4-vertex finite-logic tests for the four (28,12,6,4) graphs.

Run: python3 verify.py
Only Python's standard library is required.
"""
from itertools import combinations, permutations
from collections import Counter

PAIRS=list(combinations(range(8),2))
SWITCH={
  'triangular': [],
  'chang_3plus5':[(0,1),(1,2),(0,2),(3,4),(4,5),(5,6),(6,7),(3,7)],
  'chang_matching':[(0,4),(1,5),(2,6),(3,7)],
  'chang_8cycle':[(i,(i+1)%8) for i in range(8)],
}

def graph(sw):
    s={tuple(sorted(x)) for x in sw}
    return [[int((len(set(u)&set(v))==1) != ((u in s)!=(v in s))) if i!=j else 0
         for j,v in enumerate(PAIRS)] for i,u in enumerate(PAIRS)]

def common(M,x,y):
    return sum(M[x][w]*M[y][w] for w in range(28))

def extension_triangle(M,x,y,z):
    return any(w not in (x,y,z) and not M[w][x] and M[w][y] and M[w][z]
               for w in range(28))

def extension_edge(M,x,y,z):
    return any(w not in (x,y,z) and M[w][x] and M[w][y] and not M[w][z]
               for w in range(28))

def types4(M):
    # Canonicalize unlabeled four-vertex induced graph under every permutation.
    p4=list(permutations(range(4)))
    edges=list(combinations(range(4),2))
    observed=Counter()
    for ids in combinations(range(28),4):
        m=[[M[ids[i]][ids[j]] for j in range(4)] for i in range(4)]
        code=min(tuple(m[p[a]][p[b]] for a,b in edges) for p in p4)
        observed[code]+=1
    return observed

ALL={name:graph(sw) for name,sw in SWITCH.items()}
res={}
for name,M in ALL.items():
    assert all(sum(row)==12 for row in M)
    assert all(common(M,x,y)==(6 if M[x][y] else 4) for x,y in combinations(range(28),2))
    claw=next(((a,b,c,d) for a,b,c,d in permutations(range(28),4)
           if M[a][b] and M[a][c] and M[a][d]
           and not M[b][c] and not M[b][d] and not M[c][d]),None)
    tri=next(((a,b,c) for a,b,c in permutations(range(28),3)
           if M[a][b] and M[a][c] and M[b][c] and not extension_triangle(M,a,b,c)),None)
    edge=next(((a,b,c) for a,b,c in permutations(range(28),3)
           if not M[a][b] and not M[a][c] and M[b][c] and not extension_edge(M,a,b,c)),None)
    m4=types4(M)
    res[name]=(bool(claw),bool(tri),bool(edge),len(m4))
    def show(t): return None if t is None else tuple(''.join(map(str,PAIRS[i])) for i in t)
    print(f'{name}: 3-round parameters (28,12,6,4); claw={bool(claw)}; bad_triangle={bool(tri)}; bad_edge={bool(edge)}; four_types={len(m4)}')
    print(f'  explicit witnesses: claw={show(claw)}, triangle={show(tri)}, edge={show(edge)}')
    print(f'  unordered-four-subset count={sum(m4.values())}; all eleven types={len(m4)==11}')
assert {k:v[:3] for k,v in res.items()} == {
  'triangular':(False,False,False),
  'chang_3plus5':(True,True,False),
  'chang_matching':(True,False,True),
  'chang_8cycle':(True,False,False)}
assert [res[k][3] for k in SWITCH]==[10,11,11,11]
assert len(set(v[:3] for v in res.values()))==4
print('FO4_SEPARATION_AND_FO3_COLLAPSE_PASS')
