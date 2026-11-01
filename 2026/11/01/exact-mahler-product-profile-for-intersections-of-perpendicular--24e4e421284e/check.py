"""Independent quadrature and exact symbolic checks for the perpendicular-ellipse product.

Run with Python 3, SciPy, SymPy and mpmath installed: python check.py
"""
import math
from scipy.integrate import quad
import sympy as sp


def exact_areas(t):
    theta = math.atan(1/t)
    area = 4*t*theta
    polar = 4*theta/t + 2*(1-1/t**2)
    return area, polar


def independent_area(t):
    # Radius of the intersection along 0 <= angle <= pi/4.
    val, err = quad(lambda u: 1/(math.cos(u)**2 + math.sin(u)**2/t**2),0,math.pi/4,epsabs=1e-12)
    return 4*val


def independent_polar_area(t):
    # Independent support-function quadrature, with the active constraint
    # switching from an elliptical arc to the diagonal corner.
    angle=math.atan(1/t**2)
    corner=t/math.sqrt(t*t+1)
    h1=lambda u: math.sqrt(math.cos(u)**2+t*t*math.sin(u)**2)
    h2=lambda u: corner*(math.sin(u)+math.cos(u))
    i1=quad(lambda u: 1/h1(u)**2,0,angle,epsabs=1e-12)[0]
    i2=quad(lambda u: 1/h2(u)**2,angle,math.pi/4,epsabs=1e-12)[0]
    # Symmetry: 8 sectors of angle pi/4, and 1/2 radial area integral.
    return 4*(i1+i2)


def run():
    x=sp.symbols('x', positive=True,real=True)
    F=16*(x*x+x*sp.cot(2*x))
    deriv=sp.diff(F,x)
    factor=16*sp.cos(2*x)*(sp.sin(2*x)-2*x*sp.cos(2*x))/sp.sin(2*x)**2
    assert sp.simplify(sp.trigsimp(deriv-factor))==0
    assert sp.limit(F,x,0,dir='+')==8
    assert sp.limit(F,x,sp.pi/4,dir='-')==sp.pi**2
    assert sp.limit((F-8)/x**2,x,0,dir='+')==sp.Rational(16,3)
    assert sp.limit((sp.pi**2-F)/(sp.pi/4-x)**2,x,sp.pi/4,dir='-')==16
    checks=5
    ts=[1.0,1.0001,1.02,1.1,1.333,1.7,2,3,5,10,25,100]
    ts += [1+k/19 for k in range(1,121)]
    products=[]
    for t in sorted(set(ts)):
        a,p=exact_areas(t)
        a2=independent_area(t)
        p2=independent_polar_area(t)
        assert abs(a-a2)<1e-10*max(1,a)
        assert abs(p-p2)<1e-10*max(1,p)
        checks+=2
        prod=a*p
        products.append((t,prod))
        assert 8-1e-11<=prod<=math.pi**2+1e-11
        checks+=1
        theta=math.atan(1/t)
        assert abs(prod-(16*theta**2+8*(t-1/t)*theta))<1e-10
        checks+=1
    for (t1,p1),(t2,p2) in zip(sorted(products),sorted(products)[1:]):
        assert t1<t2 and p1>p2
        checks+=1
    print('PASSED',checks,'symbolic, geometric-integral and monotonicity checks')
    for t in [1,1.1,2,10,100]:
        a,p=exact_areas(t)
        print(f't={t:<7} area={a:.12f} polar_area={p:.12f} product={a*p:.12f}')

if __name__=='__main__':
    run()
