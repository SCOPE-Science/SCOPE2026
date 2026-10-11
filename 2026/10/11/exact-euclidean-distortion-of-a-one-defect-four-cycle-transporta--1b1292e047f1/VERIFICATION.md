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

The analytic proof gives exact outer and inner quadratic extrema over the full parameter interval \(0<t\le3\) and reduces global Euclidean distortion to a one-variable minimization. It uses group averaging to cover every Euclidean position, including non-symmetric ones. The four-branch formula is therefore not a finite-data conjecture.

Execute the included `verify_weighted_cycle.py` using Python 3 standard library. The check independently enumerates every candidate vertex of the cube clipped by the two slab planes, optimizes along facets in exact rational arithmetic, tests the proposed optimal quadratic form, and compares against a grid of alternative rational quadratic forms. It performs 189 separate rational checks and prints `WEIGHTED_CYCLE_RATIONAL_CHECK_OK 189`.

The test does not exhaust all real \(t\) or all real quadratic forms. Its scope is diagnostic; the analytic proof supplies those quantifiers. The sharpness witnesses are the explicit boundary/vertex configurations in RESULT.md. The finding is restricted to real spaces and one distinguished edge of a four-cycle.
