"""Reproduce finite common-phase graph-state fidelity checks (Python standard library)."""
from collections import Counter
from math import comb, exp, lgamma, log, pi, sqrt, cos, sin


def star(n):
    return [(0, j) for j in range(1, n)]


def complete(n):
    return [(i, j) for i in range(n) for j in range(i+1, n)]


def cycle(n):
    return [(i, (i+1) % n) for i in range(n)]


def h_value(mask, edges):
    return sum(1 for i, j in edges if (mask >> i & 1) and (mask >> j & 1))


def histogram(n, edges):
    return Counter(h_value(mask, edges) for mask in range(1 << n))


def fidelity(hist, n, sigma):
    return sum(a * b * exp(-0.5 * sigma**2 * (k-l)**2)
               for k, a in hist.items() for l, b in hist.items()) / 4**n


def k_formula(n, sigma):
    ps = [exp(lgamma(n+1)-lgamma(j+1)-lgamma(n-j+1)-n*log(2)) for j in range(n+1)]
    cs = [j*(j-1)//2 for j in range(n+1)]
    return sum(ps[j]*ps[k]*exp(-0.5*sigma**2*(cs[j]-cs[k])**2)
               for j in range(n+1) for k in range(n+1))


for n in range(3, 10):
    for graph in (star(n), cycle(n), complete(n)):
        hist = histogram(n, graph)
        m = len(graph)
        degrees = [0] * n
        for i, j in graph:
            degrees[i] += 1
            degrees[j] += 1
        s = sum(d*d for d in degrees)
        mean = sum(k*v for k, v in hist.items())/(1 << n)
        var = sum((k-mean)**2*v for k, v in hist.items())/(1 << n)
        assert abs(16*var - (s+m)) < 1e-10
        # A direct computational-basis overlap check, independent of the Gaussian integral.
        angle = 0.24
        overlap = sum((cos(angle*k) + 1j*sin(angle*k))*v for k, v in hist.items())/(1 << n)
        basis = sum(complex(cos(angle*h_value(z, graph)), sin(angle*h_value(z, graph)))
                    for z in range(1 << n))/(1 << n)
        assert abs(overlap-basis) < 1e-13
        assert 0 <= fidelity(hist, n, 0.32) <= 1

for n in range(2, 9):
    hist = histogram(n, complete(n))
    for sigma in (0.07, 0.3, 0.9):
        assert abs(fidelity(hist, n, sigma)-k_formula(n, sigma)) < 1e-12

for n in (64, 128, 256):
    critical = k_formula(n, 2/n**1.5)
    assert abs(critical - 1/sqrt(1+4/8)) < 0.012
    theta = sum(exp(-(2*r)**2/8) for r in range(-32, 33))
    crossover = k_formula(n, 2/n)
    assert abs(crossover*sqrt(pi*n)-theta) < 0.02
    saturate = k_formula(n, 0.1)
    if n >= 128:
        assert abs(saturate*sqrt(pi*n)-1) < 0.018

# Star-graph hub exception: a direct binomial calculation at the same calibration scale.
for n in (64, 128, 256):
    c = 2.0
    # Condition on center=0 (half the mass) or center=1 (Bin(n-1,1/2)).
    weights = [exp(lgamma(n)-lgamma(k+1)-lgamma(n-k)-(n-1)*log(2)) for k in range(n)]
    pm = [w/2 for w in weights]
    pm[0] += 0.5
    f = sum(pm[j]*pm[k]*exp(-0.5*(c/n)**2*(j-k)**2)
            for j in range(n) for k in range(n))
    target = (1+exp(-c*c/8))/2
    assert abs(f-target) < 0.02
    if n == 256:
        assert k_formula(n, c/n) < 0.15
        assert f > 0.75

print('VERIFY_OK')
