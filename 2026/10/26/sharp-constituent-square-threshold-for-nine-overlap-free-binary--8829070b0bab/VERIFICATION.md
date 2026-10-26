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

# Reproduction and limits
Run `python3 checker.py` in this directory with Python 3.9 or later. No third-party dependencies, timeouts, external data or heuristics are needed. The exact reproduced stdout is `checker_output.txt`.

The square-block enumerator generates every binary root of lengths one through six and tests its double directly for forbidden overlapping factors. It appends eligible squares to every previously surviving ordered product. The prefix-based enumerator extends every overlap-free binary word one symbol at a time through the intrinsic length limit \(108\), and recursively records every achievable number of consecutive square blocks with root length at most six. Their distinct final-word sets agree independently at every root cap one through six. Enumerations and counts use exact integer/string operations.

The table in `RESULT.md` lists exhaustive layer cardinalities; cap five has zero nine-square products and cap six has exactly two, which are the two printed words. Each has the sole root-length list \((3,2,2,2,6,2,2,2,3)\). The finite exhaustive argument is logically sufficient because all nine-square words subject to root cap six have length at most \(108\). No conclusions are claimed about root caps above six, independent scientific review, or unpublished research.
