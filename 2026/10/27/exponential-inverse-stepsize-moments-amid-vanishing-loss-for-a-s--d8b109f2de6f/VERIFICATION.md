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

# Reproducibility and logical boundaries

The accompanying pure-Python `verify_oracle.py` was executed against the same formulas as those embedded in this package. It checks fifteen rational inputs against the exact ideal-oracle algebra, all binary sign sequences to depth eight, and the positive-run-then-negative-event behavior. The successful run returned:

`VERIFY_OK: 15 exact oracle recurrences; 8 complete rational binary trees; 20 rare-event endpoint tests; finite product scaling`

Only the finite identities and examples are computationally verified; the infinite-product existence, all-horizon expected-value bound and inverse-moment liminf follow from the written proof. No independent audit has taken place. The result does not apply to sample-estimated or safeguarded learning rates.
