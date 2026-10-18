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

The analytic proof uses the defining real free two-convex norm, operator/nuclear duality, concavity of matrix square-root trace, the cycle Fourier spectrum, a finite sine sum, and a supporting-hyperplane optimality argument. No finite computation substitutes for those steps.

Reproduce the independent numerical checks with `python check_cycles.py` (requires Python 3, NumPy and SciPy). This program calculates the norm optimization on the entire probability simplex of edge weights, not just rotation-invariant weight choices. It also computes the exact analytical threshold independently from trigonometric sums and checks the base norm and chord derivative. On execution, it printed `FINITE_NUMERICAL_CHECKS_PASSED 77`.

Floating-point optimizer precision cannot certify equality at the mathematical boundary; the boundary follows instead from the supporting hyperplane proof. The code covers selected small and medium cycle sizes only. The claimed multi-chord criterion holds for every finite chord family by the same concavity argument, not by extrapolation from the sampled two-chord cases. The new research result has not undergone independent scientific audit.
