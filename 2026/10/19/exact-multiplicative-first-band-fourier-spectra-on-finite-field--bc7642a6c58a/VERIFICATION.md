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

# Reproducibility and proof limits

Run `python verification/verify_spectra.py` with Python 3 and NumPy from the package root. The program implements additive and multiplicative field arithmetic (including the quartic field), enumerates both prescribed hyperplane levels, constructs the actual Fourier character matrix, and computes all Gram eigenvalues with a standard Hermitian eigensolver. `verification/verification_output.txt` is the captured output of this very code. Forty-four direct finite matrix comparisons and forty-four exact point-count comparisons passed; the largest spectral discrepancy was below \(7\cdot10^{-15}\).

The universal proof does not rely on numerical tolerances: it follows from the exact finite-field sum-count formula, an explicit invariant-subspace decomposition, and algebraic positivity/coordinate-count witnesses. The checker does not certify all prime powers or dimensions, nor does it certify originality. The only external scientific validation currently specified here is not performed; independent audit remains outstanding.
