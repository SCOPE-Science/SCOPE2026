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
# Verification of the finite-sample signed-triangle identity

Running `python verify.py` (Python standard library) reproduces exact rational computations: the formula's mean and variance for \(n=3\) and \(n=4\) via an independent exhaustive finite latent-vector model that matches all required moments; the strictly positive analytic slope; and the explicit signs at \(n=6,7\).

The finite four-vector latent law reproduces the necessary moment tensors but is not claimed to reproduce every distributional feature of the uniform sphere. The proof in RESULT.md establishes the general theorem using only the shared moment identities and the complete covariance partition. Computation is not a substitute for the general proof.
