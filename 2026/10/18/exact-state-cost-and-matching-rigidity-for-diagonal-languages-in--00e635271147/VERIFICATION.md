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

# Verification record

The exact theorem is proved in `RESULT.md`. The independent executable `check.py` enumerates normalized useful NFA transition assignments, checks graph cactus edges by alternative-path counting, checks all inputs through length three, and compares the state minima and matching counts for \(n=1,2,3,4,5\). Run with `python3 check.py` from this directory; `check-output.txt` contains its observed standard output.

The finite experiment does not enumerate arbitrary-state, arbitrary-size NFAs or establish infinite lower bounds by itself. The three-layer normalization, private-middle-state lemma, \(K_{2,3}\) obstruction, construction, and rigidity argument prove the theorem for all \(n\ge1\). References, model restrictions, and novelty risks appear in `RESULT.md` and `REVIEW.md`. No independent audit or external certification is claimed.
