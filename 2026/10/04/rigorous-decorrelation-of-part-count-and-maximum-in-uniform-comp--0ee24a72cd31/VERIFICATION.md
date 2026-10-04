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

For every bit-string length \(1\le n\le16\), it exhaustively enumerates all strings, computes the number of ones and longest zero run, and verifies the covariance by two independent formulas: direct mixed moments and the coordinate-influence identity.

For every adjacent pair of fixed-weight slices it reconstructs the complete longest-run distributions and verifies strict first-order stochastic decrease.

It also verifies the explicit covariance upper bound for every tested length.

The classical longest-run variance input is not inferred from finite replay; it is taken from the cited asymptotic literature.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK bitstrings_checked=131070 covariance_checks=16 influence_checks=16 stochastic_order_checks=136 bound_checks=16`.
