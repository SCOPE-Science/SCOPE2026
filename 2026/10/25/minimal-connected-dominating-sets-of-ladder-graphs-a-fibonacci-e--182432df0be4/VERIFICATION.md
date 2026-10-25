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

# Verification procedure and scope

Use `python3 verify_ladder.py` with Python 3. The program constructs the original ladder graph, tests every nonempty vertex subset for domination and connectedness, then tests each one-vertex deletion for minimality. It separately constructs all words allowed by the proposed structural classification and demands equality of the two vertex-set families. The graph tests do not assume the classification. The enumeration is exhaustive only for \(2\le n\le10\); 1,398,087 nonempty subsets are checked. The program then checks the 49 coefficients indexed 2 through 50 of the univariate generating-function recurrence against the explicit Fibonacci formula, using exact integer arithmetic.

The recorded full output is `verification_output.txt`. All assertions passed. Larger sizes are proved structurally in `RESULT.md`, not computationally certified by the finite run. Scientific originality cannot be settled by this verifier; an independent audit remains unperformed.
