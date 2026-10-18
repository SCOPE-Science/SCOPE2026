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

# Computational and analytical verification
The analytic proof supplies global convergence, an eventual positive oriented deviation, a one-dimensional stable tracking identity, and a second-order \(O(t^{-2})\) remainder proving a finite integration constant after the explicit \(\log t\) correction. These conclusions are mathematical deductions rather than computational extrapolations.

Run `python verify_reward_edge.py` using Python 3 and SciPy. The self-contained checker performs 76 assertions across the two critical faces: exact Fraction identities for critical parameter equalities, first and second reward derivatives, leading and logarithmic coefficients, derivative of the Lyapunov energy at rational test states, and direct finite-time numerical trajectories through time 10000 using a controlled-error ODE solver. The checker reports 76 checks passed. Finite-time numerical comparisons are corroboration only and do not certify infinite-time claims or global publication priority.

Independent scientific audit was not performed. The first publicly available motivating preprint is arXiv:2308.09530v1 (2023-08-18).
