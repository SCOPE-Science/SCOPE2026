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
The packaged `verify.py` uses exact sparse-polynomial arithmetic over rational coefficients and the variables \(x,y,z,a\).

It verifies:
\[
Lz=y^2-a,
\]
\[
LQ=-2az,\qquad Q=x^2+y^2+z^2,
\]
\[
L(zQ)=(y^2-a)Q-2az^2,
\]
and
\[
L(xy)=y^2-x^2-xyz.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker certifies the algebraic generator identities. The conditional-expectation conclusions use invariance against arbitrary continuously differentiable test functions on compact coordinate ranges; the strictness and sign consequences are proved in `RESULT.md`.
