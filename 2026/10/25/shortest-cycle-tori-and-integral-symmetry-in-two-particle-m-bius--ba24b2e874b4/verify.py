"""Exact integer verification of two-point configuration homology for GP(8,3).

Dependencies: Python >=3.10, SymPy >=1.12 and NetworkX >=3.0.
Run: python verify.py
All graphs, chains, cycles, and automorphisms are constructed here.
"""
from itertools import combinations
from collections import Counter
from math import prod
import networkx as nx
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 8
V = range(16)
EDGES = sorted({tuple(sorted((i, (i+1)%N))) for i in range(N)} |
               {tuple(sorted((i, 8+i))) for i in range(N)} |
               {tuple(sorted((8+i, 8+(i+3)%N))) for i in range(N)})
ADJ = [set() for _ in V]
for a,b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)
ZEROS = list(combinations(V, 2))
ONES = [(v,e) for v in V for e in EDGES if v not in e]
TWOS = [(e,f) for e,f in combinations(EDGES, 2) if set(e).isdisjoint(f)]
ZI, OI, TI = [{x:i for i,x in enumerate(seq)} for seq in (ZEROS,ONES,TWOS)]
D1 = Matrix.zeros(len(ZEROS),len(ONES))
D2 = Matrix.zeros(len(ONES),len(TWOS))
for col,(v,(a,b)) in enumerate(ONES):
    D1[ZI[tuple(sorted((v,b)))],col] += 1
    D1[ZI[tuple(sorted((v,a)))],col] -= 1
for col,(e,f) in enumerate(TWOS):
    a,b=e;c,d=f
    for x,coeff in [((b,f),1),((a,f),-1),((d,e),-1),((c,e),1)]:
        D2[OI[x],col] += coeff
assert (len(ZEROS),len(ONES),len(TWOS)) == (120,336,228)
assert D1*D2 == Matrix.zeros(len(ZEROS),len(TWOS))

def modrank(M,p):
    """Exact Gaussian elimination over a prime field; no floating point."""
    A=[[int(x)%p for x in M.row(i)] for i in range(M.rows)]
    rank=0
    for j in range(M.cols):
        k=next((i for i in range(rank,M.rows) if A[i][j]),None)
        if k is None: continue
        A[rank],A[k]=A[k],A[rank]
        inv=pow(A[rank][j],-1,p)
        for i in range(rank+1,M.rows):
            if A[i][j]:
                fac=A[i][j]*inv%p
                for h in range(j,M.cols):
                    A[i][h]=(A[i][h]-fac*A[rank][h])%p
        rank+=1
        if rank==M.rows:break
    return rank

def diag(M):
    H=smith_normal_form(M,domain=ZZ)
    return [abs(int(H[i,i])) for i in range(min(H.shape)) if H[i,i]]

def cycles():
    out=[]
    def grow(root,path):
        for w in sorted(ADJ[path[-1]]):
            if w==root:
                if len(path)>=3 and path[1]<path[-1]:out.append(tuple(path))
            elif w>root and w not in path:
                grow(root,path+[w])
    for root in V:
        for w in sorted(ADJ[root]):
            if w>root:grow(root,[root,w])
    return out

def oriented(c):
    result={}
    for k,a in enumerate(c):
        b=c[(k+1)%len(c)]
        e=tuple(sorted((a,b)))
        result[e]=1 if (a,b)==e else -1
    return result

def torus(c,d):
    v=[0]*len(TWOS)
    for e,x in oriented(c).items():
        for f,y in oriented(d).items():
            if e<f:v[TI[(e,f)]] += x*y
            else:v[TI[(f,e)]] -= x*y
    return v

def cyclekey(c):
    return frozenset(tuple(sorted((c[i],c[(i+1)%len(c)]))) for i in range(len(c)))

def pairkey(c,d):
    return frozenset((cyclekey(c),cyclekey(d)))

assert all(len(ADJ[i])==3 for i in V)
SIMPLE=cycles()
assert Counter(map(len,SIMPLE)) == Counter({6:24,8:30,10:96,12:100,14:144,16:6})
PAIRS=[(c,d) for i,c in enumerate(SIMPLE) for d in SIMPLE[i+1:] if set(c).isdisjoint(d)]
BYTYPE={typ:[(c,d) for c,d in PAIRS if tuple(sorted((len(c),len(d))))==typ]
        for typ in [(6,6),(6,8),(6,10),(8,8)]}
assert sum(map(len,BYTYPE.values()))==111
assert {k:len(v) for k,v in BYTYPE.items()} == {(6,6):60,(6,8):24,(6,10):24,(8,8):3}
assert modrank(D2,3)==208
assert Counter(diag(D2))==Counter({1:207,2:1})
assert modrank(D1,3)==119

G=nx.Graph();G.add_nodes_from(V);G.add_edges_from(EDGES)
AUTOS=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(AUTOS)==96

def orbits(pairs):
    keys={pairkey(c,d):i for i,(c,d) in enumerate(pairs)}
    remain=set(range(len(pairs)))
    groups=[]
    while remain:
        i=min(remain);c,d=pairs[i]
        group=set()
        for a in AUTOS:
            def move(c):
                return frozenset(tuple(sorted((a[x],a[y]))) for x,y in cyclekey(c))
            group.add(keys[frozenset((move(c),move(d)))])
        assert group <= set(range(len(pairs)))
        groups.append(sorted(group))
        remain -= group
    return groups

