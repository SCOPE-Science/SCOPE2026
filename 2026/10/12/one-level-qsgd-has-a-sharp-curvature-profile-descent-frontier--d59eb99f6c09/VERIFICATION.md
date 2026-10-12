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
The package reconstructs the \(s=1\) QSGD distribution and the diagonal quadratic objective directly.

`verify.py` enumerates every Bernoulli support pattern in dimensions up to eight, checks the exact conditional expectation formula against the discrete distribution, and verifies the sharp threshold on random diagonal curvature profiles. It separately checks the attaining equal-coordinate-magnitude direction and the isotropic minimax factor.

Finite enumeration is a transcription guard only. The all-dimensional result follows from the exact coordinate moments and the sharp Cauchy--Schwarz argument in `RESULT.md`.
