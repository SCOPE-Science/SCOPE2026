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

The included `verify_rankone_funnystrom.py` is a self-contained Python 3 verifier requiring only standard-library modules. Invoke `python3 verify_rankone_funnystrom.py` from the directory containing the file. Its completed execution reported `PASS: 18081 independent full-matrix, reduced-form, rational, and Gaussian-integral checks`.

The checks independently construct the full Nyström matrix and its transformed rank-one approximation in dimensions 2–9, compare against the derived weighted-eigenvalue formula, and test monotonicity for powers 1 through 4 and six functions. Exact `Fraction` arithmetic checks the two-dimensional scalar-monotonicity counterexample. High-resolution deterministic angular integration verifies the exact Gaussian expectation for six parameter sets; separate coefficient tests check its small-ratio limit.

The critical Jensen and covariance arguments, integral evaluations, and asymptotic limits are proved in `RESULT.md`, rather than certified by finite tests. The code verifies sample computations but cannot prove an infinite family. No finite-precision stability result or independent audit is asserted.
