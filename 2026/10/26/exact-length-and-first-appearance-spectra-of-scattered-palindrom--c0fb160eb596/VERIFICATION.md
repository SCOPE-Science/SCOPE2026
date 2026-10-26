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

# Reproducible finite checks

Run `python3 verify.py` using a standard Python 3 installation. This checks all nonempty binary palindromes, separately by palindrome length, in alternating prefixes through length 21; it also checks the rational bivariate coefficient recurrence and an independent interval dynamic program for distinct palindromic subsequences through length 150.

Expected output:

`ALTERNATING_SCATTERED_PALINDROME_PASS brute_n=1..21 exact_spectrum_n=0..150 independent_interval_dp_n=0..150 rational_2d_coefficients_n=0..150`

These finite computations do not constitute a proof for arbitrary lengths. That proof uses greedy-minimal embeddings and the bijection between palindromes and equal-adjacency flags in `RESULT.md`. The originality comparison separately credits OEIS A238374 for the scalar counts and generating function. Independent mathematical audit has not been performed.
