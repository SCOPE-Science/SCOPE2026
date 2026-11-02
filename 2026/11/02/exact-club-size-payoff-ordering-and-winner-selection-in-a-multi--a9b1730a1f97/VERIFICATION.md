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

The program `verify.py` uses only the Python standard library and can be executed with `python verify.py`. It passed 16,314 exact-rational finite-payoff identity comparisons for integer diner compositions through ten diners and at most four club labels; 55 further comparisons to independently exhausted allocations of all restaurants through four diners; four numerical examples of the fixed-finite-club replicator limit (including different tied-maximal faces); and eight numerical perturbation comparisons with the explicit local eigenvalues at equal-share equilibria.

The analytic argument is essential: finite tests do not certify all possible diner counts or club counts, and finite-time integration does not imply global convergence. The complete proofs derive the exact integral payoffs, strictly positive difference kernels, uniform kernel bound, monotone replicator ratios, and all equilibrium eigenvalues directly. Verification of findings in the literature remains subject to the residual risk of inaccessible reported supplementary notebooks.
