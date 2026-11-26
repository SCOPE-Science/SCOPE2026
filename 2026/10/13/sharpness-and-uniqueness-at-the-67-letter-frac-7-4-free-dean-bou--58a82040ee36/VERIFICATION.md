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

Any admissible word of length at least 2 starts with one of eight allowed ordered pairs. The inversion-preserving permutation taking any such pair to 01 is unique, so the normalization loses no orbits and the final orbit has size eight. Alternating parity excludes exactly equal-letter and inverse-letter adjacent pairs; the repetition search handles all other constraints. A new forbidden factor after an append must be a suffix. For each p, it suffices to inspect the suffix of length ceil(7p/4), if present: any longer suffix of period p has a suffix of that length of the same period. This tests the inclusive threshold, regardless of whether the candidate period is least. The independent replay used masked two-bit comparisons for those shortest suffixes and computed D_3 from the actual sets of pairs and triples. Its length-24 probe found 350 normalized words; its full run found 414112 at length 67 with exactly the specified qualifying word, and 486776 at length 68, all pair-complete, with d3 counts 397780, 83006, 5990 for 0, 1, 2. It separately scanned the witness's factors and checked its palindrome and exact D_3={010,101,303}. Pair-completeness at length 68 ensures that further extensions can only remove minimal absent triples, so no longer qualifying word is missed; d3 need not be monotone on arbitrary incomplete prefixes. Independent reproduction: python3 /workspace/branches/4607a331-6161-4173-aef5-5e141050614b/replay.py, with exit-zero results in replay_counts.txt in the same directory. The frozen checker was inspected but not executed.

## originality

PASS

The prior lemma supplies the same strict upper bound |w|<68, but not its sharpness, the length-67 representative or the classification of equality. The distinct claim is exact attainment and a unique extremal orbit, not the prior upper bound or a new general algorithm.

## value

PASS

Length 67 is the equality case left by an existing bound at a natural sharp repetition threshold, not an arbitrary enumeration layer. The explicit attaining word and its unique symmetry orbit settle both whether the published cutoff is sharp and what its equality cases are.

The dated certificate retains the supplied scientific assessment, sources and limitations.
