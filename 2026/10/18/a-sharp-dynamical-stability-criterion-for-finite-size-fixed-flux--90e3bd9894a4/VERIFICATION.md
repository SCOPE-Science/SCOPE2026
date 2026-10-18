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

The linearization and exact renewal kernel are derived in `RESULT.md`, including treatment of the extraneous negative characteristic root introduced when clearing a denominator. The analytic stability proof covers all positive \(L,\kappa,B\) and all positive \(C^2\) growth laws meeting the assumptions; finite numerical experiments cannot replace those inequalities.

Reproduction: with Python 3 and no third-party packages, run `python verify.py` in the extracted package directory. The program checks the positivity minimum of the quadratic speed, exact polynomial coefficients, three algebraic equilibrium masses, fold heights, derivative signs, and representative closure/characteristic normalizations. It prints a PASS line only after the assertions hold. It is a consistency checker, not a general infinite-dimensional spectral certificate.

The stationary critical folds are nondegenerate since the corresponding second derivatives do not vanish. Linear stability does not imply quantified nonlinear basins, global convergence, or stochastic extinction behavior. No external independent audit is represented by this file.
