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

The theorem follows from an explicit finite-state exit-time Poisson equation, a stopped horizontal-velocity martingale, a conditional telegraph covariance integral, and the regenerative central-limit theorem under finite-second-moment cycles. The numerical program `verification/check_surface_diffusion.py` was executed from the recorded source with standard-library Python; all tests passed for generator identities, exponential reduction to the known model, strict example ordering, transform inversion, the small-turning limit, and four independently sampled physical excursion/sojourn laws at 65,000 cycles each. Its explicit numerical outputs are reproduced in `RESULT.md`.

Finite simulation is evidence of consistency only, not an exhaustive proof, and no independent audit or external validation was performed. Model restrictions and priority risks appear in `RESULT.md` and `REVIEW.md`.
