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
The package verifies the exact bilinear stability lens for Symplectic Gradient Adjustment.

`verify.py` constructs full bilinear game matrices with prescribed singular values, reconstructs the SGA iteration, and checks its operator norm against the closed singular-mode formula. It verifies strict contraction below the threshold, unit top-mode modulus at equality, expansion above it, the reciprocal fixed-step adjustment boundaries, and the exact comparison ratio to the later sufficient quadratic-game bound.

The computations are transcription guards. The if-and-only-if result and its sharp boundary witnesses are proved algebraically in `RESULT.md`.
