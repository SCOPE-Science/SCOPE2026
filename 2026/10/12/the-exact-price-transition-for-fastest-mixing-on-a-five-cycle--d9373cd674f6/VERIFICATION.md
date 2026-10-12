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

# Verification of the priced five-cycle theorem

The full proof appears in `RESULT.md` and covers all nonnegative conductance vectors and all positive real price parameters. The decisive checks are the following.

1. **Symmetry-free upper bound.** Positive scalars \(C_e,C_o\) and centered eigenvectors \(e,o\) yield a positive-semidefinite Gram matrix whose edge distances equal the entire price vector. The trace Rayleigh inequality bounds every feasible allocation; equality at the displayed rates is exact.
2. **Spectral ordering.** The two non-gap eigenvalue comparisons reduce to a positive quadratic and a positive degree-four polynomial. The latter has explicit strictly positive Bernstein coefficients on \([3/5,4/5]\).
3. **Parameter monotonicity.** The sixth-degree numerator of the defining derivative has seven strictly negative Bernstein coefficients, so the equation uniquely parametrizes every \(t\in(0,16)\).
4. **Boundary completeness.** The vector \((-2,-1,0,1,2)\) gives the sharp Rayleigh limit and forces every optimizer at \(t\ge16\) into the exact one-parameter family. The remaining even-sector eigenvalue polynomial determines its precise admissible segment.
5. **Reproduction.** Install SymPy for Python 3, then run `python3 verify.py` from a directory containing the included file. The expected output is exactly `VERIFY_OK exact five-cycle algebra, Bernstein signs and endpoint identities`. Symbolic identities, special price \(t=1\), and the critical \(t=16\) endpoint are checked using exact arithmetic. There is no reliance on a floating-point eigensolver or probabilistic experiment.

Limits: the checker verifies certificate algebra; it is not an independent formal-proof system. The literature comparison does not establish absence of undiscovered equivalent results. No independent audit or validation has been performed.
