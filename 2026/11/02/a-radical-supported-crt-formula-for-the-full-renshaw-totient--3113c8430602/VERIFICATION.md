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

# Reproducibility
Run `python3 verify.py` with Python 3.8 or later. The checker uses only the standard library and exact integer arithmetic. The core proof requires no numerical hypothesis or computed bound.

Tests verify the formula at every modulus through 2000, both parity-bias corrections and radical invariance for all odd moduli through 999, and the two-prime correction for all ordered pairs of distinct odd primes below 100. These finite tests do not certify the unrestricted claims; the proof in RESULT.md covers the infinite domains.

Scientific limitations: factoring the input is presumed for the formula's cost estimate; the prime-density statement uses an established theorem; priority is not independently established. Independent audit status is not performed.
