---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

In a fixed (A,B,C) binary Parikh fiber, if one word has subsequence-universality index >=2 then A,B>=2 and 0<C<AB, ensuring every member has index>=2. The greedy arch characterization and two-symbol-per-arch length constraint preclude any spectrum hole through length seven; at length eight an index-four word is exactly four blocks each ab or ba, forcing A=B=4 and C=6+t for t in 0..4. Explicit index-three words fill the would-be hole for C=6,7,9,10. For C=8, all nonnegative x_0..x_4 with sum 4 and weighted sum 8 correspond bijectively to the eight partitions of 8 fitting in 4x4: two have exactly two arches, the other six four arches, yielding exactly {2,4}. A new independent exhaustive implementation tested every binary subsequence pattern for all 511 words of lengths 0..8, found 255 actual fibers, verified greedy arch indices separately, and recovered just that one eight-word noninterval fiber.

## originality

PASS

Best-of-knowledge distinct exact theorem after statement-level comparison: Fazekas–Huang–Mercaş full paper remains plausible source of an uninspected example or appendix asserting the same first gap; material read is abstract only, so not treated as conclusively noncovering. Previously known ingredients are credited; no unsuccessful search is treated as novelty proof.

## value

PASS

The A,B,C fiber is exactly the natural refinement of previously studied existential and universal binary subsequence-universality indices. Demonstrating its attainable-index set need not be an interval, and locating the first possible hole uniquely at the sharp length-eight boundary, gives a finite but nonarbitrary structural obstruction and precise benchmark for future fiber-spectrum work. The precise eight-word constellation is not merely an aggregated known index table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
