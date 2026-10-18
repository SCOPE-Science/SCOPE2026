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

The proof uses the positive Toeplitz moment criterion, a direct Schur-parameter expansion, a piecewise concave scalar maximization, and the boundary angular derivative of a finite Blaschke product. These are the decisive infinite-family arguments; none depends on finite searches.

Execute `python verify.py` from this package after installing NumPy and SymPy. The packaged execution record `verification_output.txt` reports symbolic simplification of the critical equation and exact extremal expression and 99 independent numerical checks over orders 2 through 12 and nine two-phase settings per order. Those checks construct all boundary roots, their positive weights, the first \(n+3\) moments, and the normalization. The largest numerical moment residual observed was \(7.925\times10^{-15}\), with maximum radial root error \(2.887\times10^{-15}\). The finite checks do not certify all orders and do not establish originality.

The original sharpness calculation is analytic, not numerical; an independent scientific audit remains unperformed.
