---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The source proof reduces the strictly convex centered sum of squares on the finite Lipschitz polytope (modulo constants) to vertices with connected tight-pair graph. Every cross-cluster tight pair for 0<s<1 has consistent orientation, forcing values 0,s on one cluster and 1-s,1 on the other. The two-sided exchange gains 2s(1-s), ruling out simultaneous splits; comparison rules out a split confined to the smaller cluster. The remaining exact candidates F_k=L+ks²-(L+ks)²/N are all feasible. Completing the square yields nearest-integer k, global optimizer classification and phase crossings s_j=2L/(N-2j-1) with right-minus-left slope 2L/N. Equilateral s=1 reduces to balanced binary partitions. I independently recomputed 144 rational parameter cases and the completed-square expression; finite checks corroborate but do not prove the all-size statement. Domains: integer m,n>=2, real 0<s<=1, real observables, uniform atoms, counting-variance normalization.

## originality

PASS

Prior general Lipschitz variance, ultrametric free-space and exact four-point distortion theories do not imply this precise centered Lipschitz-to-Euclidean operator norm or its integer phase staircase, according to the material inspected. Claim is best-of-knowledge: other hierarchical-metric literature might contain an alias.

## value

PASS

The optimal Lipschitz variance/Poincaré constant is a canonical invariant of a natural finite ultrametric family. Its exact arithmetic optimizer and equally sized derivative jumps give a full infinite-family scale/imbalance classification with sharp extremizers, beyond a routine four-point calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
