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
# Verification record
The included `verify.py` evaluates the exact affine section equation for cyclic random-radius polygons with \(N\in\{3,4,5,6,7,10,15\}\), randomly chosen positive \(\omega_i,\lambda_i\), and both positive and negative radial displacements. It checks unperturbed crossing times, tuned perturbed times, full-revolution timing and contraction, nonzero detuned time shift, and the common regular-polygon closed form. Execute `python3 verify.py` with the Python standard library.

Analytical obligations and proof limitations: the theorem uses the explicitly integrated local vector field and positive transversality at each unperturbed vertex; small neighborhoods exist by continuity. This establishes universal edge crossing and local straight-line isochrons; finite computational runs do not prove the general case, rule out remote invariant sets, or independently certify bibliographic novelty. No independent mathematical audit has been performed.
