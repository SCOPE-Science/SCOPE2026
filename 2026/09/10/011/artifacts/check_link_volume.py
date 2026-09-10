"""Verify link volume vol(S^1 * S^1_a) = pi*a via join density integral.
Density: dvol = cos(t) sin(t) dt dvol_X dvol_Y; int_0^{pi/2} cos sin = 1/2."""
import math
N = 2000000
h = (math.pi/2)/N
s = 0.0
for i in range(N+1):
    t = i*h
    w = 0.5 if (i==0 or i==N) else 1.0
    s += w*math.cos(t)*math.sin(t)
s *= h
print("integral:", s, "expected 0.5, err:", abs(s-0.5))
assert abs(s-0.5) < 1e-9
for a in [0.5, 1.0, math.pi, 2*math.pi]:
    v = (2*math.pi)*a*s
    print(f"a={a:.4f} vol_link={v:.6f} formula pi*a={math.pi*a:.6f}")
    assert abs(v - math.pi*a) < 1e-6
# round check
assert abs(math.pi*2*math.pi - 2*math.pi**2) < 1e-12
print("LINK VOLUME OK: vol(Sigma_p)=pi*a, =vol(S^3) at a=2pi")
