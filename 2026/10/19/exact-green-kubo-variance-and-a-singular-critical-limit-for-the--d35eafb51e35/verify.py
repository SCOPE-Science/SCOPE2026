#!/usr/bin/env python3
"""Exact, finite independent checks for a stationary random interval-map correlation law.

Requires Python 3 and SymPy. Infinite-time claims depend on the accompanying proof.
"""
from functools import lru_cache
from fractions import Fraction as F
import sympy as S


def direct_cov_raw(n, p):
    q = 1-p
    @lru_cache(None)
    def iterate(x, steps):
        if not steps:
            return x
        return p*iterate((2*x) % 1, steps-1) + q*iterate(x/2, steps-1)
    r=2*q/p
    def a(k):
        return (2*p-1)/p*(k+1) if r==1 else (2*p-1)/p*(1-r**(k+1))/(1-r)
    def A(v):
        return (2*p-1)/(p*(1-v)*(1-r*v))
    den = 2**n
    total = F(0)
    for j in range(1, den):
        lo=F(j,den);hi=F(j+1,den)
        m=(2*lo+hi)/3;M=(lo+2*hi)/3
        f=iterate(m,n);g=iterate(M,n)
        slope=(g-f)/(M-m); const=f-slope*m
        k=0
        while hi<=F(1,2**(k+1)):
            k+=1
        assert lo>=F(1,2**(k+1)) and hi<=F(1,2**k)
        total += a(k)*(slope*(hi**3-lo**3)/3+const*(hi**2-lo**2)/2)
    if n==0:
        return A(F(1,8))*F(7,24)
    # Entire remaining cell (0,2^-n) is affine under all map words.
    slope=iterate(F(1,3*den),n)*3*den
    tail=A(F(1,8))-sum((a(k)*F(1,8)**k for k in range(n)),F(0))
    total+=slope*F(7,24)*tail
    return total


def shell_recurrence(n,p):
    x=S.Symbol('x')
    q=1-p;r=2*q/p
    a=(2*p-1)/(p*(1-x)*(1-r*x))
    V=a;U=S.Integer(0)
    for _ in range(n):
        v0=S.cancel(V).subs(x,0);u0=S.cancel(U).subs(x,0)
        V_next=S.cancel(p*S.Rational(1,4)*((V-v0)/x+v0/(1-x))+4*q*x*V)
        U_next=S.cancel(p*S.Rational(1,2)*((U-u0)/x+u0/(1-x))+p*S.Rational(1,4)*v0/(1-x)+2*q*x*U)
        V,U=V_next,U_next
    return S.factor(S.Rational(3,8)*U.subs(x,S.Rational(1,4))+S.Rational(7,24)*V.subs(x,S.Rational(1,8)))


def check_symbolic():
    p,t=S.symbols('p t')
    q=1-p;r=2*q/p
    z=4*t/(p+16*q*t*t)
    A=lambda x:(2*p-1)/(p*(1-x)*(1-r*x))
    v0=-4*t*(1-t)*A(t)/(z*p*(2*t-1))
    u0=-t*v0/(4*t-1)
    V=lambda x:(A(x)+z*p*S.Rational(1,4)*v0*(2*x-1)/(x*(1-x)))/(1-z*(p/(4*x)+4*q*x))
    U=lambda x:(z*p*S.Rational(1,2)*u0*(2*x-1)/(x*(1-x))+z*p*S.Rational(1,4)*v0/(1-x))/(1-z*(p/(2*x)+2*q*x))
    M=S.factor(S.Rational(3,8)*U(S.Rational(1,4))+S.Rational(7,24)*V(S.Rational(1,8)))
    expected_M=((2*p-1)*(16*p*t*t-p-16*t*t)*(16*p*t*t+13*p*t-8*p-16*t*t+7*t)
                /(6*(5*p-1)*(2*t-1)*(4*t-1)*(2*p*t+p-2*t)**2))
    assert S.cancel(M-expected_M)==0
    mean=(2*p-1)/(3*p-1)
    C=S.cancel(M-mean**2/(1-z))
    Csum=S.factor(C.subs(t,S.Rational(1,4)))
    expected_Csum=(51*p**3-51*p**2+17*p-1)/(3*(3*p-1)**3*(5*p-1))
    assert S.cancel(Csum-expected_Csum)==0
    C0=(2*p-1)*(6*p*p-3*p+1)/(3*(3*p-1)**2*(5*p-1))
    gamma=S.factor(2*Csum-C0)
    expected_gamma=(-12*p**4+50*p**3-43*p*p+14*p-1)/((3*p-1)**3*(5*p-1))
    assert S.cancel(gamma-expected_gamma)==0
    assert S.cancel(S.diff(gamma,p)+2*p*(267*p**3-371*p*p+197*p-29)/((3*p-1)**4*(5*p-1)**2))==0
    assert S.limit(gamma,p,S.Rational(1,2),dir='+')==4
    assert gamma.subs(p,1)==S.Rational(1,4)
    assert S.limit(C0/(2*p-1),p,S.Rational(1,2),dir='+')==S.Rational(8,9)
    # At fixed p>1/2, the remaining covariance denominator has no pole for |t|<=1/4.
    den=S.factor(S.denom(C))
    assert S.rem(den,4*t-1,t)!=0
    print('PASS: exact symbolic resolvent, Green-Kubo sum, endpoint and monotonicity')


def main():
    check_symbolic()
    tests=0
    for p in (F(3,5),F(2,3),F(3,4),F(9,10)):
        for n in range(6):
            a=direct_cov_raw(n,p)
            b=shell_recurrence(n,S.Rational(p.numerator,p.denominator))
            assert a==b,(p,n,a,b)
            tests+=1
    print(f'PASS: {tests} exact rational cross-checks, direct random-word enumeration vs transfer recurrence')

if __name__=='__main__':
    main()
