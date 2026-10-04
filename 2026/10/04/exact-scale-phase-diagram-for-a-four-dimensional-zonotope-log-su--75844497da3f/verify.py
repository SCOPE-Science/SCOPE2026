#!/usr/bin/env python3
from itertools import combinations

def det4(cols):
    a = [list(row) for row in zip(*cols)]
    sign = 1
    den = 1
    for k in range(3):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, 4) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, 4):
            for j in range(k + 1, 4):
                a[i][j] = (a[i][j] * p - a[i][k] * a[k][j]) // den
        den = p
        for i in range(k + 1, 4):
            a[i][k] = 0
    return sign * a[3][3]

def volume(gens):
    return sum(abs(det4(c)) for c in combinations(gens, 4))

e1 = (1,0,0,0)
e2 = (0,1,0,0)
e3 = (0,0,1,0)
d24 = (0,1,0,-1)
d34 = (0,0,1,-1)
h = (1,-1,-1,0)
w = (1,0,0,-1)
wp = (0,1,-1,0)
base = [e1,e2,e3,d24,d34]

expected = [(4,10),(12,18),(8,18),(24,32)]
extras = [[],[w],[wp],[w,wp]]
coeffs = []
for extra in extras:
    intercept = volume(base + extra)
    slope = volume(base + [h] + extra) - intercept
    coeffs.append((intercept, slope))
assert coeffs == expected, (coeffs, expected)

# If V_i(s)=a_i+b_i s, compute the quadratic defect coefficients.
(a0,b0),(a1,b1),(a2,b2),(a3,b3) = coeffs
c0 = a0*a3 - a1*a2
c1 = a0*b3 + b0*a3 - a1*b2 - b1*a2
c2 = b0*b3 - b1*b2
assert (c0,c1,c2) == (0,8,-4)
assert [a+b for a,b in coeffs] == [14,30,26,56]
print('VERIFY_OK')
print('volume_affine_coefficients=', coeffs)
print('defect_coefficients=', (c0,c1,c2), '= 4*s*(2-s)')
