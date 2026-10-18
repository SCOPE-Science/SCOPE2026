---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Total domination in KG(n,2) is equivalent to absence of 2-vertex covers in the selected edge-family graph. Vertices of degree >=3 are forced into every 2-cover and hence 0/1/2 hubs give disjoint exhaustive obstruction classes C_n,H_n,Q_n. Directly checked the 0-hub component types, 1-hub residual 0/1/2 edges, and 2-hub multinomial categories. For k>=n+1 any 2-covered graph has two degree>=3 hubs giving a unique 2-cover and binomial high-cardinality failure count. Independent enumeration of all 2^10 Petersen and 2^15 KG(6,2) edge subsets matched coefficients and endpoint formulas. All n>=5 follows analytic hub classification.

## originality

PASS

Explicit full-primary-text comparison finds complete prior Petersen n=5 polynomial and topmost regular-graph coefficients, which the reviewed result credits. For n>=6, the complete labeled all-degree polynomial and interior unique-two-cover band are stronger than the minimum/cutoff cases; the known blocking-set equivalence alone does not enumerate all hub configurations.

## value

PASS

The complete cardinality distribution of total-dominating edge families in every KG(n,2), n>=6, genuinely refines both the known minimum and the Petersen full table. The interior unique-two-cover band and 0/1/2 hub structure provide a reusable exact counting mechanism rather than a mere table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
