---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Centering gives equal positive and negative first moments \(A=D/2\). On the two sides, \(y^2\le a|y|\) and \(y^2\le b|y|\), while the endpoint masses give \(p_1a\le A\) and \(p_mb\le A\); this yields the lower constant and exact equality conditions. For the upper edge, the indicator above the mean has covariance \(A\) with the centered variable, so Cauchy--Schwarz gives the cumulative-cut ceiling; equality forces a two-level law. Collapse sequences make both bounds sharp, and connectedness fills the intervals. Fresh exact-rational replay verified the lower and upper inequalities on 1800 independent generated strict supports.

## originality

PASS

The accessible MAD literature gives general identities and universal comparisons but not the exact arbitrary fixed-profile support-shape interval. A second SCOPE record in this same assignment states the same theorem, but its import commit is eleven commits later and has the earlier record as an ancestor; it therefore cannot be prior coverage of this record. Best-of-knowledge originality passes for this earlier instance.

## value

PASS

Mean absolute deviation and standard deviation are canonical competing dispersion scales. The theorem completely quantifies how a fixed category-frequency profile constrains their ratio, including exact equality topology and simple equal-weight consequences. This is a natural exact invariant rather than a one-off numerical calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
