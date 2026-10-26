"""Independent exact and numerical checks for carbonate-only pH mixing curvature.

Standard-library Python 3. No oceanographic parameter-estimation claims are made.
"""
from fractions import Fraction as Q
from math import sqrt, log10
from random import Random


def poly(x, r):
    return x**3 + 6*r*x**2 + (16*r*r-r)*x + 2*r*r


def discr_cubic(a, b, c, d):
    return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d


def y_of_x(x, r):
    return (x*x+x+r)/(x+2*r)


def x_of_y(y, r):
    assert y > .5
    return .5 * (y-1 + sqrt((1-y)**2 + 4*r*(2*y-1)))


def pH_of_y(y, r):
    return -log10(x_of_y(y, r))  # constant -log10(K1) omitted


def curv_sign_expression(x, r):
    return poly(x, r)*(x+2*r)**3/(x*x*(x*x+4*r*x+r)**3)


def derivatives_finite(y, r, step):
    return (pH_of_y(y-step,r) -2*pH_of_y(y,r)+pH_of_y(y+step,r))/step**2


def main():
    # Discriminant of the cubic is calculated independently and compared
    # at exact rational parameter values.
    for denom in [100000, 10000, 1000, 500, 112, 100, 40, 16, 4, 2]:
        r = Q(1,denom)
        c, d = 16*r*r-r, 2*r*r
        assert discr_cubic(Q(1), 6*r, c, d) == -4*r**3*(4*r-1)**2*(112*r-1)

    rc = Q(1,112)
    for x in [Q(1,10000),Q(1,1000),Q(1,28),Q(1,9),Q(1)]:
        assert poly(x,rc) == (8*x+1)*(28*x-1)**2/Q(6272)
    assert y_of_x(Q(1,28),rc) == Q(6,7)

    # Exact signs at three physically interpretable concentration ratios.
    r=Q(1,10000)
    benchmarks=[(Q(1,10000), Q(6667,10000), +1),
                (Q(1,1000), Q(367,400), -1),
                (Q(1,50), Q(205,202), +1)]
    for x,y,sign in benchmarks:
        assert y_of_x(x,r) == y
        assert (1 if poly(x,r)>0 else -1)==sign
        yy=float(y); rr=float(r)
        d=.0005
        gap=pH_of_y(yy,rr)-(.5*pH_of_y(yy-d,rr)+.5*pH_of_y(yy+d,rr))
        assert gap*sign < 0  # Jensen defect is opposite curvature sign
        print('r=',float(r),'C/A=',y,'curvature sign=',sign,'mix-pH minus mean-pH=',f'{gap:+.12g}')

    # Independent finite-difference check of second derivative of pH(C/A).
    rng=Random(296045)
    checks=0
    for _ in range(3000):
        # Avoid nearly coalescent inflections in finite differences.
        rr=10**rng.uniform(-5,-1)
        xx=10**rng.uniform(-3.5,.3)
        yy=y_of_x(xx,rr)
        # stay within admissible positive-carbonate domain.
        d=min(3e-5*max(yy,1), .1*(yy-.5))
        analytic=curv_sign_expression(xx,rr)/__import__('math').log(10)
        numeric=derivatives_finite(yy,rr,d)
        if abs(analytic)>1e-3 and abs(numeric-analytic)<.035*abs(analytic):
            checks+=1
            assert analytic*numeric>0
    assert checks>=2400, checks

    # Critical square-root coalescence checked independently by root bracketing.
    def bisect(a,b,rr):
        fa=poly(a,rr)
        assert fa*poly(b,rr)<0
        for _ in range(100):
            mid=(a+b)/2
            fm=poly(mid,rr)
            if fm*fa>0:a=mid;fa=fm
            else:b=mid
        return (a+b)/2
    for eps in [1e-6,1e-7,1e-8,1e-9]:
        rr=float(rc)-eps
        mid=1/28
        xm=bisect(mid-2*sqrt(eps),mid,rr)
        xp=bisect(mid,mid+2*sqrt(eps),rr)
        slope=(xp-xm)/(2*sqrt(eps))
        assert abs(slope-1/3)<.01, (eps,slope)
        ywidth=(y_of_x(xp,rr)-y_of_x(xm,rr))/sqrt(eps)
        assert abs(ywidth-8/3)<.05, (eps,ywidth)
    print('PASS: exact discriminant, critical factorization, rational examples,', checks,
          'finite-difference checks, and critical-onset comparisons.')

if __name__=='__main__':
    main()
