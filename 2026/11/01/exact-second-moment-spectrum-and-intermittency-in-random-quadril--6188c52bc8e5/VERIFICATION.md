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

# Verification evidence and limits

The accompanying `verify.py` creates the affine normal form, computes the four interpolated vertices, and integrates exact polynomial coefficients over four independent uniform variables using the rational moments \(\mathbb E[u^k]=1/(k+1)\). It asserts the exact conditional area mean and both second-moment closure identities, and verifies the characteristic polynomial and the all-order parallelogram spectral formula by exact SymPy arithmetic. It also independently samples 28,000 trajectories from a fixed parallelogram at each of three step counts and compares the observed mean and second moment with the analytical predictions. This independently written Monte Carlo loop is a finite consistency test, not an infinite proof or an independent mathematical audit.

The proof in `RESULT.md` establishes the universal conditional identities by affine covariance, and derives the almost-sure normalized-area statement via square-root conditional expectation and Borel–Cantelli. The checker does not itself formally certify the almost-sure theorem, all possible external literature comparisons, or the novelty of any claim.

Dependencies: Python 3 and SymPy; run `python verify.py` after extracting the files. The successful output terminates in `ALL_QUADRILATERAL_MOMENT_CHECKS_PASSED`.
