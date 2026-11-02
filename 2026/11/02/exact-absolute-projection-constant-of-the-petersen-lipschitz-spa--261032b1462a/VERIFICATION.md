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

# Verification of the Petersen Lipschitz projection constant

Run `python verify_petersen_projection.py` using Python 3 with the standard library. Actual output:

```
CHECK_OK automorphisms=120 signed_stabilizer_rank=12 hodge_rows=15 rational_projector_identities=yes
```

The checker enumerates the 10 graph vertices and 15 edges from disjoint two-subsets, uses exact fractions for the graph Laplacian inverse on the zero-sum subspace, verifies the Petersen strongly-regular adjacency identity, and tests every entry of \(P^2=P\), \(PB=B\), and \(P^{\mathsf T}=P\) for the proposed 15-by-15 projection. It verifies all \(120\) signed automorphism conjugacy identities, the rank-12 signed-stabilizer constraints leaving precisely three free parameters, the row coefficient support multiplicities and the forcing equations, including the trace identity. The checker has no third-party dependencies.

The exact finite checks provide reproducibility for the nonstandard stabilizer, graph and projection calculations; they do not independently certify the analytic Hahn–Banach/injectivity or averaging arguments. Those arguments are proved in the main text. Historical originality and independent audit are not computationally certified.
