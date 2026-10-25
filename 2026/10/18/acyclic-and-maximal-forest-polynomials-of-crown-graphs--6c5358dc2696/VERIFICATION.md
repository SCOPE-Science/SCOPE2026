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

For H_n=K_{n,n} minus identity matching (n>=3), an induced selection with side sizes a,b and matched overlap t has ab-t edges. Forest edge bound (a-1)(b-1)<=t<=min(a,b) confines cases with a,b>=2 to (2,2,t>=1), (2,3,t=2), (3,2,t=2), each verified acyclic (no 4-cycle or is a 5-vertex path); cases min(a,b)<=1 are stars plus isolates. Counting these disjoint cases establishes the stated full bivariate polynomial F_n. One-vertex extension proves facets exactly (1,n),(n,1) for n>=4 and (2,3,t=2),(3,2,t=2), with latter alone when n=3. Thus sizes 5,n+1, pure iff n=3,4, gaps 6..n when n>=6; complement facets yield minimal-feedback-vertex polynomial and min size n-1. Independent enumerator checked all subset masks and insertion-maximality for n=3..7, matching formula. The all-n proof is structural, not inferred from finite enumeration.

## originality

PASS

Existing induced-acyclic graph polynomials give general operations on disjoint unions and actual graph joins; K_nn minus a perfect matching is neither one of those constructions nor ordinary K_nn. The well-f-covered complete-bipartite classification concerns a graph with the deleted edges present; K_n×K_n has n² vertices unlike the 2n-vertex crown. Existing published crown restrained domination enumerator is another invariant. Thus the exact crown bivariate face and facet formulas plus unbounded facet-size gaps are not established by the compared broader statements.

## value

PASS

The crown is a natural symmetrical bipartite graph, and complete bivariate classification of its induced forests and inclusion-maximal facets distinguishes minimal feedback vertex sets, purity and arbitrary long forbidden cardinality intervals. Exact natural-invariant formulas with structural consequences are useful despite an elementary proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
