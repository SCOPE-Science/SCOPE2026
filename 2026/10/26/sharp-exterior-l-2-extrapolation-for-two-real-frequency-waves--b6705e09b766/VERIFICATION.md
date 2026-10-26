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

The symbolic checker `verify.py` confirms, using exact rational algebra, the identity
\[
2q_0(3-2q_0)-(1-q_0)u=\frac{u^2(20+10u-u^2)}{3600},\qquad q_0=\frac u6-\frac{u^2}{120}.
\]
It also confirms the polynomial derivative and the two-atom Gram determinant. Its finite numerical tests exercise exterior points, separated and near-colliding frequency gaps, and the explicit sharpness sequence. The proof in `RESULT.md`, not the numerical sample, covers infinitely many frequencies and all real exterior evaluation points.

The exact nonstandard step is positivity of the above polynomial on \(0<u<4\), obtained from \(20+10u-u^2>0\) there, together with the alternating sine-series bounds valid for \(0<d<2\). Single-atom and gap-zero limits are treated separately. There is no independent audit or external certification recorded.
