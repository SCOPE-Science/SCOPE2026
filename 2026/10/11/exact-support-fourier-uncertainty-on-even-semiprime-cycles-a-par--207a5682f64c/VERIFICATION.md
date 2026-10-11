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

The analytic proof reduces the complex Fourier transform on the cyclic group of order twice an odd prime to two prime Fourier channels. The established prime Chebotarev/Tao uncertainty bound is the only imported nontrivial theorem. The case of a zero channel forces exactly even support, and two explicit constructions saturate the two alternatives.

Run `python verify_exact_semiprime_profile.py` with Python 3.8 or later. The program uses only the standard library and represents cyclotomic values by integer coefficient arrays modulo the prime cyclotomic relation. It verifies the explicit polynomial supports and zeros for seven sample primes, with 75 total support sizes. The expected terminal marker is `VERIFY_OK`.

These finite checks are not an infinite proof and do not independently assess novelty. The scope is exactly supported complex signals with support size at most the odd prime.
