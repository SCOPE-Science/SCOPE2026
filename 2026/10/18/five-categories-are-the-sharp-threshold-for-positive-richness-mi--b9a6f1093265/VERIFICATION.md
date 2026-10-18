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
# Reproducibility and limits

The accompanying standalone `verify.py` runs with Python 3 and only the standard library. It enumerates ordered draw pairs with exact rational probabilities and computes richness, missing mass, expectations, and covariance directly. For multiple all-positive rational laws, it compares this directly enumerated covariance with the power-sum formula and checks negativity when the support has two through four atoms. It also checks the exact five-category witness, examples on larger supports, the uniform formula, and the one-heavy factorizations. The successful local execution printed `PASS exact checks: 10730` and `Five-species witness: 1/1600`.

These tests are finite rational checks only. The proof for arbitrary real probability masses rests on the constrained-maximum classification and symbolic sign arguments given in `RESULT.md`. The second-order constraint qualification requires nonuniform positive masses, and uniform/boundary cases are treated separately. The finite checker does not verify historical originality or replace an independent audit.
