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

# Verification of the perimeter-moment inverse theorem

Run `python3 verify.py` in the same directory as this document. It requires only the Python 3 standard library.

The checker independently computes planar projected convex hulls of the eight box vertices and their polygonal perimeters for 320 deterministic random directions and compares them with the exact zonotope projection formula. It verifies the rational sixth-coordinate spherical moment \(4/21\), the nonvanishing bounds, the moment-to-power-sum inversion on four different positive boxes (including repeated side lengths), and the exact two-moment nonuniqueness example. Midpoint quadrature is used solely as a numerical approximation to the universal constants.

Expected successful output begins with `VERIFY_OK hull_checks 320`. Finite tests, floating point agreement, and quadrature are not proofs that the theorem holds for all box dimensions or all viewing directions. The analytic proof in RESULT.md gives universal scope; the verifier supplies reproducibility diagnostics.

Independent audit has not been performed.
