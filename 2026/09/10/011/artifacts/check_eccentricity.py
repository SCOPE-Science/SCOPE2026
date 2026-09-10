"""Exact eccentricity profile ecc(t) of J_a = S^2 * S^1_a (target-directed).

Join symmetry (both factors homogeneous): ecc depends only on join parameter t.
Claim (derived in ecc_profile.md):
  c = cos(a/2);
  if a <= pi: ecc(t) = pi - t;
  if a >  pi: ecc(t) = acos(-sqrt(cos(t)^2 + c^2 sin(t)^2)).
Radius r(a) = min_t ecc = max(pi/2, a/2); diameter = pi always (t=0 antipodes).
Checks closed form against brute-force max over (t', dx, dy) grid.
"""
import math

def join_dist(dx, dy, t1, t2):
    c = math.cos(t1)*math.cos(t2)*math.cos(dx) + math.sin(t1)*math.sin(t2)*math.cos(dy)
    return math.acos(max(-1.0, min(1.0, c)))

def ecc_closed(t, a):
    c = math.cos(a/2)
    if a <= math.pi:
        return math.pi - t
    return math.acos(-math.sqrt(math.cos(t)**2 + c**2*math.sin(t)**2))

def ecc_brute(t, a, n=121):
    best = 0.0
    diamY = a/2
    for i in range(n):
        tp = (math.pi/2)*i/(n-1)
        for j in range(n):
            dx = math.pi*j/(n-1)
            for k in range(n):
                dy = diamY*k/(n-1)
                d = join_dist(dx, dy, t, tp)
                if d > best:
                    best = d
    return best

ok = True
for a in [0.5, 1.0, 2.0, math.pi, 5.0, 2*math.pi - 0.05, 2*math.pi]:
    for t in [0.0, 0.3, math.pi/4, 1.2, math.pi/2]:
        cf = ecc_closed(t, a)
        bf = ecc_brute(t, a)
        gap = cf - bf  # closed form must dominate grid max; grid under-resolves
        status = "OK" if -1e-9 <= gap <= 0.02 else "FAIL"
        if status == "FAIL":
            ok = False
        print(f"a={a:6.3f} t={t:.3f} closed={cf:.6f} brute={bf:.6f} gap={gap:.5f} {status}")
    r = min(ecc_closed(t, a) for t in [i*0.001*math.pi/2 for i in range(1001)])
    print(f"   radius(a)={r:.6f} formula max(pi/2,a/2)={max(math.pi/2,a/2):.6f}")
    assert abs(r - max(math.pi/2, a/2)) < 1e-3
assert ok
print("ECCENTRICITY PROFILE OK: closed form dominates brute force; radius = max(pi/2,a/2)")
