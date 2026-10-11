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
The analytic proof derives the kernel from the stated Fourier multiplier, evaluates it exactly on the critical grid, proves endpoint norm attainment, splits the cotangent sum by parity, and obtains the asymptotic by Euler--Maclaurin after removing the endpoint singularity.

The standalone `verify.py` replays the following corroborative checks from the packaged path:

1. It reconstructs every kernel sample from the finite Fourier sine sum for all \(2\le n\le240\) and compares it with the cotangent formula, including the two zero samples.
2. It compares direct normalized absolute kernel sums with the closed endpoint constant for the same range.
3. It checks the exact two-scale identity for all \(2\le n\le500\).
4. It checks that the residual after the displayed asymptotic is on the predicted \(n^{-4}\) scale at five larger values of \(n\).

The recorded replay output is:

`VERIFY_OK kernel_cases=57838 norm_cases=239 dyadic_cases=499 asymptotic_cases=5 max_kernel_err=1.003e-11 max_norm_err=2.309e-14 max_dyadic_err=1.776e-15 max_scaled_asymptotic_residual=1.013e-02`

Finite numerical checks are not used to infer the infinite theorem. No claim is made about interior \(\ell^p\) norms, higher-order Cesàro tapers, or noncritical sampling ratios.
