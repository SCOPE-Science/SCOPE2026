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

The included `verify.py` runs self-contained symbolic and separate finite-sum/numerical checks using SymPy and SciPy. Executing `python verify.py` printed `PASS` and reported 96 checks in the reviewed package. It verifies the Poisson influence variance and derivative identity symbolically, the ZIP population residual exactly, and small-mean Taylor coefficients. Its finite Poisson-truncation and maximizer checks only stress-test the analytic theorem.

The proof in `RESULT.md` supplies continuum quantifiers and all endpoint and limiting cases. This is a self-review only; independent audit has not been performed. Fixed-mean, then sample-size asymptotic limits must not be exchanged with mean-varying triangular-array limits.
