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

The theorem is analytic for every \(n\ge2\) and every deterministic real weight vector.

`checker.py` exhaustively enumerates every permutation for \(2\le n\le9\). It verifies the local arbitrary-weight covariance for four weight families, including constant weights, and separately checks the local squared-displacement and Spearman identities, conditional Spearman means, total covariances, both marginal variances, and the exact correlation-squared formula.

A second exact-rational loop through \(n=1000\) verifies the conditional-coordinate means, local formulas, pairwise excedance probabilities, and the summed excedance variance from the closed identities.

Finite enumeration is supplementary and is not used as proof of the universal statement.
