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

# Mathematical verification

Execute `python verify.py` from the directory containing this file. The program uses only Python standard libraries and exact integer/fraction arithmetic. It compares the exact cherry-count distribution root-split recurrence for all PDA tree sizes through twenty with the analytic moments and conditional variance identity; it also verifies parity factorization and the strict optimal split through two hundred leaves. The reported pass establishes those finite and algebraic identities only; the proof in `RESULT.md` establishes the universal theorem using concavity, positive-coefficient shifted polynomials and finitely many exceptional evaluations.

This work has not undergone independent audit or third-party reproduction. Prior published marginal moments are distinguished from the conditional extremum theorem; complete historical-priority coverage is not claimed.
