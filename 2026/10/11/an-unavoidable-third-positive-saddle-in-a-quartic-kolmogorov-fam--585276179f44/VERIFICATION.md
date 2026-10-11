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

The primary full text was inspected for the exact vector field, its statement about positive equilibria, the parameter range, and the endpoint Jacobian matrices. The publisher record was checked for publication date and MSC classification.

`artifacts/verify_third_equilibrium.py` reconstructs the two polynomial components with symbolic exact arithmetic. It verifies \(P(x,1)=0\), factors \(Q(x,1)=(x-1)(x-2)(2x-3)\), computes \(J(1,1)\), \(J(3/2,1)\), and \(J(2,1)\), and checks the middle determinant, trace, characteristic polynomial, and exact eigenvalues. The recorded output in `artifacts/verification_output.txt` ends in `VERIFY_OK`.

The checker certifies the algebra only. The literature comparison, scope limitation to the line \(y=1\), and value judgment are stated separately. No numerical integration is used as proof, and no independent audit has been performed.
