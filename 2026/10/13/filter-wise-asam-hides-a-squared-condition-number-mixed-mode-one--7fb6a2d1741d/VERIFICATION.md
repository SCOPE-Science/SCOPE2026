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
The package verifies the exact one-filter ASAM mixed-mode formula on the stated two-dimensional quadratic.

`verify.py` reconstructs the perturbation and outer update directly, compares the direct Euclidean ratio with the closed form, checks the if-and-only-if threshold numerically on representative parameters, confirms the asymptotic constant \(4(1+\rho\sqrt2)/\rho^2\), and verifies explicit large-condition-number cases in which both pure eigendirections contract while the balanced-gradient witness expands.

The computations are transcription and asymptotic guards. The exact threshold and its limiting separation are proved analytically in `RESULT.md`.
