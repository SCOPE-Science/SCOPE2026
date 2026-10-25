"""Exact polynomial and finite Fourier checks for stride-three circulant cat maps.

The universal statements require the analytical proof in RESULT.md.
"""
import cmath
import math


def add(a, b):
    out = [0] * max(len(a), len(b))
    for j, v in enumerate(a):
        out[j] += v
    for j, v in enumerate(b):
        out[j] += v
    return out


def neg(a):
    return [-x for x in a]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for j, av in enumerate(a):
        for k, bv in enumerate(b):
            out[j+k] += av * bv
    return out


def vector(n):
    return [0] + [int((k-1) % 3 == 0 or (n-k-1) % 3 == 0)
                  for k in range(1, n)]


def phi(x):
    return 2 * math.asinh(abs(x) / 2)


checks = 0
for n in range(3, 501):
    s = vector(n)
    lhs = mul([1, 1, 1], s)
    if n % 3 == 1:
        lhs = add(lhs, [1, 0, 1])
        rhs = mul([1, 0, 1], [1] * n)
    elif n % 3 == 2:
        lhs = add(lhs, [0, -1])
        rhs = mul([0, 0, 1], [1] * n)
    else:
        lhs = mul([1, 0, 0, -1], s)
        rhs = mul([0, 1, 1], add([1], [0] * n + [-1]))
        # (z+z^2)(1-z^n) is the rank-three geometric-sum certificate.
    lhs.extend([0] * (max(len(lhs), len(rhs)) - len(lhs)))
    rhs.extend([0] * (max(len(lhs), len(rhs)) - len(rhs)))
    assert lhs == rhs, ('polynomial', n)
    checks += 1
print('EXACT_POLYNOMIAL_IDENTITIES_PASS', checks)

spec_tests = 0
for n in range(3, 121):
    s = vector(n)
    for j in range(n):
        z = cmath.exp(2j * math.pi * j / n)
        eig = sum(v * z**k for k, v in enumerate(s))
        if j == 0:
            expected = 2*(n//3) if n % 3 != 2 else n//3 + 1
        elif n % 3 == 0:
            expected = -n/3 if j in (n//3, 2*n//3) else 0
        elif n % 3 == 1:
            c = math.cos(2 * math.pi * j / n)
            expected = -2*c/(1+2*c)
        else:
            c = math.cos(2 * math.pi * j / n)
            expected = 1/(1+2*c)
        assert abs(eig - expected) < 2e-7, ('spectrum', n, j, eig, expected)
        spec_tests += 1
    if n % 3 == 0:
        m = n//3
        direct = sum(phi(sum(s[k]*cmath.exp(2j*math.pi*j*k/n) for k in range(n)).real)
                     for j in range(n))
        exact = phi(2*m)+2*phi(m)
        assert abs(direct-exact) < 2e-8, ('entropy', n)
print('FOURIER_SPECTRUM_PASS', spec_tests)

for m in range(1, 100):
    assert sum(vector(3*m)) == sum(vector(3*m+1)) == 2*m
print('EQUAL_DEGREE_RESONANCE_PASS', 99)

# Numerical diagnostics are finite checks, not a proof of the limiting integrals.
def midpoint_integral(a, count=400000):
    val = 0.0
    for j in range(count):
        theta = 2*math.pi*(j+0.337)/count
        c = math.cos(theta)
        v = (-2*c/(1+2*c)) if a == 1 else 1/(1+2*c)
        val += phi(v)
    return val/count

constants = [midpoint_integral(a) for a in (1,2)]
assert 1.38 < constants[0] < 1.40
assert 1.26 < constants[1] < 1.29
for m in (1000, 2000):
    for a in (1, 2):
        n = 3*m + a
        degree = 2*m if a == 1 else m+1
        total = phi(degree)
        for j in range(1, n):
            c = math.cos(2*math.pi*j/n)
            total += phi((-2*c/(1+2*c)) if a == 1 else 1/(1+2*c))
        assert abs(total/n - constants[a-1]) < 0.01
print('LIMIT_DIAGNOSTICS_PASS', *(f'{x:.9f}' for x in constants))
