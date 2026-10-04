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
The package verifies the exact mean-square law for paper-form AdaHessian without spatial averaging.

`verify.py` exhaustively enumerates Rademacher vectors for small matrices, checks single- and multi-probe moments, simulates bias-corrected Hessian RMS expectations, and compares numerical two-dimensional orientation maxima with the closed-form condition-number factor.

Finite enumeration and Monte Carlo checks are transcription guards. The expectation identities and sharp extremum are proved analytically in `RESULT.md`.
