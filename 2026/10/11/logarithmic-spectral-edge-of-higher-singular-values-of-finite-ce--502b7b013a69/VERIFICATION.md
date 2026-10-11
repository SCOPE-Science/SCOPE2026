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

# Verification and limits

The inverse of the finite averaging matrix has the exact formula \((C_n^{-1}x)_i=i x_i-(i-1)x_{i-1}\). Its singular spectrum is the generalized spectrum of the weighted path energy and mass in the proof. The finite-dimensional checker in `verify_cesaro.py` performs exact rational inversion and Rayleigh-form checks for several dimensions and floating-point ground-state identity checks. No finite sample or output log is used to infer an all-dimensional statement.

The critical infinite steps are proved in RESULT.md: positivity of each remainder weight, uniform endpoint control, logarithmic interpolation and mass quadrature, weak compactness with Dirichlet boundary traces, matching smooth recovery sequences, and the two min--max inequalities. The proof requires only the one-dimensional Rellich compactness theorem and standard Courant--Fischer principle, not external certification.

The numerical scalar checks and cited scholarly sources do not constitute independent audit or publication validation. The assertion is limited to fixed higher singular ranks in real or complex Euclidean spaces. Possible undiscovered historical equivalents, particularly in finite-section spectral theory, remain a bibliographic risk.
