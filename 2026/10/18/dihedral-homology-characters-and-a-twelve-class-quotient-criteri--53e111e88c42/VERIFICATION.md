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

The theorem has a self-contained general proof via signed augmented Hopf traces, orbit quotient graphs, periodic independence-polynomial recurrences and rational invariant chains. Its only imported topological premise is the established nonequivariant homotopy type of cycle independence complexes.

Execute `python verify_fixed_faces.py`. This enumerates all independent sets for each \(3\le n\le20\), every rotation and reflection, induced orientation signs and invariant-set sums. The obtained 414 characters match the theorem. It also checks invariant multiplicities from character averaging.

Execute `python verify_chain.py`. This is a separate augmented-chain computation in characteristic \(1000003\), reconstructing simplices, boundary ranks, and traces on boundary spaces to obtain actual homology traces for every group element with \(3\le n\le12\). It checks homology concentration and multiplicity. The program terminates with `CHAIN_REPRESENTATIONS_OK`.

The finite computations check instances only; field calculations do not prove an infinite or integral assertion. The quotient-homology conclusion uses rational averaging (the group order is invertible over \(\mathbb Q\)); it does not infer anything about integral torsion of the orbit space. The original cycle sphere-wedge homotopy classification and known reflection-equivariant comparisons belong to the cited literature. Independent scientific audit has not been performed.
