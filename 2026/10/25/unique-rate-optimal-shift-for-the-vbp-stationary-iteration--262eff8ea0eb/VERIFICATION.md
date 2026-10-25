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

# Reproducibility and limits

The proof in `RESULT.md` reduces the stationary iteration exactly to a symmetric generalized-eigenvalue family and proves a unique minimizer by uniform strict Rayleigh-quotient monotonicity. For every SPD \(T\), symmetric indefinite \(W\), and \(\gamma>0\), the derivative numerator is strictly positive because \(T+WT^{-1}W\) is positive definite. The stability boundary has a strict inequality; equality at a positive critical shift has a unit-modulus eigenvalue and is not convergence from every initial error.

With NumPy and SciPy versions specified in `verification/requirements.txt`, run `python verification/check_vbp_shift.py`; the expected output is embedded in `verification/output.txt`. The checker explicitly constructs the original real block operator and the complete stationary error operator, compares every computed eigenvalue with the generalized-eigenvalue reduction for three distinct \(\gamma\) values, reproduces two closed-form examples, and repeats the comparison on 80 deterministic randomly generated SPD and indefinite systems. Random tests and numerical equality within tolerance do not prove the general assertion; the all-dimensional correctness rests on the complete proof in `RESULT.md`.

The result is about exact inner solves and asymptotic spectral radius only, not nonnormal finite-step behavior or practical outer flexible GMRES convergence. The complete text of the related 2024 PMBP paper could not be obtained in this comparison; its abstract and distinct block family were considered, leaving a documented originality risk. Independent audit is not performed.
