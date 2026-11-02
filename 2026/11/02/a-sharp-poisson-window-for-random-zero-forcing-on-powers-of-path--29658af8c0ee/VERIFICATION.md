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

# Verification details

Run `python3 verify.py` using the Python standard library. It independently enumerates all seed sets for selected path lengths and forcing radii, compares full iterative propagation with an initial-neighborhood criterion, counts distinct minimal interior triggering support sets rather than nominal forcing witnesses, and computes finite random-seed success probabilities by a separate weighted local-state scan.

Observed replay output:

```text
INITIAL_FORCE_EQUIVALENCE_OK 24456
DISTINCT_MOTIF_CENSUS_OK 20
SQUARE_RANDOM_PROBABILITY 500 0.8722624 limiting 0.9502129
SQUARE_RANDOM_PROBABILITY 2000 0.8960899 limiting 0.9502129
SQUARE_RANDOM_PROBABILITY 10000 0.9155146 limiting 0.9502129
VERIFY_OK
```

These calculations check finite identities only. The infinite limiting distribution is established by the factorial-moment and finite-range-overlap argument in `RESULT.md`. No independent mathematical audit or external certification has been performed.
