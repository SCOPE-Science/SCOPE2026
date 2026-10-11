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

# Reproducibility and scope
Run `python3 verify_isocanted_ellipsoids.py` from the directory containing the extracted files. Only Python's standard library is needed. The verifier computes both single-level and adjacent-level candidate values using exact fractions; checks all retained inequalities and KKT multiplier signs; checks the stated diagonal-vertex avoidance for all sampled dimensions at least four; tests the inner facet constraints; verifies all explicit vertex coordinates for dimensions two through seven; and brackets each initial layer transition in dimensions two through thirty.

Expected summary: `VERIFY_OK exact_rational_cases=348 single_candidates=206 pair_candidates=142 explicit_vertices_checked=5904 pole_checks=324 john_facets=yes threshold_brackets=yes`.

These tests cover precisely the rational sample points coded in the script. They are not an exhaustive test of all real parameters or dimensions. The general claim is proved symbolically in RESULT.md. No independent audit is represented as having occurred.
