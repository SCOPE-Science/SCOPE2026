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

Execute `python3 verify.py` (Python 3 standard library). Expected success starts with `VERIFY_OK`, then five `bad_pair` witnesses, and `all_remaining_prime_pairs_13_to_37: PASS`. Both Legendre valuation parity and trial factorization of factorials are checked for every \(0\le c\le40\). The program verifies the small-prime failures and all necessary semiprime candidates with larger prime at most \(37\), accounting for all twenty-one distinct-prime products in the remaining finite interval.

The program does not check infinitely many primes or factorial indices. The proof uses the mathematically independent Ramanujan-prime facts \(R_3=17\) and \(R_5=41\) to bound the squarefree kernels for all remaining \(c\), and applies the gcd identity to remove all remaining pairs. The verified theorem concerns only the stated squarefree-support stratum, not arbitrary factorial-square representations. Independent mathematical review has not been performed.
