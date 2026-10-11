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
The verification starts from the source equilibrium equation
\[
0=\lambda(1-A_0)y^*-A^*(\beta+\phi y^*).
\]
Solving gives
\[
A^*=\frac{\lambda(1-A_0)y^*}{\beta+\phi y^*}.
\]
Under strict positivity, \(A_0<1\) and
\[
\frac{A^*}{\lambda(1-A_0)/\phi}=\frac{\phi y^*}{\beta+\phi y^*}<1.
\]
The same substitution gives
\[
\phi A^*-\lambda(1-A_0)=-\frac{\lambda(1-A_0)\beta}{\beta+\phi y^*}<0.
\]
Thus the published coefficient \(L_1=L_2c_2\phi/(\phi A^*-\lambda(1-A_0))\) is negative when the proof's other coefficients are positive. Holding \(x=x^*\) and \(y=y^*\) yields \(V=L_1(A-A^*)^2/2<0\) for nonzero \(A-A^*\), so the displayed candidate is not positive definite.

`verify.py` checks these substitutions symbolically and exits only if the exact simplified expressions agree with the formulas above. It does not test, and this package does not claim, that the Routh–Hurwitz condition (4.15) fails or that no alternative proof of global stability exists.
