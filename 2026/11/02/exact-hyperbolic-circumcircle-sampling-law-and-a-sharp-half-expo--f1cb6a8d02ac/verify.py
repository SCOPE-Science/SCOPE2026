"""Independent numerical and algebraic checks for a hyperbolic circumcircle law.
Run: python verify.py. Uses only the Python standard library.
"""
import math
import random
from fractions import Fraction

PI = math.pi


def shell(a, u):
    if not (0 < a < 1 and 0 < u < 1):
        raise ValueError('Poincare radii must lie strictly in (0,1)')
    if u <= a*a:
        return 0.0
    q = abs(u*u-a*a)/(u*(1-a*a))
    return 2.0/PI*math.acos(min(1.0, max(0.0, q)))


def j(a, u):
    t = math.sqrt(max(0.0, (u*u-a**4)/(1-u*u)))
    return math.atan2(t, a*a) + t/(1-a*a)


def disk(a, R):
    if R <= a*a:
        return 0.0
    b = j(a,R) if R <= a else 2*j(a,a)-j(a,R)
    return shell(a,R)/(R*R)-2*(1-R*R)*b/(PI*R*R)


def circle_exists_direct(a, u, phi):
    v = u*math.sin(phi)
    if abs(v) < 1e-14:
        return False
    cy = (u*u-a*a)/(2*v)
    return abs(cy)+math.hypot(a,cy) < 1


def simpson(f, a, b, n=8192):
    h = (b-a)/n
    s = f(a)+f(b)
    for k in range(1,n):
        s += (4 if k%2 else 2)*f(a+k*h)
    return s*h/3


def disk_integral(a,R):
    if R<=a*a:return 0.0
    return 2*(1-R*R)/(R*R)*simpson(
        lambda x:x*shell(a,x)/(1-x*x)**2,a*a,R)


def check():
    # Polynomial identity that converts the angular derivative to one radical.
    for a in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
        for u in [Fraction(9,10), Fraction(19,20)]:
            lhs = u*u*(1-a*a)**2 - (u*u-a*a)**2
            rhs = (1-u*u)*(u*u-a**4)
            assert lhs==rhs
    rng=random.Random(719302)
    # Geometrically independent circumcircle-containment test.
    for a in (.12,.35,.65,.9):
        for _ in range(6000):
            u=1e-4 + (1-2e-4)*rng.random()
            phi=2*PI*rng.random()
            direct=circle_exists_direct(a,u,phi)
            criterion= (u>a*a and abs(math.sin(phi)) > abs(u*u-a*a)/(u*(1-a*a)))
            assert direct==criterion
    # Differentiate the elementary antiderivative against its original integrand.
    for a in (.2,.5,.8):
        for u in ((a*a+a)/2, (a+1)/2, .999):
            h=min(2e-7, (u-a*a)/10,(1-u)/10)
            diff=(j(a,u+h)-j(a,u-h))/(2*h)
            integrand=(u*u+a*a)/(u*(1-u*u)**1.5*math.sqrt(u*u-a**4))
            assert abs(diff-integrand)/integrand<2e-6,(a,u,diff,integrand)
    # Compare the integrated closed form with direct radial quadrature.
    for a in (.14,.35,.65,.88):
        for R in (a*a+.08*(a-a*a), a-.001*(a-a*a), a+.001*(1-a), a+.4*(1-a), .995):
            if R<=a*a or R>=1:continue
            z=disk(a,R)
            w=disk_integral(a,R)
            assert abs(z-w)<4e-5,(a,R,z,w)
            assert 0 <= z <= 1+1e-10
    # A second simulation uses the true hyperbolic-area radial distribution.
    for a,R in ((.2,.45),(.5,.85),(.8,.95)):
        n=50000
        actual=0
        for _ in range(n):
            v=rng.random()
            u=math.sqrt(v*R*R/(1-R*R+v*R*R))
            actual += circle_exists_direct(a,u,2*PI*rng.random())
        assert abs(actual/n-disk(a,R))<.018,(a,R,actual/n,disk(a,R))
    # Sharp asymptotics and uniqueness of the disk optimizer (numerical corroboration).
    for a in (.2,.5,.8):
        d=4*math.atanh(a)
        K=4/PI*math.sqrt(math.cosh(d/2))
        for T in (11,15):
            R=math.tanh(T/2)
            assert abs(shell(a,R)*math.exp(T/2)/K-1)<.001
            assert abs(disk(a,R)*math.exp(T/2)/(2*K)-1)<.02
        Rlist=[a+(1-a)*k/300 for k in range(1,300)]
        signs=[shell(a,R)-disk(a,R) for R in Rlist]
        assert sum(signs[k]>0 and signs[k+1]<0 for k in range(len(signs)-1))==1
    print('ALL_CHECKS_PASSED')


if __name__=='__main__':
    check()
