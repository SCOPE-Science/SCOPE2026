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
The packaged `verify.py` uses only the Python standard library and exact rational sparse-polynomial arithmetic.

For
\[
\dot x=y-a x^3+b x^2-z+I,
\qquad
\dot y=c-dx^2-y,
\qquad
\dot z=r[s(x-x_R)-z],
\]
it verifies
\[
L\left(\frac{y^2}{2}\right)=y(c-dx^2-y),
\]
\[
L\left(\frac{z^2}{2}\right)=rz[s(x-x_R)-z],
\]
and the exact residual relations
\[
dx^2-c+y=-\dot y,
\qquad
r[s(x-x_R)-z]=\dot z.
\]

For the frequently used coefficients \(d=5\) and \(s=4\), it checks the exact variance multipliers \(25\) and \(16\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation and invariant-support arguments are analytic consequences described in `RESULT.md`; the checker is used only for their algebraic premises.
