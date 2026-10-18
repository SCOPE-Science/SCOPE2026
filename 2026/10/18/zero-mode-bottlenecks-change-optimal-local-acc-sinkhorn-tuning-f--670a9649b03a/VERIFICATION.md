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

# Reproduction and verification

Run `python verify_acc_sinkhorn.py` with Python 3 and NumPy available. The program runs deterministic exact-rational comparisons of trace, determinant, and quadratic stability identities; grid-based numerical checks of endpoint dominance, global minimax, and the \(1/4\) transition; and finite-difference tests against derivatives of the actual nonlinear normalized Sinkhorn map and two-state Acc-Sinkhorn recurrence. Recorded result: **PASS 27178 deterministic checks**.

The specific positive rectangular realization uses the \(2\times4\) balanced coupling given in RESULT.md, and random positive \(3\times6\) couplings supplement it. Finite numerical grids do not establish uniqueness over all real parameters, and finite-difference diagnostics are not proofs of differentiation: the analytic derivations and strict inequalities in RESULT.md are necessary for the universal claims. The observation of local stability does not assert global convergence or a finite-time guarantee. No independent audit has been performed.
