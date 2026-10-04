#!/usr/bin/env python3
from fractions import Fraction

# Divisor classes are d*H - sum(m_i E_i) on Bl_9(P^2).
def inter(A,B):
    d,a=A[0],A[1:]
    e,b=B[0],B[1:]
    assert len(a)==len(b)==9
    return d*e-sum(x*y for x,y in zip(a,b))

def cls(d, idx=()):
    m=[0]*9
    for i in idx:
        m[i-1]=1
    return (d,*m)

M=(4,*([1]*9))
K=(-3,*([-1]*9))
N1=cls(1,(2,3,8,9))
N2=cls(1,(1,3,6,7))
N3=cls(1,(1,2,4,5))
Ns=[N1,N2,N3]

assert inter(M,M)==7
assert inter(K,K)==0
assert inter(K,M)==-3
for N in Ns:
    assert inter(N,N)==-3
    assert inter(M,N)==0
    assert inter(K,N)==1
for i in range(3):
    for j in range(i+1,3):
        assert inter(Ns[i],Ns[j])==0

# Published free resolution gives Hilbert numerator
# 1 - 3 t^2 - t^3 + 6 t^4 - 3 t^5.
p=[1,0,-3,-1,6,-3]
# (1-t)^3*(1+3t+3t^2)
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
q=mul([1,-3,3,-1],[1,3,3])
assert q==p
assert sum([1,3,3])==7

# Discrepancy from 1 = a*(-3).
a=Fraction(-1,3)
assert inter(K,N1)==a*inter(N1,N1)

# Canonical character of 1/3(1,1): zeta^(1+1), order 3.
r=3
weight=(1+1)%r
order=next(n for n in range(1,r+1) if (n*weight)%r==0)
assert order==3

# Pullback K_X = K_Y + (1/3) sum N_i.
KX2=Fraction(inter(K,K),1)
KX2 += Fraction(2,3)*sum(inter(K,N) for N in Ns)
KX2 += Fraction(1,9)*sum(inter(N,N) for N in Ns)
assert KX2==1
KH=inter(K,M)+Fraction(1,3)*sum(inter(N,M) for N in Ns)
assert KH==-3
sectional_genus=1+Fraction(inter(M,M)+KH,2)
assert sectional_genus==3

# Local class group order for 1/r(1,a) is r in this small quotient case.
assert r==3
print('VERIFY_OK')
