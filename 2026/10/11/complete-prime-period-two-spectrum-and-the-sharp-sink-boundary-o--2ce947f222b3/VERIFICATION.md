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

## Reproducible verification

Run `python3 check_duffing.py` with Python 3. The checker uses only the standard library. It validates sampled return-map identities and the explicit trace and threshold; the proof of completeness for all real parameters is the symbolic factorization in RESULT.md. At the sharp upper boundary, the only assertion is a multiplier of minus one, not nonlinear stability. No independent audit has been undertaken.
