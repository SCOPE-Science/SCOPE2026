#!/usr/bin/env python3
"""Independent integer polynomial checks for the displayed Chern and Segre series."""
from math import comb
N = 5

def mul(a,b):
    return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]

def poly_power(linear, power):
    if power >= 0:
        return [comb(power,i)*linear**i if i <= power else 0 for i in range(N+1)]
    m=-power
    return [(-1)**i * comb(m+i-1,i)*linear**i for i in range(N+1)]

chern = mul(mul(poly_power(1,14),poly_power(3,1)),poly_power(2,-6))
segre = mul(mul(poly_power(-2,6),poly_power(-1,-14)),poly_power(-3,-1))
assert chern == [1,5,13,21,21,21], chern
assert segre == [1,5,12,16,8,0], segre
assert chern[5] == 21 and segre[5] == 0 and segre[4] == 8
assert (9,6-chern[1]) == (9,1)
print('VERIFY_OK chern=' + str(chern) + ' segre=' + str(segre) + ' degeneracy=21 fano_anticanonical=(9,1)')
