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

The analytic proof establishes both the exact all-length covariance and the finite-dimensional asymptotic normality. The included `verify_multiscale.py` is supplementary evidence for coefficient and normalization checks, not a proof of asymptotic convergence.

Run `python verify_multiscale.py` with Python 3 and its standard library. It integrates products of two triangular interval-overlap kernels using rational arithmetic on all 121 pairs of lengths from the denominator-12 grid; the resulting values exactly match the symmetric covariance polynomial. It also checks four cross-Fourier sums against the integrated exact covariance and nine elementary log-correlation identities or bounds, totaling 134 tests. The check was executed and printed PASS.

The uncountable-range covariance proof comes from symbolic interval geometry, not a finite grid. The asymptotic proof uses the full KMT approximation, simultaneous Brownian white-noise modes, the bound on maximum normalized coefficients, and the Lyapunov/Cramér–Wold argument. No external audit has yet been performed.
