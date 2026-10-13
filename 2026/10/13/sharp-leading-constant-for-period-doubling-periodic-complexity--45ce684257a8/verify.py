#!/usr/bin/env python3
from functools import lru_cache
from math import floor, log2

M0=((1,0,0,0,0,0),(0,0,0,1,0,1),(0,0,0,0,0,2),(0,0,0,0,1,0),(0,0,0,1,0,1),(0,0,0,0,0,0))
M1=((0,1,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,0),(0,1,1,0,0,0),(0,1,1,0,0,0),(0,0,2,0,0,0))
v=(1,0,0,0,0,0); w=(1,1,1,1,1,1)

def rv(r,M): return tuple(sum(r[i]*M[i][j] for i in range(6)) for j in range(6))
def cv(M,c): return tuple(sum(M[i][j]*c[j] for j in range(6)) for i in range(6))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
@lru_cache(None)
def row(n):
    if n==0: return v
    return rv(row(n>>1), M1 if n&1 else M0)
@lru_cache(None)
def p(n): return dot(row(n),w)

def pd_word(N):
    s='0'
    while len(s)<N: s=''.join('01' if c=='0' else '00' for c in s)
    return s[:N]
def direct_lp(s,i,cap):
    left=s[:i]
    for r in range(1,cap+1):
        u=s[i:i+r]
        if len(u)<r: break
        if left.endswith(u) or u.endswith(left): return r
    raise AssertionError((i,cap))

# Direct definition check against the published six-dimensional representation.
s=pd_word(4096)
for i in range(128): assert direct_lp(s,i,1024)==p(i)
assert [p(i) for i in range(16)]==[1,2,4,1,1,8,2,2,2,2,16,1,1,4,4,1]

M=tuple(tuple(M0[i][j]+M1[i][j] for j in range(6)) for i in range(6))
c=tuple(sum((M[i][j]-(2 if i==j else 0))*w[j] for j in range(6)) for i in range(6))
states=[
(1,1,0,1,2,0,-1),(1,1,0,2,1,0,-1),(1,2,0,1,1,0,-1),
(1,2,0,1,2,0,-1),(1,1,0,1,1,0,-1),(2,1,0,2,2,0,-1),(2,2,0,2,2,0,-1)]
trans=[(1,2),(3,4),(4,5),(1,6),(4,4),(6,2),(6,6)]
out=[0,0,0,0,0,1,1]
assert c+(-1,)==states[0]
for j,x in enumerate(states):
    for bit,Mb in enumerate((M0,M1)):
        assert cv(Mb,x[:6])+(x[6],)==states[trans[j][bit]]
    assert dot(v,x[:6])+x[6]==out[j]
@lru_cache(None)
def ks(st,n): return out[st] if n==0 else ks(trans[st][n&1],n>>1)
def q(n): return ks(0,n)
def a(n): return ks(1,n)
def b(n): return ks(2,n)

for n in range(20000):
    assert p(2*n)+p(2*n+1)-2*p(n)-1==q(n) in (0,1)
    assert q(2*n)==a(n) and q(2*n+1)==b(n)
    assert b(2*n)==0 and b(2*n+1)==1-b(n)
    assert a(2*n+1)==0
    if n: assert a(2*n)==1-a(n)

N=50000
P=[0]*(2*N+1); Q=[0]*(N+1)
for i in range(2*N): P[i+1]=P[i]+p(i)
for i in range(N): Q[i+1]=Q[i]+q(i)
for n in range(1,N+1):
    L=floor(log2(n))+1
    e=3*Q[n]-n
    assert abs(e)<=5*L
    assert P[2*n]-2*P[n]==n+Q[n]
    assert abs(3*(P[2*n]-2*P[n])-4*n)<=5*L
for ell in range(16):
    n=1<<ell
    assert 18*P[n]==(10+12*ell)*n+9-((-1)**ell)
for n in (1000,4096,10000,32768,50000):
    h=P[n]/n
    assert abs(h-(2/3)*log2(n)) < 3*max(1.0,log2(max(2.0,log2(n))))
print('VERIFY_OK direct_local_period_i<128 kernel_states=7 kernel_n<20000 discrepancy_n<=50000 doubling_identity_n<=50000 dyadic_formula_ell<=15')
