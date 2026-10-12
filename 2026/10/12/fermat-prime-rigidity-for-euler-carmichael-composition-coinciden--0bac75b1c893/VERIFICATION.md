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

Direct finite regression with standalone `verify.py` (Python 3 standard library):

`VERIFY_OK cases=1830 equality_samples=[(3, 1), (3, 4), (3, 6), (3, 10), (5, 4), (5, 6), (5, 10), (17, 6), (17, 10), (257, 10)] Fermat_thresholds=(257,65537)`

Tests include odd primes below \(300\), \(1\le a\le10\), and \(b\in\{2,3,4\}\), independently computing the two compositions and comparing to the derived integer quotient and the stated iff condition. Further threshold tests for Fermat primes \(257\) and \(65537\) are exact. The executable uses elementary trial division; no downloaded data, packages, or hidden inputs are necessary.

The infinite proof follows from the prime-power identities and the exact valuation argument in `RESULT.md`; the finite test does not establish either infinity or novelty.
