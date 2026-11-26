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

Removing a minimal element gives a smaller poset; its strict successors form an upper ideal, and adjoining a minimal point below every member of an upper ideal produces a poset. I used this dual enumeration instead of the supplied maximal-element program, deduplicating by the least full relation encoding over permutations within invariant in/out-degree blocks. Counts through eight were 1,2,5,16,63,318,2045,16999; 48346 candidate extensions entered the last deduplication. Joint exact refinement gave 1,2,5,16,63,318,2045,16997 classes and the only nontrivial class sizes were 2,2. For the poset signature, strict lower, strict upper, equality and incomparability exhaust pair types. Incomparability counts are recovered by subtracting the two strict counts and the diagonal from the colour histogram. If histograms differ at any round, the difference persists; when equal, these recovered counts therefore yield the same comparison as full pair-type refinement. Stable colours characterize the C² theories, and size is expressible by counting, so all possible finite competitors are included. I verified that the two frozen witness pairs are strict posets and that their canonical classes match exactly both collisions. Height-two connectivity and the height-three middle multiplicity matrices also distinguish the members without a computer.

## originality

PASS

The result is distinct from earlier examined work on general C² identification and from the poset object census. There is exact overlap with the later-dated November 8 Resultary record, which also proves an all-larger-orders existence statement; this is not an unmatched finding in the current index. On the available evidence the later match does not preempt the frozen October 18 result, and no earlier result inspected already gives the restricted cutoff and complete collision layer. This is not a priority certificate or a determination that the two records were independently obtained.

## value

PASS

It fixes the first loss of expressive separation for a canonical logic on a standard relational class, and identifies all minimal counterexamples rather than a selected pair. In particular the two witness mechanisms distinguish regular incidence from different middle-incidence multiplicities despite full in/out counting. The exact census and explicit witnesses are usable benchmarks for algorithms and structural classification at the minimal size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
