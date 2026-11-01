---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For planar f(x)=(a x1^2+b x2^2)/2 with a,b,h>0, the forward-difference gradient has exact curvature bias (h/2)u^THu, while the second difference returns u^THu. Under z=H^(1/2)x and v=H^(1/2)u/||H^(1/2)u|| the update is z+=(I-vv^T)z-(h/2)H^(1/2)u. Synchronous coupling contracts expected squared norm by 1-lambda_min(E[vv^T])<1; the stationary law and second moments therefore exist uniquely. Sign symmetry kills cross terms and off-diagonal stationary covariance. Independent angular quadrature verifies m=E[v1^2]=sqrt(a)/(sqrt(a)+sqrt(b)), beta=E[v1^2 v2^2]=sqrt(ab)/(2(sqrt(a)+sqrt(b))^2), giving invertible covariance system determinant 3beta. Solution yields stated Haar covariance h² diag((3a+b+2sqrt(ab))/a,(a+3b+2sqrt(ab))/b)/24 and coordinate covariance h² I/4. Thus errors h²(a+b+sqrt(ab))/12 and h²(a+b)/8 differ by h²(sqrt(a)-sqrt(b))²/24. The one-step optimizer boundary gives equal expected error h²(a+b)/16, so the limit claim is not a transient domination statement.

## originality

PASS

The update mechanism is from Berglund–Khirirat–Wang and random-direction zeroth-order optimization is classical. The complete exact stationary covariance under the two specific sketch laws and perfect-square anisotropy gap are not determined by the checked general error bounds, first-order alternatives or exact-gradient RSN. Best-of-knowledge original restricted quantitative comparison.

## value

PASS

The exact fixed-radius stationary error of a practical derivative-free Newton sketch is a natural optimization invariant. The two canonical sketch laws have the same per-step query count and the same one-step optimizer error but different sharp long-run risks. The perfect-square anisotropy gap gives a precise, experimentally testable policy contrast, while the opposing transient contraction factors expose a genuine tradeoff. This adds quantitative content beyond generic O(h²) neighborhoods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
