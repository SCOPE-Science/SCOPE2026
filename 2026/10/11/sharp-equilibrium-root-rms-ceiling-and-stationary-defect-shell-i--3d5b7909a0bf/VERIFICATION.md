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
The packaged `verify.py` uses only the Python standard library.

It verifies the pointwise identity
\[
\frac{d}{dt}
\left(
\frac{x^2}{\sigma}+y^2+z^2
\right)
=
2(1+r)xy-2x^2-2y^2-2z^2+2cy.
\]

It checks the exact stationary conversion to
\[
\operatorname{Var}(z)
+
\mathbb E\!\left[\left(\frac{\dot x}{\sigma}\right)^2\right]
=
h(r-1-h)+cm.
\]

It also checks both orthogonal-residual variance decompositions and uses deterministic bisection for the source example
\[
(r,c)=(2000,1500)
\]
to verify
\[
\xi_+\approx45.0807456556,
\qquad
\xi_+^2\approx2032.2736288672.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identifications, positive-root uniqueness, equality rigidity, and recurrence classification of zero speed defect are analytic arguments in `RESULT.md`; no finite trajectory experiment is used as proof.
