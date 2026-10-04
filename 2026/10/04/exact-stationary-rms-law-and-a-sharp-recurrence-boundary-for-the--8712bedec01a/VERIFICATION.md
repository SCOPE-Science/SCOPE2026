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
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-y-xz-yz-a,
\]
it verifies
\[
Lx=y,\qquad
Ly=z,
\]
\[
L\left(\frac{x^2}{2}\right)=xy,
\qquad
L\left(\frac{y^2}{2}\right)=yz,
\]
and
\[
L(xy)=y^2+xz.
\]

It then replays the stationary linear algebra to obtain
\[
\mathbb E[xz]=-a,
\qquad
\mathbb E[y^2]=a.
\]

For the source value
\[
a=\frac34,
\]
it verifies the exact squared RMS value \(3/4\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker verifies the algebraic certificates. The conditional laws use arbitrary one-variable antiderivative tests, while the critical \(a=0\) classification additionally uses invariant-support tangency.
