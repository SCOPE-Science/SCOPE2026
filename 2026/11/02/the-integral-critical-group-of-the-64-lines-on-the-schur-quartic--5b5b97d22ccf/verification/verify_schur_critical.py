#!/usr/bin/env python3
"""Reconstruct the 64 Schur lines from Bauer--Schmitz and certify their critical group."""
from fractions import Fraction as Q
from collections import Counter
from itertools import combinations

class E:
    """Exact Q(omega,i), omega^2+omega+1=0 and i^2+1=0."""
    __slots__=('v',)
    def __init__(self,v=0):
        if isinstance(v,E): v=v.v
        elif isinstance(v,(int,Q)):v=(v,0,0,0)
        self.v=tuple(map(Q,v))
    def __add__(self,o):return E(tuple(a+b for a,b in zip(self.v,E(o).v)))
    __radd__=__add__
    def __neg__(self):return E(tuple(-a for a in self.v))
    def __sub__(self,o):return self+-E(o)
    def __rsub__(self,o):return E(o)+-self
    def __mul__(self,o):
        a,b,c,d=self.v; e,f,g,h=E(o).v
        def pair(u,v,w,z):return (u*w-v*z,u*z+v*w-v*z)
        x,y=pair(a,b,e,f);z,t=pair(c,d,g,h)
        p,q=pair(a,b,g,h);r,s=pair(c,d,e,f)
        return E((x-z,y-t,p+r,q+s))
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        x=E(1)
        while n:
            if n&1:x=x*self
            self=self*self;n>>=1
        return x
    def __eq__(self,o):return self.v==E(o).v
    def __bool__(self):return any(self.v)

Z,O,W,I=E(0),E(1),E((0,1,0,0)),E((0,0,1,0))
eta=I*(-(O+2*W))*Q(1,3)
assert W**3==O and I**2==-O and eta**2==E(Q(1,3))
roots=[Z,O,W,W**2]
T=[[[O,Z],[Z,O]],[[-O,W],[2*W**2,O]],[[-O,W**2],[2*W,O]],[[-O,O],[E(2),O]]]
lines=[('A',a,b) for a in roots for b in roots]
for k in range(3):
    for j,t in enumerate(T):
        m=[[W**k*t[0][0],W**k*t[0][1]],[t[1][0],t[1][1]]]
        for s in range(4):
            lam=I**s*W**((3-k)%3)*(eta if j else O)
            lines.append(('B',[[lam*m[r][c] for c in range(2)] for r in range(2)]))
assert len(lines)==64

def det2(a,b,c,d):return a*d-b*c

def meets(u,v):
    if u[0]=='A' and v[0]=='A':return u[1]==v[1] or u[2]==v[2]
    if u[0]=='B' and v[0]=='A':u,v=v,u
    if u[0]=='A':
        a,b=u[1:];m=v[1]
        x=m[0][0]*a+m[0][1];y=m[1][0]*a+m[1][1]
        return det2(b,O,x,y)==Z
    m,n=u[1],v[1]
    return det2(m[0][0]-n[0][0],m[0][1]-n[0][1],m[1][0]-n[1][0],m[1][1]-n[1][1])==Z

A=[[0]*64 for _ in range(64)]
for a,b in combinations(range(64),2):
    if meets(lines[a],lines[b]):A[a][b]=A[b][a]=1
assert all(sum(row)==18 for row in A)
assert sum(map(sum,A))//2==576

# Check published adjacency spectrum without numerical floating point:
# squarefree annihilating polynomial plus five exact traces.
def matrix_mult(x,y):
    n=len(x); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,v in enumerate(x[i]):
            if v:
                for j,z in enumerate(y[k]):
                    if z:out[i][j]+=v*z
    return out

def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]
roots_spectrum=[18,2,-4,-6,-10]
expected_mult=[1,44,8,9,2]
power=identity(64);mom=[]
for k in range(5):
    mom.append(sum(power[i][i] for i in range(64)))
    power=matrix_mult(power,A)
assert mom==[64,0,1152,1728,139392]
for k,m in enumerate(mom):
    assert m==sum(roots_spectrum[j]**k*expected_mult[j] for j in range(5))
product=identity(64)
for root in roots_spectrum:
    B=[[(A[i][j]-root*int(i==j)) for j in range(64)] for i in range(64)]
    product=matrix_mult(product,B)
assert all(x==0 for row in product for x in row)
print('GRAPH_AND_SPECTRUM_OK: 64 vertices; 576 edges; eigenvalues 18^1,2^44,(-4)^8,(-6)^9,(-10)^2')

# Delete one vertex: graph Jac = coker of reduced 63x63 Laplacian.
L=[[18*int(i==j)-A[i][j] for j in range(63)] for i in range(63)]

def padic_profile(M0,p,precision=16):
    """Elementary row/column pivoting over Z/p^precision; divide residual block by p."""
    mod=p**precision;M=[[v%mod for v in row] for row in M0]
    n=len(M);lev=0;prof=Counter()
    while n:
        r=0
        while r<n:
            pivot=None
            for i in range(r,n):
                for j in range(r,n):
                    if M[i][j]%p:
                        pivot=i,j;break
                if pivot is not None:break
            if pivot is None:break
            i,j=pivot
            M[i],M[r]=M[r],M[i]
            for row in M:row[j],row[r]=row[r],row[j]
            inv=pow(M[r][r],-1,mod)
            for i in range(r+1,n):
                alpha=M[i][r]*inv%mod
                if alpha:
                    for j in range(r+1,n):
                        M[i][j]=(M[i][j]-alpha*M[r][j])%mod
            r+=1
        prof[lev]+=r
        n-=r
        if n:
            assert all(M[i][j]%p==0 for i in range(r,r+n) for j in range(r,r+n))
            M=[[M[i][j]//p for j in range(r,r+n)] for i in range(r,r+n)]
            mod//=p
            assert mod>p, 'insufficient p-adic precision'
            lev+=1
    return {e:v for e,v in sorted(prof.items()) if v}

expect={2:{0:18,2:2,4:32,5:1,6:2,7:6,9:2},
        3:{0:54,1:9},7:{0:61,1:2},11:{0:55,1:8}}
for p,ref in expect.items():
    got=padic_profile(L,p)
    assert got==ref,(p,got)
    print('PADIC_SNF_OK:',p,got)

# Matrix-tree theorem with independently certified adjacency spectrum.
# The product of all nonzero Laplacian eigenvalues is
# 16^44 * 22^8 * 24^9 * 28^2; divide by 64.
order=(16**44)*(22**8)*(24**9)*(28**2)//64
assert order==2**209*3**9*7**2*11**8
assert order==__import__('math').prod(p**sum(e*mult for e,mult in d.items()) for p,d in expect.items())
print('ORDER_OK:',order)
snf=[1]*18+[4]*2+[16]*32+[32,64,192]+[4224]*6+[118272]*2
assert len(snf)==63 and all(b%a==0 for a,b in zip(snf,snf[1:]))
assert __import__('math').prod(snf)==order
print('INVARIANT_FACTORS_OK: 1^18,4^2,16^32,32,64,192,4224^6,118272^2')
print('VERIFY_OK')
