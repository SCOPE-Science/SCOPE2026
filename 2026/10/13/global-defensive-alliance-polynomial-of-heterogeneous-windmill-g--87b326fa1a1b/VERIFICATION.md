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

# Verification

Execute the included `verify.py` using Python 3 with no nonstandard dependencies. Its checker constructs the adjacency graph independently, iterates all vertex masks for every sorted blade-size vector of total peripheral size from 4 through 12, tests the standard domination and alliance predicates, and compares with the case split and polynomial coefficients. It separately confirms the minimum and extremizer count. Expected output:

`VERIFY_OK size_vectors=65 membership_checks=251104 valid_sets=78096 coefficient_checks=782 max_vertices=13`

The exhaustive finite runs cannot establish the general theorem. The arbitrary-size proof is the closed-neighborhood count, center threshold, and local binomial convolution in `RESULT.md`. Only the stated domain is covered. No independent audit or formal proof certificate has been performed.
