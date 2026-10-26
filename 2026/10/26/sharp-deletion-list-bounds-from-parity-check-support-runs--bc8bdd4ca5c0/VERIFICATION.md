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

Run `python3 verify_parity_runs.py` using Python 3.9 or later. The executable independently forms every binary hyperplane codeword, deletes all positions, aggregates received-word parent lists, and checks the closed bounds. All nonzero masks at lengths 2 through 9 are checked exhaustively; equality constructions at lengths 10 through 14 are separately checked. The saved `verify_parity_runs.out` gives the complete test summary. These finite enumerations are corroboration, not an exhaustive proof for arbitrarily large lengths.
