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

The universal theorem is proved symbolically in `RESULT.md`; finite computation is not used to infer an infinite statement.

`verify.py` uses Python standard-library exact integers and `fractions.Fraction`. It checks the expanded SQN objective against the recurrence, the exact discriminants and endpoint values used in the sign proof, direct exhaustive SQN agreement for alphabet sizes 2 through 5, the reduced exact optimizer for alphabet sizes 2 through 9, and the claimed Blackburn equality for every alphabet size from 10 through 80.

Observed terminal line:

`VERIFY_OK theorem_q_min=10 scan_q_max=80 q9_exception=33872 blackburn_q9=33614`

The scan through 80 is a stress test. The proof for every integer alphabet size at least ten is the normalized branch argument in `RESULT.md`.
