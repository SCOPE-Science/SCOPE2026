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

With both colors eligible to act, the first-layer neighbor count is a−1_{i∈A}+1_{i∈B}, and similarly for the other layer. For a nonempty skew fort neither side can be empty. A singleton side requires the other side to be exactly the complementary indices, which is possible precisely at n≥4. A side of size two requires its indices to be in the opposite side, so the set contains a two-column fort. Both side sizes at least three always give a fort; after excluding two common columns, the inclusion-minimal possibilities are 3+3 with overlap at most one (possible starting at n=5). These and the singleton-layer forts have no proper subfort. A skew fort blocks the first force into it and a terminal nonempty white set is such a fort, validating the obstruction test independent of forcing choices. Avoidance gives the disjoint cases by side sizes, with overlap at most one in the side-two case; the apparent duplicates of the two orientations occur exactly at 1+1 and 2+2 and account for the two subtractions in W_n. For n=3 only the three two-column obstructions occur, giving twelve successful four-white sets. The top white coefficient is 56 for n=4, and 2+2n(n−1)+2 C(n,2)(C(n,2)−C(n−2,2)) for n≥5. A minimum-size skew fort has four vertices, and success/failure are monotone in opposite directions, yielding the claimed failed size and span including n=3,4. Counting 3+3 configurations with overlap zero or one gives the stated fort count. Independent adjacency and legal-move DP checked all 87360 initial subsets across 3≤n≤8, exact minimal families, coefficient vectors, and both extremal quantities and span. Minimal-fort totals: 3,14,50,227,805,2284; minimum-set counts: 12,56,182,332,548,842. Replay: python3 /workspace/reproductions/check_fan_crown_skew.py skew. The file verification/verify_skew_prism.py was inspected at its actual nested path; its claimed 174720 checks are reported evidence, distinct from the independent reproduction. The local analysis, not the finite test, establishes all orders.

## originality

PASS

The supported distinct claim is the complete-prism skew obstruction classification and full labeled forcing polynomial. Neither the same-graph one-leaky/ordinary records nor the same-parameter clique-bouquet record covers that claim. The span relation is already known and is not credited as new.

## value

PASS

Complete prisms form a natural Cartesian-product family. The three obstruction types give an all-set membership criterion and exact full coefficient array, including small-order transitions and both success and failure extrema, useful in distinguishing skew from ordinary and one-leaky forcing on the same family. This is more than an application of the known span identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
