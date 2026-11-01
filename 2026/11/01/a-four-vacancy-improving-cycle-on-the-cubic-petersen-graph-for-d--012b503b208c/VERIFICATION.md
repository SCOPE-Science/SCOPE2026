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

# Certificate verification

Run `python verify_cycle.py` (Python 3, standard library only). The script explicitly lists all 15 graph edges, all 10 elementary jumps, and six distinct labeled agents. It verifies cubic regularity and the six repetitions of the block using exact rational arithmetic. It checks every jump lands at a vacancy, its source is occupied, utility strictly improves, and all individual agent labels return to their original vertices after 60 moves. Successful output:

```text
PASS: Petersen degree 3, 4 vacancies, 6 labeled agents,
      60 exact strictly improving jumps, labeled state restored.
```

No unproved extrapolation is made from this finite witness. The verifier is ordinary executable arithmetic code, not an independent audit or a formal-proof certification.
