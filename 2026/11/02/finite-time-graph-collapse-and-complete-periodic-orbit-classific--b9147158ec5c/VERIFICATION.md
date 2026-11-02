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

# Verification details

The standalone `verification/polyhedral_certificate.py` uses exact `fractions.Fraction` calculations to propagate the full square \([-93,93]^2\) under the piecewise-affine map for nine steps. At every stage it clips at both coordinate axes and takes exact convex hulls of affine images, preserving full coverage of the continuously infinite starting set. The generated piece counts are \(4,13,21,29,33,31,28,23,18\); the final pieces are five points and thirteen segments, all contained edgewise in the specified invariant graph. The script checks all vertices and the common supporting segment before issuing `CERTIFICATE PASS`.

The accompanying proof independently supplies the five-step nilpotence of the homogeneous map, the global perturbation radius 93, the exact scalar return branches, the expanding two-step return near the exceptional four-cycle, and the invariant-probability argument. These are analytic claims, not empirical inferences from finite samples. The fourteen-step bound is an exhibited certificate rather than an optimality claim, and there is no uniform upper bound on eventual-periodic settling times.

No independent external scientific audit or proof-assistant certification has been performed.
