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

A cut just after a one partitions the word into k mixed blocks, so it is k-universal. Every length-(k+1) target with an adjacent 01 embeds by taking that pair in one block and one symbol in each remaining block. For a nonincreasing target 1^a0^(k+1−a), an embedding must double up on zeros in a long block after a blocks used for ones. Conversely, a long block of index at least a+1 makes this possible by using the first a blocks for the ones. Thus if h is the last long-block index, exactly the a from h to k+1 are absent. Reversal handles cuts immediately before ones. At a split long gap the alternating subsequence (01)^k0 has k mixed blocks and contains every length-(k+1) target except the all-ones word: greedy starts at index 1 or 2 and each change saves one position compared to a repeat. The terminal streak lengths contributed by each short-gap run of length r are 1 through r, once each on each side; zero streaks occur once per long gap on each side. This gives the claimed full histogram even for periodic words. For the Fibonacci images the cyclic source avoids 11 and 000, giving gaps 1 or 2 with no two short gaps adjacent. Letter counts determine both gap counts and are coprime, so indexed cuts there are distinct rotations.

## originality

PASS

The distinct claim supported by the comparison is the complete indexed-cut law for arbitrary runs of short gaps, not an exclusive claim on the three-point law or the Fibonacci specialization. Two materially overlapping indexed records cover the no-adjacent-short-gap case; one gives the same Fibonacci histogram exactly. Neither supplies the arbitrary-run histogram. The inspected linear-word algorithms permit a per-cut calculation but do not state the cyclic aggregation.

## value

PASS

For one necklace the least absent length does not distinguish any cuts; the number of witnesses at that length does. The complete invariant identifies why large multiplicities arise and shows that the order of the short-gap runs is immaterial, avoiding a per-rotation enumeration even for periodic words. The Fibonacci case is an illustrative specialization, not the main value beyond the exact subcase overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
