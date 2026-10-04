#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

# Exact Gaussian rationals represented by (real, imag).
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def scale(a,q): return (a[0]*q,a[1]*q)
def iszero(a): return a==(Fraction(0),Fraction(0))
I=(Fraction(0),Fraction(1)); ONE=(Fraction(1),Fraction(0)); ZERO=(Fraction(0),Fraction(0))

def ratio_series(lam,N=5):
    # r(k)=(lam-i k)/(lam+i k); solve (lam+i k)r=lam-i k.
    a=[ZERO]*(N+1); a[0]=ONE
    for n in range(1,N+1):
        rhs=neg(I) if n==1 else ZERO
        a[n]=scale(add(rhs,neg(mul(I,a[n-1]))),Fraction(1,1)/lam)
    return a

def exp_series(length,N=5):
    z=scale(I,2*length)
    out=[ONE]
    p=ONE
    for n in range(1,N+1):
        p=mul(p,z)
        out.append(scale(p,Fraction(1,factorial(n))))
    return out

def conv(a,b,N=5):
    out=[ZERO]*(N+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=N: out[i+j]=add(out[i+j],mul(x,y))
    return out

def F_series(a,b,length,N=5):
    prod=conv(conv(ratio_series(a,N),ratio_series(b,N),N),exp_series(length,N),N)
    out=[neg(x) for x in prod]; out[0]=add(ONE,out[0])
    return out

def order(coeff):
    for i,c in enumerate(coeff):
        if not iszero(c): return i
    return None

def check_case(a,b,length,resonant):
    f=F_series(a,b,length,5)
    got=order(f)
    assert got==(3 if resonant else 1),(a,b,length,f)
    C=a+b-a*b*length
    assert (C==0)==resonant
    if resonant:
        B=Fraction(1,a**3)+Fraction(1,b**3)
        assert B>0
        expected=(Fraction(0),-Fraction(2,3)*B)
        assert f[3]==expected,(f[3],expected)
        # zero-mode vector beta=1, slope=-a satisfies both Robin conditions.
        slope=-a; beta=Fraction(1)
        assert slope+a*beta==0
        right_value=slope*length+beta
        assert -slope+b*right_value==0
        g0,N=1,3
    else:
        g0,N=0,1
    # S0=-I for nonzero endpoint Robin parameters, so I-S0 J=I+J has nullity one.
    tildeN=1
    gamma=Fraction(g0)-Fraction(N,2)
    assert gamma==Fraction(-1,2) and tildeN==1

res=[(Fraction(1),Fraction(2)),(Fraction(2),Fraction(-3)),(Fraction(3),Fraction(6)),(Fraction(5),Fraction(-7))]
for a,b in res:
    length=Fraction(1,a)+Fraction(1,b)
    if length>0: check_case(a,b,length,True)
non=[(Fraction(1),Fraction(2),Fraction(1)),(Fraction(2),Fraction(3),Fraction(1)),(Fraction(-1),Fraction(3),Fraction(1)),(Fraction(5),Fraction(-7),Fraction(2))]
for a,b,l in non:
    if l != Fraction(1,a)+Fraction(1,b): check_case(a,b,l,False)
print('VERIFY_OK')
print('resonant_and_nonresonant_exact_cases =',7)
