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
`verify.py` uses exact rational arithmetic for the finite algebraic checks.

For integer refinement factors it constructs
\[
B_1(z)=\frac1{1+z},
\qquad
B_r(z)=\left(1+\frac zr\right)^{-r},
\qquad
R_r(z)=\frac{rB_r(z)-B_1(z)}{r-1},
\]
and checks the constant, linear, and quadratic Taylor coefficients \(1\), \(-1\), and \(1/2\).

For \(r=2\), it verifies the exact numerator identity and checks that the sign transition is the positive root of
\[
-z^2+4z+4=0.
\]
It also performs independent rational bisection checks of the unique sign transition for several refinement factors and confirms the comparison criterion against the exact integer-power expression.

The universal uniqueness proof and the asymptotic formula
\[
z_r=\log r+\log\log r+o(1)
\]
are analytic and appear in RESULT.md. The finite replay is corroborative only.
