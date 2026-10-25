---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For m>=3 the anchored graph-Lipschitz constraints factor over m independent three-edge paths conditioned on pole potential h in [-3,3]. Their two-internal-coordinate area is the threefold convolution of 1_{[-1,1]}, namely A(h)=3-h² for |h|<=1 and (3-|h|)²/2 for 1<=|h|<=3; integrate A(h)^m to derive both the exact rational formula and the positive pushforward density w(x)=sqrt(2/x) on (0,2), (3-x)^-1/2 on (2,3). Strict Cauchy-Schwarz proves all moment log-convexities and increasing ratios bounded by 3. The beta integral comparison B_m isolates the positive correction; at x=2-s, the density difference is (3/4)s+O(s²), yielding exactly 3·2^m/((m+1)(m+2))+O(2^m/m³). Gamma-ratio expansion gives leading 3^m sqrt(3pi/m)(1-3/(8m)+...). Independent exact rational Ehrhart difference computation recovers m=1..4 volumes 8,88/5,1536/35,12128/105. Infinite statements rest on kernel analysis, not these finite checks.

## originality

PASS

Best-of-knowledge original final claim: compared specific mathematical statements and implications against the retrieved Resultary indexed records and relevant original primary texts; known normalizations, generic tools and special cases are not counted as new. No positive coverage result was established; inaccessible/unread alternatives remain explicit risks.

## value

PASS

The equal-arm theta graph family is a natural network and metric-space test case. The explicit complete volume moment sequence, strict growth ratios, and particularly a sharp exponentially smaller 2^m/m² correction at the cross-sectional density junction identify geometric features inaccessible from leading Laplace asymptotics. This gives reusable exact benchmarks for graph-Lipschitz ball volumes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
