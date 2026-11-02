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

# Verification and limits

Run `python3 verify_cycles.py` with Python 3; it has no external dependencies. The code generates every simple-cycle matching, enumerates legal single blocking-pair moves and uses a directed-graph cycle search. It also checks existence of a terminal matching and the constructive coherent-orientation cycle.

Observed output:

```text
C_3: profiles=8 cycle_profiles=2 stable_profiles=6
C_4: profiles=16 cycle_profiles=2 stable_profiles=16
C_5: profiles=32 cycle_profiles=2 stable_profiles=30
C_6: profiles=64 cycle_profiles=2 stable_profiles=64
C_7: profiles=128 cycle_profiles=2 stable_profiles=126
C_8: profiles=256 cycle_profiles=2 stable_profiles=256
C_9: profiles=512 cycle_profiles=2 stable_profiles=510
C_10: profiles=1024 cycle_profiles=2 stable_profiles=1024
VERIFY_OK profiles=2040 cycle_profiles=16 stable_profiles=2032 no_stable_profiles=8 directed_moves=824616
```

The enumeration establishes exactly those finite cases. The arbitrary-size, arbitrary-graph conclusions depend on the written proof; nothing here represents machine certification of an infinite theorem. The polynomial move-count constant uses the cited published forest bound. Source priority and independent audit remain unperformed.
