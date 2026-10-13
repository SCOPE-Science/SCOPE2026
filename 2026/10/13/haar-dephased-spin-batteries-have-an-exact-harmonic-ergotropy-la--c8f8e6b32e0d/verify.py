"""Exact and numeric checks for Haar-dephased spin-battery ergotropy.

Run with Python 3 (standard library). The theorem's infinite-n limit uses
analytic quantile convergence; finite computations only corroborate it.
"""
from fractions import Fraction
from math import comb, sqrt, exp, pi, erfc
from random import Random


def energies(n):
    return [k for k in range(n + 1) for _ in range(comb(n, k))]


def exact_mean(n):
    e = energies(n)
    d = len(e)
    h = [Fraction(0)]
    for i in range(1, d + 1):
        h.append(h[-1] + Fraction(1, i))
    return sum((Fraction(v) * (1 + h[i] - h[d]) for i, v in enumerate(e)), Fraction(0)) / d


def exact_mean_alternate(n):
    e = energies(n)
    d = len(e)
    spacings = [Fraction(1, d*j) for j in range(1, d + 1)]
    # E(p_(i)) for descending Dirichlet(1,...,1) is sum_{j=i}^d 1/(d*j).
    sorted_mean = [sum(spacings[i:], Fraction(0)) for i in range(d)]
    return Fraction(n, 2) - sum((v*p for v, p in zip(e, sorted_mean)), Fraction(0))


def normalized_populations(rng, d):
    # Moduli squared of independent complex standard Gaussians -> iid exponentials.
    xs = [rng.expovariate(1) for _ in range(d)]
    total = sum(xs)
    return [x/total for x in xs]


def sample_work(n, rng):
    e = energies(n)
    p = normalized_populations(rng, len(e))
    return sum(a*b for a,b in zip(e,p)) - sum(a*b for a,b in zip(e,sorted(p,reverse=True)))


def standard_normal_density(z):
    return exp(-z*z/2)/sqrt(2*pi)


def normal_cdf(z):
    return 0.5*erfc(-z/sqrt(2))


def gaussian_constant(steps=40000):
    assert steps%2==0
    a,b = -9.0,9.0
    h = (b-a)/steps
    def fn(z):
        p=standard_normal_density(z)
        return p*p/normal_cdf(z)
    v=fn(a)+fn(b)
    for j in range(1,steps):
        v+=(4 if j%2 else 2)*fn(a+j*h)
    return v*h/6


def main():
    expected = {1:Fraction(1,4),2:Fraction(11,24),3:Fraction(431,672),4:Fraction(255747,320320)}
    for n in range(1,9):
        assert exact_mean(n)==exact_mean_alternate(n)
        if n in expected:
            assert exact_mean(n)==expected[n], (n,exact_mean(n),expected[n])
        assert energies(n)==sorted(energies(n))
        assert len(energies(n))==2**n
    c=gaussian_constant()
    assert abs(c-0.451598642784313)<1.e-8,c
    rng=Random(31814159)
    for n in [2,3,4,5]:
        trials=12000
        em=sum(sample_work(n,rng) for _ in range(trials))/trials
        ex=float(exact_mean(n))
        assert abs(em-ex)<0.02,(n,em,ex)
    # Direct exact discrepancy against a separate enumeration of
    # all computational labels for a small benchmark state.
    for n in (2,3,4):
        es=sorted(x.bit_count() for x in range(2**n))
        assert es==energies(n)
    print('VERIFY_OK exact=8 gaussian=',format(c,'.12f'),'samples=48000')

if __name__=='__main__':
    main()
