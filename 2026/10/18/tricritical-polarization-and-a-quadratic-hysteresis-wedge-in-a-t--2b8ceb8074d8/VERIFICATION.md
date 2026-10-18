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

# Reproduction and verification

Run `python verify.py` with Python 3, SymPy, and mpmath. The script independently forms the exact reduced vector field from the normalized logistic weights, expands its Taylor series through order seven, and checks the cubic coefficient, vanishing point, quintic coefficient, and the coefficient governing the fold unfolding. Arbitrary-precision root solutions for \(\gamma=\gamma_*+\nu\) at \(\nu=0.02,0.01,0.005\) check the signs and approach of the two fold asymptotic ratios. Direct substitution checks vector-field signs near the degenerate point. All checks passed on the packaged source script.

The infinite-parameter and long-time conclusions rest on the analytic proof in `RESULT.md`, including the implicit-function and strict-concavity arguments. The finite numerical tests do not prove uniqueness outside the specified small neighborhood; no independent validation has been performed.
