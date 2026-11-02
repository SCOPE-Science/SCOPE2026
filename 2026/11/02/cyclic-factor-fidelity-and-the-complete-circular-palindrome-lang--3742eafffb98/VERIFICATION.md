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

Execute `python checker.py` with Python 3.8 or newer and no dependencies. It checks the exact eight input digrams, four 16-bit supertiles, all 36 short palindrome strings, absence at lengths 15 and 16, rankwise full-cycle palindromes through rank 8, exact linear occurrence at rank 8, and independent overlapping-pair-parity encoding of those finite words. It checks the three-block embedding through rank 8 and samples higher-rank palindromes through rank 11.

The finite checks establish the finite enumerations used in the proof. The general containment theorem and all-rank stabilization are proved by the unbounded substitution argument and prefix nesting described in RESULT.md; they do not rely on the finite sample. Independent mathematical evaluation has not been performed.
