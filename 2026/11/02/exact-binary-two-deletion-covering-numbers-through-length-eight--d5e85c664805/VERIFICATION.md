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

# Exact finite verification

Run `python verify.py` with Python 3 (standard library only). `verification_output.txt` is the recorded replay output. The source `verify.py` contains every claimed length, every witness word and every positive orbit weight, with no external data files.

For all source lengths \(2\le n\le8\), the checker forms each source's complete set of retained length-\(n-2\) subsequences by choosing every pair of deleted positions. It independently checks the same relation via greedy subsequence matching for every possible source/target pair. It then checks every proposed cover, including the full 64-word target space at length eight.

For lengths six, seven and eight it expands the positive integer weights to reversal/complement orbits, rejects overlapping orbit specifications, calculates the total target weight, and checks the weighted sum for every possible source. The computed \((\text{total},\text{maximum single-source})\) pairs are \((8,3)\), \((10,3)\), and \((74,12)\). Therefore no smaller covering set can exist. All 21,844 incidence decisions were independently cross-checked. This is a finite exhaustive proof for the listed fixed lengths, not an infinite-length extrapolation or external certification.

The checker does not establish originality or any optimum outside the stated finite range. No independent audit was performed.
