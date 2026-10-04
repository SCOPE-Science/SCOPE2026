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
# Verification

The proof in `RESULT.md` is analytic. Its critical steps are: (i) whitening the pair \((\Sigma_0,\Sigma_0+\Sigma_\star)\) to obtain the generalized-eigenvalue weights \((1+\lambda_i)^{-1}\); (ii) converting joint ellipsoid coverage into the weighted chi-square probability \(F_Q(\tau\chi^2_{d,1-\alpha})\); (iii) using Rayleigh-quotient extremality for the all-contrast threshold; and (iv) comparing upper chi-square quantiles for the limit \(\alpha\downarrow0\).

`verify.py` checks an anisotropic two-dimensional instance without external packages. For \(\Sigma_0=I_2\), \(\Sigma_\star=\operatorname{diag}(0,3)\), and \(\alpha=0.05\), deterministic quadrature and bisection give \(\tau_{\mathrm E}\approx0.6917708845\), strictly between the generalized-eigenvalue bounds \(1/4\) and \(1\). The all-contrast threshold is \(1\).

The computation does not certify the general asymptotic theorem and is not presented as exhaustive evidence. The theorem still depends on the stated bMGP Gaussian-limit premises and on consistent covariance estimation if implemented with plug-in matrices. No finite-sample coverage claim is made.
