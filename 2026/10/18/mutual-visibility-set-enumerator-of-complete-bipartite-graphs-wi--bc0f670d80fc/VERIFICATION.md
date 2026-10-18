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

# Reproducibility and limits

Run `python verify_visibility_matching.py` with Python 3.10 or later. The script independently constructs the named bipartite graph after deleting its specified matching, uses shortest-path breadth-first search, and checks every vertex subset in a finite parameter range. It compares each cardinality distribution to the algebraic classification formula, then checks the sharp degree, exact leading count, and coefficientwise deletion monotonicity on 210 additional parameter profiles.

The actual run recorded in `verification_output.txt` reports 40 exhaustively checked graph profiles, 49,984 vertex subsets, 210 extra algebraic checks, and the final `VERIFICATION_OK` marker. Both files are included as standalone artifacts. The finite checks do not constitute a proof for the infinite parameter family; the unrestricted argument is given in `RESULT.md`. No independent scientific audit has been conducted.
