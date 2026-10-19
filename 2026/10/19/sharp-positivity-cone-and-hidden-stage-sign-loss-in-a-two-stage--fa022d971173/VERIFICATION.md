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

Run `python3 verify.py` with Python 3.11 or later. No third-party packages are required. The script checks the exact rational order equations and 2,268 rational stage-versus-recurrence instances, Schur inequalities on a rational grid, a high-precision bisection bracket for the unique positive-starter threshold, and 1,599 finite iterate checks with exact first-negative-index comparisons. The expected console output is reproduced in `verification_output.txt`.

The all-index positivity cone is proved using the two distinct characteristic roots. Monotonicity of the smaller root and the exponential starter establishes the global uniqueness claim. A logarithmic expansion of the exact strict first-negative-index formula proves the onset law. Finite computations are supplemental checks, not a proof that all iterations are positive. Floating-point arithmetic, other method coefficients, nonautonomous nonlinear positivity, and vector problems are not certified here.
