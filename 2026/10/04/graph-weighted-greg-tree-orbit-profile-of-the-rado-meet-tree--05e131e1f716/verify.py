#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

N = 10

def odd_double_factorial(m):
    r = 1
    for j in range(m, 0, -2):
        r *= j
    return r

# Route 1: classical Greg-tree triangle recurrence (OEIS A048160).
t = [[0]*(N+2) for _ in range(N+1)]
t[1][0] = 1
for n in range(2, N+1):
    for k in range(0, n):
        t[n][k] = ((n+k-2)*t[n-1][k-1] if k >= 1 else 0) \
                + (2*n+2*k-2)*t[n-1][k] \
                + (k+1)*t[n-1][k+1]

# Route 2: exact coefficient expansion of G = x exp(G) + u(exp(G)-1-G).
# P[n] is [u^k] [x^n] G, so n!*P[n][k] must equal g_(n,k).
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(a,b):
    c = [Fraction(0) for _ in range(max(len(a),len(b)))]
    for i,x in enumerate(a): c[i] += x
    for i,x in enumerate(b): c[i] += x
    return trim(c)

def mul(a,b):
    c = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    return trim(c)

def scale(a,c):
    return trim([x*c for x in a])

def ushift(a):
    return [Fraction(0)] + list(a)

P = [[Fraction(0)] for _ in range(N+1)]
E = [[Fraction(0)] for _ in range(N+1)]
E[0] = [Fraction(1)]
for n in range(1, N+1):
    # If E=exp(G), then E_n=P_n+Q_n with
    # Q_n=(1/n) sum_{j=1}^{n-1} j P_j E_{n-j}.
    q = [Fraction(0)]
    for j in range(1,n):
        q = add(q, scale(mul(P[j], E[n-j]), Fraction(j,n)))
    # Coefficient n of the defining equation simplifies to P_n=E_{n-1}+u Q_n.
    P[n] = add(E[n-1], ushift(q))
    E[n] = add(P[n], q)

species = [[0]*(N+1) for _ in range(N+1)]
for n in range(1,N+1):
    for k,c in enumerate(P[n]):
        z = c*factorial(n)
        assert z.denominator == 1
        species[n][k] = z.numerator
        assert species[n][k] == t[n][k], (n,k,species[n][k],t[n][k])

published = {
  1:[1],
  2:[2,1],
  3:[9,10,3],
  4:[64,113,70,15],
  5:[625,1526,1450,630,105],
  6:[7776,24337,31346,20650,6930,945],
  7:[117649,450066,733845,650188,329175,90090,10395],
}
for n,row in published.items():
    assert t[n][:n] == row, (n,t[n][:n],row)

# Extreme column consists of rooted binary trees with n labeled leaves.
for n in range(1,N+1):
    assert t[n][n-1] == odd_double_factorial(2*n-3)

# Apply arbitrary simple-graph decorations on each n+k vertex closure.
def orbit_count(n):
    return sum(t[n][k] * (1 << ((n+k)*(n+k-1)//2)) for k in range(n))

expected = [
    None,
    1,
    12,
    3784,
    33870848,
    7387750908928,
    34292468404362149888,
    3148355325124185283750789120,
]
for n in range(1,8):
    assert orbit_count(n) == expected[n], (n,orbit_count(n),expected[n])

print('VERIFY_OK')
