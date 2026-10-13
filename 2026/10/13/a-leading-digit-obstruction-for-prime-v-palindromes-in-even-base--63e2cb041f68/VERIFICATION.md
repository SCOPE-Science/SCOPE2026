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

Run `python3 verify.py` with Python 3's standard library. Its exact expected output is in `verification_output.txt`. The checker computes smallest prime factors, evaluates the arithmetic function \(v\) directly from prime exponents, enumerates odd composites through \(400000\), and tests odd-prime reversals below \(10000\) in every even base from \(2\) to \(40\). It specifically tests the odd leading-digit condition and the full binary-prime conclusion for all enumerated primes. It verifies the two literature examples \(175\) in base \(2\) and \(109\) in base \(16\) from their factorizations.

The infinite mathematical proof does not depend on these finite tests: it is the subadditivity lemma, the uniform odd-composite half-bound, the strict reversal bound, and complete handling of the small exceptional odd composites. No independent audit or external verification has been performed.
