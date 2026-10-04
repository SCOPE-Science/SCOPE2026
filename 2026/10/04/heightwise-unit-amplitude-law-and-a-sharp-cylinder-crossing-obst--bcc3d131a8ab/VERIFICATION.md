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
The packaged `verify.py` uses exact sparse-polynomial arithmetic over rational coefficients in the variables \(x,y,z\).

It verifies:
\[
Lz=1-x^2,
\]
\[
L(y^2)=2y(x-y),
\]
\[
L(xy)=y^2z+x^2-xy,
\]
and the algebraic relation used for the stationary partition.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker certifies the polynomial identities. The conditional expectation uses the generator identity for arbitrary antiderivatives of continuous functions on the compact \(z\)-range. Equality rigidity and cylinder crossing are proved in `RESULT.md` using support invariance and compact completeness.
