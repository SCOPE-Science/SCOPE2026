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

# Verification

Run `python3 checker.py` in a directory containing this file. It uses only the Python 3 standard library and compares the theorem's integer closed form with a separately implemented modular convolution on true base-\(q-1\) palindrome coefficients modulo \(q^2\). It additionally constructs actual palindromic integers by digit enumeration for \(q\in\{3,5,7\}\), \(m\le4\). The script's tested primes are \(3,5,7,11,13,17\) and all half-lengths \(1\) through \(25\). The character-sum argument in `RESULT.md` proves the statement for every odd prime and every half-length; enumeration alone would not establish that infinite scope. The accessible archival paper and the nearest prior finite-length classification were checked for claim implication, as distinguished from a proof of universal novelty.
