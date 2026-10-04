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
\dot x=a(y-x),\qquad
\dot y=(c-a)x-xz+cy,\qquad
\dot z=xy-bz,
\]
it verifies
\[
Lx=a(y-x),
\qquad
Lz=xy-bz,
\]
and, with
\[
d=y-x,\qquad
\rho=2c-a,
\]
it verifies
\[
Ld=(\rho-z)x+(c-a)d.
\]

For
\[
F
=
xd-\frac{c-a}{2a}x^2,
\]
the checker verifies the exact certificate
\[
LF=a d^2+(\rho-z)x^2.
\]

It also verifies the classical reductions
\[
(a,b,c)=(35,3,28),
\qquad
\rho=21,
\qquad
b\rho=63.
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the polynomial algebra and canonical arithmetic. The conditional laws additionally use arbitrary test functions through antiderivatives on compact coordinate ranges; the equality classification uses invariance of the compact support.
