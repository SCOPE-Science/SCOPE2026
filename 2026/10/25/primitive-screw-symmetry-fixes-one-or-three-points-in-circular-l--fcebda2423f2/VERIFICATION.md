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

# Verification and limits

Run `python VERIFY.py` with Python 3. For each width from 3 through 10 the verifier enumerates perfect matchings and all their subsets, constructs each primitive action directly from vertex permutations, and checks the complete invariant-face list as well as the augmented signed simplicial trace. It reports 60 passing primitive actions and 810800 face-action membership tests.

The full theorem uses the separate orbit-and-support proof in RESULT.md. Experiments at finitely many widths are not an infinite proof. The algorithm is deterministic and uses only the Python standard library; no external data or network access is needed. The dated revision abstract of the most relevant paper was examined; its technical full text was unavailable, leaving a real originality risk. Only self-review was performed.
