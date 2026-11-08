---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Fixed m≥3, n→∞, hub-started genuine nonbacktracking excludes the incoming hub neighbor. Exact avoidance for s marked vertices in a petal is 1−hS=(m−s)/(m(s+1)) and 1−hN=(m−s)(m−s−1)/(m(m−1)(s+1)), confirmed independently for m=3..7. For a tagged finite set, conditional exclusion of the incoming vertex affects hazard by O(n^-2), because its preceding petal is marked with conditional probability O(n^-1); a fixed-k factorial-moment Poisson limit follows as multi-vertex same-petal hazards satisfy h(s)>h(1). Per-excursion mean length m+1 with geometric tail, maximal deviation O_p(sqrt(n log n))=o_p(n), transferring the Gumbel limit and its mean. The uniform one-site hazard gives a summable tail. Constants qS=(m+1)/(2m), qN=(m+2)/(2m), mean speedup (m+1)/(m+2). Finite checks alone do not prove the limit.

## originality

PASS

Best-of-knowledge PASS. Fixed-m windmill hub degree nm and correlated nonbacktracking excursions materially differ from classical random regular graph Gumbel results or nonbacktracking Kemeny constants. The exact petal visit and hub-memory constants are not implied by the compared results, although broader specialized cover-time priority remains to be checked.

## value

PASS

Windmill clique graph is a natural stress test for full coverage with a hub bottleneck: the two walks have equal mean excursion length but different probabilities of discovering the last rare vertices. A sharp Gumbel law with exact speedup across all fixed m≥3, requiring nontrivial dependent-excursion control, is mathematically useful, not just coupon-collector substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
