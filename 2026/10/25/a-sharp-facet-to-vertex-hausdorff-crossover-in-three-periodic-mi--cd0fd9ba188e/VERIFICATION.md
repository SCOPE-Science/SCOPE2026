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
# Verification scope

The analytical argument is in `RESULT.md`. Checked properties include the exact facet-length recurrence, the classification of support radii and vertex radii, the discriminant and uniqueness of the positive root, a strict geometric endpoint inequality, and matching transport upper and lower bounds. The asymptotic coefficients come from analytic Taylor expansions, not numerical regression.

The accompanying standard-library script `verify.py` independently intersects support lines in Cartesian coordinates. It verifies facet lengths and perimeter, support and vertex extrema, and root signs on multiple finite examples. Execute with `python3 verify.py` and expect `VERIFY_OK 3105`. These computations do not prove statements for all integers or all real parameters.

The primary arXiv full texts and two particularly close published research documents were materially read and compared by implication. Other accessible historical claims were used solely to exclude overlap. No independent validation has been performed.
