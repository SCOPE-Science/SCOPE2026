#!/usr/bin/env python3
"""Exact verification of the dodecahedral degree-three sampling theorem.

Only Python standard-library arithmetic is used. All Q(phi) operations are exact.
The proof and definitions of the graph rank formula appear in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter

class Q:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        if isinstance(a, Q): self.a, self.b = a.a, a.b
        else: self.a, self.b = F(a), F(b)
    @staticmethod
    def coerce(x): return x if isinstance(x, Q) else Q(x)
    def __add__(self, other):
        other=Q.coerce(other);return Q(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self, other): return self+(-Q.coerce(other))
    def __rsub__(self, other): return Q.coerce(other)-self
    def __mul__(self, other):
        other=Q.coerce(other)
        return Q(self.a*other.a+self.b*other.b,
                 self.a*other.b+self.b*other.a+self.b*other.b)
    __rmul__=__mul__
    def __truediv__(self, other):
        other=Q.coerce(other)
        a,b=other.a,other.b
        norm=a*a+a*b-b*b
        if not norm: raise ZeroDivisionError
        return self*Q((a+b)/norm,-b/norm)
    def __pow__(self, n):
        if n<0:return (Q(1)/self)**(-n)
        z=Q(1);u=self
        while n:
            if n&1:z=z*u
            u=u*u;n//=2
        return z
    def __eq__(self, other):
        other=Q.coerce(other);return self.a==other.a and self.b==other.b
    def __bool__(self):return bool(self.a or self.b)
    def __repr__(self):return f"({self.a})+({self.b})*phi"

def det(A):
    A=[[Q(x) if not isinstance(x,Q) else x for x in row] for row in A]
    n=len(A);assert all(len(row)==n for row in A)
    d=Q(1)
    for j in range(n):
        r=next((i for i in range(j,n) if A[i][j]),None)
        if r is None:return Q(0)
        if r!=j: A[j],A[r]=A[r],A[j];d=-d
        t=A[j][j];d=d*t
        for i in range(j+1,n):
            if A[i][j]:
                v=A[i][j]/t
                for k in range(j+1,n):A[i][k]=A[i][k]-v*A[j][k]
                A[i][j]=Q(0)
    return d

def rank(A):
    if not A:return 0
    A=[[Q(x) if not isinstance(x,Q) else x for x in row] for row in A]
    m,n=len(A),len(A[0]);r=0
    for j in range(n):
        if r>=m:break
        i=next((i for i in range(r,m) if A[i][j]),None)
        if i is None:continue
        A[r],A[i]=A[i],A[r];v=A[r][j]
        for k in range(j,n):A[r][k]=A[r][k]/v
        for i in range(r+1,m):
            v=A[i][j]
            if v:
                for k in range(j,n):A[i][k]=A[i][k]-v*A[r][k]
        r+=1
    return r

phi=Q(0,1);inv=phi-Q(1)
X=[]
for a,b,c in product((-1,1), repeat=3):X.append((Q(a),Q(b),Q(c)))
for s,t in product((-1,1), repeat=2):
    X.extend([(Q(0),s*inv,t*phi),(s*inv,t*phi,Q(0)),(s*phi,Q(0),t*inv)])
assert len(X)==len(set((repr(a),repr(b),repr(c)) for a,b,c in X))==20
assert all(x*x+y*y+z*z==3 for x,y,z in X)
pairs=[]
for i,u in enumerate(X):
    j=next(j for j,v in enumerate(X) if all(v[k]==-u[k] for k in range(3)))
    if i<j:pairs.append((i,j))
assert len(pairs)==10
Y=[X[i] for i,j in pairs]
assert {i for pair in pairs for i in pair}==set(range(20))

def monom(u,p):return u[0]**p[0]*u[1]**p[1]*u[2]**p[2]
odd=[(a,b,c) for c in range(2) for a in range(4) for b in range(4)
     if a+b+c<=3 and (a+b+c)%2==1]
assert len(odd)==10
O=[[monom(u,m) for m in odd] for u in Y]
assert det(O)==1024, 'Odd polynomial evaluations must span ten antipodal-odd values.'
even=[(0,0,0),(2,0,0),(0,2,0),(1,1,0),(1,0,1),(0,1,1)]
E=[[monom(u,m) for m in even] for u in Y]
assert det(E[:6])==32, 'Quadratic even evaluation rank is six.'

B=[[0]*10 for _ in range(10)]
for i,j in combinations(range(10),2):
    dot=sum(Y[i][k]*Y[j][k] for k in range(3))
    assert dot*dot==Q(1) or dot*dot==Q(5)
    if dot*dot==Q(5):B[i][j]=B[j][i]=1
assert all(sum(row)==3 for row in B)
assert all(sum(B[i][k]*B[k][j] for k in range(10)) ==
           2*(i==j)-B[i][j]+1 for i in range(10) for j in range(10))

# Explicit isomorphism between the ten antipodal pairs and edges of K_5.
edge_labels=[(1,2),(1,3),(1,4),(1,5),(3,4),(4,5),(3,5),(2,5),(2,3),(2,4)]
assert all(B[i][j]==int(not(set(edge_labels[i])&set(edge_labels[j])))
           for i in range(10) for j in range(10) if i!=j)
# The six even polynomial columns occupy the Petersen adjacency 3- and 1-eigenspaces.
EV=[[Q(1),u[0]*u[0]-1,u[1]*u[1]-1,u[0]*u[1],u[0]*u[2],u[1]*u[2]] for u in Y]
assert all(sum(B[i][j]*EV[j][k] for j in range(10))==(3 if k==0 else 1)*EV[i][k]
           for i in range(10) for k in range(6))
# Projector onto eigenvalue -2: (5I-5B+J)/15. It is also the
# Gram matrix of centered incidence vectors of edges of K_5, divided by 3.
for i,j in product(range(10), repeat=2):
    dot=sum((int(a in edge_labels[i])-F(2,5))*(int(a in edge_labels[j])-F(2,5))
            for a in range(1,6))
    assert dot==F(5*(i==j)-5*B[i][j]+1,5)
# More explicitly, dot = (5I-5B+J)/5 and P = dot/3.

# Determinants of all 4-by-4 principal submatrices of 15 P = 5I-5B+J.
types=Counter()
for S in combinations(range(10),4):
    d=tuple(sorted(sum(B[i][j] for j in S) for i in S))
    edges=sum(B[i][j] for i,j in combinations(S,2))
    H=[[Q(5*(i==j)-5*B[S[i]][S[j]]+1) for j in range(4)] for i in range(4)]
    D=det(H)
    assert D.b==0 and D.a.denominator==1
    types[(edges,d,int(D.a))]+=1
expected={
  (0,(0,0,0,0),1125):5,
  (1,(0,0,1,1),500):60,
  (2,(0,1,1,2),125):60,
  (2,(1,1,1,1),0):15,
  (3,(1,1,1,3),0):10,
  (3,(1,1,2,2),125):60,
}
assert dict(types)==expected,(types,expected)

# For ANY erasure subset T, with S the touched antipodal pairs,
# rank of the remaining sampling map is 16-|T|+rank(projected edge vectors on S).
# The latter rank equals 5 - number of bipartite components - delta,
# where delta=1 precisely if every bipartite component has equal part sizes.
def graph_rank(S):
    edge_set=[edge_labels[i] for i in S]
    adj={i:set() for i in range(1,6)}
    for u,v in edge_set:adj[u].add(v);adj[v].add(u)
    unseen=set(range(1,6));bip=0;delta=1
    while unseen:
        root=min(unseen);queue=[root];side={root:0};unseen.remove(root);ok=True
        for u in queue:
            for v in adj[u]:
                if v not in side:
                    side[v]=1-side[u];queue.append(v);unseen.remove(v)
                elif side[v]==side[u]:ok=False
        if ok:
            bip+=1
            if sum(z==0 for z in side.values())!=sum(z==1 for z in side.values()):delta=0
    return 5-bip-delta

for mask in range(1<<10):
    S=[i for i in range(10) if mask>>i&1]
    centered=[[Q(5*int(v in edge_labels[i])-2) for v in range(1,6)] for i in S]
    assert rank(centered)==graph_rank(S),(mask,rank(centered),graph_rank(S))

rank4_counts=Counter()
for T in combinations(range(20),4):
    S={i for i,pair in enumerate(pairs) if any(j in T for j in pair)}
    r=16-len(T)+graph_rank(S)
    rank4_counts[r]+=1
assert dict(rank4_counts)=={16:2960,15:1840,14:45},rank4_counts
print('EXACT_VERIFY_OK')
print('antipodal pairs:',pairs)
print('odd 10x10 determinant in Q(phi):',det(O))
print('even 6x6 minor:',det(E[:6]))
print('four-pair induced graph determinant table:',sorted(expected.items()))
print('four-erasure reconstruction ranks:',sorted(rank4_counts.items()))
print('all 1024 projected edge-subset ranks independently verified')
