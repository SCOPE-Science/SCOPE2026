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

`artifacts/verify.py` reconstructs the even Poincaré polynomials with exact integer arithmetic from the published recurrence, checks the displayed source values through n=10, reconstructs the reciprocal reductions, and verifies every exact rational sign bracket stored in `artifacts/root_brackets.json`.

The proof certificate uses only sign evaluations at rational points and degree counting. Floating-point approximations are not part of verification.

The saved successful replay is `artifacts/verification_output.txt`.
