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

The companion `verify_binary_moment_stdlib.py` requires Python 3 with no external packages. Run `python verify_binary_moment_stdlib.py` in the directory containing the file. Its expected terminal line is `VERIFY_OK`. It reconstructs the order-\((r-1)\) transvectant components with exact binomial coefficients, eliminates the two pivot variables, checks nonzero critical coefficients for odd \(r=5,7,9,11,13\), and checks the nonzero antidiagonal coefficients.

The mathematical proof of the infinite family is in RESULT.md. Finite checks cannot establish uniform Jacobian support or prove a universal analytic normal form. The complete-intersection premise is from Massri's cited Theorem 1.1. No independent audit has been performed.
