---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For any missing edge uv and H=P−J, H1=0 and ⟨e_u−1/n,H(e_v−1/n)⟩=−1/n imply ||H||≥1/(n−1). Equality simultaneously at every nonedge forces H(e_v−1/n)=−(e_u−1/n)/(n−1), impossible when two nonedges share v; thus complement matching necessary. For any k missing disjoint pairs and m unmatched vertices the explicitly specified P (a=1/(n−1) on allowed entries touching a matched vertex, b=(m−1)/[m(n−1)] within unmatched class when m>0) is symmetric stochastic nonnegative, and full invariant-space decomposition has spectrum {1,a,−a,0}, proving equality. Compact feasibility gives strict inequality for any nonmatching complement. Includes m=0,1 boundary cases and disconnected graphs. Independent exact rational 63 n,k cases checked; general proof is analytic.

## originality

PASS

PASS best-of-knowledge: edge-transitive perfect-matching-deleted graphs were already covered; the universal iff equality class including arbitrary partial deleted matchings was not found as an implication of inspected primary theorems.

## value

PASS

A sharp topology-wide classification of when the optimized reversible fastest-mixing rate is as good as deletion of a single edge answers a natural robustness question. Necessity, sufficiency and the sharp strict gap distinction are new structural information beyond ordinary SDP numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
