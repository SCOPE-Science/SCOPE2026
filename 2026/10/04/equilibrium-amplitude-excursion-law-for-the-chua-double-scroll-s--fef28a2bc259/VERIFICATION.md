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

For each of the three affine branches of
\[
h(x),
\]
it verifies
\[
L\left(\frac{x^2}{2}\right)
=
\alpha x\bigl(y-h(x)\bigr)
\]
and
\[
L\left(
\frac{\beta y^2+z^2}{2}
\right)
=
\beta(xy-y^2).
\]

It also verifies the canonical source values
\[
m_0=-\frac17,\qquad
m_1=\frac27,
\qquad
r=\frac32,
\]
and checks the three corresponding equilibria exactly.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic identities and canonical arithmetic. The conditional expectations use arbitrary test functions through antiderivatives on compact coordinate ranges, while equality rigidity uses invariance of the compact support.
