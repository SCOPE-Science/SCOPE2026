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

The verification is analytic.

For a harmonic map \(f=h+\overline g\), put
\[
a=|h'|,
\qquad
b=|g'|.
\]
The two singular values of \(Df\) are \(a+b\) and \(a-b\). The distortion condition \(b/a\le(K-1)/(K+1)\) gives
\[
(a-b)^2
\ge
\frac2{K^2+1}(a^2+b^2).
\]

For any harmonic vector map \(F\), direct differentiation verifies
\[
\Delta\sqrt{|F|^2+c}
=
\frac{|DF|_F^2}{\sqrt{|F|^2+c}}
-
\frac{|DF^TF|^2}{(|F|^2+c)^{3/2}}.
\]
Applying this identity to the regularized modulus of \(f\) and to the regularized Euclidean norm of \((h,g)\) gives
\[
\Delta U_\varepsilon
\ge
\frac1{\sqrt2(K^2+1)}\Delta V_\varepsilon.
\]
Green's radial-mean identity then yields
\[
M_1(r,|h|+|g|)
\le
2(K^2+1)M_1(r,|f|).
\]
The equality of center terms in the limiting Green identity uses exactly \(g(0)=0\).

This proves \(h,g\in H^1\), so the radial boundary values converge in \(L^1\). The classical analytic Gabriel inequality with sharp constant \(2\), applied to each component, gives the final convex-curve bound.

No numerical computation, finite enumeration, or unproved limiting interchange is used.
