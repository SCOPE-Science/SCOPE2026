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

The continuous theorem follows from a rank-one killed Green-resolvent calculation (two one-attempt transforms), renewal, an exact geometric series, and Laplace/generating-function inversion; details and assumptions are in RESULT.md. The Brownian image Green density is explicitly calculated there. The accompanying checker independently solves absorbing finite birth–death Markov chains, with resetting and local-time penalties appearing together in a tilted linear system. This gives 729 direct-vs-predicted bivariate-transform comparisons and 135 Brownian analytical identity checks, all passing. These are corroborating finite models; the continuous proof is analytic. A scholarly priority determination beyond accessible primary texts is not performed.
