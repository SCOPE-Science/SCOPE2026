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
The packaged `verify.py` uses exact sparse-polynomial arithmetic over rational coefficients in the variables \(x,y,z,a,b\).

It verifies the generalized Sprott G vector field and the certificates
\[
L\!\left(\frac12x^2-b(y+z)\right)=ax^2+bx,
\]
\[
L\!\left(-\frac a2x^2-bx-ab(y+z)\right)
=b^2z(z-1)-(ax+bz)^2,
\]
as well as
\[
L(x^2)=2ax^2+2bxz,
\]
the three coordinate-generator identities, and the two equilibrium substitutions.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker certifies the algebraic identities. The conditional-expectation statement uses arbitrary antiderivative test functions on the compact \(x\)-range, and the equality/periodic-crossing deductions are proved analytically in `RESULT.md`.
