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
\dot y=x(b-kz),\qquad
\dot z=h x^2-cz,
\]
it verifies
\[
Lx=a(y-x),
\qquad
Lz=h x^2-cz,
\]
and the certificate
\[
L\left(
-hxy+\frac h2x^2+bz-\frac k2z^2
\right)
=
kc\,z^2-bc\,z-ah(y-x)^2.
\]

It also verifies the three equilibrium substitutions and, for
\[
a=10,\quad b=40,\quad c=\frac52,\quad k=1,\quad h=4,
\]
the exact constants
\[
\frac ch=\frac58,
\qquad
\frac{ah}{kc}=16,
\qquad
\frac{h}{akc}=\frac4{25},
\qquad
\frac{bc}{hk}=25.
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the polynomial algebra and canonical arithmetic. The conditional laws use arbitrary test functions through antiderivatives on compact coordinate ranges; the equality classification additionally uses invariance of the support.
