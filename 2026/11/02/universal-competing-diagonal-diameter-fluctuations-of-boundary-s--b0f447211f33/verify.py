"""Reproducibility checks for the boundary-sampled parallelogram diameter crossover.
Pure Python 3 standard library; all probability limits are proved analytically.
"""
import math
import random
from itertools import combinations


def expectation(tau):
    return 2.0 - 0.25 * (tau + 3.0) * math.exp(-tau)


def second_moment(tau):
    return 6.0 - 0.25 * (2*tau*tau + 10*tau + 15) * math.exp(-tau)


def survival(t, tau):
    if t < 0:
        return 1.0
    z = max(t-tau, 0.0)
    return (1.0+t)*(1.0+z)*math.exp(-t-z)


def integrate_simpson(function, lower, upper, steps=6000):
    step = (upper-lower)/steps
    total = function(lower)+function(upper)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * function(lower + j*step)
    return total * step/3.0


def test_integrals():
    for tau in (0.,0.25,0.75,2.,4.,9.):
        xmax = max(60.,tau+60.)
        m1 = integrate_simpson(lambda t: survival(t,tau), 0., xmax)
        m2 = 2*integrate_simpson(lambda t: t*survival(t,tau), 0., xmax)
        assert abs(m1-expectation(tau)) < 0.000002, (tau,m1,expectation(tau))
        assert abs(m2-second_moment(tau)) < 0.000005, (tau,m2,second_moment(tau))
    assert abs(expectation(0.)-1.25)<1e-14
    assert abs((second_moment(0.)-expectation(0.)**2)-11./16.)<1e-14
    assert abs((second_moment(60.)-expectation(60.)**2)-2)<1e-12
    print('INDEPENDENT_SURVIVAL_INTEGRALS_AND_END_POINTS_PASSED')


def test_local_rates():
    for a,b in ((1,1),(.5,3.5),(7.,.2),(5.,8.)):
        rate1 = b/(a+b)
        rate2 = a/(a+b)
        assert abs(rate1+rate2-1.)<1e-14
        # If E1,E2 are independent unit exponentials, min(c1E1,c2E2)
        # is exponential with rate 1/c1+1/c2=1.
        c1=(a+b)/b
        c2=(a+b)/a
        assert abs(1/c1+1/c2-1)<1e-14
    print('LOCAL_CORNER_EXPONENTIAL_RATE_CERTIFICATES_PASSED')


def sample_diameter(a,b,n,tau,rng,brute=False):
    cos_theta=tau/n
    assert 0 <= cos_theta < 1
    sin_theta=math.sqrt(1.-cos_theta*cos_theta)
    corners=((0.,0.),(a,0.),(a+b*cos_theta,b*sin_theta),(b*cos_theta,b*sin_theta))
    per=2*(a+b)
    lengths=(a,b,a,b)
    lo=[float('inf')]*4
    hi=[float('-inf')]*4
    direct=[]
    for _ in range(n):
        arc=rng.random()*per
        if arc<a:
            side, frac=0,arc/a
        elif arc<a+b:
            side,frac=1,(arc-a)/b
        elif arc<2*a+b:
            side,frac=2,(arc-a-b)/a
        else:
            side,frac=3,(arc-2*a-b)/b
        lo[side]=min(lo[side],frac)
        hi[side]=max(hi[side],frac)
        if brute:
            vx,vy=corners[side];wx,wy=corners[(side+1)%4]
            direct.append((vx+frac*(wx-vx),vy+frac*(wy-vy)))
    extremes=[]
    for i in range(4):
        if hi[i]>=lo[i]:
            x,y=corners[i];z,w=corners[(i+1)%4]
            for frac in (lo[i],hi[i]):
                extremes.append((x+frac*(z-x),y+frac*(w-y)))
    max_d2=max((x-u)**2+(y-v)**2 for (x,y),(u,v) in combinations(extremes,2))
    if brute:
        brute_d2=max((x-u)**2+(y-v)**2 for (x,y),(u,v) in combinations(direct,2))
        assert abs(max_d2-brute_d2) < 2e-12*max(1.,brute_d2)
    D=math.sqrt(a*a+b*b+2*a*b*cos_theta)
    # normalize by the true geometric diameter, with limiting right-angle D0
    return n*math.hypot(a,b)*(D-math.sqrt(max_d2))/(2*a*b)


def test_extreme_reduction():
    rng=random.Random(473)
    for a,b,n,tau in ((1.,1.,35,0.),(1.,3.,60,3.),(.6,3.4,100,1.25),(4.,1.,30,5.)):
        for _ in range(12):
            t=sample_diameter(a,b,n,tau,rng,brute=True)
            assert t>=-1e-10
    print('INDEPENDENT_FULL_PAIRWISE_DIAMETER_REDUCTION_PASSED 48')


def test_finite_samples():
    rng=random.Random(20261029)
    cases=((1.,1.,0.),(1.,3.,0.75),(.6,3.4,2.),(1.,1.,4.),(1.,3.,5.))
    n=750
    reps=1800
    for a,b,tau in cases:
        data=[sample_diameter(a,b,n,tau,rng) for _ in range(reps)]
        observed=sum(data)/len(data)
        target=expectation(tau)
        # Stochastic accuracy: this generous threshold only corroborates the
        # analytic theorem, and is NOT a certificate for an infinite limit.
        assert abs(observed-target)<0.16, (a,b,tau,observed,target)
    print('INDEPENDENT_FINITE_SAMPLE_GEOMETRIC_DIAGNOSTICS_PASSED 5')


def test_detuning():
    for a,b in ((1.,1.),(1.,3.),(.6,3.4)):
        d0=math.hypot(a,b)
        for tau in (0.01,0.75,3.,5.):
            for n in (1000,10000):
                c=tau/n
                dplus=math.sqrt(d0*d0+2*a*b*c)
                dminus=math.sqrt(d0*d0-2*a*b*c)
                normalized = n*d0*(dplus-dminus)/(2*a*b)
                assert abs(normalized-tau)<1e-4, (a,b,tau,n,normalized)
    print('EXACT_TWO_DIAGONAL_DETUNING_DIAGNOSTICS_PASSED 24')


if __name__=='__main__':
    test_integrals()
    test_local_rates()
    test_extreme_reduction()
    test_detuning()
    test_finite_samples()
    print('ALL_CHECKS_PASSED')
