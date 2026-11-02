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

# Reproducible checks

Run `python verify.py` using a recent Python 3 interpreter with only the standard library. It enumerates all possible two-hub firing words of lengths 3 and 4 and both peripheral phase choices, calculates exact integer chip-height intervals and binomially weighted populations for page counts from 1 through 25, and checks the two symbolic formulas. An independent direct update simulation examines all confined labelled chip configurations for page counts 1 through 6 and counts actual least-period 3 and 4 states. The largest direct case enumerates 802,816 confined configurations. The recorded output in `verifier_output.txt` should end in `BOOK_PHASE_34_VERIFY_OK`.

The proof for every positive page count is in RESULT.md. Neither finite enumeration nor checker success establishes novelty, independence or arbitrary-parameter correctness without the analytic proof. Nonperiodic states and other periods are outside scope.
