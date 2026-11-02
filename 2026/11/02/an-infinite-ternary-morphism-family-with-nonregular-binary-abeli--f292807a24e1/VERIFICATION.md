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

# Reproducible checks and limits

Run `python3 proof_check.py` and `python3 digit_verifier.py` using a standard Python 3 interpreter. No third-party package is needed. The recorded standard output is in `verification_output.txt`, separated by command headers.

`proof_check.py` enumerates all length-\(k^m\) factors via the nine permitted pairs of exact substitution blocks and compares their minimum, maximum, and intervening integer counts against the closed recurrence. Its tested parameters are documented in its output. The enumeration is finite but complete *for each tested parameter*, because all nine adjacent letter pairs appear in the infinite substitution word.

`digit_verifier.py` separately constructs the word from base-\(k\) digit counts and checks a finite prefix long enough to include at least one occurrence of every macroletter pair. It tests the formula for indicated small parameters and the parity-middle-coordinate equivalence for thirteen or more positive multiples of three. Its finite-prefix checks are not substitutes for the general induction or proof of irrationality.

The infinite theorem, and especially the weighted-extremum lemma and non-eventual periodicity, is proved in `RESULT.md`. The remaining scientific limitations are restricted to other alphabets, other codings, and unrelated substitution families. Independent audit: not performed.
