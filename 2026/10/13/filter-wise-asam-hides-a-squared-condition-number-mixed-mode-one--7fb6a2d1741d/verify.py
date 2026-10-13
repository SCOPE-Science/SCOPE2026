import math

def closed(kappa, rho, tau, R, alpha):
    sr = 1.0 + tau / R
    rk = math.sqrt(2.0 - kappa**-2)
    m1 = 1.0 + 1.0/kappa - 1.0/(kappa*kappa)
    m2 = 2.0 - 1.0/(kappa*kappa)
    m3 = kappa + 1.0 - 1.0/(kappa*kappa)
    m4 = kappa*kappa + 1.0 - 1.0/(kappa*kappa)
    A = m1 + rho * sr * rk
    B = m2 + 2.0*rho*sr*m3/rk + rho*rho*sr*sr*m4/m2
    return 1.0 - 2.0*alpha*A + alpha*alpha*B, 2.0*A/B

def direct(kappa, rho, tau, R, alpha):
    a = math.sqrt(1.0 - 1.0/(kappa*kappa))
    v = (a, 1.0/kappa)
    x = (R*v[0], R*v[1])
    Ax = (x[0], kappa*x[1])
    ng = math.hypot(Ax[0], Ax[1])
    scale = rho * (R + tau) / ng
    eps = (scale*Ax[0], scale*Ax[1])
    A_shift = (x[0] + eps[0], kappa*(x[1] + eps[1]))
    xp = (x[0] - alpha*A_shift[0], x[1] - alpha*A_shift[1])
    return (xp[0]*xp[0] + xp[1]*xp[1]) / (R*R)

for kappa, rho, tau, R, alpha in [
    (3.0, 0.2, 0.01, 2.0, 0.05),
    (10.0, 0.5, 0.03, 7.0, 0.01),
    (100.0, 1.0, 0.01, 20.0, 5e-4),
]:
    q, crit = closed(kappa, rho, tau, R, alpha)
    q2 = direct(kappa, rho, tau, R, alpha)
    assert abs(q-q2) < 3e-13
    below, _ = closed(kappa, rho, tau, R, 0.999*crit)
    edge, _ = closed(kappa, rho, tau, R, crit)
    above, _ = closed(kappa, rho, tau, R, 1.001*crit)
    assert below < 1.0
    assert abs(edge-1.0) < 3e-12
    assert above > 1.0

for rho in (0.1, 0.5, 1.0, 2.0):
    target = 4.0*(1.0 + rho*math.sqrt(2.0))/(rho*rho)
    vals = []
    for kappa in (1000.0, 3000.0, 10000.0):
        _, crit = closed(kappa, rho, 0.0, 1.0, 0.0)
        vals.append(kappa*kappa*crit)
    assert abs(vals[-1]-target)/target < 0.004
    assert abs(vals[-1]-target) < abs(vals[0]-target)

for rho in (0.2, 0.5, 1.0, 2.0):
    C = 4.0*(1.0 + rho*math.sqrt(2.0))/(rho*rho)
    c = 1.25*C
    kappa = max(10000.0, 20.0*c*(1.0+rho))
    alpha = c/(kappa*kappa)
    R = 1e8
    tau = 0.01
    mixed, _ = closed(kappa, rho, tau, R, alpha)
    sr = 1.0 + tau/R
    pure_top = abs(1.0 - alpha*kappa*(1.0 + rho*sr))
    pure_bottom = abs(1.0 - alpha*(1.0 + rho*sr))
    assert pure_top < 1.0
    assert pure_bottom < 1.0
    assert mixed > 1.0

print("verification passed")
