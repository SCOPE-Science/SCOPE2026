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

The claim was checked directly from the definition of a positive square point.

1. In finite dimension, approximate goodness is equivalent to an exact norming witness by compactness of the unit sphere.
2. For \(f=(a_i)\in S_{\ell_1^n}\), every norming point of the cube satisfies \(y_i=\operatorname{sgn}(a_i)\) whenever \(a_i\ne0\), while zero-coefficient coordinates are free.
3. For \(x\in\{-1,0,1\}^n\setminus\{0\}\), the condition \(f(x)\ge0\) prevents all nonzero coefficients on the saturated support from having the opposite sign; a zero coefficient on that support is itself enough to choose an exact distance-two witness.
4. If \(0<|x_j|<1\), choose \(0<\delta<|x_j|/(1+|x_j|)\), put total opposite-sign mass \(\delta\) on the saturated coordinates, and put mass \(1-\delta\) with the sign of \(x_j\) on coordinate \(j\). The resulting functional has norm one and positive value on \(x\), but every norming vector cancels all saturated coordinates. Hence exact distance two is impossible.
5. The two cases exhaust the sphere, proving the coordinate classification. The cube-face-center interpretation is immediate because a proper face is obtained by fixing a nonempty subset of coordinates to signs; its center has those coordinates equal to the fixed signs and all remaining coordinates equal to zero.

No numerical experiment, finite search, or external certificate is needed for the proof. The result is limited to finite-dimensional real \(\ell_\infty^n\); no infinite-dimensional analogue is asserted.
