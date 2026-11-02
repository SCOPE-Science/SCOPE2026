"""Numerical consistency checks for a two-particle first-passage-reset limit theorem.

Only finite checks; analytic statements are established in the accompanying proof.
Run with: python verify.py
"""
import math

PI = math.pi


def simpson(fun, a, b, n=4000):
    assert n > 0 and n % 2 == 0
    h = (b-a)/n
    s = fun(a)+fun(b)
    for j in range(1,n):
        s += (4 if j%2 else 2)*fun(a+j*h)
    return s*h/3


def surviving(t, L=1., D=1.):
    if t == 0:
        return 1.0
    return math.erf(L/math.sqrt(4*D*t))**2


def conditional_rayleigh(y, eps):
    return (math.exp(-(y-eps)**2)*(-math.expm1(-4*eps*y))
            /(math.sqrt(PI)*math.erf(eps)))


def rayleigh(y):
    return 2*y*math.exp(-y*y)


def ratio_pdf(r):
    return 2*r/(1+r*r)**2


def test():
    n=0
    for L,D in [(1.,1.),(3.,0.7),(0.2,2.)]:
        c=L*L/(PI*D)
        for k in [5,7,9]:
            t=L*L/D*10.**k
            rel=abs(t*surviving(t,L,D)/c-1)
            assert rel<1e-4
            n+=1
        # Finite-difference check of first-passage density -S'(t)=2 f_1(t) S_1(t).
        t=1.1*L*L/D
        eps=t*1e-5
        finite=(surviving(t-eps,L,D)-surviving(t+eps,L,D))/(2*eps)
        single_pdf=L/math.sqrt(4*PI*D*t**3)*math.exp(-L*L/(4*D*t))
        exact=2*single_pdf*math.erf(L/math.sqrt(4*D*t))
        assert abs(finite/exact-1)<2e-9
        n+=1
    for eps in [0.25,0.075,0.015]:
        mass=simpson(lambda y:conditional_rayleigh(y,eps),0,9)
        assert abs(mass-1)<2e-10
        n+=1
    for y in [0.2,0.5,1.,2.,3.]:
        assert abs(conditional_rayleigh(y,0.001)-rayleigh(y))<3e-6
        n+=1
    for p in [0.,.25,.5,1.,2.,3.]:
        lhs=simpson(lambda y:y**p*rayleigh(y),0,9)
        rhs=math.gamma(1+p/2)
        assert abs(lhs-rhs)<1e-6
        n+=1
    assert abs(simpson(lambda th: math.sin(2*th),0,PI/2)-1)<1e-9
    n+=1
    for r in [.1,.3,.7,1.,1.4,3.,10.]:
        res=simpson(ratio_pdf,0,r,n=2000)
        assert abs(res-r*r/(1+r*r))<1e-8
        n+=1
    # Exact ratios of asymptotic moment coefficients and limiting Pearson correlation.
    c20=4*math.gamma(2)/2
    c11=4*math.gamma(1.5)**2/2
    assert abs(c20-2)<1e-13
    assert abs(c11/c20-PI/4)<1e-13
    n+=2
    # m(t)=int_0^t S(a) da ~ c log(t/t0), direct quadrature in log-time.
    for T in [1e4,1e7,1e10]:
        m=simpson(lambda z:math.exp(z)*surviving(math.exp(z)-1),0,math.log1p(T),n=6000)
        ratio=m/(math.log(T)/PI)
        assert 1.0 < ratio < 1.40
        n+=1
    print('PASS:',n,'independent finite consistency checks')

if __name__=='__main__':
    test()
