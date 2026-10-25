---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The exact proof in `RESULT.md` establishes the all-parameter statement. Running `python3 verify.py` independently verifies in rational arithmetic the base lattice determinant and crosspolytope volume, Vandermonde's identity for the complete-root polytope, and all signed cap-inequality combinations for canonical disjoint graph edges in dimensions \(3\le n\le16\).

A separate numerical convex-hull calculation compared all canonical matching counts for \(3\le n\le8\) with the exact formula: all agreed, giving for instance normalized volumes \(3432,3368,3304,3240,3176\) for \(n=8\) and matching sizes \(r=0,1,2,3,4\). It is not relied upon as an infinite proof. There is no independent audit or historical-priority certification.
