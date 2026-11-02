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

## Reproducibility checks

Run `python3 CHECK.py` in the directory containing both `CHECK.py` and `CHECK_OUTPUT.txt`.
The program uses only the Python standard library and enumerates all multiplication-table pairs in its named finite examples; it also checks the finite-field rank formulas and convex-order stop-loss inequalities at the support breakpoints.
The expected terminal marker is `VERIFY_OK`, and the recorded output appears in `CHECK_OUTPUT.txt`.

These finite computations do not by themselves establish the universal theorem. The universal proof rests on nilpotence lifting over a nilpotent ideal, an exact matrix nilpotent count, uniformity of a block restriction, rank enumeration, and the chord inequality for convex functions.

The relative variance identity for dimension two is also obtained symbolically in the proof. The strict comparison for arbitrary semisimple products follows by iterative replacement of independent positive factors, not from the finite tests.

No independent mathematical audit has been performed.
