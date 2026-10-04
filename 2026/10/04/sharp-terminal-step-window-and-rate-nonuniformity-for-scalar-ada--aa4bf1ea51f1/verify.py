import math

def run_scaled(r, z, steps=300000, tol=1e-15):
    ratios = []
    noncontract = 0
    for k in range(steps):
        rn = math.hypot(r, z)
        if rn <= 0.5 + 1e-15:
            noncontract += 1
        mult = 1.0 - 1.0/rn
        zn = mult*z
        if z != 0.0:
            ratios.append(abs(zn/z))
        r, z = rn, zn
        if abs(z) < tol:
            break
    return r, z, ratios, noncontract

# Normalized recurrence agrees with the original variables.
for lam, eta, b0, x0 in [
    (2.0, 0.7, 0.2, 1.3),
    (0.5, 3.0, 0.9, -0.4),
    (5.0, 0.1, 2.0, 0.03),
]:
    r = b0/(eta*lam)
    z = x0/eta
    b1 = math.sqrt(b0*b0 + lam*lam*x0*x0)
    x1 = (1.0-eta*lam/b1)*x0
    rn = math.hypot(r,z)
    zn = (1.0-1.0/rn)*z
    assert abs(rn - b1/(eta*lam)) < 1e-13
    assert abs(zn - x1/eta) < 1e-13

# One-step annihilation surface.
for r0 in (0.1, 0.4, 0.7, 0.95):
    z0 = math.sqrt(1.0-r0*r0)
    r1 = math.hypot(r0,z0)
    z1 = (1.0-1.0/r1)*z0
    assert abs(r1-1.0) < 2e-15
    assert abs(z1) < 2e-15

# Terminal strict stability and exact ratio on a deterministic grid.
for r0 in (0.03,0.1,0.3,0.49,0.51,0.7,1.0,2.0,10.0):
    for z0 in (0.001,0.01,0.1,0.7,2.0):
        R,Z,ratios,M = run_scaled(r0,z0)
        assert R > 0.5 - 1e-12
        theta = 1.0/R
        assert 0.0 < theta < 2.0 + 1e-10
        if ratios and abs(Z) < 1e-10:
            rho = abs(1.0-theta)
            assert abs(ratios[-1]-rho) < 1e-6

        if r0 < 0.5:
            bound = math.floor((0.25-r0*r0)/(z0*z0) + 1e-12)
        else:
            bound = 0
        assert M <= max(0,bound)

# Upper terminal-step edge: r_infty -> 1/2, theta -> 2.
edge_thetas = []
for m in (30,60,120,300,600):
    r0 = 0.5 + 1.0/m
    q0 = 1.0/r0 - 1.0
    z0 = (1.0-q0*q0)/m
    assert r0*r0 + z0*z0/(1.0-q0*q0) < 1.0
    R,_,_,_ = run_scaled(r0,z0)
    assert R < 1.0
    edge_thetas.append(1.0/R)
assert edge_thetas[-1] > 1.99
assert all(edge_thetas[i+1] > edge_thetas[i] for i in range(len(edge_thetas)-1))

# Lower terminal-step edge: large initial accumulator forces theta -> 0.
small_thetas = []
for R0 in (10.0,30.0,100.0,300.0):
    R,_,_,_ = run_scaled(R0,0.1)
    small_thetas.append(1.0/R)
assert small_thetas[-1] < 0.004
assert all(small_thetas[i+1] < small_thetas[i] for i in range(len(small_thetas)-1))

print("verification passed")
