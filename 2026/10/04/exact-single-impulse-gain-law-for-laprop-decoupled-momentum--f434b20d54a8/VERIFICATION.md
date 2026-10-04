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
The package verifies the exact isolated-gradient response of source-form LaProp and the zero-damping Adam comparison.

`verify.py` replays both recurrences, checks the closed LaProp update terms, evaluates the cumulative gain at representative momenta, verifies numerical monotonicity, and checks the Adam subcritical, critical, and supercritical regimes.

The numerical checks are transcription guards. Finiteness, strict monotonicity, divergence of the LaProp gain, and the Adam threshold are proved analytically in `RESULT.md`.
