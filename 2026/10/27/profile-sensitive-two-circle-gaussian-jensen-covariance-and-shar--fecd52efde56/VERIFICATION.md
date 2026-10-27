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

# Computational and analytic verification

The derivation of the exact finite covariance, the compact-uniform \(n\to\infty\) convergence, the strict radial monotonicity and the large-separation asymptotic is contained in RESULT.md. No external certification is claimed.

Run `python circular_covariance_check.py` with NumPy and SciPy. The implemented executable checks exact finite polynomial kernels by a discrete Fourier transform and evaluates limiting covariance integrals for three strictly positive affine weight profiles. The run reported 34 passing numerical checks, including finite-to-limit convergence, strict fixed-midpoint separation, large-distance coefficients, profile-reversal identities and the exact \(n=1\) logarithmic Gaussian variance \(\pi^2/24\). The numerical limiting integrals are truncated at \(|x|=1000\). The proof establishes integrable tail control; the numerical program alone does not prove the limits. The strict monotonicity and asymptotic constant require analytic arguments valid at every real parameter, supplied in RESULT.md.

Scientific limits: continuous differentiability and strictly positive endpoints are assumed; no non-Gaussian coefficient law, simultaneous large-\(n\)/large-separation theorem, distributional central limit or independent historical-priority audit is supplied.
