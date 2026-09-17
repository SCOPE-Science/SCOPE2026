#!/usr/bin/env python3
"""
Reproducible certificate for SCOPE run:
A 4-coloring of [n] with asymptotic rainbow-Schur density 16/27.

The script:
1. computes the continuous-area proof exactly with fractions;
2. verifies the residue-pair area table;
3. brute-force counts the construction for several n divisible by 36;
4. checks the exact finite formula observed for those n:
      R_n = 8 n^2 / 27 + 5 n / 18.
"""

from fractions import Fraction as Q
from itertools import product

A, B, C, D = range(4)

def color_by_residue_and_bin(r, i):
    # bins: 0=L=(0,1/4], 1=M=(1/4,2/3], 2=H=(2/3,1]
    if r == 0:
        return A
    if i == 0:
        return B
    if i == 1:
        return C if r == 1 else D
    return D if r == 1 else C

bounds = [(Q(0), Q(1,4)), (Q(1,4), Q(2,3)), (Q(2,3), Q(1))]

def positive(x):
    return x if x > 0 else Q(0)

def rect_sum_leq(t, l1, u1, l2, u2):
    # Area of {(x,y) in [l1,u1]x[l2,u2] : x+y <= t}
    return Q(1,2) * (
        positive(t-l1-l2)**2
        - positive(t-u1-l2)**2
        - positive(t-l1-u2)**2
        + positive(t-u1-u2)**2
    )

def cell_area(i, j, k):
    l1,u1 = bounds[i]
    l2,u2 = bounds[j]
    l3,u3 = bounds[k]
    return rect_sum_leq(u3,l1,u1,l2,u2) - rect_sum_leq(l3,l1,u1,l2,u2)

def good_area(r, s):
    z = (r+s) % 3
    ans = Q(0)
    for i,j,k in product(range(3), repeat=3):
        ar = cell_area(i,j,k)
        if len({
            color_by_residue_and_bin(r,i),
            color_by_residue_and_bin(s,j),
            color_by_residue_and_bin(z,k)
        }) == 3:
            ans += ar
    return ans

expected = {
    (0,0): Q(0),
    (0,1): Q(47,144), (0,2): Q(47,144),
    (1,0): Q(47,144), (2,0): Q(47,144),
    (1,1): Q(1,4), (2,2): Q(1,4),
    (1,2): Q(31,72), (2,1): Q(31,72),
}

print("Residue-pair good areas:")
total_area = Q(0)
for r in range(3):
    for s in range(3):
        a = good_area(r,s)
        print((r,s), a)
        assert a == expected[(r,s)]
        total_area += a

# Each residue pair has density 1/9 in Z^2.
rainbow_n2_coefficient = total_area / 9
fraction_of_all_schur_triples = 2 * rainbow_n2_coefficient

print("\nSum of good areas =", total_area)
print("Rainbow count coefficient =", rainbow_n2_coefficient)
print("Asymptotic fraction =", fraction_of_all_schur_triples)
assert total_area == Q(8,3)
assert rainbow_n2_coefficient == Q(8,27)
assert fraction_of_all_schur_triples == Q(16,27)

def construction(n):
    c = [None]*(n+1)
    for x in range(1,n+1):
        r = x % 3
        if r == 0:
            c[x] = A
        elif 4*x <= n:
            c[x] = B
        elif 3*x <= 2*n:
            c[x] = C if r == 1 else D
        else:
            c[x] = D if r == 1 else C
    return c

def count_rainbow(n):
    c = construction(n)
    R = 0
    for x in range(1,n):
        for y in range(1,n-x+1):
            z = x+y
            if len({c[x],c[y],c[z]}) == 3:
                R += 1
    return R

print("\nFinite checks (n divisible by 36):")
for n in [36,72,108,180,252,360]:
    R = count_rainbow(n)
    formula = Q(8,27)*n*n + Q(5,18)*n
    assert formula.denominator == 1
    assert R == formula.numerator
    frac = Q(R, n*(n-1)//2)
    print(f"n={n:3d}  R={R:6d}  fraction={float(frac):.12f}")

print("\nAll checks passed.")
