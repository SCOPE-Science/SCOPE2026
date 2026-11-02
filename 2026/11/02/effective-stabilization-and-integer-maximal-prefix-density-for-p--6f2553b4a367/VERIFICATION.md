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

# Verification record

The proof uses the palindrome reflection congruence, its extension/contraction preservation under a full primitive period, the resulting two pigeonhole arguments, and the independently cited translation lemma of Rukavicka. The running maximum is the global maximum because the latter lemma makes the prefix palindromic-length sequence nondecreasing along each period residue. The ratio follows from finite congruence counting, not statistical extrapolation.

`verification.py` is a standalone Python 3 program requiring only the standard library. Run `python3 verification.py` in the directory containing it. It generates primitive binary period blocks of lengths 2 to 9 and ternary blocks of lengths 2 to 6; among these it checks 1,030 words having long palindrome prefixes. In each case it recomputes exact palindromic-factorization dynamic programming, the one-residue palindromic-prefix property, and the uniform cutoff \(n\ge p(p-1)+1\). It independently verifies the two-run family for each split at every period from 2 through 39. `verification_output.txt` contains the recorded passing execution.

These are finite checks only, not exhaustive over arbitrary periods, arbitrary alphabets, or arbitrary prefix lengths. Infinite correctness relies on the proof in `RESULT.md`. No independent mathematical audit has been performed.