ORBIT66=orbits(BYTYPE[(6,6)])
assert sorted(map(len,ORBIT66)) == [12,48]
ORBIT48=next(o for o in ORBIT66 if len(o)==48)
ORBIT12=next(o for o in ORBIT66 if len(o)==12)

def matrix_for(pairs):
    return Matrix.hstack(*(Matrix(torus(c,d)) for c,d in pairs))

T48=matrix_for([BYTYPE[(6,6)][i] for i in ORBIT48])
assert all(D2*T48[:,j]==Matrix.zeros(len(ONES),1) for j in range(T48.cols))
assert Counter(diag(T48)) == Counter({1:20})
T12=matrix_for([BYTYPE[(6,6)][i] for i in ORBIT12])
assert Counter(diag(T12)) == Counter({1:12})

# An explicit integral basis, not just a rank-20 matrix:
# Select independent columns and 20 coordinate rows over F_101 and check det = +/-1.
def independent_rows(M,p=101):
    basis={};which=[]
    for r in range(M.rows):
        q=[int(x)%p for x in M.row(r)]
        for pivot,z in sorted(basis.items()):
            if q[pivot]:
                f=q[pivot]
                q=[(x-f*y)%p for x,y in zip(q,z)]
        nz=next((j for j,x in enumerate(q) if x),None)
        if nz is not None:
            s=pow(q[nz],-1,p)
            basis[nz]=[(s*x)%p for x in q]
            which.append(r)
    return which

basis_cols=independent_rows(T48.T)
assert len(basis_cols)==20
B=T48[:,basis_cols]
rows=independent_rows(B)
assert len(rows)==20
Bminor=B[rows,:]
assert abs(Bminor.det())==1
assert D2*B == Matrix.zeros(D2.rows,20)
# Since H_2 = ker D_2 has rank <= 20 and is primitive in C_2,
# these 20 independent primitive columns are a Z-basis of H_2.

EXPECTED={(6,6):(20,()),(6,8):(19,(2,2,2)),(6,10):(19,(2,2,2,2,2)),(8,8):(3,())}
for typ,pairs in BYTYPE.items():
    T=matrix_for(pairs)
    assert D2*T==Matrix.zeros(D2.rows,T.cols)
    d=diag(T)
    assert (len(d),tuple(x for x in d if x!=1))==EXPECTED[typ]
    print('TORUS_TYPE',typ,'COUNT',len(pairs),'RANK',len(d),'SMITH_NONUNITS',tuple(x for x in d if x!=1))

# Every group automorphism permutes the oriented cubical cells with incidence signs.
# H_1(X;Q) -> H_1(G;Q) is an equivariant isomorphism: the natural
# sum-of-particle-trajectories map is surjective since the 24 graph hexagon
# classes generate H_1(G;Z) and each hexagon may be traced by one particle
# with the other particle parked at a vertex outside that hexagon.
EDGE_I={e:i for i,e in enumerate(EDGES)}
CGRAPH=Matrix.zeros(len(EDGES),24)
for j,c in enumerate(c for c in SIMPLE if len(c)==6):
    for e,v in oriented(c).items():CGRAPH[EDGE_I[e],j]=v
assert Counter(diag(CGRAPH)) == Counter({1:9})
# The connectedness and b_1=9 follow from D1 and D2 Smith data.
trace_counts=Counter()
for a in AUTOS:
    c0=sum(tuple(sorted((a[u],a[v])))==(u,v) for u,v in ZEROS)
    vertex=sum(a[u]==u for u in V)
    ce=0
    for e in EDGES:
        image=(a[e[0]],a[e[1]])
        if tuple(sorted(image))==e:
            ce += (1 if image==e else -1)
    c1=0
    for v,e in ONES:
        image=(a[e[0]],a[e[1]])
        if a[v]==v and tuple(sorted(image))==e:
            c1 += (1 if image==e else -1)
    c2=0
    for e,f in TWOS:
        ep=(a[e[0]],a[e[1]]);fp=(a[f[0]],a[f[1]])
        es=tuple(sorted(ep));fs=tuple(sorted(fp))
        if tuple(sorted((es,fs)))==(e,f):
            c2 += (1 if ep==es else -1)*(1 if fp==fs else -1)*(1 if es<fs else -1)
    trace_counts[c2-c1+c0+ce-vertex] += 1
assert trace_counts==Counter({0:66,2:16,-4:13,20:1})
assert sum(k*v for k,v in trace_counts.items()) == 0
print('GRAPH',len(V),len(EDGES),'DISCRETIZED_CELLS',len(ZEROS),len(ONES),len(TWOS))
print('BOUNDARY_D2_SMITH',Counter(diag(D2)),'H1_Z9_PLUS_Z2','H2_RANK',len(basis_cols))
print('GIRTH',min(map(len,SIMPLE)),'SIMPLE_CYCLES',len(SIMPLE),'DISJOINT_TORI',len(PAIRS))
print('AUTOMORPHISMS',len(AUTOS),'HEXAGON_TORUS_ORBITS',tuple(sorted(map(len,ORBIT66))))
print('FORTY_EIGHT_ORBIT_BASIS_COLS',tuple(basis_cols))
print('UNIT_MINOR_ROW_INDICES',tuple(rows),'DETERMINANT',int(Bminor.det()))
print('H2_CHARACTER_TRACE_MULTIPLICITIES',dict(sorted(trace_counts.items())))
print('FULL_AUTOMORPHISM_INVARIANT_RANK',0)
print('VERIFY_OK_MOBIUS_KANTOR_TWO_POINT_INTEGRAL_HEXAGON_TORI')
