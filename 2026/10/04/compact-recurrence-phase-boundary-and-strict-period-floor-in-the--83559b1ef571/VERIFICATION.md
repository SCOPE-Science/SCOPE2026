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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic over rational coefficients.

It verifies the centered vector field, the certificate
\[
H=-XZ-\frac12Y^2-XY+\frac c2X^2-\frac13X^3,
\]
the identity
\[
L H=Y^2-aX^2,
\]
the eliminated scalar equation
\[
X'''+X''+cX'+aX-XX'=0,
\]
and the original coordinate and \(x^2\) generator identities used for the barycenter.

The stored checker output is `VERIFY_OK`.

Limits: the checker validates algebraic certificates, not literature originality. The compact-support and invariant-measure deductions are proved in `RESULT.md`.
