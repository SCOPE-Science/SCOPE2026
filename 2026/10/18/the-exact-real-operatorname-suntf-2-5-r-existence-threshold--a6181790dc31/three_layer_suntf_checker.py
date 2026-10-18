"""Exact symbolic checks for a real stratified unit-norm tight-frame construction.

Dependency: SymPy >= 1.12. Run: python three_layer_suntf_checker.py
"""
from sympy import I, Rational, sqrt, simplify, re, conjugate, pi, cos, eye, ones

s = sqrt(Rational(3, 2))
a = (s - 1) / 2
b = s / 2
c = sqrt(1 - a*a)
d = sqrt(1 - b*b)
z = (1, a+I*c, a-I*c, -b+I*d, -b-I*d)

# Five algebraic points on the circle, with two balanced 3/2-sums.
assert all(simplify(w*conjugate(w) - 1) == 0 for w in z)
assert simplify(z[0]+z[1]+z[2]-s) == 0
assert simplify(z[3]+z[4]+s) == 0

rows = [tuple(z[(j+r)%3] if j < 3 else z[j] for j in range(5))
        for r in range(3)]

# Zero doubled-angle phasor sum is equivalent to a real 2D UNTF.
for row in rows:
    assert simplify(sum(row, 0)) == 0

# Exact ten pairwise squared-Gram identities, averaged over three rows.
for j in range(5):
    for k in range(j+1, 5):
        overlap = simplify(sum(re(row[j]*conjugate(row[k]))
                               for row in rows))
        assert overlap == -Rational(3, 4), (j, k, overlap)
        assert simplify((3 + overlap)/6 - Rational(3, 8)) == 0

# Independently construct the known two-layer system from five roots of unity.
for offset in range(1, 5):
    assert simplify(cos(2*pi*offset/5)+cos(4*pi*offset/5)
                    +Rational(1, 2)) == 0

# A single layer would require a rank-four Gram matrix in dimension two.
putative_real_gram = Rational(5, 4)*eye(5) - Rational(1, 4)*ones(5, 5)
assert putative_real_gram.rank() == 4

print('PASS: exact unit-phasor and tightness conditions in all three layers.')
print('PASS: exact stratification with squared overlap 3/8 for all ten pairs.')
print('PASS: exact two-layer pentagonal comparison and one-layer obstruction.')
