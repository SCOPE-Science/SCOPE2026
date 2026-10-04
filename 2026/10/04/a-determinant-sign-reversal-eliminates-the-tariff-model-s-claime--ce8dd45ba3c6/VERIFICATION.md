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

The printed system was re-differentiated directly. At an interior equilibrium the Jacobian has zero diagonal, so its determinant equals minus the product of its two off-diagonal entries. The exact witness \(A_A=A_B=1\), \(B_A=B_B=-1/2\) gives \((x^*,y^*)=(1/2,1/2)\), determinant \(-1/16\), and eigenvalues \(\pm1/4\).

The paper’s Appendix 9 first integral was independently differentiated along the displayed vector field and gives \(\dot H=0\). Its Hessian at the mixed equilibrium is diagonal with entries \(-A_B/[x^*(1-x^*)]\) and \(A_A/[y^*(1-y^*)]\), so it is definite only for \(A_AA_B<0\), confirming the reversed center condition.

`verify.py` uses exact rational arithmetic for the witness and for multiple first-integral derivative evaluations. It does not numerically infer global behavior, and no claim is made about dynamics outside the printed continuous-time replicator model.
