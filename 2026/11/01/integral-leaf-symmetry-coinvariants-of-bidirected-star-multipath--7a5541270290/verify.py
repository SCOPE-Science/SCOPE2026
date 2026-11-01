"""Exact integral verification of crown-graph cycle-lattice coinvariants.
Run: python verify.py (requires SymPy).
The verification covers m=3,...,8; the written proof covers all m>=3.
"""
from collections import deque
from itertools import combinations
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def check(m):
    edges = [(i, j) for i in range(m) for j in range(m) if i != j]
    pos = {e: k for k, e in enumerate(edges)}
    adj = [[] for _ in range(2*m)]
    for k, (i,j) in enumerate(edges):
        adj[i].append((m+j,k,1))
        adj[m+j].append((i,k,-1))
    tree, seen, paths, queue = set(), {0}, {0:{}}, deque([0])
    while queue:
        u=queue.popleft()
        for v,k,sgn in adj[u]:
            if v in seen: continue
            seen.add(v); queue.append(v); tree.add(k)
            paths[v] = {**paths[u], k: sgn}
    assert len(seen) == 2*m
    chords = [k for k in range(len(edges)) if k not in tree]
    rank = m*m-3*m+1
    assert len(chords) == rank
    cols=[]
    for k in chords:
        i,j=edges[k]; v=[0]*len(edges); v[k]=1
        for e,s in paths[i].items(): v[e]+=s
        for e,s in paths[m+j].items(): v[e]-=s
        cols.append(v)
    # Fundamental cycle basis is integral: projection onto chord coordinates is I.
    assert all(cols[a][chords[b]] == (1 if a==b else 0)
               for a in range(rank) for b in range(rank))
    perm1=list(range(m)); perm1[0],perm1[1]=1,0
    perm2=list(range(1,m))+[0]
    relations=[]
    for perm in (perm1,perm2):
        R=sp.zeros(rank,rank)
        for a,v in enumerate(cols):
            for b,ek in enumerate(chords):
                i,j=edges[ek]
                R[b,a]=v[pos[(perm.index(i),perm.index(j))]]
        relations.append(R-sp.eye(rank))
    S=smith_normal_form(relations[0].row_join(relations[1]),domain=ZZ)
    invariant=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
    expected=[2] if m in (3,4) else []
    assert len(invariant)==rank and [x for x in invariant if x>1]==expected
    # Four-cycles, when defined, span the kernel integrally.
    if m>=4:
        gammas=[]
        for a,b in combinations(range(m),2):
            for c,d in combinations([z for z in range(m) if z not in (a,b)],2):
                v=[0]*len(edges)
                for x,y,sgn in ((a,c,1),(a,d,-1),(b,c,-1),(b,d,1)):
                    v[pos[x,y]]+=sgn
                gammas.append(v)
        A=sp.Matrix([[v[k] for v in gammas] for k in chords])
        T=smith_normal_form(A,domain=ZZ)
        assert A.rank()==rank and all(abs(int(T[i,i]))==1 for i in range(rank))
    print('m=',m,'cycle_rank=',rank,'coinvariants=', 'Z/2' if expected else '0')

for m in range(3,9): check(m)
print('VERIFIED: all finite lattice tests passed; general proof is independent.')
