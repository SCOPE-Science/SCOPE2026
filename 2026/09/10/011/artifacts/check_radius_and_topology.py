"""Target stress-test supplement: (i) confirm diam constant pi while scanning
eccentricity/radius vs a (tests whether ANY diameter-based cutoff could move);
(ii) record topological-join fact used in (R) audit. Purely diagnostic."""
import math

def min_cos_for_p(t, a):
    # minimize cos d over t', dx=pi, dy=a/2 (extremal choices; cos decreasing on [0,pi])
    best = 1.0
    bt = None
    N = 2001
    for i in range(N):
        tp = (math.pi/2)*i/(N-1)
        c = math.cos(t)*math.cos(tp)*(-1.0) + math.sin(t)*math.sin(tp)*math.cos(a/2)
        if c < best:
            best = c; bt = tp
    return best, bt

print("a : ecc(t=0) ecc(t=pi/4) ecc(t=pi/2) | diam lower bound")
for a in [0.5, 1.0, 2.0, math.pi, 5.0, 2*math.pi - 0.01, 2*math.pi]:
    row = []
    for t in [0.0, math.pi/4, math.pi/2]:
        cmin, _ = min_cos_for_p(t, a)
        cmin = max(-1.0, min(1.0, cmin))
        row.append(math.acos(cmin))
    # diam lower bound via antipodal S^2 pair at t=0 is exactly pi (analytic)
    print(f"{a:6.3f} : " + " ".join(f"{v:.6f}" for v in row) + " | pi")

print()
print("Topology: S^2 * S^1 (topological join) ≅ S^(2+1+1) = S^4 for every a.")
print("Hence bare (R) conclusion holds for all a; no threshold enters.")
print("DIAGNOSTIC COMPLETE")
