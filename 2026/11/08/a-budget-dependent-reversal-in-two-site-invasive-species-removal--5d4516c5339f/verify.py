"""Independent numerical checks for the two-site one-switch survey theorem.

Run: python3 verify.py
Only Python's standard library is required. Numerical checks supplement,
not replace, the analytic proof in RESULT.md.
"""
import math
import random

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def integral_exponential(diff, cap):
    if abs(diff) < 1e-12:
        return cap
    return math.expm1(diff * cap) / diff


def expected_misses(p, alpha, q, beta, horizon, cap):
    """Closed expression obtained by conditioning on the first detection time."""
    assert 0 <= cap <= horizon
    z = beta - alpha
    return (p * math.exp(-alpha * cap)
            + q * ((1-p) * math.exp(-beta * (horizon-cap))
                   + p * math.exp(-beta*horizon)
                   * (alpha*integral_exponential(z, cap)
                      + math.exp(z*cap))))


def independent_quadrature(p, alpha, q, beta, horizon, cap, steps=600):
    """Alternative: integral over the first detection time, Simpson's rule."""
    h = cap / steps
    def density_miss(t):
        return p * alpha * math.exp(-alpha*t) * q * math.exp(-beta*(horizon-t))
    acc = density_miss(0) + density_miss(cap)
    for i in range(1, steps):
        acc += (4 if i % 2 else 2) * density_miss(i*h)
    integr = acc * h / 3
    return (p*math.exp(-alpha*cap)
            + q*(1-p)*math.exp(-beta*(horizon-cap))
            + p*q*math.exp(-alpha*cap)*math.exp(-beta*(horizon-cap))
            + integr)


def derivative_misses(p, alpha, q, beta, horizon, cap):
    return (q*beta*math.exp(-beta*(horizon-cap))
            *(1-p+p*math.exp(-alpha*cap))
            -p*alpha*math.exp(-alpha*cap))


def optimal_cap(p, alpha, q, beta, horizon):
    left = derivative_misses(p,alpha,q,beta,horizon,0)
    right = derivative_misses(p,alpha,q,beta,horizon,horizon)
    if left >= 0:
        return 0.
    if right <= 0:
        return horizon
    lo,hi=0.,horizon
    for _ in range(90):
        mid=(lo+hi)/2
        if derivative_misses(p,alpha,q,beta,horizon,mid) < 0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def asymptotic_K(p, alpha, q, beta):
    total=alpha+beta
    return ((total/beta)
            * (beta/alpha)**(alpha/total)
            * p**(beta/total)
            * (q*(1-p))**(alpha/total))


def main():
    p,a,q,b=.25, 11/5, .5, 1.
    check(p*a>q*b, 'short-horizon index comparison')
    check(3**11>2**17, 'exact long-horizon index comparison')
    check(a*(-math.log1p(-p))<b*(-math.log1p(-q)),
          'opposite long-horizon index')
    ka=asymptotic_K(p,a,q,b)
    kb=asymptotic_K(q,b,p,a)
    exact_ratio= ((1-p)**a/(1-q)**b)**(1/(a+b))
    check(abs(ka/kb-exact_ratio)<1e-12,'coefficient identity')
    check(ka>kb,'long-horizon reversal')

    rng=random.Random(617284)
    for _ in range(100):
        pp=rng.uniform(.025,.975)
        qq=rng.uniform(.025,.975)
        aa=rng.uniform(.3,4.)
        bb=rng.uniform(.3,4.)
        horizon=rng.uniform(.2,5.)
        cc=rng.uniform(0.,horizon)
        closed=expected_misses(pp,aa,qq,bb,horizon,cc)
        quadrature=independent_quadrature(pp,aa,qq,bb,horizon,cc)
        check(abs(closed-quadrature)<3e-10,'quadrature versus integral')
        h=1e-5*min(1.,cc,horizon-cc)
        if h>0:
            numerical=(expected_misses(pp,aa,qq,bb,horizon,cc+h)-
                       expected_misses(pp,aa,qq,bb,horizon,cc-h))/(2*h)
            check(abs(derivative_misses(pp,aa,qq,bb,horizon,cc)-numerical)
                  <1e-7,'analytic derivative')
        opt=optimal_cap(pp,aa,qq,bb,horizon)
        attained=expected_misses(pp,aa,qq,bb,horizon,opt)
        for k in range(31):
            check(attained <= expected_misses(pp,aa,qq,bb,horizon,min(horizon,horizon*k/30))+1e-13,
                  'global cap optimality on independent mesh')

    for horizon, expected_first in [(.01, 'A'),(.05,'A'),(1.,'B'),(2.,'B'),(6.,'B')]:
        ca=optimal_cap(p,a,q,b,horizon)
        cb=optimal_cap(q,b,p,a,horizon)
        la=expected_misses(p,a,q,b,horizon,ca)
        lb=expected_misses(q,b,p,a,horizon,cb)
        check(('A' if la<lb else 'B')==expected_first,'ordering witness')
        print('T=%.3g: A-first cap %.9g, missed %.12g; B-first cap %.9g, missed %.12g'
              %(horizon,ca,la,cb,lb))

    for horizon in [24.,32.,40.]:
        for pp,aa,qq,bb in [(p,a,q,b),(q,b,p,a)]:
            cap=optimal_cap(pp,aa,qq,bb,horizon)
            s=aa+bb
            leading=bb*horizon/s+math.log(pp*aa/(qq*bb*(1-pp)))/s
            check(abs(cap-leading)<.0003,'cap two-term asymptotic')
            scaled=expected_misses(pp,aa,qq,bb,horizon,cap)*math.exp(aa*bb*horizon/s)
            check(abs(scaled/asymptotic_K(pp,aa,qq,bb)-1)<.001,
                  'sharp loss coefficient')

    print('PASS:', CHECKS, 'numerical assertions; analytic universal proof is in RESULT.md')

if __name__=='__main__':
    main()
