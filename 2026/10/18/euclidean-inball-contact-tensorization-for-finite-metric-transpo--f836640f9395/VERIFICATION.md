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

The theorem for arbitrary finite factor metrics is proved by the polar facet correspondence, the exact equality cases of the finite product conditional-variance inequality, and orthogonality of the lifted factor normal spaces. No finite sample is used as an infinite proof.

Run `python3 verify_grids.py` using the Python 3 standard library. Exact arithmetic enumerates potential vectors via a spanning tree, tests all grid-edge constraints and connectivity, calculates the centered squared norms, and verifies the product prediction for the facet contacts and the rational normal rank. Checked grid shapes: `(2,2)`, `(2,3)`, `(3,3)`, `(2,2,2)`, `(2,2,3)`, `(2,3,3)`, `(2,2,2,2)`.

The incenter affine-dimension assertion relies on the analytic slack-and-sign argument, not numerical optimization. The script verifies the predicted contact-normal ranks and no assertion about full enumerations in arbitrary dimensions is made. Existing scalar product variance bounds are credited to Bobkov–Houdré (1996); independent scientific audit remains unperformed.
