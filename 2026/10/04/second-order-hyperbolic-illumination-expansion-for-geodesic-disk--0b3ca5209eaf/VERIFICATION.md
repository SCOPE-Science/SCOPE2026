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

The analytic verification starts from the exact hyperbolic right-triangle identities
\[
\cos\alpha=\frac{\tanh r}{\tanh(r+\varepsilon)},
\qquad
\cos\gamma=\frac{\sinh r}{\sinh(r+\varepsilon)},
\]
and the exact added-cap area
\[
\delta(\varepsilon)=2\gamma-2\cosh r\,\alpha.
\]
Expanding those identities through \(O_r(\varepsilon^{7/2})\) gives
\[
\delta(\varepsilon)=\frac{2\sqrt{2\tanh r}}{3}\varepsilon^{3/2}
-\frac{\sqrt2((\tanh r)^2+3)}{10\sqrt{\tanh r}}\varepsilon^{5/2}
+O_r(\varepsilon^{7/2}).
\]
Series inversion and the exact formula \(\operatorname{area}(B_s)=2\pi(\cosh s-1)\) then give the claimed two-term illumination-area expansion.

A separate normalization check substitutes the geodesic-circle curvature \(\coth r\) and boundary length \(2\pi\sinh r\) into the published leading-order floating-area formula and recovers the stated \(C_1(r)\) exactly.

`verify.py` performs floating-point consistency checks at \(r\in\{0.3,1,2\}\) and two shrinking radius increments. Its role is limited to detecting transcription or algebraic-sign errors in the packaged formulas; finite numerical checks do not establish the universal asymptotic statement.
