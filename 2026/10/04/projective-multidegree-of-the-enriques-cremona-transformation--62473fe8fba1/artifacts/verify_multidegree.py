#!/usr/bin/env python3
from math import comb
import json
from pathlib import Path

# Intersections on P^- = Bl_S(P^5), indexed by exponent of E:
# integral H^(5-j) E^j.
I = {0: 1, 1: 0, 2: 0, 3: 10, 4: 60, 5: 222}

def preliminary(k):
    # integral H^(5-k) (5H-2E)^k
    total = 0
    for j in range(k + 1):
        total += comb(k, j) * (5 ** (k-j)) * ((-2) ** j) * I[j]
    return total

b = [preliminary(k) for k in range(6)]
assert b == [1, 5, 25, 45, -15, 21], b

# One residual plane Pi has H|Pi=l, D|Pi=-l,
# N_{Pi/P^-}=O(-1)^3. The standard codimension-three
# blowup pushforwards give:
H2G3 = 1
HDG3 = -1
HG4 = -3
D2G3 = 1
DG4 = 3
G5 = 6

per_plane = [0, 0, 0, 0, 0, 0]
per_plane[3] = -H2G3
per_plane[4] = -4 * HDG3 + HG4
per_plane[5] = -10 * D2G3 + 5 * DG4 - G5
assert per_plane == [0, 0, 0, -1, 1, -1], per_plane

correction = [20 * c for c in per_plane]
d = [x + y for x, y in zip(b, correction)]
expected = [1, 5, 25, 25, 5, 1]
assert d == expected, (d, expected)
assert d == list(reversed(d)), d
assert d[0] == d[5] == 1
assert d[1] == d[4] == 5

cert = {
    "source_intersections_by_E_exponent": I,
    "preliminary_H_D_mixed_intersections": b,
    "per_plane_correction": per_plane,
    "number_of_disjoint_planes": 20,
    "total_correction": correction,
    "projective_multidegree": d
}
out = Path(__file__).with_name("multidegree_certificate.json")
out.write_text(json.dumps(cert, sort_keys=True, indent=2) + "\n", encoding="utf-8")

for k in range(6):
    print(k, b[k], correction[k], d[k])
print("MULTIDEGREE_OK", d)
