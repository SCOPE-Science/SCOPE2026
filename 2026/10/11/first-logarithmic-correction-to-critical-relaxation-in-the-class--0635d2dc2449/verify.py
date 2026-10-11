from fractions import Fraction as F

sigma = F(10)
beta = F(8, 3)
C = F(1, 1) / beta
A = -F(1, 1) / (beta * (sigma + 1))
D = -(beta - 2 * sigma) / (beta**3 * (sigma + 1))
B = -(2 * beta * sigma - beta + 2 * sigma**2 + 2 * sigma) / (beta**3 * (sigma + 1)**3)

# Polynomials are coefficient lists in ascending powers of x.
def add(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0)) for i in range(n)]

def mul(p, q, n=8):
    r = [F(0)] * min(n, len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            if i + j < len(r):
                r[i + j] += a * b
    return r

def scale(p, a):
    return [a * v for v in p]

def deriv(p):
    return [F(i) * p[i] for i in range(1, len(p))]

def coeff(p, k):
    return p[k] if k < len(p) else F(0)

x = [F(0), F(1)]
y = [F(0), F(1), F(0), A, F(0), B]
z = [F(0), F(0), C, F(0), D]
dx = scale(add(y, scale(x, -1)), sigma)
field_y = add(add(x, scale(y, -1)), scale(mul(x, z), -1))
field_z = add(mul(x, y), scale(z, -beta))
res_y = add(mul(deriv(y), dx), scale(field_y, -1))
res_z = add(mul(deriv(z), dx), scale(field_z, -1))
assert coeff(res_y, 3) == 0
assert coeff(res_y, 5) == 0
assert coeff(res_z, 2) == 0
assert coeff(res_z, 4) == 0

c = sigma / (beta * (sigma + 1))
q = sigma * B
assert C == F(3, 8)
assert A == -F(3, 88)
assert D == F(117, 1408)
assert B == -F(1827, 170368)
assert q == -F(9135, 85184)
assert 2 * c == F(15, 22)
assert -q / c == F(609, 1936)
print('VERIFY_OK')
