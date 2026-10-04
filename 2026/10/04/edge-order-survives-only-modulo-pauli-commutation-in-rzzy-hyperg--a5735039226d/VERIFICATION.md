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

The analytic proof checks the exact Pauli commutation sign for arbitrary pairs of RZZY edge generators. For the two star families it proves pairwise commutation for every edge count and every real choice of weights. For a two-edge chain it proves anticommutation and derives the exact order-overlap formula.

The accompanying `verify.py` independently constructs finite Pauli matrices, checks both star commutation patterns, checks the chain anticommutator, and evaluates the two circuit orders numerically at multiple parameter choices. It prints `VERIFY_OK` when all checks pass.

The finite computation is not evidence for the universal statement by itself; it only checks the indexing, sign conventions, and explicit example against the analytic derivation.
