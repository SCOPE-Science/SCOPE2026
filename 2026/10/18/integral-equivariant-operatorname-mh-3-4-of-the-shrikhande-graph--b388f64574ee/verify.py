"""Exact integral and equivariant verification for a finite graph magnitude homology calculation.

Requires Python >=3.10 and SymPy >=1.11; run: python verify.py
All graph data are generated from the Cayley generating set; no cached matrices.
"""
import itertools
from collections import deque
from sympy import Matrix, SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

V = list(itertools.product(range(4), repeat=2))
IDX = {u:i for i,u in enumerate(V)}
ZERO = (0,0)
STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def add(u,v): return ((u[0]+v[0])%4,(u[1]+v[1])%4)
def neg(u): return ((-u[0])%4,(-u[1])%4)
def mat(A,u): return ((A[0]*u[0]+A[1]*u[1])%4,(A[2]*u[0]+A[3]*u[1])%4)

# Compute shortest-path distances independently of diameter assumptions.
D = [[-1]*len(V) for _ in V]
for i,u in enumerate(V):
    D[i][i]=0
    queue=deque([i])
    while queue:
        j=queue.popleft()
        for s in STEPS:
            z=IDX[add(V[j],s)]
            if D[i][z]<0:
                D[i][z]=D[i][j]+1
                queue.append(z)
assert set(sum(D,[]))=={0,1,2}
assert all(sum(d==1 for d in row)==6 and sum(d==2 for d in row)==9 for row in D)

P = [A for A in itertools.product(range(4),repeat=4) if {mat(A,s) for s in STEPS}==STEPS]
assert len(P)==12
assert all(len({mat(A,v) for v in V})==16 for A in P)
assert len({(add(t,mat(A,u))) for t in V for A in P for u in V})==16
# All affine transformations x -> t+Ax are pairwise distinct (test images of zero and basis).
affine_keys={(add(t,mat(A,(0,0))), add(t,mat(A,(1,0))),add(t,mat(A,(0,1)))) for t in V for A in P}
assert len(affine_keys)==192

O = {}
for d in V:
    orb=frozenset(mat(A,d) for A in P)
    O[d]=orb
orbits={orb for orb in O.values()}
assert {len(x) for x in orbits}=={1,3,6}, sorted(map(len,orbits))
# Zero orbit, one adjacency orbit, and two nonadjacency orbits.
assert {O[ZERO],O[(1,0)],O[(0,2)],O[(1,2)]}==orbits
assert list(sorted(map(len,orbits)))==[1,3,6,6]
assert all(D[0][IDX[d]]==1 for d in O[(1,0)])
assert all(D[0][IDX[d]]==2 for d in O[(0,2)]|O[(1,2)])

def basis(b,k,ell=4):
    """Ordered length-ell k-chains from zero to endpoint b.
    Repetition is allowed except consecutive equality is excluded.
    """
    out=[]
    target=IDX[b]
    def walk(chain,length):
        if len(chain)==k+1:
            if chain[-1]==target and length==ell: out.append(tuple(chain))
            return
        for y in range(len(V)):
            delta=D[chain[-1]][y]
            if delta and length+delta+D[y][target]<=ell:
                walk(chain+[y],length+delta)
    walk([0],0)
    return out

def boundary(source,target):
    """Signed magnitude boundary, deleting only smooth interior vertices."""
    look={t:i for i,t in enumerate(target)}
    entries={}
    for j,c in enumerate(source):
        for p in range(1,len(c)-1):
            if D[c[p-1]][c[p+1]]==D[c[p-1]][c[p]]+D[c[p]][c[p+1]]:
                z=c[:p]+c[p+1:]
                assert z in look
                entries[(look[z],j)]=(-1)**p
    return SparseMatrix(len(target),len(source),entries)

def rank_smith_units(A):
    snf=smith_normal_form(A,domain=ZZ)
    diag=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
    assert all(q==1 for q in diag), (A.shape,diag)
    return len(diag)

stats={}
for d in [ZERO,(1,0),(0,2),(1,2)]:
    b2,b3,b4=(basis(d,k) for k in (2,3,4))
    d3,d4=boundary(b3,b2),boundary(b4,b3)
    assert d3*d4==SparseMatrix(len(b2),len(b4),{})
    rank3=rank_smith_units(d3)
    rank4=rank_smith_units(d4)
    assert rank4<=len(b3)-rank3
    betti3=len(b3)-rank3-rank4
    stats[d]=dict(b2=len(b2),b3=len(b3),b4=len(b4),rank3=rank3,rank4=rank4,betti3=betti3)
assert stats[ZERO]==dict(b2=9,b3=54,b4=96,rank3=9,rank4=45,betti3=0)
assert stats[(1,0)]==dict(b2=6,b3=54,b4=80,rank3=6,rank4=48,betti3=0)
for d in [(0,2),(1,2)]:
    assert stats[d]==dict(b2=4,b3=66,b4=80,rank3=4,rank4=61,betti3=1)

# Exact action of endpoint stabilizers on cohomology; signs on rank-one integral homology are identical.
SIGNS={}
for d in [(0,2),(1,2)]:
    b2,b3,b4=(basis(d,k) for k in (2,3,4))
    d3=boundary(b3,b2)
    d4=boundary(b4,b3)
    coboundary_rank=d3.rank()
    w=next(w for w in d4.T.nullspace() if d3.col_join(w.T).rank()>coboundary_rank)
    assert d4.T*w==Matrix.zeros(d4.cols,1)
    index3={c:j for j,c in enumerate(b3)}
    stab=[A for A in P if mat(A,d)==d]
    signs={}
    for A in stab:
        transformed=Matrix([w[index3[tuple(IDX[mat(A,V[z])] for z in c)]] for c in b3])
        found=[e for e in (-1,1) if d3.col_join((transformed-e*w).T).rank()==coboundary_rank]
        assert len(found)==1,(d,A,found)
        signs[A]=found[0]
    SIGNS[d]=signs
    assert set(signs.values())=={-1,1}
    assert len(stab)==12//len(O[d])
assert SIGNS[(0,2)]=={
    (1,0,0,1):1,(1,0,1,3):-1,(3,0,0,3):-1,(3,0,3,1):1
}
assert SIGNS[(1,2)]=={(1,0,0,1):1,(3,1,0,1):-1}
assert 16*(len(O[(0,2)])+len(O[(1,2)]))==144

# Compare independently generated results against the compact witness ledger.
from pathlib import Path
import json
cert=json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf8'))
for entry in cert['endpoint_chain_data']:
    key=tuple(entry['endpoint'])
    st=stats[key]
    assert entry['H3_free_rank']==st['betti3']
    assert entry['dimensions']=={'C2':st['b2'],'C3':st['b3'],'C4':st['b4']}
    assert entry['boundary_ranks']=={'d3':st['rank3'],'d4':st['rank4']}
    assert entry['nonzero_d3_smith_factors']==[1]*st['rank3']
    assert entry['nonzero_d4_smith_factors']==[1]*st['rank4']
for entry in cert['stabilizer_character']:
    key=tuple(entry['endpoint'])
    expected={tuple(v['matrix']):v['sign'] for v in entry['matrix_signs']}
    assert expected==SIGNS[key]
assert len(cert['endpoint_chain_data'])==4
print('VERIFY_SHRIKHANDE_INTEGRAL_MAGNITUDE_EQUIVARIANT_OK')
print('Representative endpoint Smith and homology data:',stats)
print('Signed stabilizer actions:',SIGNS)
print('Translation-restricted module: nine integral regular representations')
