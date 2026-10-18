"""Reproduce exact dual-polytope affine projection norms and the comparison certificate.
Scientific verification only. Requires Python >=3.10; SciPy is optional for independent quadrature.
"""
from fractions import Fraction as Q
from math import comb, factorial, sqrt, pi


def cross(d):
    assert isinstance(d, int) and d >= 1
    a = Q((d+1)*(d+2), 2)
    return 1 + Q(a-1, d+1)*(1-1/a)**d


def cube(d):
    assert isinstance(d, int) and d >= 1
    c = Q(3*d-1, 6)
    s = sum((-1)**j*comb(d,j)*max(c-j, Q(0))**(d+1)
            for j in range(d+1))
    return 1 + Q(12, factorial(d+1))*s


def cross_bernoulli_lower(d):
    a = Q((d+1)*(d+2), 2)
    t = Q(1, a)
    return 1 + Q(a-1, d+1)*(1-d*t)


def certify():
    count = 0
    for d in range(1,3):
        assert cross(d) == cube(d)
        count += 1
    assert cross(1)==Q(5,3) and cross(2)==Q(233,108)
    count+=2
    finite_gaps={}
    for d in range(3,13):
        v = cross(d)-cube(d)
        assert v>0
        finite_gaps[d]=str(v)
        count+=1
    for d in range(1,101):
        assert cross(d)>=cross_bernoulli_lower(d)>Q(d,2)
        count+=2
    for d in range(13,101):
        assert d*d>4*(1+3*d)  # C_d>d/2>sqrt(1+3d)>=Q_d.
        count+=1
    # For every d, cube L∞ <= sqrt(E[ (1+3 Σ U_i)^2 ]) = sqrt(1+3d).
    for d in range(1,50):
        assert cube(d)**2<=1+3*d
        count+=1
    # Additional independent integral checks against exact finite formulas.
    try:
        from scipy.integrate import quad
        for d in range(1,8):
            a=(d+1)*(d+2)/2
            f=lambda y: (d/2)*(1-abs(y))**(d-1)
            cv=sum(quad(lambda y: abs(1+a*y)*f(y), l, r, epsabs=2e-11)[0]
                   for l,r in [(-1,-1/a),(-1/a,0),(0,1)])
            assert abs(cv-float(cross(d)))<2e-10,(d,cv,float(cross(d)))
            count+=1
            def density_b(b):
                return sum((-1)**j*comb(d,j)*max(b-j,0)**(d-1)
                           for j in range(d+1) if b>j)/factorial(d-1)
            split=Q(3*d-1,6)
            pts=sorted(set([0,d]+list(range(1,d))+[float(split)]))
            bv=sum(quad(lambda b: abs(1+6*b-3*d)*density_b(b),
                        l,r,epsabs=2e-10)[0] for l,r in zip(pts,pts[1:]))
            assert abs(bv-float(cube(d)))<5e-9,(d,bv,float(cube(d)))
            count+=1
    except ImportError:
        print('SciPy unavailable; exact rational checks alone have passed.')
    print('PASS',count,'checks')
    print('finite exact gaps n=3,...,12:',finite_gaps)
    print('n=1,2:',cross(1),cross(2))
    print('asymptotic cross/d -> 1/2; cube/sqrt(d) -> sqrt(6/pi) =',sqrt(6/pi))
    print('ratio/sqrt(d) -> sqrt(pi/24) =',sqrt(pi/24))

if __name__=='__main__':
    certify()
