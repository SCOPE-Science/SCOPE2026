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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic.

For
\[
\dot x=a(y-x),\qquad
\dot y=cy-xz,\qquad
\dot z=xy-bz,
\]
it verifies
\[
L\left(\frac{x^2}{2}\right)=a(xy-x^2),
\]
\[
L\left(\frac{y^2}{2}\right)=cy^2-xyz,
\]
and
\[
L\left(\frac{z^2}{2}\right)=xyz-bz^2.
\]

It also verifies the polynomial coboundary identity whose stationary integral is
\[
b\,\mathbb E[z(z-c)]
=
c\,\mathbb E[(y-x)^2].
\]

The equilibrium constraints
\[
y=x,\qquad z=c,\qquad x^2=bc
\]
are checked symbolically, and the classical parameter product is checked exactly.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic premises. The conditional laws require arbitrary one-variable test functions, while equality rigidity additionally uses invariant-support tangency and bounded completeness.
