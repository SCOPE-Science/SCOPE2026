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
# Reproducibility and boundaries

Run `python verification.py` with Python 3 and `mpmath` installed. The reproducibility code independently constructs exact equidistributed nodes using cumulative-monitor inversion, constructs their consecutive-log expression, verifies ordering and strict maximum-ratio equivalences for randomized finite grids, checks a range of imposed caps, and prints root and representative minimum counts. The completed execution reported **PASS: 1296 independent high-precision comparisons** and \(u_{1+\sqrt2}=0.3588231634265831584937248220685824078596914898275061065\ldots\).

The universally quantified proof is analytic: a positive Laplace-transform identity and strict log-convexity imply the endpoint is the maximum; the limiting range and strict monotonicity give the unique cutoff. Finite tests verify implementations and examples but do not certify infinite parameter ranges. No independent audit, independent replication, or higher-order integrator validation has been performed. No statement about the full adaptive discretization follows automatically from this ideal-mesh theorem.
