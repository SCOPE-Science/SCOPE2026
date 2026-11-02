---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` with Python 3 and only its standard library. The program enumerates *all* binary overlap-free words of lengths from \(0\) through \(48\) by bit extension, comparing its terminal-overlap predicate with an independent global predicate at every extension. It uses the exact last-square dynamic-programming recurrence to count factorization multiplicities, and a second enumeration appending every overlap-free square block to independently calculate all minima and counts.

Expected final lines are `INDEPENDENT_BFS_AGREEMENT: PASS` and `VERIFY_OK`; the complete recorded output is in `verification_output.txt`. The replay also reproduced byte-identical output. The program has no external package, random input, proprietary solver or network dependency. Assertions verify every numerical claim in the theorem, including the exact two length-\(48\) words and their unique nine-square factorizations.

This is a complete finite enumeration because the proof establishes the prefix-extension search and the last-square recurrence as exhaustive and because the largest minimum length obtained is \(48\). It is not an independent mathematical audit, a proof for longer nonminimal products, or an exhaustive literature-priority certification.
