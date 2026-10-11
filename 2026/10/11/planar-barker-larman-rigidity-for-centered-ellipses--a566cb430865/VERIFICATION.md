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
# Verification

For
\[
E_A=\{x:x^{\mathsf T}Ax\le1\}
\]
and the tangent line
\[
H_e=\{x:e\cdot x=r\},
\]
write \(x=re+tv\), where \((e,v)\) is orthonormal. The boundary equation is
\[
\alpha t^2+2r\eta t+r^2\gamma-1=0,
\]
with
\[
\alpha=v^{\mathsf T}Av,
\quad
\eta=e^{\mathsf T}Av,
\quad
\gamma=e^{\mathsf T}Ae.
\]
Because the determinant is unchanged by the orthonormal basis change,
\[
\alpha\gamma-\eta^2=\det A.
\]
The root separation is therefore
\[
L_A(e)=2\sqrt{\alpha-r^2\det A}/\alpha.
\]

The bundled `verify.py` uses exact multivariate polynomial dictionaries with rational coefficients. It verifies two algebraic certificates:

1. Cross-multiplying the two chord formulas is exactly equivalent to the homogeneous sextic
\[
P=\alpha\beta(\beta-\alpha)+r^2s(E\alpha^2-D\beta^2).
\]

2. Under the only possible noncircular factor-divisibility alternative \(\beta=k\alpha\), one has exactly
\[
P=k(k-1)\alpha^3.
\]
Thus the polynomial identity forces \(k=1\).

The checker also re-evaluates direct quadratic intersections for several rational positive-definite matrices. These finite cases are supplementary regression tests only; the proof of the universal claim is the exact factor argument in `RESULT.md`.
