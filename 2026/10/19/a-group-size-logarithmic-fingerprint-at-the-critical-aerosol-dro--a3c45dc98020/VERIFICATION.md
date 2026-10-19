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

# Verification and reproducibility

The theorem is proved analytically in `RESULT.md`. With SymPy and SciPy installed as specified by `requirements.txt`, run `python verify.py`. The checker verifies the exact Jacobian eigenvalues, the weighted Lyapunov derivative identity, the coordinate change to the transverse displacement, the cubic cancellation leading to \(-s^2/9\) in the scalar equation, and finite-time numerical comparisons for three sizes. The finite integrations only corroborate convergence of the corrected reciprocal prevalence; they are not evidence for an infinite-time theorem on their own.

The substantive global step is the exponentially stable forcing estimate proved in `RESULT.md`, applied first with cubic forcing and then with quartic forcing. It controls the remainder on actual positive trajectories. No claim is made of computer-assisted exhaustive verification, independent review, or checking stochastic finite-network simulations.
