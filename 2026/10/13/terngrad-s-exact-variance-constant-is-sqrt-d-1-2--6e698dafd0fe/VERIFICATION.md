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
The package reconstructs the source TernGrad Bernoulli quantizer.

`verify.py` enumerates every mask for random vectors in dimensions up to eight and checks unbiasedness, the exact second moment, and the exact variance. It verifies the sharp equality family across many dimensions, tests random vectors against the proved constant, and independently computes the compressed isotropic-quadratic objective expectation.

It also checks the strict-descent boundary and minimax step on equality vectors.

Finite enumeration and random tests are transcription guards only. The all-dimensional minimal variance constant, equality family, and exact optimization frontier are proved analytically in `RESULT.md`.
