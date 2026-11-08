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

PASS. Every acyclic K_{a,b} orientation has a unique alternating ordered block description, with flippable edges precisely between adjacent blocks, giving degree sum s_i s_{i+1} and the complete multinomial degree polynomial. The identity degree-(a+b-1)=sum interior(s_i-1)+sum consecutive(s_i-1)(s_{i+1}-1) shows simple iff all interior blocks have size 1. Counting even and odd block lengths yields the stated S(a,b); legal flips of simple orientations create a non-singleton interior block or collapse to two blocks. Maximum degree ab is attained only in 2- or 3-block sequences, giving 2^a+2^b-2 orientations; the poly-Bernoulli denominator gives O(n^-2) balanced sparsity. The manuscript says a nonconsecutive reversed edge has a length-two alternative path, but in a bipartite graph the requisite intermediate path has length THREE through the two intervening alternating blocks; this minor proof-path error does not change the criterion. Independent graph-mask enumeration for (a,b)=(2,2),(2,3),(3,3),(3,4),(4,4) reproduced complete degree histograms and simple-set independence.

## originality

PASS

Best-knowledge PASS for the full local degree distribution and independent simple-vertex census, not for the prior alternating-block model or single-edge flip test. Cameron et al. Theorem 4.6 already derives the fixed-edge flip criterion; Grujić Theorem 1.1 gives aggregate face counts but not a local degree distribution.

## value

PASS

PASS. Vertex valence distribution and the combinatorial count/isolation of simplicial vertices are natural, independent refinements of the polytope f-vector; the exact balanced sparsity bound quantifies their rarity without requiring a broader conjecture. Values are not merely renamed known totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
