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
The proof is exact and global for the stated Hessenberg fivefold. The accompanying `artifacts/verify.py` checks the local algebra over the rationals/symbolically: it reconstructs the two incidence equations on an eigenbasis chart, verifies their reduction to `u+x` and `p*y+q*z`, and confirms that the Hessian of the transverse quadratic form has rank four and determinant one.

It also rewrites the published Example 5.5 patch polynomial by an invertible triangular coordinate change into the same nondegenerate quadratic normal form, and it checks that the global description contains eight torus-fixed singular flags, four on each of the two components.

These computations do not replace the global proof. The exact global step is the singularity criterion for the complete intersection `phi(v)=phi(Sv)=0`, followed by reconstruction of the projective-line fiber.

Replay with:

`python3 artifacts/verify.py`

Expected final line: `VERIFY_OK`.
