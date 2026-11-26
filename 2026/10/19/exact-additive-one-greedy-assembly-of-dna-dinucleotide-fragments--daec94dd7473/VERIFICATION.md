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

The four fixed words and six paired orbits give the stated ten classes. Chosen occurrences from different classes cannot have the same start. Ordering chosen occurrences yields feasible adjacent joins whose additional lengths are no greater than the original gaps, so the ordered-overlap optimum is exact; incidental occurrences need not be excluded. For greedy, a component and its reverse complement admit exactly the same choices of orientations, and a multiset preserves the distinction between different positions even for identical strings. The globally maximal proper overlap is recomputed from the full state, all tied legal successors are retained, and the number of components strictly falls. The independent replay found O by shortest paths on (seen orbit mask, final symbol), allowing all incidental coverage, and G by recursive fixed-size-domain enumeration with packed component words and an integer overlap test. It checked all 1023 subsets, using 2456 optimum states and 638579 greedy states. The maximum gap is 1; the gap-one counts by size are 0,0,16,55,78,69,40,17,6,1, totaling 282, with the other 741 at gap zero. All sharp ratios matched, including 5/4 for three classes. The explicit witness also checks directly: the first join has the largest possible overlap 1 and then no orientation or order has a positive overlap with the remaining class.

## originality

PASS

The direct reverse-complement greedy rule and general compression analysis are prior work. No inspected claim establishes the sharp additive gap or classified all-subset profile for the specified four-symbol length-two orbits. The strongest catalog analogue has the same number of orbits but a different overlap structure and different sharp ratios.

## value

PASS

Length two is the smallest length with nonzero proper overlaps, and the four-symbol involution is a natural fixed instance with both fixed and paired words. The census answers a concrete guarantee question left by the broad compression bound: across all class subsets and even adversarial ties, the direct rule loses at most one symbol. The frequency by size and sharp ratios give useful exact baseline data for studying how orientation and ties affect this heuristic, without extrapolating to longer words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
