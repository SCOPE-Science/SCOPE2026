---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For S_n every ideal (A,B) is either (A,∅), (N\{i},{i}) or (N,B), B nonempty. Compute rowmotion from minimal missing elements: explicit single 3-cycle, n disjoint 5-cycles, and paired complementary subsets in two distinct families of 2-cycles. For n≥4 each 2-cycle family has 2^(n−1)−n−1 cycles; total 2^n−2n−2, all ideal counts sum to 2^(n+1)+n−1. Rank-sums give mean n for 3/5-cycles and n/2 versus 3n/2 for two-cycles. At n=3 there are no two-cycles and order 15, for n≥4 order 30. Independently enumerated all ideals and cycle rank profiles n=3..9, not used for all-n proof.

## originality

PASS

Standard examples and rowmotion are classical; the available primary rowmotion theorems address other poset structures and do not give this explicit S_n orbit and rank-average partition. A natural complete all-n classification survives, qualified by the inaccessible 1995 general antichain paper.

## value

PASS

The standard examples are canonical posets of unbounded order dimension. Exact all-n rowmotion cycle lengths bounded by 5 and a sharp change in orbit-averaged cardinality between n=3 and n≥4 give a natural structural orbit classification, not arbitrary finite numerical data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
