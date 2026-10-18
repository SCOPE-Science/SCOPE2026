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

# Reproducibility and verification scope

Execute `python verify.py` in this directory after installing packages in `requirements.txt` (NumPy and SciPy). The program constructs both the closed bright-block Lyapunov candidate and the generator matrices directly, then checks: 32 matrix solutions for half-lengths 1 through 8 with four combinations of nonzero hopping and positive capture strength; 36 directly diagonalized finite Liouvillian spectra for half-lengths 1 through 4 across three dephasing rates; and corresponding 36 quadratic expansion comparisons. Recorded output for the supplied implementation:

```
VERIFY_OK bright_lyapunov=32 dense_spectra=36 quadratic_coefficients=36 max_matrix_residual=1.29e-12
```

These calculations are finite and floating-point. They do not establish the all-length identity or certify originality. The closed-form matrix entries and their symbolic cancellation, together with the spectral perturbation argument, are the mathematical proof. The \(O(\gamma^3)\) remainder is for fixed positive capture rate, fixed nonzero hopping, and fixed finite path size. No independent external audit or experimental validation has been performed.
