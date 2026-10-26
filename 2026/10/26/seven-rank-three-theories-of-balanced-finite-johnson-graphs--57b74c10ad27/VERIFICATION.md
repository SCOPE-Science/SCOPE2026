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

The proof uses the three-round Ehrenfeucht--Fraïssé game, vertex transitivity, and explicit existence/nonexistence of all four third-vertex adjacency patterns for ordered pairs. The seven resulting profile sets are distinct.

Finite corroboration: run `python3 verify_johnson.py` from a folder containing that file. `verification_output.txt` records 34 directly enumerated parameter pairs and the seven predicted masks. The script enumerates one representative of each pair-intersection orbit and all possible third vertices, checking the predicted masks. The enumeration is a finite check only; it does not certify unbounded parameters.

No separate external review or independent audit has been performed. The comparison with indexed prior work cannot guarantee uniqueness against unpublished or unindexed sources.
