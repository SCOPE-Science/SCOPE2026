from fractions import Fraction as F

def soft_threshold(x, threshold):
    if x > threshold:
        return x - threshold
    if x < -threshold:
        return x + threshold
    return F(0)

tests = [
    # mu, lambda, T, delta, x0, nu
    (F(2), F(3), F(2), F(1,10), F(1), F(0)),
    (F(3), F(2), F(1,2), F(1,4), F(-2), F(5,7)),
    (F(5), F(1), F(4), F(1,3), F(1), F(2)),
]

for mu, lam, T, delta, x, nu in tests:
    assert mu > 1
    assert 0 < delta < 1
    assert T > delta
    basin = mu * lam / max(F(1), T)
    assert 0 < abs(x) <= basin
    q = 1 - F(1, mu)

    prev_eta = None
    prev_d = None

    for k in range(12):
        xp = soft_threshold(x, mu * lam)
        assert xp == 0
        eta = (x - xp) / mu

        if k == 0:
            d = -eta
        else:
            y = eta - prev_eta
            s = prev_d
            z = y + nu * s
            denom = prev_d * z
            assert denom > 0
            beta = eta * y / denom
            gamma = eta * prev_d / denom
            assert beta * prev_d == gamma * y
            d = -eta + beta * prev_d - gamma * y
            assert d == -eta

        # Stage 1 at t=1.
        stage1_lhs = lam * abs(x + d) - lam * abs(x)
        stage1_rhs = -T * eta * eta
        assert stage1_lhs <= stage1_rhs

        # Armijo at alpha=1.
        armijo_lhs = lam * abs(x + d)
        armijo_rhs = lam * abs(x) + delta * eta * d
        assert armijo_lhs <= armijo_rhs

        xn = x + d
        assert xn == q * x
        assert abs(xn) < abs(x)

        prev_eta = eta
        prev_d = d
        x = xn

print("VERIFY_OK")
