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

# Reproducibility and verification

Run `python verify.py` with Python 3.10 or later, using the standard library only. The program checks 160 exact-rational finite-state assertions, including transition probabilities, conditional means and variances, invariant distributions, stationary mean, moment balance, one-step covariance and the exact half-grid law. It also performs 9 numerical finite-kernel convergence checks for off-half-grid parameters. The printed count refers to test groups in the script; every group can contain more than one assertion.

The finite state interval \(\{x\in\mathbb Z:|x-\theta|\le1/(1-q)\}\) is invariant because each rounding innovation has magnitude at most one. A rational stationary kernel therefore legitimately computes the invariant law in those examples. Floating-point power iteration is used only as an approximation check. The analytic martingale central limit theorem and uniqueness for all real parameters are not computationally certified by finite testing; complete proofs appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
