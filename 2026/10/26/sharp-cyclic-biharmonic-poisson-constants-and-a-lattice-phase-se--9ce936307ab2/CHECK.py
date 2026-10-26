"""Reproduction checks for the cyclic biharmonic Poisson endpoint theorem.

Requires only Python 3 standard library. These finite checks supplement,
but do not replace, the proof for all n and its asymptotic statement.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import cos, pi, sin

checks = 0

def verify(condition, message):
    global checks
    assert condition, message
    checks += 1


def kernel(n, d):
    t = d * (n - d)
    return Fraction(n**4 + 10*n*n - 11 - 30*t*(t+2), 720*n)


def cutoff(n):
    # Deliberately integer-only: no rounded square roots.
    k = 0
    for d in range(n // 2 + 1):
        if kernel(n, d) >= 0:
            k = d
        else:
            break
    return k


def exact_norm(n):
    k = cutoff(n)
    s1 = k*(k+1)//2
    s2 = k*(k+1)*(2*k+1)//6
    s3 = s1*s1
    s4 = k*(k+1)*(2*k+1)*(3*k*k+3*k-1)//30
    a = n**4 + 10*n*n - 11
    q = (n*n-2)*s2 - 2*n*s3 + s4 + 2*n*s1
    return Fraction((2*k+1)*a-60*q, 360*n)


# A zero-mean inverse for the discrete cyclic fourth derivative.
for n in range(3, 151):
    row = [kernel(n, j) for j in range(n)]
    verify(sum(row, Fraction(0)) == 0, ('zero mean', n))
    for j in range(n):
        lap2 = (6*row[j] - 4*row[(j-1)%n] - 4*row[(j+1)%n]
                + row[(j-2)%n] + row[(j+2)%n])
        verify(lap2 == Fraction(int(j == 0), 1)-Fraction(1, n),
               ('fourth difference', n, j))
    verify(exact_norm(n) == sum(map(abs, row), Fraction(0)),
           ('sharp absolute-row sum', n))
    k = cutoff(n)
    verify(all(x>=0 for x in row[:k+1]) and
           all(x<=0 for x in row[k+1:n-k]), ('sign threshold', n))

# Independent Fourier reconstruction for moderate cycle sizes.
for n in range(3, 61):
    for j in range(n):
        spectral = sum(cos(2*pi*k*j/n)/(4*sin(pi*k/n)**2)**2
                       for k in range(1, n))/n
        verify(abs(spectral-float(kernel(n,j))) < 1e-7,
               ('Fourier formula', n, j))

# High-precision asymptotic diagnostic, independent of floating-point
# cancellation in the exact rational norm.
with localcontext() as context:
    context.prec = 70
    one = Decimal(1)
    sqrt30 = Decimal(30).sqrt()
    w = (one-4/sqrt30).sqrt()
    xi = (one-w)/2
    a = xi/180-(xi**3/3-xi**4/2+xi**5/5)/6
    g = (xi-3*xi**2+2*xi**3)/18
    c = -w/(6*sqrt30)
    for n in [11, 19, 25, 53, 97, 251, 509, 1009, 2003, 10007, 20011]:
        N = Decimal(n)
        t = -one + ((N**4+10*N*N+19)/30).sqrt()
        r = (N - (N*N-4*t).sqrt())/2
        theta = r - int(r)
        bernoulli = theta*theta-theta+one/6
        actual = Decimal(exact_norm(n).numerator)/Decimal(exact_norm(n).denominator)
        predicted = a*N**4 + N*N*(g+c*bernoulli)
        verify(abs(actual-predicted)/N < Decimal('0.03'),
               ('asymptotic remainder diagnostic', n))

print(f'PASS: {checks} exact and numerical assertions.')
