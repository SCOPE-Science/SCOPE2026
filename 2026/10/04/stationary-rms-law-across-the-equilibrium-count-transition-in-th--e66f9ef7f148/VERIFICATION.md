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
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-y-x^2-xz+3y^2+a,
\]
it verifies
\[
Lx=y,\qquad Ly=z,
\]
and the critical certificate
\[
L(z+xy+x)=a-x^2+4y^2.
\]

It also verifies that substituting
\[
y=z=0,\qquad x^2=a
\]
annihilates the vector field symbolically, and it checks the exact benchmark
\[
a=-\frac1{20}
\quad\Longrightarrow\quad
-\frac a4=\frac1{80}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificate. The conditional-expectation deductions use arbitrary antiderivatives on compact coordinate ranges, and the equality classifications use invariance of the compact support.
