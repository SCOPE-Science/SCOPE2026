from fractions import Fraction
from collections import defaultdict

def nu(k):
    return {x: Fraction(1, k) for x in range(-(k - 1), k, 2)}

def law_T(alpha):
    if not 0 < alpha <= 1:
        raise ValueError("alpha must lie in (0, 1]")
    k = 1
    while not (Fraction(1, k + 1) <= alpha <= Fraction(1, k)):
        k += 1
    tau = k * (k + 1) * alpha - k
    out = defaultdict(Fraction)
    for x, p in nu(k).items():
        out[x] += tau * p
    for x, p in nu(k + 1).items():
        out[x] += (1 - tau) * p
    return {x: p for x, p in out.items() if p}

def variance(law):
    mean = sum(Fraction(x) * p for x, p in law.items())
    return sum((Fraction(x) - mean) ** 2 * p for x, p in law.items())

def convolve(a, b):
    out = defaultdict(Fraction)
    for x, px in a.items():
        for y, py in b.items():
            out[x + y] += px * py
    return {x: p for x, p in out.items() if p}

def sum_law(laws):
    out = {0: Fraction(1)}
    for law in laws:
        out = convolve(out, law)
    return out

def q2(law):
    lo, hi = min(law), max(law)
    return max(law.get(j, Fraction(0)) + law.get(j + 1, Fraction(0))
               for j in range(lo - 1, hi + 1))

def alpha_for_variance(target):
    for k in range(1, 10000):
        left = Fraction(1, k + 1)
        right = Fraction(1, k)
        v_left = variance(law_T(left))
        v_right = variance(law_T(right))
        if v_right <= target <= v_left:
            return left + (target - v_left) * (right - left) / (v_right - v_left)
    raise ValueError("no variance-matching interval found")

alphas = [Fraction(1, 20), Fraction(1, 20), Fraction(1, 10)]
laws = [law_T(a) for a in alphas]
total_variance = sum((variance(law) for law in laws), Fraction(0))
alpha_star = alpha_for_variance(total_variance / 3)
equalized_law = law_T(alpha_star)

heterogeneous = sum_law(laws)
equalized = sum_law([equalized_law] * 3)
q_heterogeneous = q2(heterogeneous)
q_equalized = q2(equalized)

assert alpha_star == Fraction(619, 10710)
assert total_variance == 299
assert variance(equalized_law) == Fraction(299, 3)
assert q_heterogeneous == Fraction(7, 160)
assert q_equalized == Fraction(219116707, 5055477000)
assert q_heterogeneous - q_equalized == Fraction(8241647, 20221908000) > 0

print("alpha_star =", alpha_star)
print("total_variance =", total_variance)
print("Q2_heterogeneous =", q_heterogeneous)
print("Q2_equalized =", q_equalized)
print("strict_gap =", q_heterogeneous - q_equalized)
