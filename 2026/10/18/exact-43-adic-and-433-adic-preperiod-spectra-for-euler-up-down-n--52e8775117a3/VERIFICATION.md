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

# Verification instructions

Run `python3 verify.py` with Python 3.8 or later and no nonstandard dependencies. The final output line must be `CERTIFICATE_OK`.

The verifier builds \(E_n\) by the Entringer (boustrophedon) triangle and independently by the exponential-generating-function convolution, modulo each tested prime square. It checks all terms through \(3d+9\), every zero residue modulo the prime, all possible prime-square second differences within those finite ranges, three exact special values and their unique linear-congruence roots. These tests witness the only finite inputs needed in the mathematical proof. The formal all-exponent step is the analytically reconstructed finite-frequency lemma and the published iff preperiod criterion; the script neither enumerates nor claims to certify all exponents directly.

Source limits: full bibliographic comparison is bounded to the cited accessible sources and searches. No independent external audit has been performed.
