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
# Reproduction

Run `python3 check_length8.py` with Python 3 (standard library only). The test terminates with `VERIFY_OK` only after checking every word over every canonical symbol-multiplicity partition of 8, and every shorter partition for lengths 1–7. The 22 partitions of eight together contain 95,503 canonical labeled words; the shorter lengths add 13,390 canonical words. The program checks actual spectrum keys against the full predicted fibers, counts each four-member multiplicity type, and separately enumerates the 2-, 3-, and 4-letter alphabets directly.

The proof of completeness for arbitrary finite alphabet size is the multiplicity-partition reduction in RESULT.md. Every substring composition is represented by a tuple of exact nonnegative integers; all 36 factors are included, with duplicates retained in sorted tuples. The checks do not use randomized hashes, heuristics, external network resources, or approximate arithmetic.

This reproduction verifies the stated mathematical certificate. It does not establish historical uniqueness of the result or constitute an independent audit.
