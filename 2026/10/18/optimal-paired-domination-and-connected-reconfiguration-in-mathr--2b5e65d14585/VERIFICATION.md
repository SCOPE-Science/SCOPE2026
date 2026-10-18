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

# Reproducible finite verification

Run `python3 verify.py` and `python3 verify_reconfiguration.py` in the directory containing these files. Both scripts depend only on Python's standard library. The captured stdout from both commands is `verification_output.txt`.

The first verifier enumerates all four-vertex subsets of the two-subset Kneser graphs for \(6\le n\le10\), totaling \(235{,}725\) configurations. It separately evaluates closed-neighborhood domination, three possible pairings, and the independent criterion that three selected ground edges form a matching. It compares the three ground-support occupancy counts with the formula in `RESULT.md`. The second verifier independently constructs the predicted optimum-configuration reconfiguration graphs for \(6\le n\le9\) and performs a complete breadth-first reachability test.

Observed: all assertions passed. The finite checks do not establish the general theorem; the proof for every integer \(n\ge6\) is supplied in `RESULT.md`. No independent audit or external verification has been performed.
