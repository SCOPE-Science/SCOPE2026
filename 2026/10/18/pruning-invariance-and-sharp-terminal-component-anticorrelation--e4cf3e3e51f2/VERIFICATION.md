---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For ordered r-set S of indegree-zero vertices, event no arrow lands in S has probability ((n-r)/n)^n. Conditional arrows restricted to T=[n]\S remain IID uniform T, giving a uniform (n-r)-mapping and leaving all original directed cycles in T; sum over S gives exact factorial-moment identity and bivariate pgf, including vector cycle counts. E C_(n,k)=(n)_k/(k n^k) yields cycle-specific and full covariance formulas, with strict monotone in n for k>=2 and equality k=1. For monotone h, cyclic-vertex survival Pr(K_m>=j)=(m)_j/m^j is monotone in m, and given K_m=j cycle count is uniform-permutation cycle count with Bernoulli(1/i) coupling. The displayed gaussian comparison and dominated Riemann-sum show n(a_n-a_(n-1))->1/2, hence covariance->-1/(2e). Independently enumerated *all* n^n maps at n=2,3,4,5 by separate functional traversal, recovering exact covariances -1/8,-34/243,-1203/8192,-295176/1953125; independently rational-computed all n=2..10. Finite enumeration does not prove the asymptotic.

## originality

PASS

Flajolet–Odlyzko 1990 Section3.1 Theorem2 separately treats component-count and terminal-node expectations; Section3.3 concerns distributions/cycle length, but inspected formulas do not provide the joint factorial-pruning law or covariance sign/limit. Finch 2022 arXiv:2205.05579 discusses components and cycles and not indegree-zero terminal nodes in inspected relevant sections. Both are credited for marginals and classic mapping decomposition. A general earlier multivariate marking identity could imply factorial deletion and remains a genuine priority risk; Resultary semantic query returned no exact theorem among inspected top12.

## value

PASS

The joint terminal/component correlation is a natural structural statistic of uniform functional digraphs beyond classical marginals. The exact distributional pruning formula, signed entire hierarchy, fixed-point exception and sharp nonzero covariance limit are independently useful facts about dependence, not merely retabulations of the mean counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
