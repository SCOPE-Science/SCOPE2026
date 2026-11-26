---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At the boundary i,i+1 the change in excedance count is [π_{i+1}=i+1]−[π_i=i+1]. Since entries are distinct, legality excludes that value in both slots, so no moved value changes excedance status. For any top set T⊆{2,…,n}, the canonical word lists T increasingly and its complement increasingly. The j-th top is ≥j+1 and the j-th complement value is ≤|T|+j, so the canonical word realizes T. Sorting in this order is legal: an adjacent inverted pair within T has both entries >i+1, an inverted pair in the complement has both <i+1, and a cross-block inversion moves each entry away from its threshold. This proves connectivity and the two-sort bound n(n−1). For T={2,…,k+1}, every boundary of the canonical word contains its forbidden value; hence that word is isolated and its fiber is a singleton. Otherwise the first top t_j>j+1 can be swapped with the next top or with 1 if j=k, so its connected fiber is nontrivial. For the edge count, the two forbidden events at each boundary are disjoint. Deleting a fixed point removes its row and column with all other strict excedance comparisons unchanged. Deleting π_i=i+1 removes row i and column i+1; the remaining rows before i and after i keep the same comparison signs, including at surviving column i and row i+1. Thus the counts of blocked incidences are A(n−1,k) and A(n−1,k−1) per boundary; subtraction and division by two gives the result. This also covers k=0, k=n−1 and n=2 under the stated convention. The frozen scripts were inspected but not executed. A separate bounded breadth-first search using the strict top-set test found distance 8 and 31 reachable vertices in the illustrative n=5 fiber {4,5}; the unrestricted relative permutation has 6 inversions.

## originality

PASS

The distinct claim is the top-value component classification for strict fixed-excedance strata of all permutations under consecutive-position swaps, including its isolates and edge formula. Value-side excedance statistics, fiber enumeration under inverse/reflection, and the closely related side-signature bubble-sort method are not claimed as new. The strongest same-day forbidden-fixed-point record uses the same sorting idea but a different vertex constraint and threshold; its theorem does not give this move rule, classification, or edge statistic.

## value

PASS

A classical statistic defines a natural subgraph of the permutahedron. The theorem gives complete reachability information in all strata via a simple conserved set, an explicit path construction, and exact isolation and edge counts. These answer structural questions not resolved by the classical Eulerian enumeration of vertices alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
