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

# Verification record

The proof uses exact algebraic orbit counts and a degree-bound estimate for nonzero determinant polynomials. The latter is valid over arbitrary finite fields, not just prime fields. The full-support sample is conditioned on matrix invertibility; the checker independently tests that conditioning in three prime-field cases.

Run `python evolution_fullsupport_checker.py` with standard Python 3; compare with `evolution_fullsupport_checker_output.txt`. The program directly enumerates 328192 full-support matrices over small prime fields, verifies transposition lift compatibility, independently evaluates ranks, and enumerates 5877 nonidentity index permutations to test the support/deficit inequalities. Outputs from finite enumeration are corroboration only; they cannot certify the infinitely many large-field cases.

The exact transposition count follows from the group-equation calculation rather than from a sampling extrapolation. A possible older equivalent asymptotic stabilizer result is not excluded by the searches performed. No independent mathematical audit or external certification is claimed.
