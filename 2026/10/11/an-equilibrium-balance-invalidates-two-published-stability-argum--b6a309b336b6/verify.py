from sympy import symbols, simplify

lam, A0, y, beta, phi, L2, c2 = symbols("lam A0 y beta phi L2 c2", positive=True)
A = lam*(1-A0)*y/(beta+phi*y)
reverse_gap = simplify(lam*(1-A0)/phi - A)
den = simplify(phi*A - lam*(1-A0))
L1 = simplify(L2*c2*phi/den)
expected_gap = simplify(lam*(1-A0)*beta/(phi*(beta+phi*y)))
expected_den = simplify(-lam*(1-A0)*beta/(beta+phi*y))
assert simplify(reverse_gap-expected_gap) == 0
assert simplify(den-expected_den) == 0
assert simplify(L1 - L2*c2*phi/expected_den) == 0
print("VERIFY_OK")
print("reverse_gap =", reverse_gap)
print("denominator =", den)
print("L1 =", L1)
