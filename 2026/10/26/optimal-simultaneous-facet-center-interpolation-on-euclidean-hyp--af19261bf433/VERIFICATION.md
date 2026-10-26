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
# Reproducible verification

Run `python3 verify.py` in the same directory. Only the Python standard library is required.

The script builds all original vertices and facet centers for each cube dimension \(3\) through \(8\). It computes actual vertex-to-center mean transport costs using every original vertex, verifies the closed binomial values for both vertex-orbit types, and checks the exact center-to-center transport values against the ambient distances. For the two center-orbits, analytic support lower bounds and explicit matching couplings are supplied in `RESULT.md`. It additionally checks a coordinate-deletion lower-bound witness for seven signed near/far mass choices.

The executed test produced: dimensions \(3\) to \(8\) PASS, **7,152** vertex–center comparisons, **365** center–center pair classifications, and all signed-orbit expectation checks PASS. Reproducibility is by source code and exact formulas, not by preservation of a machine-specific run log.

The computations are finite. In particular, they cannot prove optimality for arbitrary dimension, arbitrary nonsymmetric signed extension operators, or absence of prior coverage. Those scientific points are addressed, respectively, by the symmetry-averaged lower bound, all-dimensional analytic inequality, and documented literature comparisons in `RESULT.md` and `REVIEW.md`. Independent mathematical audit has not been performed.
