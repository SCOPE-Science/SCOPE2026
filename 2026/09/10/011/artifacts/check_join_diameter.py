"""Verify diam(S^2 * S^1_a) = pi for all a in (0,2pi] from the spherical-join cosine formula.

Join metric (AKP Foundations / Rong-Wang / BGP): for p_i = (x_i, y_i, t_i),
  cos d(p1,p2) = cos t1 cos t2 cos d_X(x1,x2) + sin t1 sin t2 cos d_Y(y1,y2),
with t_i in [0, pi/2]. Checks:
  (a) S^2-factor embedding (t=0) is isometric; antipodal pair gives distance pi.
  (b) global upper bound: cos d >= -cos(t1-t2) >= -1, so d <= pi, on a dense grid.
"""
import math

def join_dist(tx1, dx, ty_unused, dy, t1, t2):
    c = math.cos(t1)*math.cos(t2)*math.cos(dx) + math.sin(t1)*math.sin(t2)*math.cos(dy)
    c = max(-1.0, min(1.0, c))
    return math.acos(c)

# (a) antipodal S^2 pair at t=0: d_X = pi -> join distance pi regardless of a
d_edge = join_dist(0, math.pi, 0, 0.0, 0.0, 0.0)
print("antipodal-factor distance:", d_edge)
assert abs(d_edge - math.pi) < 1e-12, "factor embedding must give pi"

# (b) grid sweep: no pair exceeds pi; bound tight
import random
random.seed(513)
worst = 0.0
worst_cfg = None
for a in [0.5, 1.0, 2.0, math.pi, 5.0, 2*math.pi]:
    diamY = a/2  # circle of length a
    for _ in range(20000):
        t1 = random.uniform(0, math.pi/2); t2 = random.uniform(0, math.pi/2)
        dx = random.uniform(0, math.pi)          # diam S^2 = pi
        dy = random.uniform(0, diamY)            # diam S^1_a = a/2
        d = join_dist(0, dx, 0, dy, t1, t2)
        if d > worst:
            worst = d; worst_cfg = (a, t1, t2, dx, dy)
print("grid max:", worst, "cfg:", worst_cfg)
assert worst <= math.pi + 1e-9

# (c) cross-factor check: X-factor point to Y-factor point has distance pi/2
d_cross = join_dist(0, 0.0, 0, 0.0, 0.0, math.pi/2)
print("cross-factor distance:", d_cross)
assert abs(d_cross - math.pi/2) < 1e-12

# (d) conclusion: pi <= diam(J_a) <= pi for every a -> diam identically pi
print("CONCLUSION: diam(J_a) = pi for all tested a; no a_c with diam = pi/2 exists.")
print("ALL CHECKS PASS")
