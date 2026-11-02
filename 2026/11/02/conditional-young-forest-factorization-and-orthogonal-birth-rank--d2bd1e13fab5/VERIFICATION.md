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

The theorem is proved analytically in RESULT.md by conditional independence of previously hidden component roots and Pólya urn moments. Its assumptions include independent uniform parent choices, fixed integer \(n\ge2\), and deterministic ancestor weights. The exact conditional law concerns the entire labeled younger forest and is *not* a claim that subtree sizes are jointly independent.

The standalone `verify.py` enumerates the complete parent-vector space for each size from 2 through 8, totalling 5,913 trees. It independently constructs parent-restricted forests and descendant sizes, checks all coefficients of each observed conditional probability-generating polynomial, checks all size covariances and variances, and checks three deterministic weight profiles. It completed 9,326 exact rational assertions and reproduced the four-vertex dependence witness. This is a finite validation; general correctness follows from the structural proof, not a finite stopping point.

The available literature comparisons are necessarily non-exhaustive. Earlier standard total-path-length variance formulas and Pólya urn moments are background; historical priority of the precise conditional representation is qualified. Independent audit: not performed.
