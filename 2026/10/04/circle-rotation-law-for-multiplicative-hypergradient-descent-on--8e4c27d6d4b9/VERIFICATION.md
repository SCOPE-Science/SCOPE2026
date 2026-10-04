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
The package verifies the exact scalar multiplicative Hypergradient Descent map and its log-circle representation.

`verify.py` checks finite entry into the invariant band, the circle-rotation identity, the exact period-three example, finite dense coverage for the analytically proven irrational example, and the primal contraction after band entry.

Finite coverage tests are transcription guards. Rational periodicity, irrational density, and irrationality for \(\beta=1/2\) are proved analytically in `RESULT.md`.
