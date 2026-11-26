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

Independently verified without needing the cited sharp cutoff for cycles. After the first move on cycles of size at least 16, use a private cyclic orientation to maintain that each gap between consecutive pebbled sites is either equal on the two cycles or is at least 2^(r+1) on each, where r rounds remain. A repeat is matched exactly; a new vertex splits a gap. Equal gaps may be split identically, and for a large gap one matches a side shorter than 2^r if there is one, or splits into two gaps of at least 2^r. With no moves left the gap-1 incidences and equality are preserved, including the two-pebble wraparound case. Coordinatewise replies preserve equality and Cartesian adjacency in the products, so 105 unordered pairs with dimensions 3 through 16 suffice. The independent computation fixes the first move using transitivity and uses three disjoint vertex bitsets per pebble (equal, adjacent, otherwise). It records all nonempty intersections for fourth-move patterns, retaining sets of rooted extension types at ranks up the game tree without multiplicities. This is precisely the back-and-forth criterion, not a heuristic invariant. It found the asserted 19-class partition and largest least representative (64, 8, 8), and also distinguished C8 from C11. Any noncanonical smaller representative would truncate to one no larger, so sharpness holds throughout the family.

## originality

PASS

Supported distinct claim: the exact rank-four partition of the unmarked two-cycle Cartesian-product family, including its sharp least-representative ceiling of 64. The plausible indexed comparisons change the rank or graph family; the cycle cutoff and coordinatewise preservation provide an upper reduction but do not determine the strict quotient partition. No equivalent exact table or dominating implication was found in the bounded review.

## value

PASS

The natural class of toroidal grids has an exact finite set of logical theories at a specified rank. In particular the merger threshold 8 for the large product class, despite rank-four distinctions between some factor cycles of those sizes, shows why the exact table is not just the known factor cutoff. The table gives a precise sharp representative-size result useful for testing rank-four statements in this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
