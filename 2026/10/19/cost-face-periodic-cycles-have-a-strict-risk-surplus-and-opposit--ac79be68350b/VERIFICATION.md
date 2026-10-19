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

# Verification record

The analytical proof establishes the exact derivative cancellation \(\nabla H\cdot F=0\), the nondegenerate positive Hessian, the existence of local periodic level sets, both periodic logit averages, and the scalar normal Floquet equation. None of these requires a finite numerical experiment.

The standalone file `verify.py` uses SymPy for exact symbolic simplification in four cases (three, five, and eight players) and SciPy's adaptive integration on both faces of the explicit three-player example. The numerical returns close to relative errors below \(10^{-9}\) under the declared integration tolerances. The checker independently evaluates \(H\) using the defining integral and reports its conservation discrepancy, the orbit's mean cooperation and risk, the cost-normal exponent, and the limiting linear period.

Checked examples: group and threshold pairs \((N,M)=(3,2),(5,3),(8,5)\); both extreme costs in the three-player example. Numerical period and mean-risk observations are demonstrations, not proof for all admissible parameters. The statement does not establish the global organization of the center annulus, global three-dimensional basins, or independent scientific verification.
