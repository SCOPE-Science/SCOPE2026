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

Execution: `python3 verify.py` with Python standard library.

Observed result: `VERIFY_OK cases= 45`.

The checker enumerates high-density inventory states and directly simulates the deterministic map, checking the stabilization bound and exact maximal-delay counts against the closed Raney formula. Capacities 1 through 3, ring sizes 2 through 6, and surplus inventories 0 through 2 were covered when the total composition count was within 100000; the 45 reported cases satisfy that limit. Capacity 1 is an additional consistency check. Finite tests are not a proof for all integer parameters: the proof is the min-plus identity, strict event characterization, and Raney forest bijection. No independent audit or independent validation was performed.
