"""Exact rational tests for the four-size moment order and the five-size boundary.

No numerical approximation is used. Run with Python 3.9+:
    python check.py
The tests corroborate, but do not replace, the analytic divided-difference proof.
"""
from fractions import Fraction as F
from itertools import combinations


def moment(p, ns, order):
    return sum((a * (n ** order) for a, n in zip(p, ns)), F(0))


def pgf(p, ns, q):
    return sum((a * (q ** (n-1)) for a, n in zip(p, ns)), F(0))


def weights(ns):
    return [F(1, __import__('math').prod((ni - nj) for j, nj in enumerate(ns) if j != i))
            for i, ni in enumerate(ns)]


checks = 0
for ns in combinations(range(2, 12), 4):
    w = weights(ns)
    for k in range(3):
        assert moment(w, ns, k) == 0
        checks += 1
    assert moment(w, ns, 3) == 1
    checks += 1

    amplitude = F(1, 8) / max(abs(x) for x in w)
    p_hi = [F(1, 4) + amplitude*x for x in w]
    p_lo = [F(1, 4) - amplitude*x for x in w]
    assert min(p_hi + p_lo) > 0
    assert moment(p_hi, ns, 3) > moment(p_lo, ns, 3)
    for k in range(3):
        assert moment(p_hi, ns, k) == moment(p_lo, ns, k)
        checks += 1
    for q in (F(1, 5), F(1, 3), F(1, 2), F(4, 5)):
        assert pgf(p_hi, ns, q) < pgf(p_lo, ns, q)
        checks += 1

ns4 = [2, 3, 4, 5]
p_lower_m3 = [F(v, 24) for v in (7, 3, 9, 5)]
p_higher_m3 = [F(v, 24) for v in (5, 9, 3, 7)]
for k in range(3):
    assert moment(p_lower_m3, ns4, k) == moment(p_higher_m3, ns4, k)
    checks += 1
assert moment(p_higher_m3, ns4, 3) - moment(p_lower_m3, ns4, 3) == F(1, 2)
assert pgf(p_lower_m3, ns4, F(1, 2)) == F(91, 384)
assert pgf(p_higher_m3, ns4, F(1, 2)) == F(89, 384)
assert pgf(p_lower_m3, ns4, F(1, 2)) > F(15, 64) > pgf(p_higher_m3, ns4, F(1, 2))
checks += 4

ns5 = [2, 3, 4, 5, 6]
p_plus = [F(v, 40) for v in (9, 4, 14, 4, 9)]
p_minus = [F(v, 40) for v in (7, 12, 2, 12, 7)]
assert min(p_plus + p_minus) > 0
for k in range(4):
    assert moment(p_plus, ns5, k) == moment(p_minus, ns5, k)
    checks += 1
assert [moment(p_plus, ns5, i) for i in range(4)] == [F(1), F(4), F(18), F(88)]
assert pgf(p_plus, ns5, F(1, 2)) == F(249, 1280)
assert pgf(p_minus, ns5, F(1, 2)) == F(247, 1280)
assert pgf(p_plus, ns5, F(1, 2)) > F(31, 160) > pgf(p_minus, ns5, F(1, 2))
for q in (F(1, 7), F(1, 3), F(1, 2), F(5, 7)):
    assert pgf(p_plus, ns5, q) - pgf(p_minus, ns5, q) == F(1, 20)*q*(1-q)**4
    checks += 1
checks += 5

print(f"PASS: {checks} exact-rational assertions; 210 ordered four-size support choices; two explicit sharp examples.")
