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

# Reproducible checks

Run `python verify_bipyramid_shadow.py` with Python 3 and its standard library. This program uses only locally generated vertices, independently calculated projected convex hulls and direct spherical quadrature. It checks: complete four-atom normalization for the pentagonal solid; actual projection vertex counts versus facet-sign formula for multiple heights and odd orders; the general closed-form quadrilateral probability versus an independent numerical spherical integral; sharp fixed-height inverse-order decay; independent exterior-dihedral-angle mean; and Haar sampling of the full pentagonal law.

The intended successful final line is `ALL_PENTAGONAL_BIPYRAMID_SHADOW_CHECKS_OK`. Numerical checks and finite samples are not proofs of the statements over infinitely many odd orders; the proof in RESULT.md supplies the quantifiers, exact integral and analytic asymptotic. Independent audit has not been performed.
