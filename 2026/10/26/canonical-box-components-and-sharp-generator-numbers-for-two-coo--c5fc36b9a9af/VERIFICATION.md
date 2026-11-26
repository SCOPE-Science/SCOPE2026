---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The implication stays in a box and cannot cross boxes at distance at least three. A new symbol in just one coordinate can be propagated over the base box one distance-one step at a time: the new-symbol word at the old base and the old-symbol word at the next base are the two distance-two premises. For a point at distance two, the first rectangle supplies the two one-symbol extensions, after which both can be absorbed. Traversing a distance-one spanning tree in the second box extends this to the box merge. The resulting greedy process stays in the actual closure and terminates in a closed cover of the seed, so it yields the closure for any merge order. For a closed set the distance-one components are precisely the boxes; the merge lemma rules out components at distance two. This includes the empty union. Coordinate coverage forces k≥1+M, and for a merge the rank Σ(|Bᵢ|−1) increases over the sum of the two ranks by Σ(1−|Bᵢ∩Dᵢ|)≤2, proving the other lower bound. For attainment, if the largest symbol class dominates, pair each other token with a distinct token of that class. Otherwise pair from two largest classes: with n tokens and each class at most ceil(n/2), any class attaining that cap must be among the two selected, so after removal the new cap ceil((n−2)/2) is maintained. The construction yields max(M,ceil(T/2)) groups. With the common base word, the group words generate all one-change words and then all words by the rectangle rule and induction on support. In dimension one this gives exactly q₁, consistent with there being no triggers.

## originality

PASS

The structural recursion has a strong antecedent in ordinary P₃ convexity: connected hulls factor and nearby subproducts can merge, and in the binary case the two rules coincide. The supported distinct result is the exact induced-P₃ structure with arbitrary coordinate symbol subsets and its sharp heterogeneous generator count. Ordinary P₃ hulls fill an entire clique fibre as soon as there are two symbols in it; that operation is unavailable for induced P₃. The known geodesic result has a different closure and generator count in general.

## value

PASS

Separated product components are a canonical description of the actual implication closure, making the box-merge algorithm exact rather than just an upper bound. The minimum generator formula distinguishes a single large alphabet's supply constraint from the total two-symbol growth budget. Those are natural structural features not detected by the established dimension-only ordinary-P₃ result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
