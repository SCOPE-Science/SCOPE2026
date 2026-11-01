#!/usr/bin/env python3
"""Exact, self-contained algebra checks for Fock Taylor-jet approximation asymptotics.

These finite checks do not establish the infinite-dimensional asymptotic theorem;
the analytic proof gives that conclusion.
"""
from fractions import Fraction as F
from math import comb, factorial

count = 0


def det(a):
    """Exact determinant by elimination with rational pivots."""
    n = len(a)
    if n == 0:
        return F(1)
    x = [row[:] for row in a]
    d = F(1)
    for k in range(n):
        p = next((i for i in range(k, n) if x[i][k]), None)
        if p is None:
            return F(0)
        if p != k:
            x[k], x[p] = x[p], x[k]
            d = -d
        v = x[k][k]
        d *= v
        for i in range(k+1, n):
            if x[i][k]:
                r = x[i][k] / v
                for h in range(k+1, n):
                    x[i][h] -= r*x[k][h]
                x[i][k] = F(0)
    return d


def gram_jet(m, n, c):
    """Fock Gaussian moment inner product of (z-c)^m and (z-c)^n for real c."""
    return sum(F(comb(m,k)*comb(n,k)*factorial(k)) * (-c)**(m+n-2*k)
               for k in range(min(m,n)+1))


def truncated_kernel(j, c):
    return sum(c**(2*k)/factorial(k) for k in range(j))


for c in [F(0), F(1,3), F(1,2), F(1), F(3,2), F(2)]:
    last = F(1)
    for j in range(1, 9):
        G = [[gram_jet(m, n, c) for n in range(1,j+1)]
             for m in range(1,j+1)]
        now = det(G)
        delta = now/last
        K = truncated_kernel(j,c)
        expected = F(factorial(j)) + c**(2*j)/K
        assert delta == expected, (c,j,delta,expected)
        count += 1
        last = now
        # Weyl-translated derivative representers have Gram diagonal scale 1/j!.
        # Consequently their Gram pivots are exp(|c|^2)*delta/(j!)^2.
        # Verify the determinant pivot for the rational (exponential-free) part.
        H = [[gram_jet(m,n,-c)/F(factorial(m)*factorial(n))
              for n in range(1,j+1)] for m in range(1,j+1)]
        H0 = [[gram_jet(m,n,-c)/F(factorial(m)*factorial(n))
              for n in range(1,j)] for m in range(1,j)]
        assert det(H)/det(H0) == expected / F(factorial(j)**2)
        count += 1

# The rank-one Taylor-jet decomposition holds as a rational polynomial identity
# for arbitrary f(z)=z^n, with coefficients in t.
for c in [F(0),F(1,4),F(1),F(-3,2)]:
    for n in range(1,12):
        for t in [F(1,3),F(-1,4)]:
            for z in [F(0),F(3,4),F(-5,4)]:
                lhs=(c+t*(z-c))**n-c**n
                rhs=sum(t**j*(z-c)**j*F(comb(n,j))*c**(n-j)
                        for j in range(1,n+1))
                assert lhs==rhs
                count+=1

# Exact upper bound used for trace-norm Taylor convergence.
def math_falling(m,l):
    x=1
    for k in range(l): x*=m-k
    return x

for c in [F(0),F(1,3),F(1),F(5,2)]:
    for m in range(1,25):
        # E|Z-c|^(2m)/m! = sum_{l<=m} (m)_l/(l!)^2 |c|^(2l)
        a=sum(F(math_falling(m,l),factorial(l)**2)*c**(2*l)
              for l in range(m+1))
        b=sum(F(m**l,factorial(l)**2)*c**(2*l)
              for l in range(m+1))
        assert a<=b
        count+=1

print(f'PASS: {count} exact rational assertions (jet Gram pivots, Taylor expansion, trace bounds).')


