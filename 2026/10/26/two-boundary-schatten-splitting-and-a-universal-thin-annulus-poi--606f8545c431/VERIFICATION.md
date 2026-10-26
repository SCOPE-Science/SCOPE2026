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

# Reproducibility and verification

The standalone `verification/verify.py` script requires Python, NumPy, and SciPy. Run `python verification/verify.py` from the extracted package root. It uses Gauss–Jacobi quadrature to integrate the exact probability-normalized annular Fourier Gram matrices for multiple weights, widths, and frequencies. It checks positivity, the closed-form unweighted limiting eigenvalues, the high-frequency boundary-layer constants, and a finite set of relative comparisons between finite width and the limiting profile.

Those finite computations are corroborating checks. The theorem's global-in-Fourier-mode limit, all \(p\)-threshold claims, and sharp trace limit follow from the analytic proof in `RESULT.md`: exact fiber formula, uniform radial-density ratio, endpoint Laplace asymptotics, and dominated Riemann sums. These are not inferred from finite numerics. Historical priority has not been independently adjudicated.
