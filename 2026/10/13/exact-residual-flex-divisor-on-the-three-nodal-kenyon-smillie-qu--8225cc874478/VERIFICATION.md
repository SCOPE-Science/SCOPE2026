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
The verification artifact `verify.py` reconstructs the published \(t=1\) quartic exactly and uses symbolic rational arithmetic to check the core identities.

It verifies:

- the normalized affine Hessian resultant
  \[
  729x^3(x^3-3x+1)^6(106x^3+3x^2-6x-2);
  \]
- absence of quartic–Hessian intersection at infinity;
- the residual Gröbner basis
  \[
  106x^2+23x+19y+3,\qquad 106x^3+3x^2-6x-2;
  \]
- the known three-node singular locus relation \(y=1-x-x^2\);
- tangent contact order three at \([0:0:1]\) and four at \([0:-1:1]\);
- squarefreeness and coprimality of the residual cubic;
- irreducibility modulo \(5\);
- discriminant \(-1026^2\).

The script was replayed from the packaged artifact path with SymPy 1.14.0 and returned `VERIFY_OK`.

Limits: the script certifies exact polynomial identities for the specified quartic only. It does not certify other fibers, family monodromy, or any independent review status.
