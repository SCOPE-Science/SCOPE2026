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

Run `python verify.py` alongside the other files in this package. The script requires only Python standard-library modules and uses exact rational arithmetic. The completed verification enumerated every \(\{1,2\}\)-valued initial state on cycles of lengths \(4\) through \(10\) at seven rational coupling values \(5/4,3/2,7/4,2,9/4,5/2,4\), for 14,224 configurations. Each trajectory is independently updated for five steps and matched to the predicted eventual state or two-cycle. Exact uniform-initialization averages were checked against the claimed formulas. All checks passed.

The proof in `RESULT.md`, rather than the finite enumeration, establishes the universal parameter and cycle-size assertions. The verification does not cover other graph families, nonuniform interactions, different initial biomass distributions, or historical originality. There has been no independent scientific audit.
