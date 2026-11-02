"""Exact-rational verification of the Petersen graph edge-gradient projection."""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import Counter

V = list(combinations(range(5), 2))
E = [(i,j) for i in range(10) for j in range(i+1,10)
     if not set(V[i]).intersection(V[j])]
assert len(V)==10 and len(E)==15
B = [[F((j==v)-(i==v)) for v in range(10)] for i,j in E]
A = [[F(0) for _ in V] for _ in V]
for i,j in E:
    A[i][j]=A[j][i]=F(1)

def matrix_rank(rows):
    X = [[F(v) for v in row] for row in rows]
    piv=0
    for col in range(len(X[0])):
        k = next((t for t in range(piv,len(X)) if X[t][col]), None)
        if k is None: continue
        X[piv],X[k]=X[k],X[piv]
        factor=X[piv][col]
        X[piv]=[v/factor for v in X[piv]]
        for h in range(len(X)):
            if h!=piv and X[h][col]:
                c=X[h][col];X[h]=[x-c*y for x,y in zip(X[h],X[piv])]
        piv+=1
        if piv==len(X): break
    return piv

assert matrix_rank(B)==9

def gradient(h):
    return [h[j]-h[i] for i,j in E]

# On mean-zero vertex vectors, the inverse Laplacian is (4I+A)/10,
# since the graph is strongly regular with adjacency identity A^2=2I-A+J.
for i in range(10):
    for j in range(10):
        assert sum(A[i][k]*A[k][j] for k in range(10)) == F(2*(i==j))-A[i][j]+1

def potential(i,j):
    b=[F((v==j)-(v==i)) for v in range(10)]
    return [(4*b[v]+sum(A[v][w]*b[w] for w in range(10)))/10
            for v in range(10)]

P=[gradient(potential(i,j)) for i,j in E]
assert all(sum(abs(x) for x in row)==F(11,5) for row in P)
assert all(Counter(abs(x) for x in row)==
           Counter({F(3,5):1,F(1,5):4,F(1,10):8,F(0):2}) for row in P)
for i in range(15):
    for v in range(10):
        assert sum(P[i][j]*B[j][v] for j in range(15))==B[i][v]
    for j in range(15):
        assert sum(P[i][k]*P[k][j] for k in range(15))==P[i][j]
        assert P[i][j]==P[j][i]

# Enumerate signed edge-permutation actions of all 120 automorphisms.
group=[]
for g in permutations(range(5)):
    action=[V.index(tuple(sorted(g[v] for v in s))) for s in V]
    edge_action=[]
    for i,j in E:
        aa,bb=action[i],action[j]
        edge_action.append((E.index(tuple(sorted((aa,bb)))), F(1 if aa<bb else -1)))
    group.append(edge_action)
assert len(group)==120

# Matrix U_g sends the oriented edge gradient of a function f to that of g.f.
# Check that Hodge projection commutes with this signed action.
for action in group:
    for i in range(15):
        dest,sgn=action[i]
        for j in range(15):
            destj,sgnj=action[j]
            assert P[dest][destj]*sgnj==sgn*P[i][j]

# The signed base-edge stabilizer has fixed-row dimension exactly three.
# In the row convention U_g e_f = sign(g,f) e_{g f}, the stabilizer
# condition is q U_g = sign(g,e0) q.
H=[act for act in group if act[0][0]==0]
assert len(H)==8
rows=[]
for act in H:
    eps=act[0][1]
    for j in range(15):
        r=[F(0)]*15
        for f,(dest,sgn) in enumerate(act):
            if f==j:
                r[dest]+=sgn
        r[j]-=eps
        rows.append(r)
assert matrix_rank(rows)==12

base=E[0]; neighbors=set()
for f,(i,j) in enumerate(E):
    if f and (i in base or j in base): neighbors.add(f)
assert len(neighbors)==4
remote=set(f for f in range(15) if f not in neighbors and f!=0 and P[0][f]!=0)
assert len(remote)==8
missing=set(range(15))-neighbors-remote-{0}
assert len(missing)==2

basis=[]
for orbit in [{0},neighbors,remote]:
    basis.append([F(1 if P[0][f]>0 else (-1 if P[0][f]<0 else 0)) if f in orbit else F(0)
                  for f in range(15)])
for q in basis:
    assert all(sum(a*b for a,b in zip(r,q))==0 for r in rows)

# The qB constraints, together with trace nine and edge transitivity,
# determine the unique equivariant retraction.
q0,q1,q2=basis
v0=[sum(q0[f]*B[f][v] for f in range(15)) for v in range(10)]
v1=[sum(q1[f]*B[f][v] for f in range(15)) for v in range(10)]
v2=[sum(q2[f]*B[f][v] for f in range(15)) for v in range(10)]
assert v0==B[0]
assert v1[base[0]]==-2 and v1[base[1]]==2
assert all(v1[i]==0 for i in range(10) if i not in base and A[i][base[0]]==0 and A[i][base[1]]==0)
assert v2[base[0]]==0 and v2[base[1]]==0
for v in range(10):
    if v not in base:
        assert v1[v]+F(1,2)*v2[v]==0
# Thus for a q=a*q0+b*q1+c*q2 with qB=B_e,
# a+2b=1 and b=2c. Equivariance and tr(Q)=9 imply 15a=9.
a,b,c=F(3,5),F(1,5),F(1,10)
assert a+2*b==1 and b==2*c and 15*a==9
assert [a*q0[j]+b*q1[j]+c*q2[j] for j in range(15)]==P[0]
print('CHECK_OK automorphisms=120 signed_stabilizer_rank=12 '
      'hodge_rows=15 rational_projector_identities=yes')
