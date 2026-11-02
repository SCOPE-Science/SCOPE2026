#!/usr/bin/env python3
"""Reproducible arithmetic checks for a sampled scalar actuator-noise stability frontier.

The proof is analytic; these checks guard algebra, quadrature discretizations,
and independent numerical perturbations of the optimal hold.
"""
import math
import random

rng = random.Random(87423659)
checks = 0


def close(x, y, tol=1e-10):
    global checks
    checks += 1
    if not math.isclose(x, y, rel_tol=tol, abs_tol=tol):
        raise AssertionError((x, y, x-y))


def test_shaped():
    global checks
    for seed in range(90):
        tau = 0.35 + rng.random()*1.8
        a0 = 0.3 + rng.random()*.75
        a1 = (rng.random()-.5)*.6
        b0 = .65 + rng.random()*1.3
        b1 = (rng.random()-.5)*.5
        sigma2 = .08 + rng.random()*1.2
        n = 400
        dt = tau/n
        ell_count = 1 + rng.randrange(n)
        # Different position patterns, all with equal measure.
        if seed % 3 == 0:
            S = set(range(ell_count))
        elif seed % 3 == 1:
            S = set(range(n-ell_count,n))
        else:
            S = set(rng.sample(range(n), ell_count))
        ell = ell_count*dt
        A=lambda s:a0*s + a1*s*s/(2*tau)
        G = math.exp(A(tau))
        target = G*G*sigma2/(ell+sigma2)
        vk = []
        for j in range(n):
            s=(j+.5)*dt
            b=b0+b1*s/tau
            k = -math.exp(A(s))/(b*(ell+sigma2)) if j in S else 0.0
            v = math.exp(A(tau)-A(s))*b*k
            vk.append(v)
            if j in S: close(v,-G/(ell+sigma2))
        R = (G+dt*sum(vk))**2 + sigma2*dt*sum(v*v for v in vk)
        close(R,target,1e-9)
        # Complete-square representation; proves discrete nonnegativity.
        for _ in range(10):
            vtest = [v + (rng.random()-.5)*3.5 if j in S else 0.0
                     for j,v in enumerate(vk)]
            sumv = dt*sum(vtest)
            Rtest=(G+sumv)**2 + sigma2*dt*sum(v*v for v in vtest)
            close(Rtest-target,(1+sigma2/ell)*(sumv+G*ell/(ell+sigma2))**2
                +sigma2*dt*sum((vtest[j]-(sumv/ell if j in S else 0))**2
                                 for j in S), 1e-9)
            checks += 1
            assert Rtest >= target-1e-9


def test_zero_order_hold():
    global checks
    for _ in range(300):
        a = .1 + rng.random()*3
        tau = .02 + rng.random()*2.5
        b = .3 + rng.random()*3
        sigma2 = .02 + rng.random()*1.5
        E=math.exp(a*tau)
        I=math.expm1(a*tau)/a
        J=math.expm1(2*a*tau)/(2*a)
        ell_eff=I*I/J
        close(ell_eff,2/a*math.tanh(a*tau/2))
        checks += 1
        assert ell_eff<tau
        k=-E*I/(b*(I*I+sigma2*J))
        R=(E+b*I*k)**2+sigma2*b*b*J*k*k
        close(R,E*E*sigma2/(sigma2+ell_eff))
        shaped= tau/(E*E-1)
        zoh=2/(a*(E+1)**2)
        close(shaped/zoh,(a*tau/2)/math.tanh(a*tau/2))
        checks += 1
        assert shaped>zoh
        # Random competing constant gains cannot do better.
        for _ in range(5):
            z=k+(rng.random()-.5)*6
            r=(E+b*I*z)**2+sigma2*b*b*J*z*z
            checks+=1
            assert r>=R-1e-10


def test_independent_gaussian_moment():
    global checks
    for _ in range(10):
        tau=.4+rng.random()
        a=.05+rng.random()
        sigma2=.1+rng.random()
        ell=(.2+.8*rng.random())*tau
        E=math.exp(a*tau)
        v=-E/(ell+sigma2)
        mean=E+ell*v
        variance=sigma2*ell*v*v
        exact=E*E*sigma2/(ell+sigma2)
        close(mean*mean+variance,exact)
        # Independent direct Gaussian sampling of the actual stochastic integral.
        N=30000
        sample=sum((mean+math.sqrt(variance)*rng.gauss(0,1))**2 for j in range(N))/N
        checks+=1
        assert abs(sample-exact)<.035*exact,(sample,exact)


if __name__ == '__main__':
    test_shaped()
    test_zero_order_hold()
    test_independent_gaussian_moment()
    print('PASS:',checks,'independent numerical identities, perturbation inequalities, and Gaussian moment tests')
