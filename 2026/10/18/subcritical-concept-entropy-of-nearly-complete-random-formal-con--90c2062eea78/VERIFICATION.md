---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

A concept (A,B) corresponds bijectively to a maximal independent set A union B in the bipartite complement, even when either side is empty, and m multiplies over components. For a fixed side-coloured tree with a+b=v vertices and colour-preserving automorphism group u, exact labelled component expectation is (n)_a(n)_b/u*(c/n)^(v-1)*(1-c/n)^(nv-ab-v+1); isolated left/right trees yield e^-c. Disjoint-embedding covariance is O(1/n), fixed type fluctuations O(n), so type counts/n converge L2. Every fixed cyclic component count is O(1) in expectation; a Poisson(d) with c<d<1 dominates binomial exploration for large n, providing exponential total-progeny tail and uniform large-component weighted bound <=2 log2 Ae^-eta K. Thus fixed-K L1 convergence passes to full series, establishing absolute convergence and L1/probability without mistaking expected C for log C. For v=2,3,4, side-coloured tree types give c e^-2c log2 + c²e^-3c log2 + c³e^-4c(log3+log2/3); expansion matches displayed cubic. Rooted (selected,already dominated,needs parent) DP m(T)=A+B is correct. Tested source verifier logic against mathematical definitions; unrestricted limit derives from analytic argument rather than enumeration.

## originality

PASS

Semantic FCA graph correspondence is classical; component count and subcritical branching methods are standard. The assessed new mathematical statement is the quenched L1 limit and explicit coloured-tree entropy series/cubic law in nearly-complete independent-incidence contexts. Sakurai addresses expectation of concept counts in another regime; Felde/Hanika/Stumme treat generation/null models; Drmota et al enumerate maximal independent sets of uniformly sampled trees and other classes rather than logarithmic MIS counts in sparse balanced binomial bipartite graphs. Possible pre-existing general random-graph additive-component-functional law could imply the limit, so retain substantive priority caution rather than asserting exhaustive novelty.

## value

PASS

Natural high-density FCA question: typical concept number can still grow exponentially. Exact L1 rate, effective convergent series, positive lower bound and low-density expansion identify the subcritical quantitative regime. The normalization (per n, not per 2n) and inclusion of empty extents/intents are essential useful boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
