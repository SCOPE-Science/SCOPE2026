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

In connected simple homogeneous-unit endpoint-valued graphs, EF1 is automatic: any agent values at most the single edge shared with another agent. EQ1 is precisely indegree spread <=1. The integral Frank–Gyárfás orientation cut criterion requires e(S)<=(q+1)|S| and i(S)>=q|S| for q=floor(m/n). It guarantees every connected n<=6 example (tree orientation when m=n-1; q=1 cycles; q=2 dense n<=6) and all connected n=7,m<=13. At n=7,m=14 all indegrees must equal two; Hall capacity inequalities reduce to e(S)<=2|S|, violated precisely by a six-vertex subset with 13 internal edges, i.e. a degree-one vertex. Such a graph has a unique leaf and K6 core missing exactly two edges, hence 7*6*C(15,2)=4410 failures. The connected total is C(21,14)-7*C(15,14)=116175, and the exact ratio is 294/7745. Independently checked all integer counts; proof analytic over every graph in stated finite domain, not dependent on sampling.

## originality

PASS

The powerful general integer degree-bounded orientation cut criterion belongs to Frank–Gyárfás and is not claimed new. Sun–Wang–Li 2026 Proposition 4.2 exhibits EQ1 failure with weighted edges (their illustrated weights include 1/3), and their complexity theorem likewise allows nonunit values. The present sharper connected uniform-unit threshold and full first-boundary classification were not stated in inspected source sections. As a finite corollary of the general cut theorem, the result may have been previously recorded under balanced graph orientations; best-of-knowledge PASS with that residual risk.

## value

PASS

The parameter boundary is determined by a fairness-model restriction that materially changes existence (identical unit endpoint values instead of heterogeneous weights). Finding the first connected market size, minimal number of goods and all boundary obstructions is a natural complete finite classification with an exact failure frequency, not an arbitrary tiny graph counterexample or a new claim to the generic flow theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
