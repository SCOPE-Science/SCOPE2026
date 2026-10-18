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

# Computational checks and limits

Run `python verify.py` with NumPy, SciPy and SymPy available. The executable checks the fifth-order magnetization Taylor series, the analytic square-root eigenvalue expansion to quadratic order in magnetization, and the original coupled complex Fourier-mode evolution integrated through physical time 2000. It uses a rescaled Fourier amplitude to avoid numerical underflow.

For one test with initial magnetization \(1/2\) and first torus Fourier mode, the renormalized log amplitudes at times 100, 250, 400, 700, 1200 and 2000 are approximately \(-2.279830216665\), \(-2.369069006809\), \(-2.402841376618\), \(-2.434813139377\), \(-2.458793841488\), and \(-2.476632957281\). These values exhibit convergence toward a finite offset consistent with the exact theorem. The symbolic checks and numeric assertions passed on the provided environment.

The infinite-time statement follows from the explicit asymptotic-analysis argument in RESULT.md; the finite numerical horizon alone would not certify it. No independent scientific audit has been performed.
