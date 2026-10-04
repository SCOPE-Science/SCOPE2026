from decimal import Decimal

pi_h = Decimal("0.0684")
pi_m = Decimal("0.2223")
assert pi_h < pi_m
assert pi_m - pi_h == Decimal("0.1539")
print("VERIFY_OK")
