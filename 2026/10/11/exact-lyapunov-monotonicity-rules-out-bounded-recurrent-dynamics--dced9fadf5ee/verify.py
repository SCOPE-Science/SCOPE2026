from fractions import Fraction as F
import cmath
import itertools


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0) for _ in range(n)]
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pneg(a):
    return [-v for v in a]


def pmul(a, b):
    out = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def parity(perm):
    inv = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inv += perm[i] > perm[j]
    return -1 if inv % 2 else 1


def det_poly(mat):
    n = len(mat)
    total = [F(0)]
    for perm in itertools.permutations(range(n)):
        term = [F(parity(perm))]
        for i, j in enumerate(perm):
            term = pmul(term, mat[i][j])
        total = padd(total, term)
    return total


def cubic_roots(coeffs):
    # Monic cubic, coefficients in descending order.
    def p(z):
        out = 0j
        for c in coeffs:
            out = out * z + complex(float(c))
        return out

    roots = [cmath.rect(12.0, 2.0 * cmath.pi * k / 3.0) for k in range(3)]
    for _ in range(500):
        new = []
        movement = 0.0
        for i, z in enumerate(roots):
            denom = 1 + 0j
            for j, w in enumerate(roots):
                if i != j:
                    denom *= z - w
            zn = z - p(z) / denom
            movement = max(movement, abs(zn - z))
            new.append(zn)
        roots = new
        if movement < 1e-14:
            break
    return sorted(roots, key=lambda z: (round(z.real, 10), z.imag))


m = F(11, 10)
r = F(61, 10)
g = F(12)
k6 = F(-100)
c = g * (1 + m) / (2 * r)
assert c == F(126, 61)

# H' = dz + 2*c*x*dx.  Track only coefficients of x^2 and x*y.
dz_x2 = g * m
dz_xy = -g * (1 + m)
correction = 2 * c * r
assert dz_x2 - correction == -g
assert dz_xy + correction == 0

# Jacobian at the origin for variables (x,y,z,u,v).
J = [
    [-r, r, F(0), F(0), F(0)],
    [m, -(1 + m), F(0), F(0), F(1)],
    [F(0), F(0), F(0), F(0), F(0)],
    [F(0), F(0), F(0), F(0), F(0)],
    [k6, F(0), F(0), F(-1), F(0)],
]

# Polynomial entries of lambda*I - J, represented in ascending powers.
M = []
for i in range(5):
    row = []
    for j in range(5):
        const = -J[i][j]
        if i == j:
            row.append([const, F(1)])
        else:
            row.append([const])
    M.append(row)

charpoly = det_poly(M)
expected = [F(0), F(0), F(610), F(61, 10), F(41, 5), F(1)]
assert charpoly == expected, (charpoly, expected)

roots = cubic_roots([F(1), F(41, 5), F(61, 10), F(610)])
real_root = min(roots, key=lambda z: z.real)
complex_roots = sorted([z for z in roots if z is not real_root], key=lambda z: z.imag)
assert abs(real_root.real + 11.9566842997270) < 1e-9
assert abs(real_root.imag) < 1e-9
for z in complex_roots:
    assert abs(z.real - 1.87834214986351) < 1e-9
assert abs(complex_roots[0].imag + 6.89124944793202) < 1e-9
assert abs(complex_roots[1].imag - 6.89124944793202) < 1e-9

print('VERIFY_OK')
