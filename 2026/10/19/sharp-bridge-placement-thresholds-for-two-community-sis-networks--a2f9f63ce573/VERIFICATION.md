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

# Reproduction and scope

Execute `python checker.py` in this directory with Python 3 and NumPy. The checker constructs actual adjacency matrices and numerically diagonalizes every possible \(k\)-edge bipartite bridge set for \(n=2,3,4\), together with seeded samples for larger communities. It compares the computed spectral radii against both analytic extrema, including equality cases, and directly checks the bridge-degree square-sum bound. It also verifies nine large-size comparisons with the scaling law.

Recorded run: `PASS: 5421 spectral, equality, and degree-square configurations; 9 large-size comparisons`. For \(n=4\), \(k=3\): matching radius \(3.791287847478\), star radius \(3.975584306695\).

The analytic proof in RESULT.md is necessary for all sizes. Floating-point tolerance checks and finite enumeration are not infinite certifications. Independent scientific audit has not been performed.
