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
Run `python3 verify.py` under ordinary Python 3. The verifier checks all state graphs for cyclic ring sizes 3 through 11, a single-excitation maximal transient witness at each such size, particle ancestry and pure-wave behavior for small state spaces, and seeded random samples on larger rings. Expected output: `VERIFY_OK exhaustive_states 265707 local_particle_checks 9828 random_large 2000`. Every code test is finite; the all-size claim relies on the analytic particle argument in `RESULT.md`. No independent audit has been performed.
