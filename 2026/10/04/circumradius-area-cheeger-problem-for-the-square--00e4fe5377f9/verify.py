from math import acos, cos, pi, sin, sqrt

def bisect_root():
    lo, hi = 0.0, pi/2
    for _ in range(120):
        mid = (lo + hi) / 2
        if cos(mid) - mid > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def area_centered_square_disk(a, r):
    if r <= a:
        return pi * r * r
    if r >= sqrt(2) * a:
        return 4 * a * a
    theta = acos(a / r)
    return pi*r*r - 4*(r*r*theta - a*sqrt(r*r-a*a))

alpha = bisect_root()
theta = pi/4 - alpha/2
a = 1.0
r = a / cos(theta)
A = area_centered_square_disk(a, r)
value = r / A
closed = cos(theta) / (4*a*alpha)

assert abs(alpha - cos(alpha)) < 2e-15
assert 1.0 < r < sqrt(2)
assert abs(A - 4*alpha*r*r) < 3e-14
assert abs(value - closed) < 3e-15

# Check the analytic minimizer against a dense independent one-dimensional scan.
best = None
best_r = None
for j in range(200001):
    rr = 0.2 + (sqrt(2)-0.2)*j/200000
    f = rr / area_centered_square_disk(a, rr)
    if best is None or f < best:
        best, best_r = f, rr

assert abs(best_r - r) < 2e-5
assert abs(best - closed) < 2e-10

# Check derivative sign on both sides of the critical radius.
def objective(rr):
    return rr / area_centered_square_disk(a, rr)

eps = 1e-5
assert objective(r-eps) > objective(r)
assert objective(r+eps) > objective(r)

print("VERIFY_OK square circumradius-area constant")
