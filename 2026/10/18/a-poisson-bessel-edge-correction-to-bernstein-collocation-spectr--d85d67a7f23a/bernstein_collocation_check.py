"""Finite tests for the endpoint-corrected Bernstein collocation energy law.

Only Python's standard library is needed. Numeric tests illustrate, not prove,
the all-dimensional asymptotic theorem.
"""
from fractions import Fraction
from math import comb, sqrt, pi, exp, sin, fsum


def trace_exact(n):
    assert n >= 1
    total = Fraction(0)
    for j in range(n + 1):
        x = Fraction(j, n)
        row = [comb(n, k) * x**k * (1-x)**(n-k) for k in range(n+1)]
        assert sum(row) == 1
        total += sum(t*t for t in row)
    return total


def trace_numeric(n):
    assert n >= 1
    s = 2.
    for j in range(1, n):
        p = j / n
        # Start near the mode and propagate in both directions to avoid underflow.
        k = min(n, int((n + 1) * p))
        term = comb(n, k) * (p**k) * ((1-p)**(n-k))
        # For n <= 2000 this direct evaluation stays finite.
        row = [0.0] * (n+1)
        row[k] = term
        for r in range(k, 0, -1):
            row[r-1] = row[r] * r / (n-r+1) * (1-p)/p
        for r in range(k,n):
            row[r+1] = row[r] * (n-r)/(r+1) * p/(1-p)
        s += fsum(x*x for x in row)
    return s


def poisson_collision(j, m=4096):
    # Simpson quadrature for exp(-2*j)*I_0(2*j), stable for all j.
    assert j >= 1 and m % 2 == 0
    step=pi/m
    v=exp(-4*j)
    for k in range(1,m):
        v += (4 if k%2 else 2) * exp(-4*j*sin(k*step/2)**2)
    return (v+1)*step/(3*pi)


def main():
    vals={1:2, 2:Fraction(19,8)}
    for n, target in vals.items():
        assert trace_exact(n)==target,(n,trace_exact(n),target)
    for n in range(1, 13):
        ex=trace_exact(n)
        nu=trace_numeric(n)
        assert abs(float(ex)-nu)<5.e-11,(n,ex,nu)
    # The j=1 Poisson collision is independent also check by direct Poisson pmf.
    for j in (1,2,4,8,20):
        term=exp(-j)
        terms=[term]
        for k in range(1, max(50,4*j+30)):
            term *= j/k
            terms.append(term)
        independent=fsum(t*t for t in terms)
        assert abs(poisson_collision(j)-independent)<3.e-10,(j,independent)
    # The two boundary rows contribute exactly 2 for every n.
    # The bulk grows on sqrt(n) scale; the correction visibly stabilizes.
    differences=[]
    for n in (16,32,64,128,256,512):
        val=trace_numeric(n)
        differences.append(val - sqrt(pi*n)/2)
    assert 1.1 < differences[-1] < 1.4, differences
    assert differences[-1] > differences[-2], differences
    print('PASS: 12 exact rational/numeric matrix comparisons, 5 Poisson checks')
    print('endpoint corrected residuals:', [round(x, 10) for x in differences])

if __name__=='__main__':
    main()
