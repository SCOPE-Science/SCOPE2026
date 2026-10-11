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

Execute `python3 verify.py` using Python 3 with only the standard library. The checker uses exact `fractions.Fraction` values throughout all mathematical comparisons. It reconstructs the stated piecewise Löwner coefficients and orbit weights in each dimension \(2\le d\le70\); verifies positive weights summing to one, orbit means, longitudinal and transverse covariance, strict shape positivity, exact contact orbit equalities, and containment of all orbit types. It independently enumerates all cube vertices and cut-edge midpoints through dimension nine, confirming contact classification and counts. It also evaluates the John shape's boundary support equalities and lower-facet strictness. A successful run prints:

`VERIFY_OK exact_Loewner_certificates_dimensions=2..70 exhaustive_vertices_dimensions=2..9 John_support=yes parity_and_exceptions=yes`

These are finite arithmetic tests. The full-dimensional, all-integer claim is supported by the algebraic proof in RESULT.md, not by extrapolating the test range. No external independent audit or certification has been performed.
