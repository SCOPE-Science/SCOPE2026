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

# Verification notes

The proof is analytic; the periodized inverse-Gram Green function is checked against the cyclic matrix equation and the continuous kernel absolute integral is evaluated exactly. The script `verify.py` requires only the Python standard library and outputs exact rational norms for small dimensions. It passed 1,041 checks for knot counts \(3\) through \(25\). The computed quantities are finite checks, not an infinite proof or an independent scientific assessment.

The uniform bound follows from the \(L^1\) triangle inequality applied to the periodization of the infinite Green spline. Strictness is certified by a positive-measure interval of opposite-sign translates, with separate explicit cases for odd and even knot counts. The limiting constant follows from the exponentially decaying remainder outside a central period.

Known scope limits: uniform periodic knots, continuous piecewise-affine splines, real continuous \(L^2\) projection; no claims about general knots, other spline degrees, or alternate fitting measures. A possible implicit older exact uniform-spline formula remains a literature risk.
