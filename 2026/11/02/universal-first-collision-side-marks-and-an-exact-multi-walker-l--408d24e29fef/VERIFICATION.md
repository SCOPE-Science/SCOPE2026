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

# Verification and limitations
Run `python collision_mark_checker.py` using Python 3 and the standard library. This actual embedded checker passed 6,133 exact rational comparisons. It directly enumerates per-vertex moves for all legal count classes in bounded finite parameter ranges and checks total and marked Laplace transforms at three rational values of the Laplace parameter. It does not attempt to exhaust infinitely many graph sizes. The infinite-size exponential limit is justified by an explicit finite-dimensional generator perturbation in `RESULT.md`; no external independent validation has been performed. The marked-side result assumes equal rate-one walker clocks, no initial coincidences, complete bipartite topology, and independent uniformly chosen jumps.
