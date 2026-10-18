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

Run `python3 verify.py` with standard Python 3. The script directly enumerates the stated uniform permutations for 151 selected positive-margin pairs with total size at most six, tests the complete upper-tail conditional-order inequalities using exact rational fractions, and separately verifies all displayed cell-count covariance formulas. The observed output was `PASS: 151 distinct positive-margin pairs; 48818 exact rational conditional tail comparisons and covariance identities; all permutations of size <= 6 used for each case.`

Finite exhaustive checks are corroboration. Arbitrary-size correctness depends on the nested hypergeometric couplings and covariance symmetrization in `RESULT.md`. Independent audit has not been performed.
