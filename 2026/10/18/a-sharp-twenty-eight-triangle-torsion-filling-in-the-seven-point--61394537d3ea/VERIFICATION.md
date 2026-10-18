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

The command `python3 verify.py` rebuilds the simplicial boundaries from seven ground labels and checks the full supplied primal and dual certificates with integer arithmetic. Its independent enumeration finds 945 four-cycles, 630 chordless and 315 chorded, and its mod-three reduction detects the nonzero class of the canonical cycle. Expected output: `VERIFY_OK 945_FOUR_CYCLES 630_TORSION_GENERATORS 315_BOUNDARIES SHARP_FILLING_28`. The checked area is the simplicial chain \(\ell^1\) norm for a boundary equal to three times an oriented four-cycle, not the unrestricted minimal geometric area of a singular filling.
