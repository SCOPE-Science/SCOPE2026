"""Numerical checks for the cubic-chirp Gabor projector spectrum.

Run: python cubic_chirp_check.py
Requires numpy; all classification formulas are proved independently in RESULT.md.
"""
import math
from collections import Counter
import numpy as np


def factor_good(n):
    factors = []
    d = 2
    m = n
    while d*d <= m:
        if m % d == 0:
            r = 0
            while m % d == 0:
                r += 1
                m //= d
            factors.append((d, r))
        d += 1
    if m > 1:
        factors.append((m, 1))
    assert n > 1 and all(p >= 5 for p, _ in factors)
    return factors


def predict(n):
    local = []
    for p,r in factor_good(n):
        states = {p**r: 1}
        for t in range(r):
            states[p**t] = (p-1)*p**(2*(r-t)-1)
        local.append(states)
    result = Counter({1:1})
    for states in local:
        nxt = Counter()
        for val,mult in result.items():
            for val2,mult2 in states.items():
                nxt[val*val2] += mult*mult2
        result = nxt
    nonzero = sum(result.values())
    result[0] = n*n-nonzero
    return result


def direct_ambiguity(n, a=1):
    # T_u g(x)=g(x+u), M_v g(x)=exp(-2 pi i vx/n)g(x).
    x = np.arange(n, dtype=np.int64)
    g = np.exp((2j*np.pi/n) * ((a*x*x*x) % n)) / np.sqrt(n)
    values = np.empty((n,n), dtype=np.float64)
    for u in range(n):
        h = np.conj(g) * np.roll(g, -u)
        values[u] = np.abs(np.fft.fft(h))**2
    return values


def check(n):
    A2 = direct_ambiguity(n)
    observed = Counter()
    pred = predict(n)
    for row in A2:
        for q in row:
            x = n*float(q)
            val = round(x)
            assert abs(x-val) < 3e-8, (n,x,val)
            observed[val] += 1
    assert observed == pred, (n, observed, pred)
    assert abs(n * sum(A2.ravel()) - n*n) < 2e-7
    # Independently diagonalize projector Gram's 2D circulant kernel,
    # rather than using the Weyl operator-basis calculation.
    eig = np.fft.fft2(A2).real
    assert np.max(np.abs(np.fft.fft2(A2).imag)) < 4e-9
    observed_from_gram = Counter()
    for val in eig.ravel():
        k = round(float(val))
        assert abs(float(val)-k) < 3e-8, (n,val)
        observed_from_gram[k] += 1
    assert observed_from_gram == pred, (n,observed_from_gram,pred)
    return pred


if __name__ == '__main__':
    for n in (5,7,25,35,49,55,125):
        c = check(n)
        print(n, 'rank', n*n-c[0], 'nullity', c[0],
              'positive_eigenvalues', sorted((k,v) for k,v in c.items() if k))
    # Flat-state phase-retrieval stability inequality, verified against
    # direct nonlinear intensity measurements (not inferred from A alone).
    rng = np.random.default_rng(19072013)
    for n in (5, 25, 35):
        j = np.arange(n)
        g = np.exp((2j*np.pi/n) * ((j**3)%n)) / np.sqrt(n)
        for sample in range(8):
            x = np.exp(1j*rng.uniform(-np.pi, np.pi, n))/np.sqrt(n)
            y = np.exp(1j*rng.uniform(-np.pi, np.pi, n))/np.sqrt(n)
            measures = []
            for z in (x, y):
                vals = []
                for u in range(n):
                    h = np.conj(np.roll(g,-u)) * z
                    vals.extend(np.abs(np.fft.ifft(h)*n)**2)
                measures.append(np.array(vals))
            left = float(np.linalg.norm(measures[0]-measures[1])**2)
            dist2 = 2-2*abs(np.vdot(x,y))
            lower = (4*np.sin(np.pi/n)**2/n)*dist2
            assert left + 1e-10 >= lower, (n,left,lower)
    print('FLAT_SIGNAL_STABILITY_DIRECT_INTENSITY_OK')
    print('CUBIC_CHIRP_GABOR_SPECTRUM_CHECK_OK')
