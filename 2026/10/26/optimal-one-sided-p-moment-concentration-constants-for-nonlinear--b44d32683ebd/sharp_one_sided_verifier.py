"""Numerical checks for the exact one-sided p-moment concentration constant.
Not a substitute for the analytic proof in RESULT.md.
"""
import itertools
import math
import random


def constants(p):
    if p == 2.0:
        return 0.5, 0.5, 0.0
    def k(u):
        e = math.exp(-u)
        return u * (-math.expm1(-u)) / (u + math.expm1(-u))
    lo, hi = 1e-7, max(4., 4. / (p - 1))
    assert k(lo) > p and k(hi) < p
    for _ in range(100):
        mid = (lo + hi) / 2
        if k(mid) > p:
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2
    F = u + math.expm1(-u)
    C = F / u**p
    c = (p-1) / p * (p*C)**(-1/(p-1))
    return C,c,u


def test_non_linear(p, n, probs, vals):
    patterns=list(itertools.product((0,1), repeat=n))
    weights={x: math.prod(probs[i] if x[i] else 1-probs[i]
                           for i in range(n)) for x in patterns}
    mean=sum(weights[x]*vals[x] for x in patterns)
    V=0.0
    for x in patterns:
        variance_proxy=0.0
        for i in range(n):
            zero=list(x); one=list(x)
            zero[i]=0; one[i]=1
            y0,y1=vals[tuple(zero)],vals[tuple(one)]
            upper=max(y0,y1)
            variance_proxy+=(1-probs[i])*(upper-y0)**p+probs[i]*(upper-y1)**p
        V=max(V,variance_proxy)
    C,_,_=constants(p)
    for beta in (0.03,0.2,0.8,1.9,4.5):
        mgf=sum(weights[x]*math.exp(beta*(vals[x]-mean)) for x in patterns)
        assert math.log(mgf) <= C*V*beta**p + 2e-11, (p,n,beta,V,mgf)
    return 5


def main():
    ps=(1.1,1.2,1.5,1.8,1.95,2.)
    tests=0
    rng=random.Random(20261015)
    for p in ps:
        C,c,u=constants(p)
        old=(p-1)/p
        assert C <= 1/p+1e-12 and c >= old-1e-12
        if p<2:
            assert C<1/p and c>old
            kappa=math.exp(-u)
            rate=(1-kappa+kappa*math.log(kappa))/(1-kappa)**(p/(p-1))
            assert abs(rate-c)<2e-8, (p,c,rate)
        for n in (2,3,4):
            for _ in range(40):
                probs=[rng.uniform(.08,.92) for i in range(n)]
                vals={x:rng.uniform(-4.,0.) for x in itertools.product((0,1),repeat=n)}
                tests+=test_non_linear(p,n,probs,vals)
        print('p',p,'C',round(C,10),'c',round(c,10),
              'old c',round(old,10),'unique maximizing u',round(u,10))
    print('PASS: %d nonlinear conditional-moment / exact-MGF checks' % tests)


if __name__=='__main__': main()
