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

The proof is analytic. The accompanying checker uses exact integer and rational arithmetic.

It exhaustively generates all labeled trees through \(n=7\) by Prüfer sequences, recomputes one-edge and two-edge inclusion probabilities, and verifies the covariance classes.

For every \(4\le n\le12\), it constructs the grounded covariance matrix and proposed precision matrix and verifies their product is exactly the identity.

For every realized pair orbit it verifies the exact squared partial-correlation formula and the negative sign.

Finite replay does not prove the all-\(n\) theorem; the universal proof is the transfer-current and grounded line-graph calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK trees_enumerated=18247 one_edge_checks=55 two_edge_checks=378 covariance_checks=433 product_entries=11733 partial_orbit_checks=5730`.
