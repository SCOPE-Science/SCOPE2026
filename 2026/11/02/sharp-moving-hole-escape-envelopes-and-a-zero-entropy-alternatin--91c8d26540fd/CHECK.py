"""Exact finite checks for complementary moving Markov holes in the doubling map.

The assertions verify enumerated binary prefixes, recurrences and equality classes.
The spectral and asymptotic statements follow from the separate analytic proof.
"""
from itertools import product
from fractions import Fraction

M = (
    ((0, 1), (1, 1)),
    ((1, 1), (1, 0)),
)

def matrices_count(schedule):
    v = (1, 1)
    for s in schedule:
        a, b = v
        v = (b, a + b) if s == 0 else (a + b, a)
    return sum(v)

def brute_count(schedule):
    n = len(schedule)
    return sum(all(not (w[j] == w[j+1] == schedule[j]) for j in range(n))
               for w in product((0, 1), repeat=n+1))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def is_alternating(schedule):
    return all(schedule[j] != schedule[j+1] for j in range(len(schedule)-1))

def is_constant(schedule):
    return len(set(schedule)) <= 1

cases = 0
for n in range(0, 10):
    for s in product((0, 1), repeat=n):
        c = matrices_count(s)
        assert c == brute_count(s), (s,c)
        assert n + 2 <= c <= fibonacci(n+3), (s,c)
        if n >= 2:
            assert (c == n + 2) == is_alternating(s), (s,c,'min')
            assert (c == fibonacci(n+3)) == is_constant(s), (s,c,'max')
        cases += 1
print('PASS',cases,'exact matrix/brute/envelope/equality comparisons')

# Determinant-trace calculation for period products (integer only).
def prod2(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def spectral_radius_2(P):
    tr = P[0][0] + P[1][1]
    det = P[0][0]*P[1][1] - P[0][1]*P[1][0]
    import math
    return (tr + math.sqrt(tr*tr - 4*det))/2

spec_cases=0
phi=(1+5**0.5)/2
for r in range(1,11):
    for s in product((0,1),repeat=r):
        P=((1,0),(0,1))
        for bit in s:P=prod2(P,M[bit])
        rho=spectral_radius_2(P)
        circular_alt=all(s[j]!=s[(j+1)%r] for j in range(r))
        constant=is_constant(s)
        if circular_alt:assert abs(rho-1)<1e-8,(r,s,rho)
        elif constant:assert abs(rho-phi**r)<1e-8,(r,s,rho)
        else:assert 1<rho<phi**r,(r,s,rho)
        spec_cases+=1
print('PASS',spec_cases,'periodic product spectral-trichotomy comparisons')

# Finite rational survival coefficients for two extremizers.
for n in range(1,20):
    low=Fraction(n+2,2**(n+1))
    high=Fraction(fibonacci(n+3),2**(n+1))
    assert low<=high
print('PASS finite-horizon rational probabilities; infinite expectation 3 and 5 analytically.')
