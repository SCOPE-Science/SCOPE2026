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
The packaged `verify.py` uses only exact sparse-polynomial and rational arithmetic.

For the real form
\[
X=c+u(xC-yS),
\qquad
Y=u(xS+yC),
\]
it verifies
\[
(X-c)^2+Y^2
=
u^2(x^2+y^2)(C^2+S^2),
\]
with \(u=u\). Therefore the trigonometric constraint
\[
C^2+S^2=1
\]
gives the exact radial identity.

At
\[
c=1,
\qquad
u=\frac9{10},
\]
it verifies exactly
\[
R=10,
\qquad
d=\frac{100}{19},
\qquad
\rho=\frac{90}{19}.
\]
It also checks coefficient-by-coefficient that the second-moment equation
\[
(1-u^2)M_2-2M_x+1=0
\]
is equivalent to
\[
M_2-2dM_x+d^2-\rho^2=0.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The support theorem, distributional pushforward, and fixed-point boundary classification are analytic arguments in `RESULT.md` and are not inferred from finite computation.
