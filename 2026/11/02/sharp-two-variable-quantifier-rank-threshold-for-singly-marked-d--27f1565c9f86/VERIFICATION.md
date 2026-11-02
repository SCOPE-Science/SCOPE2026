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

# Verification
Run `python3 verify_marked_cycles.py` with the standard Python library, inside the directory containing this file and `verification_output.txt`. The test performs two independent exhaustive finite recurrences for rank-type equivalence: unary color-support refinement and full formula-type recursion for two variable assignments. It checks all 3,872 ordered length-pair/rank combinations with lengths 3 through 24 and ranks 1 through 8. A clean run yields the exact provided output.

The infinite parameter statement is justified by the structural inductive palette proof in `RESULT.md`; the bounded tests do not independently establish it. Literary priority has not been exhaustively established. Independent mathematical audit has not been carried out.
