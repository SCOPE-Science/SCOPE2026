---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is analytic and valid for arbitrary positive shore sizes. The critical steps checked independently are:

1. For \(m,n\ge2\), a set in \(K_{m,n}\) is locating-dominating exactly when it omits at most one vertex from each shore.
2. The three-block construction works for every star of order at least three and every nonstar biclique with a shore of size at least three.
3. The all-singleton partition gives four blocks for \(K_{2,2}\).
4. In any hypothetical four-block partition, choosing one coalition pair forces the two remaining blocks to be opposite-shore singletons; following the required partner of each singleton forces \(K_{2,2}\).
5. \(K_2\) has no LDC-partition because each singleton is already an LD-set.

`verify.py` exhaustively enumerates all set partitions for \(1\le m\le n\) and \(m+n\le9\), recomputes the LD predicate from graph adjacency, and confirms the claimed coalition number or no-partition status. It also checks the explicit constructions for all \(1\le m\le n\le40\). The finite enumeration is not used to infer the infinite theorem.
