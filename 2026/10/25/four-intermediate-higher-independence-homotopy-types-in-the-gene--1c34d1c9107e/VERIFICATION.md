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

Run the embedded standalone file with `python3 verify_gp2.py` from the extracted package directory. It uses only Python's standard library, no external data or network access, and recomputes each bitmask complex and matching from its mathematical definition.

The four runs have nonempty faces 809, 2268, 6710, 20799 and matching pairs 402, 1133, 3351, 10397. Critical dimensions are exactly `n=6: {0:1,3:3,4:1}`, `n=7: {0:1,5:1}`, `n=8: {0:1,5:7}`, `n=9: {0:1,5:4}`. The Hasse acyclicity checks visit all 3180, 10248, 34576, 121482 cover relations. The one potentially nontrivial Morse differential (the 4-to-3 differential for `n=6`) vanishes as an **integer** vector `(0,0,0)` after recursive signed gradient cancellation.

By Forman's discrete Morse theorem these validated critical complexes are homotopy equivalent to the originals. The single `n=6` four-cell is attached to a two-connected wedge of three three-spheres; Hurewicz identifies its integral degree vector with its homotopy class, so zero vector proves a null attachment. This is a finite exhaustive certificate, not a claim about any untested graphs.

All computations are integer-exact. No independent audit or external certification is claimed. Originality remains subject to possible unindexed equivalent work.
