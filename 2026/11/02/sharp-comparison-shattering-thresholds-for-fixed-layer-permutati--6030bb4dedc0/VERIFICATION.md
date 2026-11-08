---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each exactly r+1 decreasing-layer permutation corresponds to an r-element cut set C in [n-1]; inversion query (i,j) is 1 iff C misses interval [i,j-1]. For any t shattered intervals, t private points exist. Interval convexity shows any point lies in at most two intervals when all have distinct private points, hence all-positive pattern needs t<=2r. If t=2r, require 2r private positions, r zero-incidence positions realizing all negatives, and r further double-incidence positions realizing all positives: m>=4r; conversely r disjoint four-point gadgets realize 2r independently, giving iff n>=4r+1. For r=2, necessary witness counts and explicit intervals imply VC=0,1,2,3,4 at successive cut-position thresholds m=2,3,4,6,8. The supplied depth-three tree plus |C(5,2)|=10 establishes Ldim=3 at n=6, while n<=5 has Ldim<=2. Independent separate exhaustive interval-hit VC enumeration reproduced m=2..8 values (0,1,2,2,3,3,4); did not independently replay JSON tree, so online first-gap argument relies on inspected explicit nodes and source-described witness certificate. General online bounds follow independent r-block threshold search and concept count. Finite verification is not the all-r proof.

## originality

PASS

The fixed-layer permutation family is a natural r-subset interval-hitting concept class. Exact 2r saturation at n=4r+1 and first adaptive/static gap are not covered by the inspected distinct pattern-theoretic permutation VC literature.

## value

PASS

Exactly r+1 layered permutations form a canonical constrained ranking family. The sharp finite saturation threshold, exact three-layer VC staircase and first adaptive/static gap provide useful combinatorial learning invariants; the unbounded Ldim growth despite bounded VC supplies qualitative structural content, not only tiny-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
