import math

def run(rho, gamma, theta, delta, t0, steps=200):
    t = float(t0)
    for k in range(steps):
        r = math.exp(t)
        assert r > 0.0
        s = r**(2.0-delta)/(r**(2.0-delta)+theta)
        assert 0.0 < s < 1.0
        zeta = 0.1/(k+1)**2
        l = 0
        while True:
            lam = rho**l
            lhs = math.exp(-lam*s)
            rhs = 1.0 + zeta - gamma*lam*lam*r
            if lhs <= rhs:
                break
            l += 1
            assert l < 10000
        t_new = t - lam*s
        assert t_new < t
        t = t_new
    return t, math.exp(t)

cases = [
    (0.5, 0.5, 1.0, 1.0, 0.0),
    (0.8, 0.2, 3.0, 1.5, 2.0),
    (0.7, 0.9, 0.4, 2.0, -1.0),
]
for case in cases:
    t, residual = run(*case)
    assert t < case[-1]
    assert residual > 0.0
print("VERIFY_OK")
