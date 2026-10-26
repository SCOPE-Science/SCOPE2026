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

# Reproduction and scientific limits
Run `python3 verify.py` with standard Python 3 (no external dependencies). The program enumerates all 63 canonical structures and forms exact Hintikka signatures by bottom-up recursion over all tuples. Its second checker is a direct three-round Ehrenfeucht–Fraïssé game with explicit spoiler and duplicator choices, separate from the signatures. It checks 210 inter-representative pairs and 63 membership equivalences, and reports `VERIFY_OK`.

The canonical reduction for arbitrary finite structures is proved in RESULT.md by a three-round class-matching strategy; finite enumeration is not being extrapolated. The lower bound nine follows from an explicit rank-three sentence, not from a machine run. This verification is reproducible self-review work; independent external audit and validation have not been performed.
