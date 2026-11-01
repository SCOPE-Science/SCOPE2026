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

Run `python3 verify.py` with a standard Python 3 interpreter. It performs polynomial arithmetic in the real parameter symbol through exact integer coefficient arrays, reconstructs the Bergman numerator and Cayley coefficients for boundary exponents 0 through 4, and algebraically verifies the critical Routh identities and special factorization. The expected output is `BERGMAN_ROUTH_EXACT_POLYNOMIAL_IDENTITIES_OK`. The analytic proof in RESULT.md supplies the positivity and root-count implications. The finite series comparisons in the program are illustrative only; they do not certify any infinite claim. No independent audit was conducted.
