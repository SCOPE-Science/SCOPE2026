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

Execute `python3 artifacts/verify.py`. This requires only Python's standard library. The program evaluates all \(\binom92=36\) Jordan products in both explicit seeds; checks that their sum with the prescribed parameter matrix is exactly a square of an integral upper-triangular matrix; ensures nine pairwise distinct nonzero matrices and nonzero Jordan products; and repeats the check on seven nonzero positive and negative scaling parameters for both diagonal scaling types. It prints exact divisibility witnesses for the six diagonal-pair cases. Total tested pair identities: 1080.

The proof of the infinite statement is in the symbolic product identities and scaling transformations in RESULT.md, together with the published upper bound of nine. Finite tests do not prove infinite assertions. The bibliography and unindexed sources pose a residual literature limitation. Independent audit: not yet performed.
