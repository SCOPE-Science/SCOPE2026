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

# Verification evidence and limitations

`CHECK.py` is a standalone Python 3 standard-library checker. Invoke `python3 CHECK.py` from the directory containing the scientific files. The packaged `CHECK_OUTPUT.txt` records the actual executed output: `CHECKS_PASSED 220`. Checks include exact rational Poisson-equation and martingale-covariance identities for strictly positive binary kernels, finite path-enumeration agreements with normalized matrix recursions, independent pressure-curvature finite differences, and finite-horizon stabilization of the predicted normalized log-survival residual.

The analytic proof in `RESULT.md`, not the finite computation, establishes the infinite-horizon theorem. Projective contraction and eigenvalue analyticity are standard mathematical theorems invoked with explicit hypotheses. The convergence constant is positive but not evaluated in general. No independent mathematical audit has been performed. The priority survey is limited to the specifically identified literature and record comparisons and is not a completeness guarantee.
