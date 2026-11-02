---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For V_d={±e_i}, P_d={||x||_1<=1}, twofold equal-weight midpoint set M_d=(V_d+V_d)/2 including repeated vertices, put y=2x so ||y||_1<=2 and doubled sites are 0, ±2e_i, ±e_i±e_j. By signed permutations sort a=y1>=b=y2>=0; R=||y||_2²<=a²+b(2-a). Squared distances to sites 0, 2e1, e1+e2 are respectively R, R+4−4a, R+2−2(a+b). The threshold b=(a−1)²/a proves one squared distance <1 for every open a-interval (1/2,1) and (1,2), and for a<=1/2 the bound R<=2a<=1 is sharp only at precisely four entries y_i=1/2. At a=1 the sole equality is y=e_i; a=2 is itself a site. Full site enumeration confirms the listed equality families and none else, giving d_H(P_d,M_d)=1/2 and 2d+16*C(d,4) holes; the original vertices have covering distance exactly 1, achieved at x=0. Independent rational grid count 843 points in d=2,3,4 found exactly 4,6,24 equality samples, consistent with theorem but not its infinite-dimensional proof.

## originality

PASS

Compared direct equivalences, stronger implications, exact tables, and the original papers; no decisive prior coverage identified for the same final statement. Residual priority and access risks separately recorded.

## value

PASS

A Euclidean cross-polytope is a canonical centrally symmetric lattice polytope and the first Minkowski midpoint average is the natural earliest convexification stage. The exact first-step gap, complete farthest-point classification and first appearance of a second symmetry orbit at dimension four are an all-dimensional exact classification, not a selected isolated finite example or generic lattice site computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
