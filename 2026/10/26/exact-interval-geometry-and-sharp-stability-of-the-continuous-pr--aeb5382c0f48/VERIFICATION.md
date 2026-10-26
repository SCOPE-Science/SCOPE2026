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

## Direct checks

The algebraic proof covers all finite electorate sizes, all peak multiplicities, all candidates in the continuum, and all nonnegative relaxation parameters. Directly computed exact-rational checks of 26,874 finite configurations compare the formula with the original coalitional blocking rule, including boundary candidates, arbitrary coalitions, and perturbation sensitivity. Reproduce with `python pvc_interval_checker.py`; it uses only Python's standard library.

## Interpretation and limits

The finite enumeration is not treated as a proof of a universal real-variable theorem. The main proof independently derives the prefix/suffix reduction, the interval and nonemptiness, and the optimal perturbation constant. A separate independent scientific audit has not been performed. The precise historical-originality assessment is conditional on accessible literature, as documented in the review.
