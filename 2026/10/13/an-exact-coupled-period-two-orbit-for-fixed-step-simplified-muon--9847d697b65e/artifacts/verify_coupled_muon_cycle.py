import math


def step(eta, chi, x):
    a, b, c = x
    z = (a*a - 1.0, b*b, c*c)
    force = (
        z[0] + chi*z[1],
        chi*z[0] + z[1],
        z[2],
    )
    blocks = (a*force[0], b*force[1], c*force[2])
    assert all(abs(v) > 1e-14 for v in blocks)
    sgn = tuple(1.0 if v > 0 else -1.0 for v in blocks)
    return tuple(v - eta*s for v, s in zip(x, sgn)), force


def loss(chi, x):
    a, b, c = x
    z0, z1, z2 = a*a - 1.0, b*b, c*c
    return 0.5*(z0*z0 + 2.0*chi*z0*z1 + z1*z1 + z2*z2)

for eta in (0.03, 0.1, 0.25, 0.5, 0.8, 0.97):
    delta = eta*eta/4.0
    t = eta*math.sqrt(8.0 - eta*eta)/4.0
    q = 2.0*delta - delta*delta
    assert 0.0 < delta < eta
    assert 0.0 < t < eta
    assert abs(t*t - q) < 2e-15
    for chi in (0.01, 0.08, 0.2, 0.3, 0.329):
        assert 0.0 < chi < 1.0/3.0
        # Sigma times r^2 has eigenvalues 1/3+chi, 1/3-chi, 1/3.
        assert 1.0/3.0 - chi > 0.0
        xp = (1.0 + eta - delta, eta - t, eta/2.0)
        xm = (1.0 - delta, -t, -eta/2.0)
        y, fp = step(eta, chi, xp)
        assert max(abs(a-b) for a,b in zip(y, xm)) < 2e-14
        z, fm = step(eta, chi, xm)
        assert max(abs(a-b) for a,b in zip(z, xp)) < 2e-14
        expected_force_m = (-(1.0-chi)*q, (1.0-chi)*q, eta*eta/4.0)
        assert max(abs(a-b) for a,b in zip(fm, expected_force_m)) < 2e-14
        expected_loss_m = (1.0-chi)*q*q + eta**4/32.0
        assert abs(loss(chi, xm) - expected_loss_m) < 2e-14
        assert expected_loss_m > 0.0

print('VERIFY_OK')
