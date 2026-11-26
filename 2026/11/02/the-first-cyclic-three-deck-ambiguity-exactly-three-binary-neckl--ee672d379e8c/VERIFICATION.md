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

Independently reproduced the finite census using the necklace portion of /tmp/opencode/small_frozen_review.py. For each n=1,…,8 start from all binary n-tuples, repeatedly take the least remaining word, and remove its entire rotation orbit. For each root calculate the triple coordinates by summing L_a R_c over positions bearing middle letter b, where L_a and R_c count letters strictly before and after the position, respectively. Pair counts are first-letter prefix counts summed over positions bearing the second letter, and one-letter counts are frequencies. Group by the resulting full 14-coordinate signature and require at least two distinct rooted strings in a group, not just distinct cut labels. The necklace counts are 2,3,4,6,8,14,20,36 and no collision survives the distinct-root test through length 7. At length 8 the sole exceptions are 00011011 with {4,6} and {5,7}; 00100111 with {1,3} and {2,4}; and 00101101 with {3,7}. Thus there are five unordered pairs, all at weight four, and the histogram over 1,2,4,6,7,8 profiles is 2,1,3,2,1,27. The displayed witness has identical singles, pairs and triples, with the given triple vector. The 01 cut identity also follows directly by subtracting the two cross-block counts. The computation includes periodic and constant words and proves only the stated binary finite domain. The frozen verifier implements exhaustive direct combinations and a subsequence recurrence; it was inspected, not used as the independent computation.

## originality

PASS

The creditable distinct claim is the complete length-eight orbit-conditioned census and distribution, including the two non-Thue–Morse necklaces and their cut classes. The known finite Thue–Morse result covers the third row, and the lower-length exclusion follows from the published global table together with the explicit length-seven pair and its complement. Neither covered piece is counted as a separate novelty here. The strongest checked results do not imply the remaining length-eight census; in particular, global deck counts forget the necklaces containing each deck's roots. This is a best-of-knowledge assessment of the full classification, not a claim of priority for discovering cyclic ambiguity at length eight in an example.

## value

PASS

The finite object is naturally singled out by the first possible failure of distinguishing a circular word's starting cut. The complete exceptions and exact multiplicities distinguish genuine information loss at that boundary from identical periodic roots. They provide a reconstruction test set that a global deck count or the single Thue–Morse example cannot supply. No value is assigned to arbitrary larger slices or to extrapolation beyond length eight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
