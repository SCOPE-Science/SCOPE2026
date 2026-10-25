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

# Verification of the regular-polygon crossing-angle theorem

Run `python diagonal_transversality_verify.py` using a standard Python 3 interpreter. The file is embedded alongside this document and relies only on the standard library.

The program calculates the acute angle directly from Cartesian chord direction vectors for every four-element subset for \(4\le n\le24\) and checks its exact integer multiplicity against the stated formula, including the even midpoint atom. For larger polygons it checks normalization, the limiting folded-beta CDF, and sampled fixed-order moments with independent quadrature and convergent series. The checks completed successfully in the package preparation environment; the final status line is `ALL_CROSSING_DIAGONAL_ANGLE_CERTIFICATES_OK`.

The exact probability formula, all real moment orders and all infinite-size limits are **analytical theorems** proved in `RESULT.md`. Finite enumeration and numerical quadrature are corroboration only, not exhaustive proofs of limits. No external independent validation or certification is claimed.
