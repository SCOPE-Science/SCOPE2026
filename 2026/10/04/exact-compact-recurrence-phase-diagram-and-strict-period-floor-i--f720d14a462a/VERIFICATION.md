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
\dot x=-x-ay,\qquad
\dot y=x+z^2,\qquad
\dot z=b+x,
\]
it verifies
\[
Lz=b+x,\qquad
Ly=x+z^2.
\]

With
\[
v=x+b,\qquad
w=-x-ay,
\]
and
\[
F
=
vw+\frac12v^2
+a\left(\frac13z^3-bz\right),
\]
it verifies
\[
L F=w^2-a v^2.
\]

It also verifies
\[
Lw+w+av+a(z^2-b)=0,
\]
the state-space form of
\[
z'''+z''+a z'+a(z^2-b)=0.
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificates. The phase classification additionally uses support invariance, and the strict period proof uses the classical equality case of Wirtinger's inequality.
