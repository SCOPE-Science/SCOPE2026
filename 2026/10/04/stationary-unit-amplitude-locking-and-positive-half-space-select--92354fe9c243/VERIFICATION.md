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

For
\[
\dot x=\alpha x(1-y)-\beta z,
\qquad
\dot y=\gamma y(x^2-1),
\qquad
\dot z=\mu x,
\]
it verifies
\[
Lz=\mu x,
\qquad
Ly=\gamma y(x^2-1),
\]
\[
L(z^2)=2\mu xz,
\]
and
\[
L(x^2)=2\alpha x^2(1-y)-2\beta xz.
\]

It also verifies directly that the characteristic polynomial of the \(y=0\) subsystem matrix
\[
\begin{pmatrix}
\alpha&-\beta\\
\mu&0
\end{pmatrix}
\]
is
\[
\lambda^2-\alpha\lambda+\beta\mu.
\]

The stored checker output is `VERIFY_OK`.

The checker validates the algebraic certificates. The conditional laws additionally use arbitrary test functions through antiderivatives on compact coordinate ranges. The half-space and equality classifications use invariance of the sign regions and compact support.
