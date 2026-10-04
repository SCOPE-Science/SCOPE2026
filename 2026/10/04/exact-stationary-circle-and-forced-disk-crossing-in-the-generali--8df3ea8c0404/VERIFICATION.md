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

It verifies
\[
L(xy+z-bx)=x^2+y^2+ax,
\]
\[
L(x^2+y^2+ax)=y(4x-2z+a),
\]
and
\[
L(yz)=xz-z^2+axy+xyz+by^2.
\]
It also verifies that \((0,0,0)\) and \((-a,0,-a)\) are equilibria symbolically and that, after imposing a non-equilibrium boundary arc with \(b\ne2\), the cleared polynomial obtained from \(F=0\) has nonzero quartic coefficient \(4\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

Limits: the checker certifies the algebraic identities, not the literature comparison. The support-invariance and interval-polynomial arguments are proved explicitly in `RESULT.md`.
