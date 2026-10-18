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

# Verification of the product-spectrum theorem

The analytic proof is in `RESULT.md`. Its decisive identities are the exact factorization of facet masses, the same-factor ridge conductance, and the cross-factor ridge conductance. The weighted operator then reduces to a direct sum of centered factor eigenmodes and a finite block-constant sector. The latter has eigenvalues zero and the ambient dimension, with the latter repeated one less than the number of factors. No computer enumeration is used to infer the general theorem.

The executable `verify.py` uses only Python's standard library. It builds exact rational networks from independently specified regular cross-polytopes and segments, forms the product masses and edge conductances, and checks every predicted even Walsh eigenvector and the block-constant eigenvectors by direct application of the mass-normalized graph Laplacian. The command `python verify.py` succeeded with the exact output:

`VERIFY_OK exact weighted facet graph eigenidentities 26 product networks; largest dimension 10`

The finite tests cover 26 products and ambient dimensions through ten; they do not exhaust all polytopes or establish the infinite theorem. The proof covers general polytopes via the exact geometric identity. Bibliographic uniqueness and independent mathematical audit are not certified.
