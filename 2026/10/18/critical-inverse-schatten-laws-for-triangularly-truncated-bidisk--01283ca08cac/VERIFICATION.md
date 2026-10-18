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

The analytical proof is in `RESULT.md`. To reproduce finite-dimensional consistency checks use Python 3 and NumPy and run `python checker.py` in the same extracted directory. The expected terminal output is `PASS 549 finite-matrix/moment/endpoint/crossover assertions`.

The program independently builds compressed analytic multiplication matrices in the monomial basis, computes their numerical singular values, compares the full positive singular multiset with the trigonometric formula, checks nullity and extremal singular values for several complex coefficient choices, compares the exact \(p=2\) trace for many truncation depths, and checks convergence of the \(p=2\) critical-window integral at representative parameters. The comparisons are floating-point and specify tolerances. Numerical truncation cannot prove general-dimension, asymptotic or priority claims; their mathematical arguments are given separately.

The spectral and inverse-power claims concern the Moore–Penrose inverse and do not assert bounded inverse symbols or an unrestricted multivariate Toeplitz theorem. Independent mathematical and bibliographic audit has not been performed.
