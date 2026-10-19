"""Self-contained reproduction of algebraic witnesses and scalar phase bounds.

Run: python3 verify.py
Finite-grid comparisons are numerical diagnostics, not a proof of the theorem.
"""
from fractions import Fraction as F
from dataclasses import dataclass
import math
import random

@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def make(x):
        return x if isinstance(x, Q3) else Q3(F(x))

    def __add__(self, other):
        other = self.make(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.make(other))

    def __rsub__(self, other):
        return self.make(other) - self

    def __mul__(self, other):
        other = self.make(other)
        return Q3(self.a * other.a + 3 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.make(other)
        denom = other.a * other.a - 3 * other.b * other.b
        assert denom != 0
        return self * Q3(other.a / denom, -other.b / denom)

    def __rtruediv__(self, other):
        return self.make(other) / self

    def __float__(self):
        return float(self.a) + math.sqrt(3) * float(self.b)

ONE = Q3.make(1)
THREE = Q3.make(3)
SQRT3 = Q3(F(0), F(1))

# Exact witness: Q=[[3,1],[1,1]], variance=1, budget=3.
a = Q3.make(2)
b = ONE
d = 2 * SQRT3
c = a / d
critical = (3 - c) / (1 + c)
s = (1 + c) * (3 - critical) / 4
K = 4 * b / (a + d)
v = 1 + s
t = K * v
r = K * K * v
p = s + r
objective = 3 * v + 2 * t + p
assert critical == 5 - 2 * SQRT3
assert s == 1 / SQRT3
assert K == SQRT3 - 1
assert t == 2 / SQRT3
assert p == 2 - 1 / SQRT3
assert v + p == THREE
assert t * t == v * r
assert objective == 5 + 2 * SQRT3
assert 3 * 1 - 1 * 1 == 2  # positive definite Q
lambda_critical = ONE + (a + d) / 4
assert 2 * lambda_critical - 4 - ONE / (lambda_critical - ONE) == Q3.make(0)
assert ONE + ONE / ((lambda_critical - ONE) * (lambda_critical - ONE)) == critical
assert float(objective) > 5 + 2 * math.sqrt(2)
exact_identities = 13


def formula(xx, uu, cross, variance, beta):
    aa = xx - uu
    bb = abs(cross)
    dd = math.hypot(aa, math.sqrt(8.0) * bb)
    cc = aa / dd
    threshold = variance * (3.0 - cc) / (1.0 + cc)
    q = beta - variance
    ss = max(0.0, (1.0 + cc) * (beta - threshold) / 4.0)
    if beta <= threshold:
        kk = math.copysign(math.sqrt(q / variance), cross)
        optimum = xx * variance + uu * q + 2 * bb * math.sqrt(variance * q)
    else:
        kk = math.copysign(4 * bb / (aa + dd), cross)
        optimum = (xx * variance + uu * q
                   + (aa * (q - 2 * variance) + dd * (q + 2 * variance)) / 4)
    return ss, kk, optimum, threshold

rng = random.Random(342611)
comparisons = 0
dual_checks = 0
phase_cases = [0, 0]
for _ in range(160):
    xx = 10 ** rng.uniform(-1, 1)
    uu = 10 ** rng.uniform(-1, 1)
    cross = rng.choice((-1, 1)) * rng.uniform(0.025, 0.90) * math.sqrt(xx * uu)
    variance = 10 ** rng.uniform(-1, 1)
    aa = xx - uu
    bb = abs(cross)
    dd = math.hypot(aa, math.sqrt(8) * bb)
    cc = aa / dd
    critical = variance * (3 - cc) / (1 + cc)
    tcrit = (aa + dd) / 4
    lcrit = uu + tcrit
    assert tcrit > 0
    assert abs(2 * lcrit - xx - uu - bb * bb / (lcrit - uu)) <= 2e-9 * (1 + abs(lcrit))
    assert abs(variance * (1 + (bb / tcrit) ** 2) - critical) <= 2e-9 * (1 + critical)
    dual_checks += 2
    # Exercise both sides of the transition, including near the boundary.
    for beta in (variance + 0.5 * (critical - variance),
                 critical + 0.25 * (critical - variance)):
        ss, kk, opt, crit2 = formula(xx, uu, cross, variance, beta)
        assert abs(crit2 - critical) < 1e-9 * (1 + critical)
        assert ss >= -1e-10 and ss <= (beta - variance) / 2 + 1e-9
        phase_cases[int(beta > critical)] += 1
        q = beta - variance
        rr = q - 2 * ss
        assert rr >= -1e-9
        kk2 = math.copysign(math.sqrt(rr / (variance + ss)), cross)
        assert abs(kk - kk2) <= 1e-8 * (1 + abs(kk2))
        target = xx * variance + uu * q + aa * ss + 2 * bb * math.sqrt((variance + ss) * max(0.0, rr))
        assert abs(opt - target) <= 1e-8 * (1 + abs(opt))
        for j in range(100):
            test_s = (q / 2) * j / 99
            trial = (xx * variance + uu * q + aa * test_s
                     + 2 * bb * math.sqrt(max(0., (variance + test_s) * (q - 2 * test_s))))
            assert trial <= opt + 2e-8 * (1 + abs(opt))
            comparisons += 1
assert phase_cases == [160, 160]
print('VERIFY_OK exact_quadratic_surd_witness_identities=%d dual_boundary_checks=%d grid_global_inequalities=%d phase_cases=%d' %
      (exact_identities, dual_checks, comparisons, sum(phase_cases)))
