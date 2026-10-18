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

# Reproducibility and proof limits

Run the included `CHECK.py` with a stock Python 3 interpreter, without third-party packages. The expected output is:

```
UNIVERSAL_APEX_CHECKS_OK
face_decompositions 210
finite_field_homology_splittings 255
full_permutation_character_comparisons 34406
cyclic_obstruction_lattice_models 7
```

The checker reconstructs graph membership by connected-component exploration, tests the exact face decomposition for all graphs on two through four labeled vertices, computes ordinary homology ranks modulo \(1000003\) for those and additional five- and six-vertex graphs, computes exterior-power traces independently by signed simplex-face fixed-point counts for all permutations up to seven vertices, and tests the twisted norm signs for cyclic rotations of orders three through nine. Counts reflect instances actually evaluated, not an exhaustive graph census above four vertices.

The infinite proof resides in `RESULT.md`: the apex faces are exactly the cone on a simplex skeleton, the skeleton inclusion is null-homotopic by an old-vertex cone, the relative homology is the exterior augmentation lattice, the complete-graph top cycles form a genuine integral regular orbit basis, and the \(\operatorname{Ext}^{1}\) calculation is a projective-resolution cokernel equal to \(\mathbb Z/n\mathbb Z\). This is a proof of an exact obstruction order and nonexistence of equivariant retractions, not a proof that arbitrary integral equivariant decompositions are classified. No independent audit has been performed.
