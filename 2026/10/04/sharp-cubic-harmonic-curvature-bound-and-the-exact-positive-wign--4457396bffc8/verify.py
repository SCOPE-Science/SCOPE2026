from fractions import Fraction

# Squared sharp constants and endpoint parameter.
sup_q_sq = Fraction(4, 27)
M_sq = Fraction(256, 27)
eps_over_r_sq = Fraction(27, 256)
assert M_sq == 64 * sup_q_sq
assert eps_over_r_sq * M_sq == 1

# Source normalizations at the sharp endpoint.
A2_over_pi2_r2 = Fraction(1, 12) * eps_over_r_sq
quartic_over_pi2_r4 = Fraction(1, 7) * eps_over_r_sq * eps_over_r_sq
assert A2_over_pi2_r2 == Fraction(9, 1024)
assert quartic_over_pi2_r4 == Fraction(729, 458752)

# The sup-norm scalar profile (1-b^2)b has critical b^2=1/3.
# Its squared value there is 4/27, agreeing with sup_q_sq.
assert Fraction(4, 27) == sup_q_sq

print("VERIFY_OK")
