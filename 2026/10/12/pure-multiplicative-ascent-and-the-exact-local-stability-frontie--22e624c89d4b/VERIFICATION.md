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

The proof in `RESULT.md` is analytic.

`artifacts/verify_hmgd_frontier.py` symbolically differentiates the scalar core map at the minimizer and checks representative stable and unstable parameter choices. It also simulates the pure multiplicative recurrence and verifies convergence of its increment toward \(\eta_M\log3\).

The numerical trajectory is supporting evidence only. Local stability follows from the exact derivative, and global pure-branch divergence follows from the sign and fixed-point argument in the proof.
