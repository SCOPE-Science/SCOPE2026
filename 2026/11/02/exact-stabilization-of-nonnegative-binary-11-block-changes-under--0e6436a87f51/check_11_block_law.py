#!/usr/bin/env python3
"""Exact finite-matrix certificate for the two-one shift 11-block law.
Run: python3 check_11_block_law.py (requires sympy).
"""
import sympy as S

z, lam = S.symbols('z lam')
states = [(u, v, c) for u in (0, 1) for v in (0, 1) for c in (0, 1)]
idx = {w: i for i, w in enumerate(states)}

def transition(bit):
    M = S.zeros(8)
    for i, (u, v, carry) in enumerate(states):
        for x in (0, 1):
            total = x + bit + carry
            y, newcarry = total % 2, total // 2
            M[i, idx[(x, y, newcarry)]] += z ** (v * y - u * x) / 2
    return M

M0, M1 = transition(0), transition(1)
# In the zero-suffix expectation, carry propagation is geometric.
core = z * (1 + z) / (2 * (2 * z - 1))
tail = S.Matrix([
    (S.Integer(1) if u == v else (1 + z ** (v-u))/2)
    if carry == 0 else (z**v * (1 + z) / 4 + z**(-u) * core / 2)
    for (u, v, carry) in states
])
row = S.zeros(1,8)
row[0, idx[(0,0,0)]] = 1
row = row * M1

def polynomial_part_at_infinity(expr):
    num, den = S.fraction(S.cancel(expr))
    q, rem = S.div(num, den, z)
    assert S.degree(rem, z) < S.degree(den, z)
    return S.expand(q)

Q_expected = [
    (8*z**2 + 22*z + 17)/64,
    (2*z**3 + 4*z**2 + 7*z + 9)/32,
    (16*z**3 + 36*z**2 + 62*z + 59)/256,
    (24*z**3 + 92*z**2 + 122*z + 105)/512,
    (6*z**3 + 22*z**2 + 33*z + 26)/128,
    (24*z**3 + 88*z**2 + 130*z + 109)/512,
    (12*z**3 + 44*z**2 + 65*z + 54)/256,
]
Fs = []
for a in range(1, 13):
    F = S.cancel((row * M1 * tail)[0])
    Fs.append(F)
    q = polynomial_part_at_infinity(F)
    assert S.expand(q - Q_expected[min(a-1,6)]) == 0, (a, q)
    assert S.cancel(F.subs(z, 1) - 1) == 0
    row = row * M0

characteristic = M0.charpoly(lam).as_expr()
assert S.cancel(characteristic - lam**6*(lam-1)*(lam-1/(2*z))) == 0
# Check Cayley-Hamilton starting at the correct power, not merely its eigenvalues.
Id = S.eye(8)
assert all(S.cancel(x) == 0 for x in (M0**6 * (M0-Id) * (M0-Id/(2*z))))

delta = S.cancel(Fs[7] - Fs[6])
expected_delta = -((z-1)**2 * (z+1) *
    (4*z**5-8*z**4+2*z**3-4*z**2+2*z-1) /
    (2048*z**8*(2*z-1)))
assert S.cancel(delta - expected_delta) == 0
assert polynomial_part_at_infinity(delta) == 0
for a in range(7, 11):
    assert S.cancel((Fs[a+1]-Fs[a]) - (Fs[a]-Fs[a-1])/(2*z)) == 0

assert S.expand(Q_expected[-1] - (54+65*z+44*z**2+12*z**3)/256) == 0
assert S.cancel(Q_expected[-1].subs(z,1) - S.Rational(175,256)) == 0
assert S.cancel(Q_expected[5].subs(z,1) - S.Rational(175,256)) != 0

# Independent finite enumerations of actual integer digit-pattern counts.
def adjacent_11(n):
    return (n & (n >> 1)).bit_count()
for a in range(1, 8):
    size = 1 << (a + 11)
    shift = (1 << a) + 1
    counts = [0, 0, 0, 0]
    for n in range(size):
        d = adjacent_11(n + shift) - adjacent_11(n)
        if 0 <= d <= 3:
            counts[d] += 1
        assert d <= 3
    for j in range(4):
        exact = S.Rational(counts[j], size)
        desired = Q_expected[a-1].coeff(z, j)
        assert abs(exact - desired) <= S.Rational(2, 1 << 10), (a, j, exact, desired)
print('VERIFY_OK: 12 exact rational generating functions, matrix CH identity, sharp threshold, 7 direct binary-count comparisons')
