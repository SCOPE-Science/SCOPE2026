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

# Verification and reproducibility
The formal all-parameter proof identifies all \(2n+1\) facets, computes the signed-coordinate image of the saturated integral character lattice, and checks the canonical Cartier pairing on each cone ray. No computer package is used to assert these general facts.

`CHECKER.py` is a standalone Python 3 script using only standard-library modules (`fractions`, `itertools`, `math`). Running `python3 CHECKER.py` produces exactly `CHECKER_OUTPUT.txt` for the listed finite ranges. The exact rational matrix-rank computations check facet support and the predicted local incidence data for 682 fixed-point configurations. The test cannot rule out unforeseen behavior outside its parameters and does not independently certify any theorem or novelty assessment.

Limitations: no computation of the whole toric singular scheme, the local analytic equations at non-fixed points, or the canonical ring. The public sources and mathematical steps are recorded in `RESULT.md` and `REVIEW.md`. Independent mathematical audit has not been performed.
