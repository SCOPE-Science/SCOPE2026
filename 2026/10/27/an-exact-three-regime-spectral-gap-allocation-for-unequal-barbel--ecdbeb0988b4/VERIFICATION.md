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

The mathematical proof is in `RESULT.md`. An independently executable finite consistency script, `barbell_verification.py`, constructs weighted Laplacians for every integer pair \(2\le q\le p\le50\) (1225 cases) and checks the budget, \(\lambda_2\), the four-group eigenvector, the centered embedding norm, nonnegative weights and simplex feasibility. The script completed all 1225 cases successfully using NumPy symmetric eigensolvers. Floating-point computations are diagnostics only: they do not establish uniqueness, the exact transition, or the infinite-family theorem. The latter depend on the analytic eigenvalue decomposition, dual inequality and equality conditions in `RESULT.md`.

The paper attributed to Song et al. (2024), DOI 10.1016/j.disc.2024.114027, was checked at abstract level only. Complete literature coverage and independent validation have not been performed.
