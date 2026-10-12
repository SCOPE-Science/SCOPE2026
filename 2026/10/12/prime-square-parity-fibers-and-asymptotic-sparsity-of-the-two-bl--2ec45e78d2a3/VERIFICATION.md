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

# Reproducible finite verification

Execute `python3 verify_parity.py` with Python 3. The program requires no nonstandard libraries. Actual successful output is recorded verbatim in `verification_output.txt`. It checks: signed coefficient enumeration for every \(1\le n\le220\); the exact divisor identity and new parity classification for every \(1\le n\le300000\); and the prime-power congruence modulo eight for 1232 pairs, with exponents from zero through fifteen and odd primes below 400.

The mathematical proof is independent of this finite census. In particular, finite verification cannot establish asymptotic density or exhaust all positive integers. The infinite classification follows from multiplicativity and congruence (3) in `RESULT.md`; the counting asymptotic invokes the prime number theorem for the two reduced classes modulo eight. Independent external assessment has not been performed.
