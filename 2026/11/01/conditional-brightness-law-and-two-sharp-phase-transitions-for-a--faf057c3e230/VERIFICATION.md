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

# Reproducibility and limits

Run `python3 verify.py` using the standard Python 3 library. In this package, the checker printed:

`VERIFY_OK: 360000 azimuth/facet checks; conditional means and atom fractions match`

The verifier reconstructs projections independently from all eight octahedron facets, compares them with the closed law, and numerically checks the conditional expected brightness, atom proportion and extremal support at twelve fixed alignments. These finite angular checks do not establish the continuum theorem. The continuum result rests on Cauchy's facet formula, signed-coordinate symmetry, an exact Haar disintegration, and an elementary one-dimensional change of variables. No external independent validation or proof certification has been conducted. The cited broader 2026 random-brightness manuscript remained inaccessible as full text, leaving a historical priority risk.
