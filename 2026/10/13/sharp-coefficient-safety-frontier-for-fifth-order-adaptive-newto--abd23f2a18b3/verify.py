"""Standalone checks for the adaptive fifth-degree polar iteration frontier.

All exact identities use standard-library rational arithmetic. Floating-point
trajectories and high-precision boundary evaluations are supplementary tests,
not certificates for the universal assertions proved analytically.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import sqrt


def cubic(a):
    return 128*a**3 + 496*a**2 - 1026*a + 27


def peak(a):
    return (8*a-3)/(10*a)


def g(a,t):
    return 1 + t/2 + a*t*t


def p(a,t):
    return (1-t)*g(a,t)**2


def h(a,t):
    return 1-p(a,t)


def polynomial_h(a,t):
    return (F(3,4)-2*a)*t**2+(a+F(1,4))*t**3+(a-a*a)*t**4+a*a*t**5


def peak_value(a):
    return (2*a+3)**3 * (16*a-1)**2/(25000*a**3)


def derivative(a,t):
    return -t*(10*a*t-8*a+3)*(2*a*t*t+t+2)/4


def derivative_product(a,t):
    # d/dt [(1-t)g(t)^2].
    f=g(a,t)
    return -f*f+2*(1-t)*f*(F(1,2)+2*a*t)


def exact_checks():
    n=0
    for ai in range(15,121):
        a=F(ai,40)
        tp=peak(a)
        assert p(a,tp)==peak_value(a)
        assert peak_value(a)-(1+1/(2*a))==(4*a+1)**2*cubic(a)/(25000*a**3)
        for j in range(-9,10):
            t=F(j,13)
            assert h(a,t)==polynomial_h(a,t)
            assert derivative(a,t)==derivative_product(a,t)
            n+=1
    assert cubic(F(29,20))==F(-6909,250)
    assert cubic(F(3,2))==36
    return n


def endpoint_check():
    with localcontext() as ctx:
        ctx.prec=65
        lo=Decimal(29)/Decimal(20)
        hi=Decimal(3)/Decimal(2)
        for _ in range(214):
            mid=(lo+hi)/2
            if cubic(mid)<0: lo=mid
            else: hi=mid
        a=(lo+hi)/2
        assert abs(cubic(a))<Decimal('1e-56')
        tp=peak(a)
        xp=p(a,tp).sqrt() # x_1 from x_0 squared times g^2
        r1=1-xp*xp
        assert abs(r1+1/(2*a))<Decimal('1e-55')
        assert abs(g(a,r1)-1)<Decimal('1e-55')
        return a


def trajectory_checks():
    tests=0
    lower=0.375
    upper=1.45
    for den in range(2,95):
        x0=1/den
        for scheme in range(4):
            x=x0
            for k in range(200):
                a=[lower,upper][scheme % 2] if scheme<2 else (upper if (k+scheme)%3 else lower)
                t=1-x*x
                x=x*g(a,t)
                assert x>0 and x<2 and x==x
            assert abs(x-1)<1e-12
            tests+=1
    a=1.5
    tp=float(peak(F(3,2)))
    x0=sqrt(1-tp)
    x1=x0*g(a,tp)
    x2=x1*g(a,1-x1*x1)
    assert x1>sqrt(1+1/(2*a)) and x2>x1
    return tests


if __name__=='__main__':
    ne=exact_checks()
    root=endpoint_check()
    nt=trajectory_checks()
    print(f'VERIFY_OK exact_rational_identities={ne} stable_trajectories={nt} root={root:.15f} scalar_divergence_witness=1')
