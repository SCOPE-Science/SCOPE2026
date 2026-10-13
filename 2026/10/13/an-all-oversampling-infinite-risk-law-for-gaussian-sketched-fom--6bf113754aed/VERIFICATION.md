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
The standalone `verify.py` evaluates the published one-step sketched Petrov–Galerkin and sketched minimum-residual coefficients on an SPD two-by-two system. It checks their independent Gaussian-direction decompositions, their deterministic residual and energy identities, and the exact Student variance and pole-density constants.

These computations are transcription and algebra guards. The \(1/t\) tail limit and infinite absolute moments for unregularized sketched FOM are established by the analytic density and layer-cake proof in `RESULT.md`, not by a truncated numerical experiment. The result makes no claim of independent audit or global convergence.
