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

# Verification instructions and limits
Execute `python3 verify.py` using Python 3.9+; no nonstandard dependencies or downloaded data are required. The script reconstructs the sixteen-state weighted transfer matrix from the triple-neighborhood rule, then establishes the proposed degree-six determinant polynomial using exact integer Newton identities at 33 integer values of the weight. This is an exhaustive algebraic identity test because every coefficient has polynomial degree at most 32. It also reconstructs circular-ladder adjacency independently and enumerates every subset for \(3\le n\le10\), comparing all coefficients; then checks the largest coefficient for \(3\le n\le35\). Successful execution prints `EXACT_DETERMINANT_IDENTITY_OK`, `EXHAUSTIVE_SUBSETS_n3_TO_n10_OK`, `EXTREMAL_SEQUENCE_n3_TO_n35_OK`, and `VERIFY_OK`.

The infinite classification of maximum configurations is proved mathematically in RESULT.md. Finite enumeration alone cannot establish infinite results, and no independent review or external certification has occurred.
