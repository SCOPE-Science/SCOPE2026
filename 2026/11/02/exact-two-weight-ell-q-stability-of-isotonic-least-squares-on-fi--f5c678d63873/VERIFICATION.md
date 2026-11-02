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

# Reproducibility and scope

Execute `python3 verify_weighted_isotonic.py` with Python 3.10 or newer (only standard library). It exhaustively enumerates admissible convex-connected blocks and feasible equality partitions for seven small finite posets, checks exact rational block norms in the 1-norm and squared 2-norm, verifies constructed normal-cone/KKT identities, and tests the rigidity condition plus a sharp two-vertex witness. Expected output:

```
PASS: 84 weighted graph cases; 1164 admissible-block checks; 1152 feasible-partition comparisons.
PASS: 63 exact rigidity comparisons.
PASS: two-node witness L1=9/5; L2 squared=41/25; L-infinity=1.
```

The universal theorem follows from the proof's finite-face decomposition and relative-interior normal-cone construction, not from sample enumeration. The code does not verify all positive real weight assignments or all finite posets. No independent audit has been performed.
