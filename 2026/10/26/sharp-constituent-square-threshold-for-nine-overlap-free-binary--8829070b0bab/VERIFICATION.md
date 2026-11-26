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

Each factor of an overlap-free word is overlap-free, so the square-block recurrence enumerates every admissible ordered factorization by removing or appending its last block. For an independent replay I instead generated every overlap-free binary word through the intrinsic bound 108, testing new suffix overlaps via shifts and bit masks, then counted all paths in the graph of square cuts of each complete word, retaining their root sequences. The suffix test compares the last p+1 letters with their shift by p exactly when 2p+1 fits, so it includes cubes at p=1 and discards precisely newly introduced overlaps. The replay visited 50,295 words including empty, matched every table row, and yielded zero nine-square factorizations with cap 5 and exactly two with cap 6. The length-48 words are different, each has the sole root-length vector (3,2,2,2,6,2,2,2,3), and reversal and complementation both exchange them. Larger caps are unnecessary to establish the universal lower bound since every counterexample would have cap at most 5.

## originality

PASS

The full classification by maximum constituent root length is distinct in the compared evidence: the example and its decomposition are known, and an indexed length-96 census even implies the lower threshold and sharpness, while covering only part of the cap-six domain. The originality decision rests on exhaustive rigidity under the root cap, not on credit for the known example, the shortest-length classification, or the isolated lower threshold. Indexed record dates are not treated as evidence of priority.

## value

PASS

The cap studied is attained by the canonical example at the maximum known number of squares, not an arbitrary slice. The complete rigidity result distinguishes optimal local constituent size from optimal total word length: minimizing the largest constituent does not add any further words, even when much greater total lengths are allowed. This is an exact structural constraint on extremal factorizations, not a repeat of the witness or a small-table check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
