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

# Verification and reproducibility

Run `python check.py` from the directory containing the accompanying complete script. It uses only the Python standard library. In the executed review, the checker produced: `PASS: 62 exact rational assertions, including independent permutation enumeration`.

The tests independently enumerate every vertex ordering for paths of lengths 1 through 7, cycles of lengths 3 through 7, and wheels with 3 through 6 rim vertices. Rational recurrences reconstruct the expected distributions; the analytic path mean and factorial-second-moment generating-function coefficients are checked for lengths 1 through 14; finite wheel mixtures and conditional-variance identities are compared exactly.

The infinite statements are not algorithmically certified by finite enumeration. Their justification is the complete analytic proof: first-step decomposition, generating-function coefficient asymptotics, published path Gaussian limit, fourth-moment stabilization and exact mixture moment identities. In particular the Gaussian limit is not a variance-convergence statement. No independent mathematical audit has been conducted.
