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

# Reproducible verification

Execute `python verify.py` with the packages in `requirements.txt`. The checker computes the exact conditional bridge area covariance, verifies the fixed-node Gram-inverse formula at 45 distinct rational configurations, and independently derives the uniform expectation. Symbolic identities check the density-normalization formula, monotonic root equation, and derivative cancellation behind the flat support potential. High-precision integration verifies mass one, second moment, the obstacle profile at interior/exterior test points, and the exact optimum.

The unique root exists analytically because the normalizing function is strictly increasing from zero to \(1+\pi/2\) on \([0,1]\). The global bound for all Borel sampling distributions follows from the positive interval-mass quadratic identity and the constructed potential, not from any finite grid or Monte Carlo exercise.

Limits: these are scientific cross-checks of the supplied proof, not a machine-formal proof or an independent audit. They do not verify absent prior art, other kernel families, alternative minimax risk order, or larger sample sizes.
