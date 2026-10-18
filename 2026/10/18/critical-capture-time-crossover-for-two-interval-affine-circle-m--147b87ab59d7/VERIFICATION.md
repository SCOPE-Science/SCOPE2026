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

# Verification of the first-entry and landing-undershoot law

The proof is analytical: invert the exact affine recurrence \(u_{j+1}=s_\delta u_j-\Delta_\delta\), use the threshold sum to enumerate every nonterminal first-entry cell, and apply the affine map between each complete cell and its normalized landing depth. The Riemann-sum approximation is uniform over times of size \(1/\delta\); the inverse slow-flow profile has derivative bounded away from zero on the relevant compact interval. This proves the first-passage limit and the \(W_1\) upper bound. The initial-mass mismatch in \((0,\delta)\) supplies the positive linear lower bound. The sole truncated cell has \(O(\delta)\) probability and controls the joint-law product error.

Execute `python3 capture_verify.py` with Python 3 and no external dependencies. The code checks three exact-rational slope-perturbation choices, the exact first-entry threshold and landing-undershoot identity on representative cells, and numerical limits at three parameter slopes. Successful run ends with `ALL_CHECKS_OK`. Finite checks are supplemental; they do not prove the uniform-in-parameter asymptotic statements, and no independent audit has taken place.

The theorem concerns fixed geometric and slope parameters and sufficiently small positive \(\delta\). Weak convergence is not total-variation convergence between discrete and continuous time distributions. Publication priority outside the cited and inspected sources remains uncertain.
