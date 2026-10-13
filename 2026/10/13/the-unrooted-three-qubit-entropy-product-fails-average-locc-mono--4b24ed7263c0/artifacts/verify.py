from fractions import Fraction
from math import log2

# Initial state: sqrt(1/8)|000> + sqrt(7/8)|111>.
p0 = Fraction(1, 8)
p1 = Fraction(7, 8)

# Local measurement on qubit 1:
# K1 = diag(1,1/sqrt(7)), K2 = diag(0,sqrt(6/7)).
# Completeness is checked at the level of squared diagonal entries.
assert Fraction(1,1) + Fraction(0,1) == 1
assert Fraction(1,7) + Fraction(6,7) == 1

q1 = p0 + p1 * Fraction(1, 7)
q2 = p1 * Fraction(6, 7)
assert q1 == Fraction(1, 4)
assert q2 == Fraction(3, 4)
assert q1 + q2 == 1

# In branch 1, the two surviving squared amplitudes are equal to 1/8,
# hence the normalized branch is GHZ with one-site entropy 1.
assert p0 == p1 * Fraction(1, 7)
# Branch 2 is |111>, hence all one-site entropies vanish.
expected_after = q1 * 1 + q2 * 0
assert expected_after == Fraction(1, 4)

# Exact strict inequality for the initial entropy product.
# h2(1/8)=3-(7/8)log2(7), and 2^19 < 7^7 implies log2(7)>19/7.
assert 2**19 < 7**7
entropy_upper = Fraction(5, 8)
product_upper = entropy_upper ** 3
assert product_upper == Fraction(125, 512)
assert product_upper < Fraction(1, 4)

h = -(1/8)*log2(1/8) - (7/8)*log2(7/8)
initial_numeric = h**3
assert initial_numeric < 0.25

print("VERIFY_OK")
print(f"q1={q1} q2={q2}")
print(f"exact_log_witness={2**19}<{7**7}")
print(f"initial_product_upper={product_upper}<1/4")
print(f"initial_product_numeric={initial_numeric:.15f}")
print("expected_after=1/4")
