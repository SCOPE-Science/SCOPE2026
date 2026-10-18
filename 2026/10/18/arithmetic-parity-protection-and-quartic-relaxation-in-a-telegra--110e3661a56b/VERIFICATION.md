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

# Reproducibility checks

Install compatible NumPy and SciPy versions as specified in `requirements.txt` and run `OPENBLAS_NUM_THREADS=1 python verify_flux.py`. The script constructs, independently from the Fourier probability formula, a block classical-environment Liouvillian for the conditional density operators and evaluates the matrix exponential. Its tested physical site distributions match the analytical expression. The script additionally checks the exceptional half-phase stationary profile, the exact minimum sine separation for odd cycle sizes, and the limiting coefficient in the \(N^{-4}\) law.

The limiting spatial law for even cycles is obtained by a finite Fourier root-of-unity identity. The sine-gap minimization and exact logarithmic exponent are established analytically in `RESULT.md`; the executable checks finite examples and do not certify all sizes, phase parameters or times. The main statement does not assert pointwise density-matrix mixing or finite-precision mixing-time bounds. No independent audit has been conducted.
