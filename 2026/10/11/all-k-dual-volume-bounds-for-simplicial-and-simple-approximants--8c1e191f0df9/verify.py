from fractions import Fraction
from math import comb

def phi(d,k,v):
    if k == 0:
        return v
    if 1 <= k <= d-2:
        return comb(d,k)*v - k*comb(d+1,k+1)
    if k == d-1:
        return (d-1)*v - (d+1)*(d-2)
    raise ValueError

def Lambda(d,k,M):
    if k == 0:
        return Fraction(M,1)
    if 1 <= k <= d-2:
        return Fraction(M + k*comb(d+1,k+1), comb(d,k))
    if k == d-1:
        return Fraction(M + (d+1)*(d-2), d-1)
    raise ValueError

for d in range(2,41):
    for k in range(d):
        for extra in (0,1,2,5,d,2*d+3):
            v = d+1+extra
            M = phi(d,k,v)
            assert Lambda(d,k,M) == v
            assert phi(d,k,d+1) == comb(d+1,k+1)
        ell = d-1-k
        assert 0 <= ell <= d-1
        assert d-1-ell == k

# Explicit endpoint consistency.
for d in range(2,41):
    for M in (d+1, 2*d+5, 1000):
        assert Lambda(d,0,M) == M
        assert Lambda(d,d-1,phi(d,d-1,M)) == M

print('VERIFY_OK')
print('dimensions=2..40')
print('stacked_face_formula_inverse=exact')
print('polarity_index_map=exact')
