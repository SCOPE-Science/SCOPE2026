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

The proof is analytic for every \(n\ge2\), every position, and every deterministic real weight vector.

`checker.py` exhaustively enumerates every permutation for \(2\le n\le9\). It checks all local record/Spearman covariances, conditional Spearman means, the total-record covariance, the record-count variance, the Spearman variance, and the correlation-squared formula. For \(2\le n\le8\), it additionally checks the arbitrary-weight covariance theorem on several signed integer weight sequences.

A separate exact finite-sum calculation through \(n=100\) verifies the expected maximum of a uniform prefix subset and the mean of each earlier selected value, independently replaying the critical conditional step.

Finite computations are supplementary and do not establish the universal quantifiers.
