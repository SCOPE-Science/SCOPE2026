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

The standalone `verify_rankone_nijenhuis.py` enumerates all nonzero functional/image pairs for six selected stem two-step Lie brackets over prime fields. The defining Nijenhuis torsion is checked directly for every basis pair and compared with the separately computed alternating-form rank-spectrum expression; an additional \(\mathbb F_5\) Heisenberg case was run. The expected terminal marker is `RANK_ONE_STEM_NIJENHUIS_OK`. An exhaustive finite test is not a proof for all prime powers; the proof in `RESULT.md` is symbolic and characteristic-independent. No external independent audit or validation has been performed.
