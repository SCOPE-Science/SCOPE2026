"""Verify chaining-constant arithmetic cited in DRAFT.md section 5.

Checks that with cubic tail rate c1 = 1/32 and modulus constant A,
c1 * A^3 > ln(base) holds for natural/binary/decimal logs, i.e. the
random-s0 chaining remark has room below the target constant 6.
"""
import math

c1 = 1 / 32
for base_name, base in [("e", math.e), ("2", 2.0), ("10", 10.0)]:
    need = math.log(base)  # threshold value of c1*A^3 depends on log base
    A_needed = (need / c1) ** (1 / 3)
    print(f"log base {base_name}: need c1*A^3 > {need:.4f} -> A > {A_needed:.4f} (< 6: {A_needed < 6})")

for A in [3.5, 4.0, 4.2, 5.0, 6.0]:
    print(f"A={A}: c1*A^3 = {c1*A**3:.4f}  (> ln10={math.log(10):.4f}: {c1*A**3 > math.log(10)})")

# oscillation-error suppression factor 2^{-2m/3} for mesh refinement m
for m in [6, 9, 10, 12]:
    print(f"m={m}: 2^(-2m/3) = {2**(-2*m/3):.5f}")
