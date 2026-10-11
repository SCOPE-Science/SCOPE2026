import math

pi = math.pi
rt3 = math.sqrt(3.0)

def p(t):
    return pi - (pi - 3.0)*t

def a(t):
    return pi/4.0 + (3.0-pi)*t/2.0 + (pi+rt3-6.0)*t*t/4.0

def q(t):
    return a(t)/(p(t)*p(t))

def qs(theta):
    return theta/(2.0*(2.0+theta)**2)

def ts(theta):
    return (pi-2.0-theta)/(pi-3.0)

theta_star = pi-2.0-(pi-3.0)*math.sqrt(4.0-pi)/math.sqrt(6.0-pi-rt3)

def g(theta):
    return a(ts(theta))-theta/2.0

assert 1.0 < theta_star < pi/3.0
assert abs(g(theta_star)) < 5e-15
assert pi*rt3 - 9.0 < 0.0
assert 6.0-pi-rt3 > 0.0
assert (2.0+pi/3.0)**2 > 2.0*pi*(pi/3.0)

samples = [1.0, (1.0+theta_star)/2.0, 1.0 + 0.9*(theta_star-1.0)]
rows = []
for theta in samples:
    t_hi = ts(theta)
    target = qs(theta)
    assert q(0.0) > target > q(t_hi)
    lo, hi = 0.0, t_hi
    for _ in range(100):
        mid = (lo+hi)/2.0
        if q(mid) > target:
            lo = mid
        else:
            hi = mid
    t = (lo+hi)/2.0
    assert 0.0 < t < t_hi
    assert abs(q(t)-target) < 2e-15
    assert p(t) > 2.0+theta
    P = pi
    scale_sector = P/(2.0+theta)
    scale_round = P/p(t)
    area_sector = scale_sector**2 * theta/2.0
    area_round = scale_round**2 * a(t)
    assert abs(area_sector-area_round) < 2e-14
    assert scale_round < scale_sector
    rows.append((theta,t,p(t),scale_sector-scale_round))

A_low = pi*pi/18.0
A_star = pi*pi*theta_star/(2.0*(2.0+theta_star)**2)

print("VERIFY_OK")
print("theta_star", format(theta_star, ".16f"))
print("A_low_P_pi", format(A_low, ".16f"))
print("A_star_P_pi", format(A_star, ".16f"))
for row in rows:
    print("sample", " ".join(format(x, ".16f") for x in row))
