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

# Verification and scientific limits

Run `python3 verify_heawood_action.py` using Python 3 standard library. The checker does not download data. It reconstructs the exact Fano-plane incidence relation, enumerates all 3461 matching simplices, and calculates the complete mod-two simplicial boundary ranks (20, 148, 496, 722, 312, 24). The proof in RESULT.md explains why chain rank bounds force the same ranks over the rational numbers.

The checker finds exactly 168 bipartition-preserving incidence automorphisms and, using an explicit point–line duality, all 336 full graph automorphisms. It uses two independent fixed-matching descriptions to calculate identical signed Lefschetz traces for every element. It also constructs eight distinct Sylow-seven subgroups, calculates their reduced permutation character, and verifies the exact orthonormality matrix for the trivial, seven-dimensional and residual eight-dimensional rational characters. Successful execution ends with `VERIFY_OK`, followed by the face vector, rank vector and group-character type counts.

There is no claimed integral irreducible splitting, no equivariant homotopy equivalence, and no independence or external certification. Computation is exhaustive for the specified finite graph; it does not support a claim for all incidence graphs.
