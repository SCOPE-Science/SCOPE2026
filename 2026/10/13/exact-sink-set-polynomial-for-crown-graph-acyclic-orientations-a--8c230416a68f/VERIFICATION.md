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

# Reproducibility

The self-contained `verify.py` script uses Python 3 and only standard-library modules. Execute `python3 verify.py` in the same directory as this document. A passing run prints:

`VERIFY_OK color_checks=72 orientation_bitstrings=4164 multivariate_checks=6 cubic_discriminant=-50430544`

The code tests 72 proper-coloring instances by direct assignment; enumerates every edge orientation for crowns of matched size \(2,3,4\) and checks acyclicity using independent topological deletion; compares all coefficients to the closed restricted-Stirling count; evaluates the full multivariate polynomial at six distinct assignments; checks additional coefficient rows at \(n=5,6\); and recomputes the cubic discriminant exactly. The symbolic arguments in RESULT.md establish the infinite family; finite checks are supplemental and are not independent mathematical certification.
