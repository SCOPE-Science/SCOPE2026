"""Volume scaling of J_a and collapse as a->0 (target (R)-route audit).
Spherical-join volume element (warped-product form): for X=S^2, Y=S^1_a,
so vol(J_a) = vol(S^2)*a*C0 with C0 = int_0^{pi/2} cos^2 t sin t dt = 1/3.
Hence vol(J_a) = (4pi * a)/3; in particular vol -> 0 as a -> 0 (circle fibers
shrink; small-a members far from S^4(1) in GH by volume continuity), and vol(J_{2pi}) = 8pi^2/3 = vol(S^4(1)). Confirms:
- J_{2pi} is round S^4(1) (join of unit spheres), vol matches;
- small-a members are collapsed (vol ratio -> 0), so no uniform GH-closeness
  to S^4(1) and no uniform Perelman-stability input across a.
"""
import math

C0 = 1.0/3.0
volS2 = 4*math.pi
volS4 = 8*math.pi**2/3
print(f"C0={C0}, vol(S^2)={volS2:.6f}, vol(S^4)={volS4:.6f}")
for a in [0.1, 0.5, 1.0, 2.0, math.pi, 5.0, 2*math.pi]:
    v = volS2 * a * C0
    print(f"a={a:6.3f} vol(J_a)={v:.6f} ratio vol/volS4={v/volS4:.6f}")
    if abs(a - 2*math.pi) < 1e-9:
        assert abs(v - volS4) < 1e-9, "J_{2pi} must be round S^4 volume"
print("VOLUME SCALING OK: linear in a, collapse as a->0, round at 2pi")
