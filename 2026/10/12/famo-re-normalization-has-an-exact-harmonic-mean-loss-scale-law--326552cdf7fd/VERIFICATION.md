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
The package verifies the exact task-rescaling law of paper-form FAMO.

`verify.py` checks randomized positive task objectives, simplex coefficients, vector gradients, and independent scale factors against the weighted harmonic-mean multiplier. It also replays a deterministic two-task quadratic example and verifies exact full-trajectory equivalence under common loss scaling with reciprocal model-learning-rate compensation.

The computations are transcription guards. The rescaling identity and trajectory equivalence are proved algebraically in `RESULT.md`.
