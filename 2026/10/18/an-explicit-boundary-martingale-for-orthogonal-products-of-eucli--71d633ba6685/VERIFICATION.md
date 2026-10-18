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

The supplied `verify.py` is a standalone standard-library checker. Execute `python verify.py` in an ordinary Python 3 environment. It checks 128 exact rational surface-mixture/covariance identities across dimension triples, and performs a fixed-seed simulation of 60,000 pairs in a mixed-radius three-dimensional cylindrical example. The expected exact squared-distance excess is 0.864040404... and the observed finite-sample value on the specified deterministic seed is 0.859806539...

Analytical proof checks: (1) boundary stratum Euclidean area weights are dimension/radius ratios; (2) the sign flip conditioned on a radial point preserves its vector mean; (3) uniform directions with a radial-dependent sign still give uniform surface directions; (4) Jensen proves all finite convex observables; (5) blockwise second moments establish the exact covariance gap. The standalone checker tests finite instances only and is not an independent audit or a substitute for the proof. Full text of the motivating convex-order preprint remained inaccessible; corresponding literature-priority risk remains explicit.
