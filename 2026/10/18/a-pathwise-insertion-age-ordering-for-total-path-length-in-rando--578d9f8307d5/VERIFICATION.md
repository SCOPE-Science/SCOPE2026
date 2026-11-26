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

Deleting the maximum contracts just the inserted node: the keys above the prefix maximum constitute its only subtree, and the depth of the inserted node is the prefix record count. This gives (1) for the empty prefix too. On moving the maximum one slot, a new record x adds one to the record count and subtracts x−R from the subtree size, proving (2). For the tail, sample the unordered set of the first t entries, then require its largest element to arrive last (probability 1/t); lowering that largest element by k is a bijection to t-subsets of {1,…,n−1−k} when its spacing from the preceding maximum is at least k+1 (sentinel zero for t=1). This gives (3), and summing gives (4). The relative-order ranks of the prefix are independent uniform ranks, independent of the set of prefix values; this gives the two factors in (5). The standard root split gives the base mean in (6). At t=n−1 there can be no positive jump; at n=2 the only gap is zero. The conditional law is under uniform insertions, not uniform tree shapes. The suggested subtraction direction in the middle of proof §Exact decrement tails (RESULT.md line 56) is reversed; (4), (6), the final subtraction and the independent tail-sum proof give the correct sign. Own replay via recursive root splitting, exhaustive base permutations for 2≤n≤8, verifies (1)–(6), with tails computed from actual path-length differences and the PGF checked as exact coefficient counts. This finite check supplements the all-n argument.

## originality

PASS

The underlying path-length representation and record laws are classical. The supported distinct contribution is the evaluated simultaneous maximum-slot comparison, including exact neighboring-gap laws and the increment PGF, not path-length enumeration generally. Neither the closest Resultary covariance/tilt result nor the inspected general literature supplies those conditional laws.

## value

PASS

A natural arrival statistic for the extreme key affects a canonical global search-cost statistic. The result orders every conditional law in one coupling and measures exactly when and by how much neighboring slots differ, including the terminal equality; this is more informative than another moment of the unconditioned path length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
