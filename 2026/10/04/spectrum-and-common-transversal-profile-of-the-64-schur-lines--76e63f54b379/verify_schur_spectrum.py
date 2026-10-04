#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations, combinations
from collections import Counter, deque

class K:
    """Exact Q(i,sqrt(3)) element a+b*i+c*r+d*i*r, with r^2=3."""
    __slots__ = ('a','b','c','d')
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a,self.b,self.c,self.d = map(F,(a,b,c,d))
    def __add__(self,o):
        o=C(o); return K(self.a+o.a,self.b+o.b,self.c+o.c,self.d+o.d)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b,-self.c,-self.d)
    def __sub__(self,o): return self+(-C(o))
    def __rsub__(self,o): return C(o)-self
    def __mul__(self,o):
        o=C(o); a,b,c,d=self.a,self.b,self.c,self.d; e,f,g,h=o.a,o.b,o.c,o.d
        return K(a*e-b*f+3*c*g-3*d*h,
                 a*f+b*e+3*c*h+3*d*g,
                 a*g+c*e-b*h-d*f,
                 a*h+d*e+b*g+c*f)
    __rmul__=__mul__
    def __pow__(self,n):
        if n < 0: raise ValueError('nonnegative exponents only')
        out=K(1); x=self
        while n:
            if n & 1: out=out*x
            x=x*x; n//=2
        return out
    def __eq__(self,o):
        o=C(o); return (self.a,self.b,self.c,self.d)==(o.a,o.b,o.c,o.d)
def C(x): return x if isinstance(x,K) else K(x)

ZERO,ONE,I,R=K(),K(1),K(0,1),K(0,0,1)
XI=K(F(-1,2),0,0,F(1,2))
ETA=R*F(1,3)
assert XI**3 == ONE and I**2 == K(-1) and R**2 == K(3)

def det4(M):
    s=ZERO
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        t=ONE
        for i in range(4): t=t*M[i][p[i]]
        s = s-t if inv & 1 else s+t
    return s

# Bauer--Schmitz parametrization, Proposition 2.2 and the preceding table.
a_vals=[ZERO,ONE,XI,XI**2]
lines=[]
for a in a_vals:
    for b in a_vals:
        lines.append([[K(-1),a,ZERO,ZERO],[ZERO,ZERO,K(-1),b]])
T=[
    [[ONE,ZERO],[ZERO,ONE]],
    [[K(-1),XI],[K(2)*(XI**2),ONE]],
    [[K(-1),XI**2],[K(2)*XI,ONE]],
    [[K(-1),ONE],[K(2),ONE]],
]
for k in range(3):
    Z=[[XI**k,ZERO],[ZERO,ONE]]
    for j in range(4):
        M=[[sum((Z[r][q]*T[j][q][c] for q in range(2)),ZERO)
            for c in range(2)] for r in range(2)]
        for m in range(4):
            lam=(I**m)*(XI**((3-k)%3))
            if j>0: lam=lam*ETA
            a,b=M[0]; c,d=M[1]
            lines.append([[lam*a,lam*b,K(-1),ZERO],
                          [lam*c,lam*d,ZERO,K(-1)]])
assert len(lines)==64

# Two projective lines given by two independent linear equations each meet iff
# the stacked 4-by-4 coefficient determinant vanishes.
A=[[0]*64 for _ in range(64)]
for x,y in combinations(range(64),2):
    if det4(lines[x]+lines[y]) == ZERO:
        A[x][y]=A[y][x]=1
assert Counter(map(sum,A)) == Counter({18:64})
assert sum(map(sum,A))//2 == 576

# Connectedness and diameter.
diameter=0
for s in range(64):
    dist=[-1]*64; dist[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v,e in enumerate(A[u]):
            if e and dist[v] < 0:
                dist[v]=dist[u]+1; q.append(v)
    assert -1 not in dist
    diameter=max(diameter,max(dist))
assert diameter == 2

adj,non=Counter(),Counter()
for i,j in combinations(range(64),2):
    common=sum(A[i][k] and A[j][k] for k in range(64))
    (adj if A[i][j] else non)[common]+=1
assert adj == Counter({2:432,0:144})
assert non == Counter({6:648,7:384,4:240,8:144,10:24})

def mm(X,Y):
    n,m,q=len(X),len(Y),len(Y[0])
    return [[sum(X[i][k]*Y[k][j] for k in range(m)) for j in range(q)] for i in range(n)]
def shift(X,c):
    Y=[row[:] for row in X]
    for i in range(len(Y)): Y[i][i]+=c
    return Y
I64=[[int(i==j) for j in range(64)] for i in range(64)]

# Exact squarefree annihilator certificate.
P=I64
roots=[18,2,-4,-6,-10]
for root in roots:
    P=mm(P,shift(A,-root))
assert all(v==0 for row in P for v in row)

# Trace moments determine multiplicities uniquely because the roots are distinct.
Apow=I64; traces=[]
for _ in range(5):
    traces.append(sum(Apow[i][i] for i in range(64)))
    Apow=mm(Apow,A)
assert traces == [64,0,1152,1728,139392]
mult=[1,44,8,9,2]
for k,t in enumerate(traces):
    assert sum(m*(r**k) for r,m in zip(roots,mult)) == t

print('vertices=64 edges=576 degree=18 diameter=2')
print('adjacent_common_neighbors=',dict(sorted(adj.items())))
print('skew_common_neighbors=',dict(sorted(non.items())))
print('adjacency_spectrum=',list(zip(roots,mult)))
print('intersection_spectrum=',[(16,1),(0,44),(-6,8),(-8,9),(-12,2)])
print('VERIFY_OK')
