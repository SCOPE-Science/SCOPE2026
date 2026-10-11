"""Reproduce finite tests of the stated planar-hybrid correlation identities."""
import math

pi = math.pi

def logistic(r):
    return 4.0 * r * (1.0 - r)

def half_flight(r, side, age):
    assert side in (0, 1) and 0.0 <= age <= pi
    return ((-1 if side == 0 else 1) * r * math.sin(age),
            r * math.cos(age))

for r in (0.08, 0.27, 0.62, 0.91):
    for side in (0, 1):
        x0, y0 = half_flight(r, side, 0.0)
        x1, y1 = half_flight(r, side, pi)
        assert abs(x0) < 2e-15 and abs(y0-r) < 2e-15
        assert abs(x1) < 2e-15 and abs(y1+r) < 2e-15
        assert abs(-4*y1*(1+y1) - logistic(r)) < 3e-15

# Deterministic quadrature of the trigonometric inner product under the arcsine law.
N = 2048
for m in range(1, 11):
    for n in range(1, 11):
        for k in range(5):
            integral = sum(math.cos(2*pi*m*(j+0.5)/N) *
                           math.cos(2*pi*(2**k)*n*(j+0.5)/N)
                           for j in range(N)) / N
            target = 0.5 if m == (2**k)*n else 0.0
            assert abs(integral-target) < 2e-13, (m, n, k, integral, target)

# Direct angle and arcsine quadrature, with no use of the covariance formulas.
Nu, Nphi = 1024, 2048
rvals = [math.sin(pi*(j+0.5)/Nu)**2 for j in range(Nu)]
for t in (0.0, pi/4, pi/2, 3*pi/4, pi, 1.5*pi, 2*pi, 2.5*pi):
    mean_rr = 0.0
    mean_xx = 0.0
    for j in range(Nphi):
        phi = 2*pi*(j+0.5)/Nphi
        age = phi % pi
        steps = int(math.floor((age+t)/pi))
        rnow = rvals
        for _ in range(steps):
            rnow = [logistic(r) for r in rnow]
        rr = sum(a*b for a,b in zip(rvals,rnow)) / Nu
        mean_rr += rr/Nphi
        mean_xx += math.sin(phi)*math.sin(phi+t)*rr/Nphi
    predicted_rr = 0.25 + 0.125 * max(1-t/pi, 0)
    if t <= pi:
        predicted_xx = math.cos(t)/8 + ((pi-t)*math.cos(t)+math.sin(t))/(16*pi)
    else:
        predicted_xx = math.cos(t)/8
    assert abs(mean_rr-predicted_rr) < 4e-4, (t, mean_rr, predicted_rr)
    assert abs(mean_xx-predicted_xx) < 4e-4, (t, mean_xx, predicted_xx)

print('CHECK_OK')
