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

# Reproducibility notes

A standalone `verify.py` file executes a conservative cell-centered finite-volume discretization of the heat equation with two reactive boundary fluxes. It is separate from the analytical Neumann-kernel proof. Its three case families consist of asymmetric nonzero wall coefficients, one reflecting wall, and symmetric reactive walls. For each, it checks \(t=60,120,240\) and compares the scaled conditional-density residual with the quadratic formula, and the instantaneous summed wall flux with \(S(t)(a_0+a_L)\kappa(t)/L\).

Run `python verify.py` with NumPy and SciPy installed. In the checked execution, all nine time points met the specified mass, flux-ratio, and profile-error assertions. At the last time point, the worst profile error across three configurations was approximately \(6.1272\times10^{-4}\), while each total-flux ratio was within \(6\times10^{-5}\) of unity. The finite grid is not a certificate for all times, initial data, or coefficient choices. The infinite-dimensional proof is in RESULT.md.

Only self-review has been carried out. No independent audit, external validation, or formal proof certification is asserted.
