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

# Reproducible verification

Execute `python3 paley17_verify.py` with standard Python 3. The implementation constructs quadratic residues of \(\mathbb F_{17}\), all faces of \(\operatorname{Cl}(P_{17})\), an explicit valid spanning tree, a maximal-tree presentation, and signed simplicial chain actions. It performs these checks without network access or third-party modules.

The output of the completed execution was:

```
PI1_T0_RELATOR_ELIMINATIONS_VERIFIED 52
INTEGER_FREE_H2_RANK_BY_PI1_AND_EULER_VERIFIED 16
ALL_AFFINE_LEFSCHETZ_CHARACTERS_VERIFIED 136
PALEY17_WEDGE_AND_AFFINE_CHARACTER_VERIFIED
```

Every triangular-relator substitution is recomputed and verified to eliminate a unique generator; all remaining relators are empty. A separate mod-two rank check confirms rank \(52\) for the triangle boundary. Graph diameter two and the absence of four-cliques are exhaustively checked. The symmetry check independently evaluates oriented chain traces for each of the 136 maps and matches the three predicted classes.

The program establishes the stated **finite** combinatorial certificate. The conversion of the trivial fundamental-group presentation and Euler characteristic to a sphere wedge, and of group characters to rational module isomorphism, uses standard mathematical theorems stated in `RESULT.md`. It does not calculate integral equivariant module extensions or prove a family-wide Paley graph theorem. Independent mathematical assessment is not included.
