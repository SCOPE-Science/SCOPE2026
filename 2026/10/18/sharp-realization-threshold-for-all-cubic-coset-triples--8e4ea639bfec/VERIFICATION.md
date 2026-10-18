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

Run `python3 verify.py` with a current Python 3 interpreter. The local check is exhaustive for every prime less than 900, with complete word support computed by discrete logarithms and independently by cubic-power cosets; it reports `VERIFY_OK`. In the paper, the separate Weil-bound argument establishes the claim for all remaining primes, without numerical extrapolation. The large-prime step applies only when the character polynomial is not a cube; this condition is checked via exponents 1 or 2 at distinct linear roots. The result and novelty have not received independent auditing.
