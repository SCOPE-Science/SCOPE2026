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

# Reproduction and verification

The theorem is analytic; its key checkable logical steps are the cone-radial factorization, the boundary-support equivalence, the halfspace containment of common-facet samples, and compact moment uniqueness. In particular, a finite numerical run cannot verify the universal quantifiers over convex bodies or all orders.

Run the included standalone Python file with `python3 verify_shell_moments.py` (Python 3 standard library only). It samples planar polygon shells using the exact radial-coordinate coupling, clips independent sample segments against the inner homothetic polygon, verifies every sampled same-facet pair remains outside the inner core, and checks empirical facet-label coincidence against its exact probability. The deterministic invocation returned `VERIFY_OK`. The examples are a centered square, a triangle anchored at its centroid, and a non-centroid-anchored triangle, with shell ratios \(0.92\), \(0.98\), and \(0.997\).

The script tests only \(q=2\), only planar polygons, and finite random samples; it is evidence of consistency and code reproducibility, not a certificate of the general limiting theorem. The inverse-moment argument depends on uniqueness of finite Borel measures on compact \([0,1]\), not on numerical reconstruction. No independent review has been performed.
