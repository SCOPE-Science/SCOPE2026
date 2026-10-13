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

The exact-capacity proof is given in RESULT.md, including the distance-to-graph equivalence, upper bounds, and explicit constructions in every residue class. `verify.py` is a standalone Python 3 script requiring only the standard library.

Run `python3 verify.py`. The script checks the claimed construction and graph condition for every length 6 through 180, directly computes all cyclic three-symbol read distances for all pairs of constructed words through length 24, and independently enumerates the entire conflict graph and solves the maximum independent set problem exhaustively for lengths 6 through 11. The expected terminal line is `VERIFY_OK`. No finite bound is extrapolated into the proof of all lengths. Scientific scope and bibliographic limitations appear in RESULT.md and REVIEW.md.
