from itertools import combinations
from collections import Counter
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

n=9
# Bagchi--Datta path-deletion model K^3_9
facets_path=set()
for i in range(n):
    p=[(i+j)%n for j in range(5)]
    for j in (1,2,3):
        facets_path.add(tuple(sorted(p[:j]+p[j+1:])))
# Spreer difference cycles (1:1:2:5),(1:1:5:2),(1:2:1:5)
def orbit_from_gaps(g):
    s=[0]
    for x in g[:-1]: s.append((s[-1]+x)%n)
    return {tuple(sorted(((v+k)%n for v in s))) for k in range(n)}
facets_diff=set()
for g in [(1,1,2,5),(1,1,5,2),(1,2,1,5)]: facets_diff |= orbit_from_gaps(g)
assert facets_path==facets_diff
facets=facets_path
faces={r:set() for r in range(1,5)}
for F in facets:
    for r in range(1,5):
        for s in combinations(F,r): faces[r].add(tuple(sorted(s)))
assert [len(faces[r]) for r in range(1,5)]==[9,36,54,27]
# H1 presentation after collapsing the star tree at vertex 0.
edges=sorted(faces[2]); tris=sorted(faces[3])
non_tree=[e for e in edges if 0 not in e]
idx={e:i for i,e in enumerate(non_tree)}
rows=[]
for a,b,c in tris:
    row=[0]*len(non_tree)
    for e,sgn in [((a,b),1),((a,c),-1),((b,c),1)]:
        if 0 not in e: row[idx[e]]+=sgn
    rows.append(row)
R=Matrix(rows)
S=smith_normal_form(R,domain=ZZ)
diag=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
assert len(non_tree)==28 and len(diag)==27 and diag==[1]*27
# Therefore H1 is Z.
alltris=set(combinations(range(n),3)); empty=sorted(alltris-faces[3])
assert len(empty)==30

def gaps(t):
    a,b,c=sorted(t); return (b-a,c-b,a+n-c)
def canon(g):
    return min(tuple(g[i:]+g[:i]) for i in range(3))
assert all((max(gaps(t))<=4)==(t in empty) for t in alltris)
prof=Counter(canon(list(gaps(t))) for t in empty)
assert prof==Counter({(1,4,4):9,(2,3,4):9,(2,4,3):9,(3,3,3):3})
# Winding cocycle: signed least residue in {-4,-3,...,4}; cycles have sum divisible by 9.
def step(a,b):
    d=(b-a)%n
    return d if d<=4 else d-9
for a,b,c in tris:
    assert step(a,b)+step(b,c)+step(c,a)==0
for t in empty:
    a,b,c=sorted(t)
    # orient by cyclic order a->b->c->a
    assert step(a,b)+step(b,c)+step(c,a)==9
# shift action preserves winding
for t in empty:
    a,b,c=sorted(t)
    seq=(a,b,c)
    val=sum(step(seq[i],seq[(i+1)%3]) for i in range(3))
    for k in range(n):
        q=tuple((x+k)%n for x in seq)
        assert sum(step(q[i],q[(i+1)%3]) for i in range(3))==val
print('VERIFY_OK f=9,36,54,27 H1=Z empty3=30 gap_orbits=1:4:4x9,2:3:4x9,2:4:3x9,3:3:3x3 winding=1_all_missing shift_action=+1')
