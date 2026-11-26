---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Inducing on shore sizes a,b gives K_{a,b} minus a matching of size t. For both sides of size at least two with one of size at least three, any two vertices on the shore opposite the larger shore have a common neighbor, and each vertex on the larger shore meets the other. When both sizes are two, only t=2 disconnects. For t>0 and a<=b, a right vertex has degree a-1; deleting at most a-2 vertices leaves both sizes at least two and, when a>=3, at least b+2>=5 vertices, giving the matching lower bound. For t=0 the connectivity is min(a,b). Sizes below k cannot meet the connectivity requirement, and with k>=2 there is automatic domination since every unselected vertex misses at most one selected vertex on the opposite shore. The qualifying side-size regimes give the independent large-shore polynomial and the two disjoint-shore terms, subtracting the double-count of (k,k). Minima have side sizes (k,k) and disjoint indices if n>=2k, else independently chosen (k+1,k+1). In the latter regime a shore-changing jump would need disjoint sets of combined size 2k+2>n, so precisely the Johnson-product edges remain (including singleton factors). In the former regime moves exchange a colored token with one of n-2k empty indices. No empty index means isolated vertices; otherwise holes can be repositioned and any two occupied colors can be swapped in three moves returning one hole to its position. Each of 2k tokens has exactly n-2k distinct neighbors by its choice of destination. These arguments verify all parameters, including endpoints n=3 and k=n-1, without relying on finite checks.

## originality

PASS

The ordinary induced-connectivity lemma is known and an earlier Resultary finding classifies the same disjoint (2,2) state family and count, under a different move rule. The contribution that passes is the all-k robust bivariate census and the classification of its minimum-state token-jumping graph, not the ordinary lemma or the overlapping k=2 count alone.

## value

PASS

This combines a complete two-shore selection census with an exact change from one connected class to many isolated optima at n=2k and back to a connected space above threshold. It explains rigid optimality through the absence of a spare index and gives a constructive reachability argument when one exists, an exact distinction that counts or ordinary connectedness alone do not provide.

The dated certificate retains the supplied scientific assessment, sources and limitations.
