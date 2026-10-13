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
The package reconstructs the first source-form Adafactor matrix step on a \(2\times2\) isotropic quadratic.

`verify.py` forms \(G^2+\epsilon_1\mathbf1\mathbf1^\top\), computes row and column marginals, reconstructs the rank-one second moment, performs matrix-RMS update clipping, applies the parameter-relative scale, and checks the default objective increase using high-precision decimal arithmetic.

It also checks increasing scale-separation sequences against the two proved limiting ratios. Finite computations are transcription guards only; the limits are proved in `RESULT.md`.
