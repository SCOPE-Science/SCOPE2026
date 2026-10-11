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

The proof identifies the complete restricted Walsh Gram matrix by conditioning on one and two Bernoulli coordinates, splits its permutation-invariant sectors, and proves strict eigenvalue interlacing by a negative determinant at the intermediate level. Injectivity uses the \(n+1\) evaluations on the radius-one ball. The critical-window limit invokes the binomial central and local limit theorems; the balanced odd-dimensional monotonicity is an exact central-binomial ratio.

Run `python verify.py` with Python 3 and its standard library. The checker independently enumerates the cube and calculates exact Gram matrices and characteristic polynomials for every \(3\le n\le8\) and every radius (39 cases), checks 99 monotonicity ratios with exact rational arithmetic, and compares three large-dimension spectra with Gaussian predictions. The code reports `VERIFY_OK` on success. Finite checks do not imply the infinite-dimensional theorem without the analytic proof.

Independent external validation has not been performed. Numerical Gaussian comparisons are within a stated fixed tolerance; they are consistency checks, not convergence-rate certifications.
