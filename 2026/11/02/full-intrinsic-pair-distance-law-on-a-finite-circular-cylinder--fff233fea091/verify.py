"""Independent numeric checks for the intrinsic distance law on a finite circular cylindrical lateral surface.

Python 3, standard library only. Run: python verify.py
The theorem's universal claims are proved analytically; these are finite sanity checks.
"""
from math import asin, hypot, pi, sqrt
from random import Random


def cdf(r, a, h):
    assert a > 0 and h > 0
    if r <= 0:
        return 0.0
    if r >= hypot(a, h):
        return 1.0
    x = min(r, a)
    b = min(a, sqrt(max(0.0, r*r-h*h)))

    def arc_integral(z):
        return 0.5 * (z*sqrt(max(0.0,r*r-z*z)) + r*r*asin(min(1.0,z/r)))

    return (2.0/(a*h*h)) * (
        0.5*h*h*b + h*(arc_integral(x)-arc_integral(b))
        - 0.5*(r*r*(x-b)-(x**3-b**3)/3.0)
    )


def cdf_midpoint(r, a, h, n=12000):
    if r <= 0: return 0.0
    bound = min(a,r)
    step = bound/n
    total = 0.0
    for j in range(n):
        x = (j+0.5)*step
        v = min(h, sqrt(max(0.0,r*r-x*x)))
        total += h*v-v*v/2
    return 2.0 * total*step/(a*h*h)


def pair_distance(rng, a, h):
    v = 2.0*a*rng.random()
    w = 2.0*a*rng.random()
    x = abs(v-w)
    x = min(x,2.0*a-x)
    z = h*rng.random()
    zz = h*rng.random()
    return hypot(x,z-zz)


def second_moment(a, h):
    return a*a/3+h*h/6


def fourth_moment(a, h):
    return a**4/5 + a*a*h*h/9 + h**4/15


def test():
    rng=Random(20261027)
    a_h=[(1,2),(2,1),(1,1),(0.25,5),(5,0.25),(0.7,1.3),(2.75,3.5)]
    comparisons=0
    max_cdf_error=0.0
    for a,h in a_h:
        R=hypot(a,h)
        vals=[]
        for j in range(1,49):
            r=R*j/49
            value=cdf(r,a,h)
            numerical=cdf_midpoint(r,a,h)
            max_cdf_error=max(max_cdf_error, abs(value-numerical))
            assert abs(value-numerical)<4e-5, (a,h,r,value,numerical)
            assert -1e-11<=value<=1+1e-11
            vals.append(value)
            comparisons+=1
        assert all(v<=w+1e-12 for v,w in zip(vals,vals[1:]))
        assert abs(cdf(0,a,h))<1e-13 and cdf(R,a,h)==1.0
        N=50000
        vals=[pair_distance(rng,a,h) for _ in range(N)]
        for t in (0.25,0.55,0.85):
            r=t*R
            empirical=sum(v<=r for v in vals)/N
            assert abs(empirical-cdf(r,a,h))<0.015, (a,h,t,empirical,cdf(r,a,h))
        empirical_m2=sum(v*v for v in vals)/N
        empirical_m4=sum(v**4 for v in vals)/N
        assert abs(empirical_m2-second_moment(a,h))<0.04*R*R
        assert abs(empirical_m4-fourth_moment(a,h))<0.07*R**4
        recovered_a2=6*second_moment(a,h)-R*R
        recovered_h2=2*R*R-6*second_moment(a,h)
        assert abs(recovered_a2-a*a)<1e-12*max(1,a*a)
        assert abs(recovered_h2-h*h)<1e-12*max(1,h*h)
    # The isolated angular cutoff has order 3/2 and a negative coefficient.
    a,h=1.,2.
    for delta in (1e-2,1e-3,1e-4):
        r=a+delta
        baseline=pi*r*r/(2*a*h)-2*r**3/(3*a*h*h)
        ratio=(cdf(r,a,h)-baseline)/(delta**1.5)
        target=-4*sqrt(2)/(3*h*sqrt(a))
        assert abs(ratio/target-1)<0.04
    # The isolated axial cutoff has order 5/2 and a positive coefficient.
    a,h=2.,1.
    for delta in (1e-2,1e-3,1e-4):
        r=h+delta
        baseline=pi*r*r/(2*a*h)-2*r**3/(3*a*h*h)
        ratio=(cdf(r,a,h)-baseline)/(delta**2.5)
        target=8*sqrt(2)/(15*a*h**1.5)
        assert abs(ratio/target-1)<0.005
    # Cubic tail: use moderate deficits to avoid float cancellation.
    for a,h in [(1.,2.),(2.,1.),(1.,1.)]:
        R=hypot(a,h)
        delta=1e-3
        ratio=(1-cdf(R-delta,a,h))/delta**3
        target=R**3/(3*a*a*h**4)
        assert abs(ratio/target-1)<0.003
    print('PASS: 336 independent midpoint comparisons, 350,000 random pairs,')
    print('      moment/inverse identities, both cutoff powers, cubic endpoint tail')
    print('max midpoint CDF discrepancy',max_cdf_error)


if __name__=='__main__': test()
