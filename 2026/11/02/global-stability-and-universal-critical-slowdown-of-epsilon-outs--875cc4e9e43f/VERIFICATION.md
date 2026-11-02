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
# Verification of the critical endpoint theorem

Run `python3 check.py` in the package directory. The checker needs only Python 3 standard libraries and replays exact rational and numerical checks. Its actual output is stored in `CHECK_OUTPUT.txt`, including the exact finite-hit witness, multidimensional positive-definite quadratic descent checks, and two long scalar trajectories under distinct memory coefficients.

The following statements are **proved analytically**, not by a computation: endpoint global asymptotic stability for all dimensions and strongly convex globally smooth objectives, asymptotic tracking of squared gradients by memory for every nonterminating scalar quadratic orbit, and the inverse-time limits. These follow respectively from strict endpoint descent with compactness, an eventually contractive memory-ratio recursion, and convergence of reciprocal-amplitude increments.

Finite numerical observations are horizon-specific and should not be read as universal or infinite-time certificates. No independent audit or external validation has been performed.
