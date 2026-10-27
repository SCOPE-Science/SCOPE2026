from fractions import Fraction as F

# Exact representative point inside (4 - 2*sqrt(2), 2).
B = F(6, 5)
RMAX = F(3)
assert B > 1 and B < 2
# 6/5 > 4 - 2*sqrt(2) is equivalent to sqrt(2) > 7/5,
# which follows exactly from 2 > 49/25.
assert F(2) > F(49, 25)

# Candidate Nash flow: shortcut only, of total size B.
x_eq, y_eq, z_eq = B, F(0), F(0)
u_eq, v_eq = x_eq + y_eq, x_eq + z_eq
path_costs_eq = (max(u_eq, v_eq), max(u_eq, F(1)), max(F(1), v_eq))
assert path_costs_eq == (B, B, B)
assert x_eq + y_eq + z_eq <= RMAX
cc_eq = B * RMAX
assert cc_eq == F(18, 5)

# Candidate unique social optimum: one unit on each outer path, none on shortcut.
x_opt, y_opt, z_opt = F(0), F(1), F(1)
u_opt, v_opt = x_opt + y_opt, x_opt + z_opt
path_costs_opt = (max(u_opt, v_opt), max(u_opt, F(1)), max(F(1), v_opt))
assert path_costs_opt == (F(1), F(1), F(1))
assert x_opt + y_opt + z_opt <= RMAX
cc_opt = x_opt * path_costs_opt[0] + y_opt * path_costs_opt[1] + z_opt * path_costs_opt[2] + B * (RMAX - x_opt - y_opt - z_opt)
assert cc_opt == F(16, 5)
assert cc_eq / cc_opt == F(9, 8)

# Exact comparisons used in the general interval proof.
assert F(2) * (F(1) - B) == F(-2, 5)
assert -B * B / 4 == F(-9, 25)
assert F(-2, 5) < F(-9, 25)
assert F(1) - B == F(-1, 5)

# For general B in (4 - 2*sqrt(2), 2), the written proof shows that
# minimizing the objective for fixed u=x+y and v=x+z reduces to x=0
# or x=min(u,v). The x=0 branch is minimized at u=v=1; the x=min
# branch is bounded below by min(-B^2/4, 1-B), which is strictly above
# 2(1-B) throughout this interval. This script verifies exact rational
# arithmetic at B=6/5; it is not an independent proof of the continuum.
print("VERIFY_OK representative_B=6/5 equilibrium_CC=18/5 optimum_CC=16/5 PoA=9/8 equilibrium_flow=6/5 optimum_flow=2")
