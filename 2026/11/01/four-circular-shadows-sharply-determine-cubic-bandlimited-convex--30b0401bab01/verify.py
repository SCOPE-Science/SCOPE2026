#!/usr/bin/env python3
"""Self-contained rational rank and diagonal-plane identity checks."""
from fractions import Fraction
from math import pi, sqrt, sin, cos

def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    if not a: return 0
    n = len(a[0])
    for col in range(n):
        k = next((j for j in range(r, len(a)) if a[j][col]), None)
        if k is None: continue
        a[r], a[k] = a[k], a[r]
        pivot = a[r][col]
        a[r] = [v/pivot for v in a[r]]
        for j in range(len(a)):
            if j != r and a[j][col]:
                z = a[j][col]
                a[j] = [v-z*w for v,w in zip(a[j],a[r])]
        r += 1
        if r == len(a): break
    return r

# Q = A*x*x + B*y*y + C*z*z + 2*D*x*y + 2*E*x*z + 2*F*y*z.
quadratic = [
    [1,-1,0,0,0,0], [0,0,0,1,0,0],
    [1,0,-1,0,0,0], [0,0,0,0,1,0],
    [0,1,-1,0,0,0], [0,0,0,0,0,1],
    [1,1,1,0,0,0],
]
assert rank(quadratic) == 6

# C = p*x^3+q*y^3+r*z^3+s*x^2*y+t*x^2*z+v*x*y^2+
#     w*y^2*z+j*x*z^2+k*y*z^2+gamma*x*y*z.
# Six planar third-mode equations plus the three Laplace equations.
cubic = [
    [-1,0,0,0,0,1,0,0,0,0],  # v-p
    [0,-1,0,1,0,0,0,0,0,0],   # s-q
    [-1,0,0,0,0,0,0,1,0,0],  # j-p
    [0,0,-1,0,1,0,0,0,0,0],  # t-r
    [0,-1,0,0,0,0,0,0,1,0],  # k-q
    [0,0,-1,0,0,0,1,0,0,0],  # w-r
    [3,0,0,0,0,1,0,1,0,0],   # Laplacian coefficient x/2
    [0,3,0,1,0,0,0,0,1,0],   # Laplacian coefficient y/2
    [0,0,3,0,1,0,1,0,0,0],   # Laplacian coefficient z/2
]
assert rank(cubic) == 9
assert rank(cubic+[[0,0,0,0,0,0,0,0,0,1]]) == 10

# In the diagonal orthonormal frame, xyz equals sin(3theta)/(3sqrt(6)).
for j in range(720):
    theta = (j + 0.34) * 2*pi/720
    a,b = cos(theta), sin(theta)
    x = a/sqrt(2)+b/sqrt(6)
    y = -a/sqrt(2)+b/sqrt(6)
    z = -2*b/sqrt(6)
    assert abs(x*y*z - sin(3*theta)/(3*sqrt(6))) < 2e-14

# The eight cube diagonal directions are exact extremizers.
for x in (-1,1):
  for y in (-1,1):
    for z in (-1,1):
      u1,u2,u3 = x/sqrt(3),y/sqrt(3),z/sqrt(3)
      assert abs(abs(u1*u2*u3)-1/(3*sqrt(3))) < 1e-14
assert abs((1/(3*sqrt(3)))/(1/(3*sqrt(6)))-sqrt(2)) < 1e-14
print('PASS: exact rational ranks (6,9,10), 720 angular identities, eight extremizers, and sqrt(2) residual ratio')
