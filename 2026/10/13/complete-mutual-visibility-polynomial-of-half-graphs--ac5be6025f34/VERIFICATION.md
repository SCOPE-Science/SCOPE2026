---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For selected A,B in the half graph H_n (a_i adjacent to b_j iff i<=j), when both sides nonempty let q=max A, p=min B. If q<p all mixed pairs adjacent and boundary omitted witnesses cover same-side pairs; if q>p the opposite extreme pair needs both an omitted A index <=p and omitted B index >=q, sufficient for every selected pair. If q=p, precisely two all-prefix/all-suffix obstructions require inclusion-exclusion. Counting boundary cases independently gives the stated F_{q,p} terms; substituting z=1 and finite geometric arithmetic sums gives (4^(n+1)+24n-13)/9. Top coefficient one follows extremal witness. Independent definition-based shortest-path BFS enumerated all sets for n=3,4,5,6, with totals 35,123,467,1835 matching polynomial; this finite check supports the all-n proof.

## originality

PASS

The complete bipartite-graph visibility polynomial formula in Bujtás–Klavžar–Tian Proposition 3.2 is for K_{n,n}; its geodesic structure differs from nested-neighborhood half graphs. The half-graph maximum 2n−2 and uniqueness is conceded prior. No inspected primary source or relevant published Resultary record gives the complete half-graph all-cardinality coefficients or total-set formula. Any unindexed chain-graph enumerator remains a reasonable risk.

## value

PASS

Mutual-visibility sets are a natural graph-geodesic invariant, and the all-cardinality polynomial refines a previously known maximum for an important canonical chain graph. The boundary-index decomposition enables exact counting, size distributions, and nontrivial total counts; it is not a rephrasing of the maximum or a substitution into the complete-bipartite result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
