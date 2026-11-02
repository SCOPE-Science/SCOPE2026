"""Independent checks for Markov-modulated Brownian search with nonrenewed reset intensity.
Standard-library only. Execute: python verify.py
"""
from math import exp, sqrt, log, isfinite
from random import Random


def mean_vector(switch, intensity, diffusivity, distance):
    nu, rho, D, a = switch, intensity, diffusivity, distance
    assert min(nu, rho, D, a) > 0
    root = sqrt(nu*nu + rho*rho/4)
    bm = nu + rho/2 - root
    bp = nu + rho/2 + root
    # Numerically stable small eigenvalue: determinant divided by large eigenvalue.
    bm = nu*rho/bp
    delta = bp - bm
    p0 = bp/delta
    p1 = (bp-rho)/delta
    qm = exp(-a*sqrt(bm/D))
    qp = exp(-a*sqrt(bp/D))
    hm = -__import__('math').expm1(-a*sqrt(bm/D))/bm
    hp = -__import__('math').expm1(-a*sqrt(bp/D))/bp
    e0 = qm*p0 + qp*(1-p0)
    e1 = qm*p1 + qp*(1-p1)
    h0 = hm*p0 + hp*(1-p0)
    h1 = hm*p1 + hp*(1-p1)
    m1 = h1/e1
    m0 = h0 + (1-e0)*m1
    return m0,m1


def hom_mean(rate, diffusivity, distance):
    return __import__('math').expm1(distance*sqrt(rate/diffusivity))/rate


def hom_derivative(rate, diffusivity, distance):
    z=distance*sqrt(rate/diffusivity)
    return (1+exp(z)*(z/2-1))/(rate*rate)


def killed_endpoint(rng, x, target, diffusivity, span):
    """Sample Brownian endpoint conditional on not reaching absorbing target."""
    scale=sqrt(2*diffusivity*span)
    while True:
        y=x+scale*rng.gauss(0,1)
        if y < target and rng.random() > exp(-(target-x)*(target-y)/(diffusivity*span)):
            return y


def search_sample(rng, nu, rho, D, target):
    phase=int(rng.random()>=0.5)
    x=0.0
    elapsed=0.0
    for j in range(300000):
        rate=nu+(rho if phase else 0.0)
        event=rng.expovariate(rate)
        # Exact free-Brownian first-hitting distribution, from reflection principle.
        z=rng.gauss(0,1)
        while z==0:
            z=rng.gauss(0,1)
        hit=(target-x)**2/(2*D*z*z)
        if hit < event:
            return elapsed+hit
        elapsed+=event
        x=killed_endpoint(rng,x,target,D,event)
        if phase==1 and rng.random()<rho/rate:
            x=0.0
        else:
            phase=1-phase
    raise AssertionError('Unexpectedly long trajectory')


def test():
    checks=0
    for rho in [0.5,1.0,3.0,6.0]:
        for D in [0.7,1.0,2.0]:
            for a in [0.4,1.0,2.0]:
                for nu in [0.04,0.3,1.0,4.0,25.0]:
                    p=mean_vector(nu,rho,D,a)
                    assert all(isfinite(x) and x>0 for x in p)
                    checks+=2
                    # The exact matrix equation: its unique bounded solution has
                    # the source term for resets and target boundary zero.
                    bm=nu*rho/(nu+rho/2+sqrt(nu*nu+rho*rho/4))
                    bp=nu+rho/2+sqrt(nu*nu+rho*rho/4)
                    deltab=bp-bm
                    p0=bp/deltab
                    p1=(bp-rho)/deltab
                    qm=exp(-a*sqrt(bm/D)); qp=exp(-a*sqrt(bp/D))
                    hm=-__import__('math').expm1(-a*sqrt(bm/D))/bm
                    hp=-__import__('math').expm1(-a*sqrt(bp/D))/bp
                    h0=hm*p0+hp*(1-p0);h1=hm*p1+hp*(1-p1)
                    e0=qm*p0+qp*(1-p0);e1=qm*p1+qp*(1-p1)
                    assert abs(p[1]*e1-h1)<2e-10*(1+p[1])
                    assert abs(p[0]-(h0+(1-e0)*p[1]))<2e-10*(1+p[0])
                    checks+=2
    # Asymptotic rates and coefficient including both signs.
    for rho,D,a in [(1,1,1),(1,1,3),(1,1,5),(3,0.7,2),(.6,2,4)]:
        fast_rate=rho/2
        baseline=hom_mean(fast_rate,D,a)
        slope=-(rho*rho/8)*hom_derivative(fast_rate,D,a)
        for nu in [1e3,1e4]:
            val=sum(mean_vector(nu,rho,D,a))/2
            assert abs(nu*(val-baseline)-slope) < 0.015*(1+abs(slope))
            checks+=1
        nu=1e-7
        val=sum(mean_vector(nu,rho,D,a))/2
        assert abs(val*sqrt(nu)-(a/(2*sqrt(D)))) < 0.035*a/(2*sqrt(D))
        checks+=1
    # For a target beyond the constant-reset optimal distance, some
    # finite environmental switching outperforms arbitrarily fast switching.
    assert sum(mean_vector(0.3,1.,1.,5.))/2 < hom_mean(.5,1.,5.)
    checks+=1
    # Independent path-level simulation: Brownian segment hitting times are
    # sampled exactly; surviving Brownian endpoints use killed heat kernel.
    rng=Random(752731)
    mc_results=[]
    for nu,rho,D,a,count in [(0.6,1.,1.,1.,16000),(1.7,1.,1.,2.,16000),(1.,3.,1.,1.,16000)]:
        samples=[search_sample(rng,nu,rho,D,a) for _ in range(count)]
        avg=sum(samples)/count
        var=sum((x-avg)**2 for x in samples)/(count-1)
        se=sqrt(var/count)
        truth=sum(mean_vector(nu,rho,D,a))/2
        assert abs(avg-truth) <= 6*se+0.01
        mc_results.append((nu,rho,D,a,count,round(avg,6),round(truth,6),round(se,6)))
        checks+=1
    print('PASS',checks,'checks; independent exact-path Monte Carlo',mc_results)

if __name__=='__main__':
    test()
