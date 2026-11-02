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

The included program `verify_envelope.py` was executed against the included standalone source code. It produced the included `verification_output.txt`, which records 1,612 passed assertions. The exact checks enumerate all parent histories in three nonuniform rational-weight trees of four vertices, compare the conditional innovation variances with the analytical recurrence, test the completed-square identity and deficit relation over rational grids, and verify finite-horizon strict global dominance. An additional deterministic numerical test compares large-horizon recurrence values with the predicted asymptotic scale. Numerical tests do **not** certify the asymptotic theorem, whose proof is in RESULT.md.

The independent audit is not performed, and no claim of third-party certification is made.
