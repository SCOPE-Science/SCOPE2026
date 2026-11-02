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

## Checks performed
Exact symbolic arithmetic in `verify.py` confirms the characteristic-two cubic identity, the middle coefficient of the elimination quadratic, the reduction of its discriminant, and the projective-bundle degree calculation. It also exhaustively checks all nonzero `F2` points for the equivalence of the gradient-zero and cyclic-matrix-product-zero criteria; the test returns `VERIFY_OK`.

## Limits
These checks are supplemental. The claim for all algebraically closed fields of characteristic two follows from the detailed algebraic-geometric proof, not from finite examples. No claim is made about the nonreduced Jacobian singular scheme, other characteristics, or independent certification.
