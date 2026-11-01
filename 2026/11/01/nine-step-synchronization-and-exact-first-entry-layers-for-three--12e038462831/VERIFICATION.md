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

The proof uses the exact cohort quotient described in `RESULT.md`, checked exhaustively by `verify_symbolic.py` over 441 representatives. The independently coded *labelled* transition implementation in `verify_labeled.cpp` was run over clique orders 2 through 6 on both sides (25 graph sizes, 1,185,921 initial configurations). Stored outputs are `symbolic_output.txt` and `labeled_output.txt`. A separate independent scientific audit has not been performed. The labelled tests corroborate; the all-size mathematical conclusion follows from the exact quotient and finite case enumeration.
