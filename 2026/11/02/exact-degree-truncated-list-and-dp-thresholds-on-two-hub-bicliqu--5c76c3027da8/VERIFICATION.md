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

The standalone file `verify.py` uses Python's standard library. Its checks are:

- Exhaustive enumeration of all local two-color DP edge-matchings for hub-fiber sizes two through seven, verifying the upper bound of two excluded hub pairs and the matching condition on a pair of exclusions.
- Construction and direct checking of the block partition and each common-neighbor DP gadget for the same sizes.
- A separately implemented exact subset dynamic program for the minimum number of allowed blocked-pair blocks covering the full hub-pair grid at hub sizes two, three, and four.
- Direct enumeration of the prescribed ordinary-list obstruction and integer threshold tests for every integer \(3\le n\le500\).

Command: `python verify.py`.

Expected terminal line: `VERIFY_OK`.

These are finite checks only. The written combinatorial proof establishes the universal statements. No independent audit or external certification is claimed.
