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

Run `python3 check_hessian.py` with Python 3 and the standard library. The script checks exact first and second rational differences at 34 indices, checks the predicted minimal modes at sizes 2–18, and compares four direct finite-difference curvatures with the spectral prediction.

Observed output:

`PASS: 68 exact difference identities; central modes N=2..18; 4 direct-energy curvature tests`

The convergence of the energy Fourier series after two angular derivatives, the full real-Hessian diagonalization, strict eigenvalue positivity, exact minimizer modes for every size, and the asymptotic coefficients are proved symbolically in `RESULT.md`. Finite truncations are only supplementary diagnostic checks. No third-party independent audit has been performed.
