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
The package verifies SPI-Optimizer's exact overshoot branch on a scalar quadratic.

`verify.py` replays the source sign-gated momentum update over deterministic parameter grids, checks permanent momentum erasure and the closed form after the first crossing, verifies the neutral two-cycle at \(r\lambda=2\), and compares the sharp SPI boundary against ordinary-momentum eigenvalues.

The computations are transcription guards. The phase law is proved analytically in `RESULT.md`.
