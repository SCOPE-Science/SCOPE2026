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
# Verification details

The proof in `RESULT.md` uses an exact polytope decomposition, simplex Dirichlet second moments, the Wallis product, and explicit strict inequalities. The supporting `check.py` executable recomputes (1) the odd and even central-binomial comparisons by rational arithmetic through \(m=10\), (2) both elementary Taylor-series rational inequalities used for the infinite tails, and (3) independently triangulated numerical volume and radial second moments of all six polytopes \(\Omega_n\) with \(3\le n\le8\).

**Execution:** `OPENBLAS_NUM_THREADS=1 python check.py` using Python 3.10 or later, NumPy, and SciPy. Observed output: `CHECK_OK odd_exact=10 even_exact=10 independent_hulls=6 (+ analytical infinite proof)`. The hull comparisons used tolerance \(10^{-10}\); they are finite corroboration only. Strict assertions beyond the finite checked range are proved by the inequalities written in `RESULT.md`, not by extrapolation or timeout.

The inexact floating-point hull tests cannot certify asymptotic signs. Independent mathematical validation has not been performed.
