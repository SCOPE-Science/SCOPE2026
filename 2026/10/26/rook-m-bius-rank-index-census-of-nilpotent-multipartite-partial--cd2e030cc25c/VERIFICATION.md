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

For k >= 3 and all part sizes positive, pairwise distance preservation is exactly preservation of the equivalence of belonging to the same part. This gives a unique partial injection of represented source parts, even for parts represented by one vertex. Nilpotence removes all vertex cycles; the longest chain in vertices is the index, including index 1 for the empty map. For fixed potential part action, the ordered color words enumerate directed labeled chains, isolated vertices included, and rank is the sum of their lengths minus one per chain. The multivariate exponential counts unordered collections of those chains on the fixed labeled parts. For an actual part action theta, the weight of all extensions sums to 1: write each mu as the signed sum over further extensions, then for each final extension the intermediate maps form a Boolean interval whose sum vanishes unless it equals theta. Differences in successive L therefore give the claimed joint polynomial. Under the stated restriction n_i >= 2 a longest chain repeats a part (two rounds over all parts are feasible). A repeat forces a periodic color word starting on its cycle, since a tail into a cycle would violate part-injectivity. If the smallest capacity on that cycle is s, at most s full rounds plus a prefix of larger parts are feasible; ordering all parts of size >= s with the larger ones first attains s c_s + c_(s+1). A spanning chain visits all parts with counts differing by at most one. Ordering the large and small blocks within the first period and then assigning labeled vertices gives exactly h!(k-h)! times the product of the part factorials, with no rotation factor because the chain has a distinguished start. Independent enumeration gave totals 835 and 3,089, maximum indices 6 and 7, and 48 maps of maximum index in each three-part test.

## originality

PASS

The supported distinct contribution is the all-index joint census for k >= 3 and the sharp maximum formula also in the unbalanced, nonspanning regime. The bipartite census and all-partite index-at-most-two slice are credited separately. The later catalogue result for disjoint unions of cliques explicitly covers the same spanning criterion and multiplicity after complementation; it does not cover the full distribution or the nonspanning maximum. No historical exclusivity is asserted for the spanning subresult.

## value

PASS

The joint invariant measures two natural and different aspects of the monoid: the domain size and the iteration time to zero. The part-action formula enumerates it without looping over all vertex partial injections, and the capacity formula gives a sharp answer even when imbalance prevents spanning. These are useful extensions beyond the already known two-part and square-zero boundaries rather than new presentations of those counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
