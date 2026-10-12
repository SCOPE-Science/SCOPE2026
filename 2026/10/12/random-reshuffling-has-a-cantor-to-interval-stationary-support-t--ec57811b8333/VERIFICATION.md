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
The package reconstructs both possible two-sample random-reshuffling epoch maps from the component gradients.

`verify.py` checks the exact affine recurrence, the invariant second moment, equality with the defining source's two-sample quadratic MSD expression, the exact central-gap endpoints, finite-depth separation in the Cantor regime, and exact interval tiling at the boundary contraction \(r=1/2\).

Finite calculations are transcription guards only. The infinite invariant-law and support results are proved analytically in `RESULT.md`.
