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

The analytic check rewrites the source sums as Riemann sums and verifies uniform convergence of the removable-singularity integrands on each fixed compact density interval. The standard exponential-integral series then prove the closed forms and their derivatives.

The bundled `verify.py` evaluates the two convergent series, checks the source's quoted values at several densities, and compares direct finite-\(M\) sums against the limiting values. Its successful output is `VERIFY_OK`.

Limits: the computation is not used as a proof of the infinite-\(M\) limit. The result evaluates the threshold functions already present in the source; it does not independently derive the source's evolutionary fixation conditions.
