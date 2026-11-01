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

# Reproducibility and limits

Run `python3 verify_parallelogram.py` with the standard Python library. It performs an independent finite reconstruction of the arclength integrals of \(|x|^{2k}\), for \(k=0,1,2,3\), from each of the four oriented edges of a rationally parametrized nondegenerate parallelogram. Every coefficient is an exact `fractions.Fraction`.

A completed invocation returned:

`EXACT_CHECK_OK systems=305 E0 E2 E4 area-deficit E6 convex-power equality; square_cases=3`

For each of 305 systems the checked invariants include the Euclidean perimeter, quadratic radial moment \(L^3/48\), the quartic formula \(L^5/1280-LA^2/12\), its sharp deficit from the equal-perimeter square, the strict equality condition for the quartic difference, and the nonnegative sixth-moment comparison. This program is not exhaustive across all real parameters, does not test all convex functions, and does not establish the proof's \(C^2\) rigidity step. Those parts follow from the analytic argument in `RESULT.md`.

No independent mathematical audit has been performed.
