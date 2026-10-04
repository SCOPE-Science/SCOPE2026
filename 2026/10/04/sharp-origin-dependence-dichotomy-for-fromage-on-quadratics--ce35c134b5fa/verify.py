import math

def cmin(kappa):
    return 2.0*math.sqrt(kappa)/(kappa+1.0)

def q_fromage(eta, kappa):
    return math.sqrt(max(0.0, 1.0 - 4.0*eta*math.sqrt(kappa)/((1.0+eta*eta)*(kappa+1.0))))

def q_lars(eta, kappa):
    return math.sqrt(max(0.0, 1.0 + eta*eta - 4.0*eta*math.sqrt(kappa)/(kappa+1.0)))

# Exact two-eigenvalue witness, evaluated numerically.
for kappa in (1.0, 2.0, 4.0, 10.0, 100.0):
    x1 = 1.0
    x2 = 1.0/math.sqrt(kappa)
    hx1 = x1
    hx2 = kappa*x2
    dot = x1*hx1 + x2*hx2
    nx = math.hypot(x1, x2)
    nh = math.hypot(hx1, hx2)
    c = dot/(nx*nh)
    assert abs(c-cmin(kappa)) < 2e-14

    # Fromage optimum.
    qstar = (math.sqrt(kappa)-1.0)/math.sqrt(kappa+1.0)
    assert abs(q_fromage(1.0, kappa)-qstar) < 2e-14

    # LARS-type optimum.
    eta_l = cmin(kappa)
    qlstar = (kappa-1.0)/(kappa+1.0)
    assert abs(q_lars(eta_l, kappa)-qlstar) < 2e-14

# Direct norm-ratio identities on deterministic diagonal SPD examples.
for kappa in (1.5, 3.0, 9.0, 50.0):
    for eta in (0.05, 0.4, 1.0, 2.0, 10.0):
        for x1, x2 in ((1.0, 0.2), (0.4, 1.3), (2.0, -0.7)):
            hx1, hx2 = x1, kappa*x2
            nx = math.hypot(x1, x2)
            nh = math.hypot(hx1, hx2)
            c = (x1*hx1+x2*hx2)/(nx*nh)

            scale = nx/nh
            y1 = (x1-eta*scale*hx1)/math.sqrt(1+eta*eta)
            y2 = (x2-eta*scale*hx2)/math.sqrt(1+eta*eta)
            ratio2 = (y1*y1+y2*y2)/(nx*nx)
            formula = 1.0-2.0*eta*c/(1.0+eta*eta)
            assert abs(ratio2-formula) < 2e-13
            assert math.sqrt(ratio2) <= q_fromage(eta, kappa) + 2e-13

            z1 = x1-eta*scale*hx1
            z2 = x2-eta*scale*hx2
            ratio2_l = (z1*z1+z2*z2)/(nx*nx)
            formula_l = 1.0+eta*eta-2.0*eta*c
            assert abs(ratio2_l-formula_l) < 2e-13
            assert math.sqrt(max(0.0,ratio2_l)) <= q_lars(eta,kappa) + 2e-13

# Uniform contraction frontier for the unprefactored comparison.
for kappa in (1.0, 2.0, 5.0, 20.0, 100.0):
    cap = 4.0*math.sqrt(kappa)/(kappa+1.0)
    assert q_lars(0.999999*cap, kappa) < 1.0
    assert q_lars(1.000001*cap, kappa) > 1.0
    for eta in (0.03, 0.3, 1.0, 3.0, 30.0):
        assert q_fromage(eta,kappa) < 1.0 + 2e-14

# Shifted scalar branch and log-rotation checks.
for eta in (0.05, 0.2, 0.6, 0.95):
    a = 3.0
    c = 1.0/math.sqrt(1.0+eta*eta)
    A = (1.0+eta)*c
    B = (1.0-eta)*c
    assert A > 1.0
    assert 0.0 < B < 1.0
    assert B*a < c*a < a < A*a

    u = math.log(A)
    v = -math.log(B)

    # Check each branch against circle addition by u modulo u+v.
    for y in (-0.9*v, -0.2*v, 0.2*u, 0.8*u):
        if y < 0:
            y1 = y + u
        else:
            y1 = y - v
        z = y + v
        z1 = (z + u) % (u+v)
        y_circle = z1 - v
        assert abs(y1-y_circle) < 2e-14

    # Positive orbit reaches and remains in the invariant multiplicative band.
    for x0 in (0.01*a, 0.2*a, 2.0*a, 50.0*a):
        x = x0
        entered = False
        for _ in range(1000):
            if B*a <= x <= A*a:
                entered = True
            if x < a:
                x = A*x
            elif x > a:
                x = B*x
            else:
                x = c*a
            if entered:
                assert B*a - 1e-12 <= x <= A*a + 1e-12
        assert entered

print("verification passed")
