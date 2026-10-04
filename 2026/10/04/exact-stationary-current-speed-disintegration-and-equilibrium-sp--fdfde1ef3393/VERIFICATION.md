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
The packaged `verify.py` symbolically checks the polynomial generator identities used in the proof.

For
\[
\dot x=x(y-1)-\beta z,
\qquad
\dot y=\alpha(1-x^2)-\kappa y,
\qquad
\dot z=x-\lambda z,
\]
it verifies
\[
L\left(\frac{x^2}{2}\right)
=x^2(y-1)-\beta xz,
\]
\[
L\left(\frac{z^2}{2}\right)
=xz-\lambda z^2,
\]
and the coordinate-generator identities underlying the two conditional laws.

It also verifies the exact algebraic rearrangement
\[
1+\frac{\beta\lambda Z_2}{X_2}
=
1+\frac{\beta}{\lambda}
-
\frac{\beta}{\lambda X_2}
\left(X_2-\lambda^2 Z_2\right),
\]
and the formal equilibrium relations obtained when the defect vanishes.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificates. The conditional-expectation conclusions use arbitrary one-variable test functions, and the equality classification additionally uses invariant-support tangency and bounded completeness.
