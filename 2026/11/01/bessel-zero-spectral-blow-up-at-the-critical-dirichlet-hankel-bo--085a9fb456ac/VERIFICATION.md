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

# Verification record

The reproducible finite consistency checks reside in `check.py` and use NumPy and SciPy. The extracted script ran successfully with 54 assertions. It checks beta-moment formulas and bounds, the first four eigenvalues of a finite Nyström approximation of the limiting Bessel kernel, partial sums of positive Bessel-zero reciprocals, and sample values of the logarithmic step kernels. It avoids subtracting nearly equal large gamma functions by using a large-index asymptotic for the corresponding diagnostic only.

The general statement is proved by the analytical Hilbert–Schmidt convergence and the Sturm–Liouville/Bessel boundary calculation in `RESULT.md`, not by finite matrix extrapolation. The script does not certify an infinite-dimensional limit, exhaustive priority, or correctness of the analytic proof independently. The original norm convention and unnormalized measure are stated explicitly.

Independent audit and validation have not been performed.
