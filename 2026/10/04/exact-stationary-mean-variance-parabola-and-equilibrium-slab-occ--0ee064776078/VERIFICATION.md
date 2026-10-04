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
\dot x=a y+z,\qquad
\dot y=-x+y^2,\qquad
\dot z=x+b y,
\]
it verifies
\[
L(y+z)=y(y+b)
\]
and the exact completion of the square
\[
y(y+b)=\left(y+\frac b2\right)^2-\frac{b^2}{4}.
\]

It also substitutes the two symbolic equilibria
\[
(0,0,0),\qquad (b^2,-b,ab)
\]
into all three components and verifies zero residuals, then checks the original parameters \(a=27/10\), \(b=1\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificate. Conditional expectations require arbitrary test functions, Jensen's inequality is used for the parameter range, and the slab-rigidity conclusion uses invariance and continuity of the compact support.
