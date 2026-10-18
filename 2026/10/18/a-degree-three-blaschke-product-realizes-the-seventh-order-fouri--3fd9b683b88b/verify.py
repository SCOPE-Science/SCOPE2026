"""Reproducible arithmetic checks for a cubic Blaschke product.

Requires only Python 3 standard library. The asymptotic theorem is proved
analytically in RESULT.md; finite sampling below is a numerical check only.
"""
import cmath
import math


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def subtract(a, b):
    length = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(length)]


# With x=t^2, the common denominator of the phase derivative is D(x).
D = multiply([1, 9], [1, 2, 49])
N = multiply(multiply([7], [1, 1]), [1, 10, 57])
assert D == [1, 11, 67, 441]
assert N == [7, 77, 469, 399]
assert subtract([7 * q for q in D], N) == [0, 0, 0, 2688]
# Differentiating 7 - 2688*x^3 / D gives a strictly negative derivative.
Dprime = [(i + 1) * D[i + 1] for i in range(len(D) - 1)]
threeD_minus_xDprime = subtract([3 * q for q in D], [0] + Dprime)
assert threeD_minus_xDprime == [3, 22, 67, 0]
print("EXACT identity: phase slope = 7 - 2688*x^3/(1+11*x+67*x^2+441*x^3)")
print("EXACT monotonicity numerator: 3+22*x+67*x^2 > 0 for x >= 0")

root = math.sqrt(3)
zeros = (0.5, 0.5 + 1j*root/6, 0.5 - 1j*root/6)
assert all(abs(a) < 1 for a in zeros)


def B(z):
    return (6*z**3 - 9*z*z + 5*z - 1)/(6 - 9*z + 5*z*z - z**3)


for j in range(1, 40):
    theta = 2*math.pi*j/41
    z = cmath.exp(1j*theta)
    factorized = 1.0+0.0j
    for a in zeros:
        factorized *= (z-a)/(1-a.conjugate()*z)
    assert abs(B(z)-factorized) < 2e-11
    assert abs(abs(B(z))-1) < 2e-11
for t in (0.0, 0.07, -0.35, 1.25, -3.2):
    z = (1+1j*t)/(1-1j*t)
    slope_from_zeros = sum((1-abs(a)**2)/abs(z-a)**2 for a in zeros)
    x = t*t
    slope_closed = 7-2688*x**3/((1+9*x)*(1+2*x+49*x*x))
    assert abs(slope_from_zeros - slope_closed) < 2e-12
print("POINTWISE: factorization, unimodularity, and phase derivative agree")

K = math.gamma(1/7)*math.cos(math.pi/14)/(7*math.pi*(6**(1/7)))
print("THEORETICAL asymptotic constant:", format(K, ".12f"))
for n in (100, 500, 2000):
    M = 1
    while M < 40*n:
        M *= 2
    coefficient = sum(B(cmath.exp(2j*math.pi*j/M))**n
                      * cmath.exp(-2j*math.pi*7*n*j/M)
                      for j in range(M))/M
    print("NUMERICAL n=%d: n^(1/7)*[z^(7n)]B(z)^n = %.12f + %.2g i (M=%d)" %
          (n, (n**(1/7))*coefficient.real,
           (n**(1/7))*coefficient.imag, M))
print("All checks passed. Numerical calculations do not replace the infinite proof.")
