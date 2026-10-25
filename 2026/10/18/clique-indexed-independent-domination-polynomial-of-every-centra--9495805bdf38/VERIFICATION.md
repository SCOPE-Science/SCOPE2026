---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Reconstructed the entire-set bijection: independent original vertices form a clique A of G; subdivision vertices are forced exactly for edges disjoint from A; an omitted original vertex v is undominated exactly if N_G(v)=A. Thus admissible cliques index all maximal independent sets, with exponent |A|+m-sum_A degree+binom(|A|,2). The n=1 and K_n boundary cases, empty clique, isolated vertices, and degree-count normalization are consistent. Independent direct graph construction and independent-domination subset enumeration matched the formula for every labeled simple graph on n<=4 (75 graphs). Finite checks corroborate, not prove, the arbitrary-graph bijection.

## originality

PASS

Best-of-knowledge PASS for the complete cardinality-generating polynomial on arbitrary simple base graphs, rather than only minimum independent domination numbers. The 2026 prior Theorem 2.1 contains a closely related minimizing clique construction and P_G(A) obstruction, so the new all-set enumeration is a natural but non-identical strengthening; its structural ingredients are explicitly credited.

## value

PASS

The independent-domination polynomial is a natural invariant recording all minimal-independent dominating sets, distinct from the previously known minimum. A closed clique-indexed formula for arbitrary central graphs and bounded clique-number polynomial algorithm allow extraction of all sizes and optimum multiplicities; counting minimal sets is independently useful even if underlying structural reasoning is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
