#!/usr/bin/env python3
"""Exact verification of a twelve-node Gaussian-integer cubic phase-retrieval design.

Requires SymPy 1.12 or later; uses exact rational symbolic arithmetic only.
"""
import itertools
import sympy as S

I = S.I
omega = [S.expand(b * I**j) for b in (1, 1+I, 2+I) for j in range(4)]
assert len(omega) == len(set(omega)) == 12
w, x, y, t = S.symbols('w x y t', real=True)

H = S.zeros(4)
for j, val in enumerate((-20*w, 34*w, -16*w, 2*w)):
    H[j, j] = val
upper = {
    (0, 1): 12*y+4*t+I*(-4*y+12*t),
    (0, 2): 2*x*(1-2*I),
    (0, 3): -2*y-t+I*(-y+2*t),
    (1, 2): -12*y-3*t+I*(3*y-12*t),
    (1, 3): 2*x*(-1+I),
    (2, 3): 2*y+2*I*t,
}
for (i, j), val in upper.items():
    H[i, j] = val
    H[j, i] = S.conjugate(val)

# Independently compute the full real-linear measurement matrix.
full = S.zeros(4)
params = []
for i in range(4):
    a = S.symbols(f'd{i}', real=True)
    full[i, i] = a
    params.append(a)
for i in range(4):
    for j in range(i+1, 4):
        a, b = S.symbols(f'a{i}{j} b{i}{j}', real=True)
        full[i, j] = a + I*b
        full[j, i] = a - I*b
        params.extend([a, b])

def evaluation(matrix, zz):
    return S.expand(sum(matrix[i, j] * zz**i * S.conjugate(zz)**j
                        for i in range(4) for j in range(4)))

measurements = S.Matrix([
    [S.expand(evaluation(full, zz)).coeff(q) for q in params]
    for zz in omega
])
assert measurements.shape == (12, 16)
assert measurements.rank() == 12, 'The measurement map must have nullity four'
for v in (w, x, y, t):
    assert all(S.expand(evaluation(H.diff(v), zz)) == 0 for zz in omega)
# Dimension 4 and four independent directions imply H spans the entire kernel.
Hcoordinates = S.Matrix([[S.expand(H[i,j]).coeff(v) for v in (w,x,y,t)]
     for i in range(4) for j in range(i,4)])
# Matrix entries can be complex, and diagonal already verifies w independence.
assert Hcoordinates.rank() == 4

# All 16 3x3 minors. Form real and imaginary parts as exact rational polynomials.
minors = []
for rows in itertools.combinations(range(4), 3):
    for cols in itertools.combinations(range(4), 3):
        q = S.expand(H.extract(rows, cols).det(method='berkowitz'))
        for f in (S.expand(S.re(q)), S.expand(S.im(q))):
            if f != 0 and f not in minors and -f not in minors:
                minors.append(f)
assert len(minors) == 16
G = S.groebner(minors, w, x, y, t, order='grevlex', domain=S.QQ)
forced = [
    t**5,
    4*w**3+w*t**2,
    3*x**3+12*x*t**2+85*w*t**2,
    81*y**3-1237*y*t**2-306*t**3,
]
for f in forced:
    assert G.reduce(f)[1] == 0, 'Specified elimination consequence absent'
# They force t=0, followed by w=x=y=0, over even the complex numbers.
# Hence no nonzero matrix in the four-dimensional kernel has rank <=2.

# First three distinct Gaussian-integer square orbits below radius sqrt(5)
# do not retrieve phase. Confirm this obstruction exactly.
small = [S.expand(b*I**j) for b in (1,1+I,2) for j in range(4)]
for zz in small:
    pa = 2*S.sqrt(7)*zz - I*S.sqrt(2)*zz**3
    pb = 4 - I*S.sqrt(14)*zz**2
    gap = S.expand(pa*S.conjugate(pa)-pb*S.conjugate(pb))
    assert S.simplify(S.expand_complex(gap)) == 0
assert 2*S.sqrt(7) != 0 and 4 != 0
print('PASS: 12 unique Gaussian-integer sites; 12x16 measurement rank 12; four-dimensional exact kernel')
print('PASS: all sixteen cubic minors and four Groebner elimination consequences')
print('PASS: no nonzero rank-at-most-two Hermitian kernel element over C')
print('PASS: explicit ambiguity at maximal squared radius four; squared radius five attained')
