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

# Verification

The analytic derivation begins with the exact joint probability of two prescribed, disjoint connected-component events. A shared absence requirement for each of the cross-edges gives factor \( (1-p)^{-hk} \). Summation over disjoint vertex sets supplies the falling-factorial ratio. The strictly ordered threshold is derived from a rectangular average of strictly increasing summands. Fixed-size Taylor expansion gives the displayed second-order threshold and the nonzero critical-window covariance constant.

Run `python verify_component_covariance.py` using Python 3.9 or newer and the standard library. In the completed package this executed successfully with `PASS 8676 exact pair-moment and numeric threshold checks`. The tests exhaustively enumerate graphs through six vertices and several probabilities. They do not prove the all-size statements.

The historical-priority check was not exhaustive. The 1990 tree-census full text was not accessible; the accessible abstract establishes the already-known first-order Gaussian component census. Independent mathematical audit has not been performed.
