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
The checker enumerates edge subsets of small complete bipartite graphs.

For each edge subset, it computes the maximum matching size by dynamic programming. Independently, it checks whether some \(r\)-by-\(r\) row-column block contains the full support of a permutation monomial. These predicates agree exactly, reproducing the coordinate criterion for determinant and permanent restrictions.

The checker groups admissible subsets by edge count, verifies the bound
\[
|E|\le(r-1)n,
\]
and, for \(r=2\) with at least two selected edges, verifies
\[
B_{m,n,2}(q)=m\binom nq+n\binom mq.
\]

These finite checks are regression evidence only. The theorem for arbitrary parameters is proved by the published fixed-point classification together with algebraic \(\mathbb C^*\)-localization in `RESULT.md`.
