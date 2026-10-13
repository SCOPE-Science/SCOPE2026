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

# Verification record

Run `python3 verify_coverage.py` with Python 3 and only its standard library. The checker constructs points and lines in \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\), verifies cardinalities, regularity and unique pair incidence, and exhaustively enumerates \(127\) and \(8191\) nonempty missing-point sets. It reproduces all signed avoidance coefficients and complete-model coefficients by exact integer arithmetic. It checks the displayed rational tail differences for \(t=4,5,6\), compares the two finite exponential representations over twenty small time horizons using exact fractions, and checks the two strict analytic positive lower-bound constants.

An additional, separate exact cross-check computed finite-time coverage probabilities by summing the onto-assignment counts over line subfamilies whose union is the full point set: the finite horizons tested in each geometry agreed with the missing-point inclusion-exclusion calculations. This independent derivation is a consistency check, not an independent scientific audit.

The universal comparisons for *all* integers \(t\ge7\) rest on the analytical grouping of decreasing exponential ratios and its positive rational thresholds in `RESULT.md`, not on the finite checker loop. The proof does not cover larger projective planes, general fair block mechanisms, or asymptotic stochastic comparisons in an increasing-plane-order limit. Independent scientific validation has not been performed.
