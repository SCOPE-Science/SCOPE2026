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

# Verification and limitations

Run `python3 verify_dirichlet.py` with Python 3 (standard library only). The script directly differentiates the finite Dirichlet moment formula at all integer parameter vectors for dimension 2 through 5 and concentrations 1 through 5: 3,900 exact rational comparisons against the stated covariance formula, plus exact sign checks. It separately checks symmetric cases and the two contrasting two-category examples, including a half-integer digamma difference.

These are finite algebraic diagnostics and cannot establish arbitrary-real-parameter validity. The proof in RESULT.md uses the general Dirichlet moment identity, legitimate exponent differentiation for positive parameters, and monotonicity of the digamma function. No independent audit or external validation has occurred.
