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
\dot y=x-\lambda y-xz,\qquad
\dot z=x^2-\alpha z,
\]
it verifies
\[
Lz=x^2-\alpha z,
\]
\[
L\left(\frac{x^2}{2}\right)=xy,
\]
and
\[
L(xy)=y^2+x^2(1-z)-\lambda xy.
\]

It also verifies the origin equilibrium and, symbolically under
\[
y=0,\qquad z=1,\qquad x^2=\alpha,
\]
the two nonzero equilibrium branches.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The exact conditional law is an analytic consequence of applying the verified \(Lz\) identity to arbitrary antiderivative test functions of \(z\). The support-positivity statement uses the exact variation-of-constants formula and is not a finite experiment.
