"""Verify the TARGET refutation for lane-821 (stdlib only).

Checks:
 1. Certified lower bound F_v >= 0.456 >= 0.25 via one closed-form square
    integral P'=[0.25,0.5]^2 with contrast 3 (monotonicity lower bound).
 2. Rotation symmetry: Rv=(-0.5,0.5), dist(v,Rv)=1.0>=0.5, F_Rv=F_v exactly.
 3. Conclusion: adapted corner-test indicator cannot satisfy
    |I(5;v)|>=0.25 with |I(5;v')|<=0.05 for all v' at distance>=0.5.
"""
import math

tau = 5.0
# Rigorous sqrt(2) enclosure: 1.4142^2=1.99996164<2<2.00002749=1.4143^2
s2_lo, s2_hi = 1.4142, 1.4143
a_lo, a_hi = tau * s2_lo, tau * s2_hi   # a = tau*sqrt(2)
print(f"a in [{a_lo},{a_hi}]")

# Crude hand-checkable certificate: e^{0.767} >= 1+x+x^2/2+x^3/6
x = 0.767
taylor_lo = 1 + x + x**2 / 2 + x**3 / 6
e1_lo = 2.718  # e > 2.718
e_a4_lo = e1_lo * taylor_lo   # <= e^{a/4} since a/4 >= 1.76775 > 1.767=1+0.767
print(f"Taylor lower e^0.767 >= {taylor_lo:.6f}, e^(a/4) >= {e_a4_lo:.4f}")
e_neg_a4_hi = 1.0 / e_a4_lo
q_lo = (1.0 - e_neg_a4_hi) / a_hi       # (1-e^{-a/4})/a lower bound
E_lo = q_lo ** 2                        # E(P') lower bound
F_lo = (100.0 / 3.0) * E_lo             # 2tau^2*(2/3)*E(P')
print(f"(1-e^-a/4)/a >= {q_lo:.6f}, E(P') >= {E_lo:.6f}, F_v >= {F_lo:.4f}")

# Sharp numerical values (for the record; margin is huge)
a = tau * math.sqrt(2)
E_num = ((1 - math.exp(-a / 4)) / a) ** 2
F_num = (100.0 / 3.0) * E_num
print(f"numeric: E(P')={E_num:.6f}, F_v>={F_num:.4f}")

# Full-D1 monotonicity lower bound (for the record)
E1 = ((1 - math.exp(-a)) / a) ** 2
E2 = ((math.exp(-a / 4) - math.exp(-3 * a / 4)) / a) ** 2
F_full_lo = 2 * tau**2 * ((2 / 3) * (E1 - E2) + (4 / 5) * E2)
print(f"numeric full-D1 lower: {F_full_lo:.4f}")

# Symmetry facts
v = (0.5, 0.5); Rv = (-0.5, 0.5)
d = math.dist(v, Rv)
print(f"dist(v,Rv)={d:.4f} >= 0.5: {d >= 0.5}")
print(f"F_Rv = F_v >= {F_lo:.4f} > 0.05  =>  distant-smallness clause violated")

ok = (F_lo >= 0.25) and (d >= 0.5) and (F_lo > 0.05)
print("VERIFY_OK" if ok else "VERIFY_FAIL")
