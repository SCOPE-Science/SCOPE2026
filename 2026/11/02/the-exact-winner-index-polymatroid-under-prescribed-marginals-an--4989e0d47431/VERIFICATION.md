---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

With gamma<=sum mu_i as measures and G<=Fi pointwise, maximum/winner submeasures nu_i satisfy nu_i<=mu_i and sum nu_i=gamma. Thus subset mass p(S)<=int min(g,sum_i in S f_i), a normalized increasing submodular function. The greedy pointwise splitting v_i=min(f_i,[g-sum previous f]_+) gives every Edmonds base vertex, and the full base is their convex hull by the linear support-function argument. For each feasible nu_i, the quantile coupling of residual measures (gamma-nu_i)/(1-p_i) and (mu_i-nu_i)/(1-p_i) ensures all losers <= M; atomless laws and Fi>G in distribution interior force strict <. The uniform example gives rank r_k=k-(d-1)k/d*(k/d)^(1/(d-1)) and d=2 winner range [1/4,3/4]. Independent discrete submodularity, greedy and integer atom allocations confirmed case d=3 on 3 atoms (normalized total 30, r({i})=19); general measure proof is analytic and relies on checked quantile construction.

## originality

PASS

Ansari (2026) proves the same necessary/sufficient prescribed-maximum feasibility conditions and quantile construction and is credited. Inspection of complete original arXiv HTML including Theorem 1 and construction Section 6 did not find a characterization of the full attainable winner-label marginal vector or polymatroid rank. Edmonds greedy theorem is general and credited; the new content is identifying and realizing this exact rank for a prescribed maximum coupling. Generic optimal-transport duality remains possible stronger implication but no exact matching theorem established.

## value

PASS

Attaining the maximum is a natural competing-risks/attribution statistic that is not fixed by prescribed marginals and maximum distribution. The exact attainable winner-label polytope, explicit rank function, sharp vertices and unique-winner realization solve a full natural multivariate coupling classification, not merely recompute feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
