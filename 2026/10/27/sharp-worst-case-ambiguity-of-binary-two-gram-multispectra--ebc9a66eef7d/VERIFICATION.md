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

# Reproducibility
Run `python3 verify.py` with Python 3 (standard library only). The expected first line is `VERIFY_OK`. The program enumerates 131070 binary words through length 16, compares literal adjacency-profile counts with independent positive-run-composition formulas, checks the exact extremal values and maximizing profiles, then checks 2004266 additional feasible profiles through length 200. These tests cannot establish the all-length theorem by themselves; the proof in RESULT.md supplies infinite validity. The base cases at lengths one and two are handled separately, with two one-symbol strings sharing an empty read multiset at length one. No external or independent audit has been performed.
