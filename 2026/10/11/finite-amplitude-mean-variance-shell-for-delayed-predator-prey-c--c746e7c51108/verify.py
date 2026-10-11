from math import exp, isclose

def verify_point(xbar, xstar):
    ybar = 1.0 - xbar
    ystar = 1.0 - xstar
    varx_a = (xbar - xstar) * (1.0 - xbar)
    varx_b = ybar * (ystar - ybar)
    cov = (xstar - xbar) * ybar
    assert isclose(varx_a, varx_b, rel_tol=0.0, abs_tol=1e-14)
    assert isclose(cov, -varx_a, rel_tol=0.0, abs_tol=1e-14)
    return varx_a

for xstar, xbar in [(0.2, 0.4), (0.6, 0.8), (0.1, 0.55)]:
    assert verify_point(xbar, xstar) > 0.0

xstar81 = exp(81.0/50.0) / 30.0
assert isclose(xstar81, 0.16843634388546225, rel_tol=0.0, abs_tol=2e-16)
assert 0.0 < xstar81 < 1.0
print("VERIFY_OK")
