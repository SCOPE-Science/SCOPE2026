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
# Verification details

The standalone `verify.py` needs Python 3 and only the standard library. Execute `python verify.py` from the directory containing this file.

Actual package-path execution returned:

`VERIFY_OK exhaustive_gap_tuples=5985 raw_subsequence_cases=495 random_cases=300 envelope_scans=75`

The check compares the all-gap closed form with an interval dynamic program for distinct palindromic subsequences for every nonnegative gap tuple of total size at most 17 (5,985 cases). For 495 of these cases it also constructs the literal set of distinct subsequences before selecting palindromes, a method independent of the counting formula and of the interval recurrence. Further randomized gap examples and finite maximum scans check broad boundaries. An additional exact SymPy calculation, performed separately, verified the displayed sum-of-squares identity in the extremal proof; SymPy is not a dependency of the released verifier.

All finite checks are examples, not proofs of a general infinite statement. The proof of the closed form is a complete partition of palindromic embeddings by one-count, and the asymptotic claims rest on the homogeneous four-case inequality. Existing literature coverage remains subject to unindexed-work risk; no independent scientific audit or independent validation has been conducted.
