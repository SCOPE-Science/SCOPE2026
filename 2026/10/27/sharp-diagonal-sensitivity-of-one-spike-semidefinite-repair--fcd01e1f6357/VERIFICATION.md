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

Run `python verify.py` with Python 3, NumPy and SciPy. The standalone check run completed with `ALL CHECKS PASSED: 1671 assertions`. It includes exact-rational matrix coefficient identities and independent numerical finite-difference reconstruction at base matrices with separated positive and negative spectra, as well as consistency checks for small orders, the cubic stationary point and asymptotic scaling. No finite enumeration is used to claim the infinite-dimensional-parameter conclusions, which rest on the mathematical proof in RESULT.md.

The Fréchet derivative is asserted only at nonsingular matrices with the two specified distinct spectral levels. At the singular gap limit, the theorem claims only a supremum of derivatives approached through regular matrices, not differentiability of positive-part clipping at the singular matrix. The exact global max-entry Lipschitz constant in arbitrary dimension is outside the theorem's scope.
