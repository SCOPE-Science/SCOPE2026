"""Numerical consistency checks for the quadrant resetting exit-front theorem.

Requires Python 3.10+ and SciPy. Run: python verify.py
All finite checks corroborate, but do not prove, asymptotic assertions.
"""
import math
from scipy.integrate import quad
from scipy.special import k0, k1

PI = math.pi
TESTS = 0


def verify(statement, explanation):
    global TESTS
    TESTS += 1
    if not statement:
        raise AssertionError(f"Check {TESTS}: {explanation}")


def correction_integral(x, y, q, D=1.0):
    """Discounted x-axis arrival excluded by an earlier y-axis arrival."""
    def integrand(t):
        if t <= 0:
            return 0.0
        return (x / math.sqrt(4 * PI * D) / (t ** 1.5)
                * math.exp(-x*x/(4*D*t) - D*q*q*t)
                * math.erfc(y / math.sqrt(4*D*t)))
    return quad(integrand, 0.0, math.inf, epsabs=1.e-23,
                epsrel=3.e-10, limit=250)[0]


def upper_corner(x, y, q):
    return 2*x/(PI*y) * k0(q*math.hypot(x,y))


def bound_gap(x, y, q):
    R=math.hypot(x,y)
    return 2*x*R/(PI*y**3*q) * k1(q*R)


def split(x, y, q):
    A=math.exp(-q*x)
    B=math.exp(-q*y)
    dx=correction_integral(x,y,q)
    dy=correction_integral(y,x,q)
    return (A-dx)/(A+B-dx-dy)


def logistic(z):
    return 1.0/(1.0+math.exp(-z))


def front_constant(a,z):
    h=z/2
    return (math.sqrt(PI/(2*math.sqrt(2)*a))/PI
            * math.sinh(h)/math.cosh(h)**2)


def main():
    # The sharp global K0/K1 error envelope is tested on both sides.
    for D in (0.5, 1.0, 2.0):
        for x in (0.5, 0.9, 1.25, 1.75):
            for y in (0.6, 1.0, 1.5):
                for q in (1.0, 2.0, 4.0, 7.0, 12.0):
                    delta=correction_integral(x,y,q,D)
                    up=upper_corner(x,y,q)
                    tol=max(1e-15, 2e-9*up)
                    verify(delta>0, "discounted corner correction positive")
                    verify(delta<=up+tol, "corner bound above")
                    verify(up-delta <= bound_gap(x,y,q)+tol,
                           "K1 error envelope")
                    verify(math.exp(-q*x)>delta,
                           "strictly positive successful x-exit weight")
    # Reflection exactly exchanges the two boundary marks, numerically.
    for x,y in ((0.8,1.2), (1.3,0.8), (1.0,1.0)):
        for q in (1.0,2.0,5.0,10.0):
            px=split(x,y,q)
            py=split(y,x,q)
            verify(abs(px+py-1)<2e-12, "side exchange")
            verify(0<px<1, "proper splitting probability")
    # Closed form one-sided Laplace transform and first tilted moment.
    for D in (0.7,1.6):
        for x in (0.6,1.25,2.0):
            for q in (1.0,2.5,5.0):
                lam=D*q*q
                def f(t):
                    return x/math.sqrt(4*PI*D*t**3)*math.exp(-x*x/(4*D*t))
                val=quad(lambda t: math.exp(-lam*t)*f(t),0,math.inf,
                         epsabs=2e-17,epsrel=5e-11)[0]
                m1=quad(lambda t: t*math.exp(-lam*t)*f(t),0,math.inf,
                        epsabs=2e-17,epsrel=5e-11)[0]
                verify(abs(val/math.exp(-x*q)-1)<1e-8,
                       "one-sided hit-time Laplace law")
                verify(abs(m1/val-x/(2*D*q))<1e-8,
                       "tilted mean of successful duration")
    # Switching-profile correction: deterministic finite-parameter trend.
    for a,z in ((1.0,1.0),(1.0,-1.0),(0.8,0.5),(1.3,2.0)):
        c=front_constant(a,z)
        errors=[]
        for q in (8.0,12.0,16.0,20.0):
            x=a-z/(2*q)
            y=a+z/(2*q)
            p=split(x,y,q)
            scaled=(p-logistic(z))*math.sqrt(q)*math.exp((math.sqrt(2)-1)*a*q)
            errors.append(abs(scaled-c))
            verify(math.copysign(1,scaled)==math.copysign(1,c),
                   "sign of boundary-layer correction")
            verify(abs(scaled-c)<0.45*abs(c)+1e-6,
                   "finite-parameter boundary-layer agreement")
        verify(errors[-1] < errors[0], "corner asymptotic trend")
    print(f"PASS: {TESTS} deterministic checks")

if __name__ == '__main__':
    main()
