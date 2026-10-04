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
The package reconstructs the zero-momentum, zero-smoothing Padam boundary recurrence on a deterministic scalar quadratic.

`verify.py` checks the exact reduction to the max-memory scalar recurrence, agreement between direct Padam simulation and the reduced map, persistence above \(2\) for exponents at and below one quarter, finite crossing for representative exponents above one quarter, and convergence of the historical maximum to the predicted critical radius.

Finite simulations are transcription guards. The infinite-time dichotomy is proved analytically in `RESULT.md`.
