"""Finite checks for a quadratic-Gaussian Fock weighted contraction.

Requires Python 3, NumPy and SciPy. Execute: python CHECK.py.
Truncations are consistency checks, not proofs of infinite spectra.
"""
import math
import numpy as np
from scipy.linalg import svdvals
from scipy.special import gammaln

count = 0


def check(condition, message):
    global count
    assert bool(condition), message
    count += 1


def geometric_parameter(t, b):
    h = t*t + (1-4*abs(b)**2)/(t*t)
    check(h > 2, "interior geometric parameter")
    return 2 / (h + math.sqrt(h*h-4))


def coefficient_matrix(t, b, dimension):
    A = np.zeros((dimension, dimension), dtype=complex)
    for n in range(dimension):
        for j in range((dimension-n-1)//2 + 1):
            m = n + 2*j
            if j == 0:
                A[m,n] = t**(n+1)
            elif b != 0:
                logfactor = 0.5*(gammaln(m+1)-gammaln(n+1))-gammaln(j+1)
                A[m,n] = t**(n+1)*b**j*math.exp(logfactor)
    return A


cases = [(.70, 0.0, 120), (.70, .12, 120), (.70, -.17, 150),
         (.70, .18j, 150), (.70, .24, 190), (.45, .10, 140),
         (.83, .10+0.02j, 160)]
for t, b, dim in cases:
    cutoff = (1-t*t)/2
    check(abs(b) < cutoff, "case lies in compact region")
    r = geometric_parameter(t,b)
    S = svdvals(coefficient_matrix(t,b,dim))
    model = math.sqrt(t) * r**((2*np.arange(6)+1)/4)
    tolerance = 5e-7 if abs(b)/cutoff>.9 else 3e-9
    for j in range(6):
        check(abs(S[j]/model[j]-1) < tolerance,
              f"singular value t={t}, b={b}, index={j}: {S[j]} vs {model[j]}")
    Q = (1-t*t)**2 - 4*abs(b)**2
    hs2 = t*t/math.sqrt(Q)
    sum_squares = t*math.sqrt(r)/(1-r)
    check(abs(sum_squares/hs2-1)<2e-12, "Hilbert-Schmidt trace identity")
    for p in [0.5,1.0,2.0,3.0,4.0]:
        moment = t**(p/2)*r**(p/4)/(1-r**(p/2))
        geometric = sum((math.sqrt(t)*r**((2*j+1)/4))**p for j in range(1000))
        check(abs(moment/geometric-1) < 3e-9, "Schatten moment geometric check")

for t in [.42,.65,.83]:
    boundary = (1-t*t)/2
    for delta in [1e-3,1e-5,1e-7]:
        if delta >= boundary:
            continue
        b = boundary - delta
        r = geometric_parameter(t,b)
        ratio = (1-r)/(2*math.sqrt(1-t*t)*math.sqrt(delta)/t)
        check(abs(ratio-1) < 0.12, "critical square-root ratio")
        p = 1.3
        exact = t**(p/2)*r**(p/4)/(1-r**(p/2))
        asymptotic = t**(p/2+1)/(p*math.sqrt(1-t*t)*math.sqrt(delta))
        check(abs(exact/asymptotic-1)<0.15, "critical Schatten limit consistency")

print(f"PASS: {count} finite analytical/numerical consistency assertions")
