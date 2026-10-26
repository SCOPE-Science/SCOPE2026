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

The proof is the sequence of arguments in `RESULT.md`: arithmetic-state invariants, the crossing-run correction, pairwise residual distinguishability, exact reachability by levels, and summation. No finite test is offered as a proof of the infinite statement.

The standalone `check_pattern_shift.py` was run with Python and produced the embedded `check_output.txt`. Its automaton transitions were independently minimized, and outputs were compared against direct pattern enumeration. Tested: 190 dyadic parameter pairs, 194,560 direct inputs, and 405 additional arbitrary-shift parameter pairs. All passed. These are finite corroborating checks only.

The source text was inspected for the relevant definitions and state-complexity claims; the available sources do not establish the presented formula. No claim of exhaustive global priority or independent verification is made.
