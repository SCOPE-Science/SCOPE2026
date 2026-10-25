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

# Mathematical verification and limitations

The critical Hermite ambiguity formula is reduced to three explicit radial Laguerre-polynomial squares in `RESULT.md`. A positive primal and dual solution proves a tight two-node covering bound. The disk boundary forces the sharp upper expansion; an explicit feasible allocation, compact local quadratic zero estimates, and monotone radial tails establish the lower expansion. A compactness/unique-LP-optimizer argument proves asymptotic precision shares for all maximizing allocations.

Run `python verify.py` with Python 3's standard library. The checker ran successfully with **844 finite numerical assertions**. It tests the primal/dual equalities and positivity, the weight normalization, stationarity-based minima, and finite-radius bounds at \(R=12,14,16,18,20,22,24,27,30,34\). Floating-point checks are illustrative, not complete certificates of asymptotic limits or of global uniqueness at fixed \(R\).

The theorem does not cover sampled reconstruction, nonlinear phase retrieval, or more than three Hermite windows. No independent verification of the asserted asymptotic theorem is represented in this record.
