"""Reproduce finite cycle graph-entropy probing identities.

Python 3 standard library only. Run: python verify.py
Analytical infinity and asymptotic statements are proved in RESULT.md;
these finite tests do not constitute proofs of those statements.
"""
import itertools
import math
from fractions import Fraction

checks = 0

def close(a, b, atol=1e-10, rtol=1e-9):
    global checks
    assert math.isclose(a, b, rel_tol=rtol, abs_tol=atol), (a, b, abs(a-b))
    checks += 1

def exact(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1

def coefficient(k):
    assert k >= 2
    return Fraction(1, k*(k*k-1))

def error_series(m, L, terms=25000):
    """Positive series truncated with O((m*terms)^-2) tail; term lengths finite."""
    return math.fsum(2 / (m*r*((m*r)**2-1)) for r in range(1,terms+1) if r % L)

def F(m,terms=25000):
    return math.fsum(2/(m*r*((m*r)**2-1)) for r in range(1,terms+1))

def spectra_and_probe(m,L):
    """Independent discrete Fourier spectral construction of f(rho) and probe."""
    n=m*L
    def sf(v): return -v*math.log(v) if v > 1e-14 else 0.0
    spectral = [sf((1-math.cos(2*math.pi*j/n))/n) for j in range(n)]
    trace = math.fsum(spectral)
    # Circulant entry through inverse discrete Fourier transform
    offsets=[math.fsum(spectral[j]*math.cos(2*math.pi*j*m*h/n)
                       for j in range(n))/n for h in range(L)]
    # One vector per residue class; each ordered offset occurs n times
    det = n*math.fsum(offsets)
    return trace,det,offsets

for k in range(2,250):
    a = -Fraction(1,k) + Fraction(1,2)*(Fraction(1,k-1)+Fraction(1,k+1))
    exact(a, coefficient(k))

for m in [3,4,5,7,11,20,39]:
    for L in [2,3,4,6]:
        trace, det, offsets = spectra_and_probe(m,L)
        delta = trace-det
        series = error_series(m,L)
        close(delta, series, atol=1e-10, rtol=5e-8)
        close(delta, F(m)-F(m*L), atol=1e-10, rtol=5e-8)
        assert delta > 0
        checks += 1
        for h in range(1,L):
            # Sign check on off diagonal matrix function entries.
            assert offsets[h] < 1e-12
            checks += 1

for m in [3,4,5,7,9]:
    trace, det, offsets = spectra_and_probe(m,2)
    delta = trace-det
    b=offsets[1]
    close(b, -delta/(2*m), atol=1e-12)
    # Enumerate products of independent vertex signs (equivalent to fair pair signs).
    error_values=[]
    for signs in itertools.product([-1,1], repeat=m):
        # each pair contributes 2*b*sign
        estimate = trace + 2*b*sum(signs)
        err = estimate-trace
        close(err, -(delta/m)*sum(signs),atol=1e-12)
        error_values.append(err)
    close(math.fsum(error_values)/len(error_values), 0,atol=1e-12)
    close(math.fsum(e*e for e in error_values)/len(error_values),
          delta*delta/m,atol=1e-12)
    exact(sum(abs(e) >= delta-1e-12 for e in error_values),2)
    exact(len(error_values),2**m)
    for k in range(m+1):
        exact(sum(sum(signs)==m-2*k for signs in itertools.product([-1,1],repeat=m)),
              math.comb(m,k))

for m in [30,100,300,1000]:
    for L in [2,3,8]:
        series = F(m)-F(m*L)
        leading = 2*math.zeta(3) if hasattr(math, 'zeta') else 2*sum(1/j**3 for j in range(1,200000))
        approx = leading*(1-L**(-3))/m**3
        # Numerical test of exact first+second asymptotic terms with integral-safe sums.
        first = 2*sum(j**-3 for j in range(1,50000))*(1-L**-3)/m**3
        second = 2*sum(j**-5 for j in range(1,2000))*(1-L**-5)/m**5
        close(series, first+second, atol=3e-11,rtol=4e-5)

print('PASS: %d finite symbolic, independent Fourier, series, binomial and asymptotic checks' % checks)
