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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and no third-party libraries. The program checks all forward-edge presentations on one through five vertices and 120 deterministically seeded six-vertex presentations. It computes transitive closures and cover relations, the longest-chain height, all lattice points of the predicted scaled Minkowski-center region, critical elements, and exact rational affine ranks. For each enumerated integer center it also checks the defining reflected order-polytope vertex inequalities.

Observed execution output:

`PASS 1219 poset presentations, 3072 integer center points, exact affine ranks and vertex tests`

The integer points of the center polytope are not generally **all** of its points. The mathematical proof separately invokes total unimodularity to pass from integral vertices to the entire real convex polytope. Finite checks do not cover every finite poset and are not used as a substitute for the all-poset proof. The asserted exact equality concerns Minkowski asymmetry, not Euclidean inradius or John and Löwner ellipsoids. Literature identity under alternative names remains a residual originality risk.
