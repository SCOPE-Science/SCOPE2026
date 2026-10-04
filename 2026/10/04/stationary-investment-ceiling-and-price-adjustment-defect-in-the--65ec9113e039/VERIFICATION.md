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
\dot x=z+x(y-a),\qquad
\dot y=1-by-x^2,\qquad
\dot z=-x-cz,
\]
it verifies
\[
L\left(\frac{z^2}{2}\right)
=
-xz-cz^2
\]
and
\[
L\left(\frac{x^2+z^2}{2}\right)
=
x^2(y-a)-cz^2.
\]

After clearing the factor \(c\), it also verifies the algebraic reduction
\[
c x^2\left(a+\frac1c-y\right)
=
x^2-cx^2(y-a).
\]

Finally it verifies that the nonzero-equilibrium relations
\[
z=-\frac{x}{c},
\qquad
y=a+\frac1c,
\qquad
x^2=1-b\left(a+\frac1c\right)
\]
make all three vector-field components vanish after denominators are cleared.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the polynomial certificates. Conditional expectations and equality rigidity are analytic consequences of stationarity and invariant support, as detailed in `RESULT.md`.
