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
# Exact finite-check reproduction

Run `python3 verify.py` with Python 3.8 or later. No nonstandard libraries, network, external datasets, or random seeds are required.

The verifier enumerates every binary source word of lengths \(2\) to \(14\); the number of source words is \(\sum_{n=2}^{14}2^n=32764\). It computes all scattered-subword multiplicities by appending one input symbol at a time and applying the exact split into occurrences that omit or use the final position. For each input it checks whether the maximum among all subwords exceeds the maximum among lengths at most \(\lceil n/2\rceil\). It asserts that there are no earlier failures and that precisely four length-fourteen words fail.

It then checks the exact unique length-eight maximizing subsequences and their frequencies, all fifteen lengthwise maxima for each representative, and—using a separate algorithm—counts all \(2^{14}\) position subsets for each representative and compares every pattern count. The second method does not call the recurrence. Complementation and reversal preserve subsequence occurrences by bijections on position subsets, which explains the orbit pairings.

The successful result is: `VERIFY_OK all_binary_words_n=2..14 failures_before14=0 failures_at14=4 unique_maximizers=2 independent_mask_checks=32768` followed by details. Finite exhaustion establishes exact results only for the stated finite input universe; no extrapolation beyond it or independent certification is claimed.
