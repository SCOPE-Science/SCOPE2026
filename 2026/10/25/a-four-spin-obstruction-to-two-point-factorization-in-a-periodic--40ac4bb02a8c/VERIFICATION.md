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

The local finite-state checker `verify.py` builds the full rate generator, obtains a normalized stationary distribution, and checks positivity, the master-equation residual, seven stationary moments, an exact cumulant and the three-distinct-bath sign witness for six and nine spins. Execute `python verify.py` with `numpy` and `scipy` as listed in `requirements.txt`.

The analytical proof requires more than these calculations. Exact closed local moment equations give the formulas for all admissible ring sizes and infinite volume at the hot-bath endpoint. A marked-clock ancestry coupling gives the independent-of-size sixteen-delta perturbation bound and guarantees uniqueness for all parameters strictly below one.

No independent review is claimed. Verification of priority remains bounded by inspected source availability; the strictly finite-bath example is certified by an analytic inequality, not solely by floating-point computation.
