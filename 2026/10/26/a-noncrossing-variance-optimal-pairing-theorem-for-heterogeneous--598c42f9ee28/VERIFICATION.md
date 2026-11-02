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

For an independent disjoint two-person pool {i,j}, its count is 1+2B_ij with B_ij Bernoulli(1-q_i q_j); disjoint pools are independent, so Var(total)=4 sum f(q_i q_j), f(t)=t(1-t). For a>=b>=c>=d, direct symbolic expansion independently confirmed sep-cross=(a-d)(b-c)[1-(a+d)(b+c)] and cross-nest=(a-b)(c-d)[1-(a+b)(c+d)]. The bracket thresholds are ordered by (a-c)(b-d)>=0, guaranteeing at least one non-increasing uncrossing; minimizing total index spans, then maximizing squared spans rules out crossings even in equality cases. The Catalan interval DP follows by splitting across the partner of the first index; O(m^3) time and O(m^2) memory. A separate exact Fraction enumeration of all 15 six-person matchings confirmed the unique optimum f sum 144/343, neither adjacent nor extreme. This is an all-m, all-interior-q proof; finite tests are not its logical basis.

## originality

PASS

The noncrossing variance theorem is not established by the inspected informative-Dorfman or optimal heterogeneous-group screening results, which optimize expected tests and possibly group size, rather than the fixed-size-two assay-count variance. The weight q_i q_j(1-q_i q_j) changes Monge sign, so ordinary homogeneous-side assortative rules cannot substitute for the two-alternative four-point argument. Best-of-knowledge PASS, with limited earlier full-text access explicitly qualified.

## value

PASS

The size-two perfect-pool constraint is essential: unrestricted individual tests have zero assay-count variance. Within that motivated screening-risk model, the noncrossing theorem reduces exponentially many pairings to an exact cubic-time optimizer despite mixed low/high risks. The six-person optimum disproves the simple adjacent-versus-opposite choice. This is structural information, not merely a routine calculation of moments or a recommendation for clinical testing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
