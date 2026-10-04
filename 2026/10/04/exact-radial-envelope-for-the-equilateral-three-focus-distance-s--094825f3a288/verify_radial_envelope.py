import math


def distances(R, rho, theta):
    return [
        math.sqrt(max(0.0, R*R + rho*rho - 2.0*R*rho*math.cos(theta - 2.0*math.pi*k/3.0)))
        for k in range(3)
    ]


def bounds(R, rho):
    lo = abs(R-rho) + 2.0*math.sqrt(R*R + R*rho + rho*rho)
    hi = R + rho + 2.0*math.sqrt(R*R - R*rho + rho*rho)
    return lo, hi


def check(R, rho):
    lo, hi = bounds(R, rho)
    tol = 2e-11 * max(1.0, R + rho)
    min_seen = float("inf")
    max_seen = -float("inf")
    for j in range(7201):
        theta = 2.0*math.pi*j/7200.0
        ds = distances(R, rho, theta)
        p = sum(ds)
        min_seen = min(min_seen, p)
        max_seen = max(max_seen, p)
        if p < lo - tol or p > hi + tol:
            raise AssertionError((R, rho, theta, p, lo, hi))
        x = [d*d for d in ds]
        s1 = sum(x)
        s2 = x[0]*x[1] + x[1]*x[2] + x[2]*x[0]
        prod = x[0]*x[1]*x[2]
        target1 = 3.0*(R*R + rho*rho)
        target2 = 3.0*(R**4 + R*R*rho*rho + rho**4)
        target3 = R**6 + rho**6 - 2.0*R**3*rho**3*math.cos(3.0*theta)
        scale = max(1.0, R**6 + rho**6)
        if abs(s1-target1) > 2e-10*max(1.0, target1):
            raise AssertionError("S1")
        if abs(s2-target2) > 4e-10*max(1.0, target2):
            raise AssertionError("S2")
        if abs(prod-target3) > 2e-9*scale:
            raise AssertionError("product")
    for k in range(3):
        theta = 2.0*math.pi*k/3.0
        if abs(sum(distances(R, rho, theta))-lo) > tol:
            raise AssertionError("lower equality")
        theta = math.pi/3.0 + 2.0*math.pi*k/3.0
        if abs(sum(distances(R, rho, theta))-hi) > tol:
            raise AssertionError("upper equality")
    if abs(min_seen-lo) > 5e-9*max(1.0, R+rho):
        raise AssertionError("grid minimum")
    if abs(max_seen-hi) > 5e-9*max(1.0, R+rho):
        raise AssertionError("grid maximum")


for R in (0.37, 1.0, 3.2):
    for factor in (0.0, 0.01, 0.25, 0.75, 1.0, 1.25, 2.0, 7.0):
        check(R, factor*R)

print("all deterministic checks passed")
