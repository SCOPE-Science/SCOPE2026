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

# Verification of exact rank-one risk law

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The code uses `fractions.Fraction` to propagate the complete first- and second-moment tensors through all row/column choices and compare each iteration with the analytical reconstruction formula. It separately enumerates all histories of lengths one through six in the concrete two-row case. Additional exact checks cover the strictly increasing-risk three-coordinate case and the residual-optimal step. The current package passes 5,579 exact comparisons. The proof of the infinite-time statements is analytical, using a martingale decomposition, bounded second moments and summability; finite computation is not an infinite certificate.

The result applies only to the specified rank-one finite-dimensional, independent uniform sampling model with exact arithmetic. The examples identify an omission in a prior convergence argument but do not inspect or certify implementations of that paper. No independent audit has been performed.
