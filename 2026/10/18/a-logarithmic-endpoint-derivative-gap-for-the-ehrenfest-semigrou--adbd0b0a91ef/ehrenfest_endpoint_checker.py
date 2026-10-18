#!/usr/bin/env python3
"""Standalone finite-dimensional consistency checks for the Ehrenfest endpoint identities.

Uses only the Python standard library. Finite tests do not certify the
large-dimension limits; those follow from the proof in RESULT.md.
"""
import math

checks = 0

def close(actual, expected, tolerance=8e-11):
    global checks
    checks += 1
    if abs(actual - expected) > tolerance * (1 + abs(expected)):
        raise AssertionError((actual, expected, tolerance))


def simpson(fun, a, b, panels=3000):
    assert panels % 2 == 0
    h = (b-a) / panels
    acc = fun(a) + fun(b)
    for k in range(1, panels):
        acc += (4 if k % 2 else 2) * fun(a + k*h)
    return acc*h/3


def poissonized_urn(n, t):
    """Compute exp(t Q) by uniformizing Q with rate n."""
    nstates = n + 1
    z = n*t
    factor = math.exp(-z)
    rows = []
    for start in range(nstates):
        v = [0.0]*nstates
        v[start] = 1.0
        out = [factor*x for x in v]
        coeff = factor
        for k in range(1, 800):
            nv = [0.0]*nstates
            for i in range(nstates):
                if i:
                    nv[i-1] += v[i]*i/n
                if i<n:
                    nv[i+1] += v[i]*(n-i)/n
            v = nv
            coeff *= z/k
            for j in range(nstates):
                out[j] += coeff*v[j]
            if k > z + 20 and coeff < 1e-16:
                break
        rows.append(out)
    return rows


def formulas(n, t):
    a = math.exp(-2*t)
    p = (1-a)/2
    mode = math.floor(n*p)
    binompmf = math.exp(math.lgamma(n)-math.lgamma(mode+1)-math.lgamma(n-mode) + mode*math.log(p)+(n-1-mode)*math.log1p(-p))
    infinity_derivative = 2*n*a*binompmf
    if n % 2:
        return None, None, infinity_derivative
    m = n//2
    c = math.exp(math.log(n+1)+math.lgamma(n+1)-2*math.lgamma(m+1)-n*math.log(2))
    average = simpson(lambda s:(1-s*s)**m, 0,a)/a
    l1_semigroup = c*average
    central_derivative = 2*c*(average-(1-a*a)**m)
    return l1_semigroup, central_derivative, infinity_derivative


for n in (2,3,4,5,6,8,10,12,16):
    for t in (0.07, 0.19, 0.4, 0.9):
        P = poissonized_urn(n,t)
        DP = []
        for i in range(n+1):
            DP.append([(n-i)*P[i+1][j]+i*P[i-1][j]-n*P[i][j]
                       if 0<i<n else
                       ((n*P[1][j]-n*P[0][j]) if i==0 else
                        (n*P[n-1][j]-n*P[n][j]))
                       for j in range(n+1)])
        for i in range(n+1):
            close(sum(P[i]), 1)
        l1P = max(sum(P[i][j] for i in range(n+1)) for j in range(n+1))
        linftyDP = max(sum(abs(v) for v in row) for row in DP)
        exactP, exactSlope, exactDerivative = formulas(n,t)
        close(linftyDP, exactDerivative)
        if not n % 2:
            close(l1P, exactP)
            close(sum(DP[i][n//2] for i in range(n+1)), exactSlope)
            close(l1P, sum(P[i][n//2] for i in range(n+1)))

sqrt2pi = math.sqrt(2/math.pi)
I = simpson(lambda u: math.exp(-u*u/2), 0, 1, 6000)
beta = .5*sqrt2pi*(I-math.exp(-.5))
for n in (20,40,80,160,320,640,1280):
    a = n**(-.5)
    t = math.log(n)/4
    _, slope, _ = formulas(n,t)
    close(slope/math.sqrt(n), 4*beta, tolerance=1.0/n)

print('Finite consistency comparisons:', checks)
print('Derivative coefficient:', format(4*beta,'.15f'))
print('Logarithmic lower-bound coefficient:', format(beta,'.15f'))
