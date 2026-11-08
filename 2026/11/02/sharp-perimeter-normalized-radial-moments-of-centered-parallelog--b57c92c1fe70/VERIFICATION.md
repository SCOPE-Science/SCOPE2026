---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For centered parallelogram conv{±u±v}, lengths a,b and angle cosine c, exact boundary parameterization yields F_p(c)=2b∫_-1^1(a²+b²t²+2abct)^(p/2)dt +2a∫_-1^1(b²+a²t²+2abct)^(p/2)dt. Evenness and strict convexity in c for p>2 give sharp degenerate endpoint F_p(1)=4(a+b)^(p+1)/(p+1); p<2 gives orthogonal angular maximum and p=2 angle-independent L³/48. Comparing with disk L^(p+1)/(2π)^p establishes unique cutoff (π/2)^p=p+1 at p≈3.1529558562. Curvature lower bound for 2<p<=4 gives angular stability and exact quartic I4=L^5/1280 - L A²/12. All nondegenerate p>2 cases have strict inequality to the supremum; no general convex-curve p=3 theorem is claimed.

## originality

PASS

Second-moment parallelogram identity was known (Sachs, as recalled in Csató-Giovagnoli-Roy). Dietze-Kachmar-Lotoreichik raise the general p=3 conjecture and show high-p failure using limiting segments, but not the complete family-specific p cutoff and sharp angular/area formula.

## value

PASS

Exact all-exponent disk-comparison threshold within a geometric test family sharpens the open broad p=3 boundary inequality without claiming to settle it. The quartic area deficit and angular extremizer reversal expose natural geometric shape sensitivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
