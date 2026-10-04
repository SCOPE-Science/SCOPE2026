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
\dot x=-yz+ax,\qquad
\dot y=xz+by,\qquad
\dot z=\frac13xy+cz,
\]
it verifies
\[
L\left(\frac{x^2}{2}\right)
=
-xyz+ax^2,
\]
\[
L\left(\frac{y^2}{2}\right)
=
xyz+by^2,
\]
and
\[
L\left(\frac{z^2}{2}\right)
=
\frac13xyz+cz^2.
\]

For the classical source parameters
\[
\left(5,-10,-\frac{19}{5}\right),
\]
it verifies the exact stationary coefficients
\[
5,\qquad
10,\qquad
\frac{57}{5},
\]
and the nonzero-equilibrium square relations
\[
x^2=114,\qquad
y^2=57,\qquad
z^2=50.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates algebraic certificates. The conditional laws use arbitrary test functions through antiderivatives; the sign-rigidity theorem additionally uses invariant-support tangency and bounded completeness.
