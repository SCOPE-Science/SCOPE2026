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

# Reproducibility and proof obligations

Run `python3 verify.py` in the directory containing this document, `RESULT.md`, and `verify.py`. The program uses only the Python standard library.

Actual completed finite checks:

1. For every integer \(1\le k\le28\), explicitly generated all binary palindromes of length \(k\) and tested each against the claimed word \(W_k\), checking length, run count, and at least \(k-1\) complete arches after removal of either designated endpoint.
2. For every binary host of lengths \(1\) through \(12\), tested all feasible palindrome orders and checked that any universal host has at least \(2\lceil k/2\rceil\) runs and at least \(k\) copies of each letter.
3. For every integer \(1\le r\le36\), checked that the stated extremal witness has exactly \(r\) runs and exhibits the claimed palindrome-subsequence order.

The program reported `ALL FINITE CHECKS PASSED; infinite statement follows from RESULT.md`.

These tests are finite. They do not establish the theorem for all lengths, do not certify originality, and are not an independent audit. The infinite theorem is proved by the run-injection lower bound, explicit arch decompositions, and constructive upper bounds in `RESULT.md`.
