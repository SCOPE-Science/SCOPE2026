from fractions import Fraction


def delta_bernoulli(p: Fraction) -> Fraction:
    m = max(p, 1 - p)
    return 1 / (m * m) - 1


def delta_sum(p: Fraction, q: Fraction) -> Fraction:
    probs = ((1-p)*(1-q), p*(1-q)+(1-p)*q, p*q)
    m = max(probs)
    return 1 / (m * m) - 1

# Exact rational stress test on a dense finite grid.  The theorem itself is
# proved analytically in RESULT.md; this finite check is only supplemental.
for i in range(101):
    p = Fraction(i, 100)
    for j in range(101):
        q = Fraction(j, 100)
        lhs = delta_sum(p, q)
        rhs = (delta_bernoulli(p) + delta_bernoulli(q)) / 2
        assert lhs >= rhs

p = q = Fraction(1, 2)
ratio = delta_sum(p, q) / (delta_bernoulli(p) + delta_bernoulli(q))
assert ratio == Fraction(1, 2)
print(f"VERIFY_OK ratio={ratio.numerator}/{ratio.denominator} grid_pairs={101*101}")
