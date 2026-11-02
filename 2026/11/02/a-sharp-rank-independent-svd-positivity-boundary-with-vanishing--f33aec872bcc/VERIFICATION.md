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

# Verification performed

The self-contained `verify.py` was run with the Python standard library and returned `PASS: 36 exact-rational dimension/rank cases and the 3x3 illustration`.

It reconstructs the attaining orthogonal projector and block-factorizable positive projector, checks their exact rational idempotence and signs for all intermediate ranks in dimensions 3 through 10, checks the Frobenius-error identities, and confirms the three-dimensional perturbed unique-truncation entry.

The arbitrary-dimensional theorem, sharpness and strict optimization gap rely on the algebraic proof in RESULT.md, not on extrapolation from finite tests. The tests do not assess literature priority, floating-point algorithms, or independent scientific validation.
