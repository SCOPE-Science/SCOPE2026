---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: In R_{m,n} a currently blue rook cell (i,j) has exactly degree_H(row_i)+degree_H(col_j) white neighbors. Existence of a first move iff an isolate on one side and degree-one opposite side. Any white bipartite cycle cannot have its first edge forced, so success requires acyclic H. After the first leaf force a row and column are isolated, and every remaining nonempty forest has a leaf which can be paired with opposite isolate; induction forces all white edges. Component EGF correctly uses p^(q-1)q^(p-1) bipartite trees and surjective-word Stirling counts of no-row/no-column-leaf cases. Two-sort exponential formula counts all eligible forests. Minimum sets arise from one isolate plus a spanning tree with an opposite-color leaf, yielding the stated Stirling expression; m=n=1 and min(m,n)=1 treated separately. Independent direct ZF simulation matches forest criterion for 1x1,2x3,3x3,4x4 (65,536 colorings at 4x4), including polynomial white-edge profiles.

## originality

PASS

PASS best-of-knowledge: Montazeri–Soltankhah 2021 Theorem 2.1 supplies F_k(K_m square K_n)=mn-k(m+n)+k^2+k, so its k=1 minimum Z is prior, but it does not count all successful sets or their complete polynomial. Boyer 2018 gives generic highest polynomial coefficients but cannot determine all coefficients of growing rook boards. Resultary searches and other line-graph literature did not identify the submitted exact forest-isolate-leaf criterion, component EGF or general minimum-set multiplicity. Residual risk of analogous line-graph forest formulations is acknowledged.

## value

PASS

PASS: A natural complete classification of all ordinary zero forcing sets on every rectangular rook graph, plus the exact all-coefficient polynomial and labeled minimum-set count. These are graph-theoretically and enumeratively useful refinements of a previously known minimum forcing cardinality, not arbitrary tiny cases or algorithm-only assertions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
