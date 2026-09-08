"""Replay verifier for lane-203 Loewner flat-moduli stability (stdlib only).

Checks every numeric threshold used in DRAFT.md with exact integer/Fraction
arithmetic, plus a float sanity scan of the ratio delta/min(d_c^2,1).
Run: python3 verify_stability.py  (must print ALL CHECKS PASSED)
"""
from fractions import Fraction
import math

ok = []


def check(name, cond):
    assert cond, "FAILED: %s" % name
    ok.append(name)
    print("ok:", name)


# 1. sqrt(3) brackets: 1.732^2 < 3 < 1.733^2
check("1732^2<3e6", 1732**2 < 3_000_000)
check("1733^2>3e6", 1733**2 > 3_000_000)
SLO, SHI = Fraction(1732, 1000), Fraction(1733, 1000)  # sqrt3 in [SLO,SHI]

# 2. Tail: delta(8/5) >= 1/2  <=>  2/sqrt3 >= 9/8  (use sqrt3 <= SHI: 2/SHI>=9/8?)
check("tail: 2000/1733 >= 9/8", Fraction(2000, 1733) >= Fraction(9, 8))
# i.e. 16000 >= 15597
check("tail integer: 16000>=9*1733", 16_000 >= 9 * 1733)

# 3. Cap-a: delta(8/5) <= 13/24  <=>  2/sqrt3 <= 7/6  (use sqrt3 >= SLO)
check("cap-a: 12 <= 7*1.732 (scaled)", 12_000 <= 7 * 1732)
# exact form: 144 <= 49*3
check("cap-a integer: 144<=147", 144 <= 147)

# 4. Cap-b: 13/24 <= cosh(1)-1 via series cosh1 >= 1111/720 >= 37/24
# 1111/720 = 1+1/2+1/24+1/720 (positive-term truncation of cosh series)
check("cap-b: 37*30<=1111", 37 * 30 <= 1111)

# 5. Piece A slope: g'(y)/2 = 1-y+yh >= yh-3/5 > 0 on [1,8/5]; yh>0.866
check("slope: 0.866-0.6>0", Fraction(866, 1000) - Fraction(3, 5) > 0)

# 6. Piece A endpoint value g(8/5) > 0 (loose rigorous bound)
# g(8/5) >= 3.2-1.733-0.25-0.734^2
check("g(8/5)>0", Fraction(32, 10) - SHI - Fraction(1, 4)
      - Fraction(734, 1000) ** 2 > 0)

# 7. Piece B threshold identity: ((2+s)^2-1)/((2+s)^2+1) = s/2 for s^2=3
# (2+s)^2 = 7+4s; cross-multiply 2*(6+4s) =?= s*(8+4s) = 8s+4s^2.
# With s^2=3: LHS-RHS = 12+8s-8s-12 = (12-4*3) + (8-8)*s = 0. Exact integers:
check("threshold identity const part: 12-4*3==0", 12 - 4 * 3 == 0)
check("threshold identity s-coeff part: 8-8==0", 8 - 8 == 0)

# 8. (2-sqrt3)(2+sqrt3) = 4-3 = 1 (exact, needs only s^2=3)
check("(2-s)(2+s)=1 skeleton: 4-3==1", 4 - 3 == 1)

# 9. Float sanity scan: min over folded domain of delta/min(d_c^2,1) >= 0.5
yh = math.sqrt(3) / 2


def tmax(y):
    if y >= 1.0:
        N = 0.25 + (y - yh) ** 2
    else:
        w = math.sqrt(max(0.0, 1 - y * y))
        N = (0.5 - w) ** 2 + (y - yh) ** 2
    return N / (2 * y * yh)


def dmax(y):
    return math.acosh(1 + tmax(y))


def delta(y):
    return 2 / math.sqrt(3) - 1 / y


worst = 1e9
wy = None
y = yh + 1e-6
while y <= 30.0:
    d = dmax(y)
    m = min(d * d, 1.0)
    r = delta(y) / m
    if r < worst:
        worst, wy = r, y
    y += 1e-4
print("float scan: worst ratio %.6f at y=%.4f" % (worst, wy))
check("float worst ratio >= 0.51", worst >= 0.51)

# 10. Cap float sanity: tmax(8/5) <= delta(8/5), dmax(8/5) <= 1
check("t(8/5)<=delta(8/5)", tmax(1.6) <= delta(1.6))
check("dmax(8/5)<=1", dmax(1.6) <= 1.0)

print("\nALL CHECKS PASSED (%d)" % len(ok))
