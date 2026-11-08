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

For KG(n,3) in pure graph language, after at most three EF moves three selected 3-subsets use at most nine underlying elements. For n,m>=12 Duplicator maintains the exact labeled Venn-region counts INSIDE the chosen triples and can match up to three new elements from the exterior in round four, preserving equality and disjointness; hence all n,m>=12 are rank-four equivalent. For n=6..12, enumerate EVERY eight-cell nonnegative Venn count vector obeying triple-size sums 3 and total n. For every vector, enumerate EVERY split of a new triple into eight cells to compute all realizable 4-vertex equality/edge atomic diagrams. Each resulting 3-vertex atomic profile plus its exact set of one-extension diagrams is definable by a first-order quantifier-rank-one formula with three free vertex variables; existentially closing it has rank four. Independent Python enumeration reproduced profile sizes (11,31,25,26,28,25,25) for n=6..12 and all stated directed pairwise difference counts, proving their inequivalence; P_12=P_13 also checked but is not used as infinite-tail proof. Exact seven rank-four theories and minimal last representative 220 vertices follow.

## originality

PASS

Verbitsky 2004 establishes EF graph-definability methodology for separator families, not an exact rank-four KG(n,3) classification. Harvey-Wood 2013 studies the treewidth of Kneser graphs, a graph structural parameter not an EF equivalence criterion; neither result implies finite ordered-triple one-extension profile tables. Published Resultary semantic search found no exact same rank-four Kneser theory, but search failure is not a guarantee of novelty.

## value

PASS

Exact complete first-order rank-four classification of the canonical three-subset Kneser graph family is a natural descriptive-complexity invariant, with a nontrivial finite-boundary and infinite-tail proof. The 220-vertex final class boundary is meaningful and the exhaustive certificate is mathematically motivated, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
