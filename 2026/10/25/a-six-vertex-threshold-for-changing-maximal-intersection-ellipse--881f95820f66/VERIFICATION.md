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

# Reproduction and limits

Run the accompanying `verify.py` under Python 3 (standard library only). It executes exact `fractions.Fraction` arithmetic, derives the six vertices from strip-line intersections, verifies all six normal contacts and both positive isotropic moment decompositions, checks positive definiteness and the explicit inverse of the Löwner matrix, and returns the nonzero commutator entry \(-3/130\). A successful execution prints one PASS line.

The infinite-family conclusion does not come from exhaustive computation. It follows from the exact endpoint certificates and Bochi's published uniqueness-and-continuity theorem, applied to two parameters in the strict interior. The quadrilateral obstruction follows from quarter-turn invariance of the unique maximal-intersection ellipses of a square and affine covariance. No intermediate ellipse is constructed in closed form; independent mathematical review is not recorded.
