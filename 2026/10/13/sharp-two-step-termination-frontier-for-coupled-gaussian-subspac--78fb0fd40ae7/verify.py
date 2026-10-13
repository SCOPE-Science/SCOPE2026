#!/usr/bin/env python3
"""Independent finite diagnostics for an exact planar coupled-sketch theorem.

No finite sampling is used to establish the universal probability formula.
"""
import math, random

TAU = 2.0 * math.pi

def density(theta, kappa):
    a, b = math.cos(theta), math.sin(theta)
    return math.sqrt(kappa) / (TAU * (a*a + kappa*b*b))

def exact_success(kappa):
    return 4.0 / math.pi * math.atan(1.0/math.sqrt(kappa))

def sample_theta(kappa, rng):
    return math.atan2(rng.gauss(0.,1.),math.sqrt(kappa)*rng.gauss(0.,1.))

def sample_gaussian_given_angle(theta, kappa, rng):
    c, s = math.cos(theta), math.sin(theta)
    rate = c*c/kappa + s*s
    radius = math.sqrt(-2.0*math.log(max(rng.random(), 1.0e-300))/rate)
    return radius*c/math.sqrt(kappa), radius*s

def pair(kappa, rng):
    # Density of phi = theta2 - pi/2 is g(phi) = p(phi + pi/2).
    t1 = sample_theta(kappa, rng)
    f = density(t1, kappa)
    g = density(t1 + math.pi/2, kappa)
    success = rng.random() < min(1.0, g/f)
    if success:
        phi = t1
    else:
        # Rejection sampler for excess density [g(phi)-f(phi)]_+ / (1-q).
        for _ in range(100000):
            t = sample_theta(kappa, rng)
            candidate = t - math.pi/2
            f_c = density(candidate, kappa)
            g_c = density(candidate + math.pi/2, kappa)
            if rng.random() < max(0.0,1.0-f_c/g_c):
                phi = candidate
                break
        else:
            raise RuntimeError('failed to sample residual; κ too close to 1')
    t2 = phi + math.pi/2
    s1 = sample_gaussian_given_angle(t1,kappa,rng)
    s2 = sample_gaussian_given_angle(t2,kappa,rng)
    return s1,s2,success

def step(x, s, kappa):
    sx = kappa*s[0]*x[0] + s[1]*x[1]
    ss = kappa*s[0]*s[0] + s[1]*s[1]
    return (x[0]-s[0]*sx/ss, x[1]-s[1]*sx/ss)

def main():
    rng = random.Random(20261009)
    for kappa in (1., 4., 9., 25.):
        q = exact_success(kappa)
        n=16000
        succ=0
        means=[0.]*4
        cov=[0.]*4
        squared_max=0.
        for _ in range(n):
            a,b,ok=pair(kappa,rng)
            succ+=ok
            x=step(step((1.,-2.), a,kappa),b,kappa)
            if ok:
                squared_max=max(squared_max, x[0]*x[0]+x[1]*x[1])
            for j,vec in enumerate((a,b)):
                means[j*2] += vec[0]
                means[j*2+1] += vec[1]
                cov[j*2] += vec[0]*vec[0]
                cov[j*2+1] += vec[1]*vec[1]
        observed=succ/n
        means=[x/n for x in means]
        cov=[x/n for x in cov]
        assert abs(observed-q)<0.025,(kappa,observed,q)
        assert max(abs(x) for x in means)<0.05,(kappa,means)
        assert max(abs(x-1.) for x in cov)<0.06,(kappa,cov)
        assert squared_max<1.e-26,(kappa,squared_max)
        # Deterministic midpoint integration of overlap; checks only finite quadrature.
        nodes=20000
        overlap = (TAU/nodes)*sum(min(density(TAU*(j+.5)/nodes,kappa),
             density(TAU*(j+.5)/nodes+math.pi/2,kappa)) for j in range(nodes))
        assert abs(overlap-q)<3.e-7,(kappa,overlap,q)
        print('kappa',kappa,'exact_q',round(q,10),'observed_q',round(observed,6),
              'integral',round(overlap,10),'means',[round(v,3) for v in means],
              'marginal_2nd',[round(v,3) for v in cov],
              'max_success_sq_error',format(squared_max,'.3g'))
    print('PASSED finite probabilistic diagnostics: 64000 coupled Gaussian sketch pairs')

if __name__ == '__main__':
    main()
