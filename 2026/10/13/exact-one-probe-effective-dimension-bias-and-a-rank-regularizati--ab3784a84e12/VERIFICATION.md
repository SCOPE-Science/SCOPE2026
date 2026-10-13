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

# Reproduction and mathematical limits

Run `python3 verify.py` with Python 3.9 or newer. No third-party dependencies are needed. Successful output begins `VERIFY_OK` and reports the counts of independently checked rational identities, directly reconstructed rank-one matrix function evaluations, angular integrations, and matched-regularization limits.

The exact-rational checks use positive spectral values parametrized so that both \(\sqrt{a(a+\zeta)}\) and \(\sqrt{b(b+\zeta)}\) are rational. The matrix reconstruction checks compute the actual Nyström matrix and its single nonzero eigenvalue before evaluating the matrix function. Separately, midpoint angular quadrature numerically integrates the original polar expression, not merely the closed-form bias. Small-scale checks evaluate the boundary-layer limit at multiple parameters. These are finite tests; the integral identities and all universally quantified claims are established analytically in `RESULT.md`.

The result does not address finite precision, higher dimensions, multicolumn sketches, statistical variance, or an independent audit.
