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

Run `python check_periodic_momentum.py` from the same directory. The Python standard library `fractions.Fraction` is used for all exact arithmetic. The verifier checks 6,400 rational parameter triples against direct two-step matrix multiplication and Schur identities, 36 recurrence updates of the exact unstable rest-initialized witness, and 5 distinct rational small-contrast families. These calculations supplement the analytic Schur and discriminant proof in `RESULT.md`. In particular, finite sampling does not prove the continuum classification. No independent audit has been performed.
