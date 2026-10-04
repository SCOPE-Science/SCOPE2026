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
`verify.py` uses exact rational polynomial arithmetic and a two-component representation of \(\mathbb Q(\sqrt3)\).

It reconstructs the four uniform-node Lagrange basis functions and verifies
\[
L_0+L_1+L_2+L_3=1.
\]
It then derives the three increment coefficients and checks the factorization
\[
1-q_1(t)=\frac{(t-2)(t-1)(2t+3)}6.
\]

The checker verifies that the lower defect is
\[
\frac{t-t^3}{6},
\]
that its derivative is \((1-3t^2)/6\), and that exact substitution of \(t=1/\sqrt3\) gives \(\sqrt3/27\). It verifies the reflection identity for the upper defect and the exact strictly increasing witness formula.

The continuous optimization over all monotone bounded data is proved analytically in RESULT.md by coefficient ordering and simplex linearity. No finite grid search is used to justify the sharp constant.
