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

# Verification and its limits

`artifacts/direct_check.py` uses the ordinary Hamming-distance definition to test all 32 vertices against every landmark four-set (35,960 cases), tests all sets of size one through three, builds the unrestricted single-replacement graph of all 1,280 bases, and checks connected components and every distance from each of the 1,280 bases.

Expected final markers:

```text
DIRECT_Q5_ALL_35960_QUADRUPLES_AND_ALL_1280_BFS_PASS
BASES 1280 COMPONENTS 16 COMPONENT_SIZE 80
EDGES 7680 SHELLS {0: 1, 1: 12, 2: 30, 3: 28, 4: 9}
```

`artifacts/algebraic_check.py` independently produces every root/hole/transversal configuration, verifies primitive integer null vectors and absence of ternary null vectors for each basis, reconstructs all legal exchanges by set intersections, and checks every 4-by-4 sign determinant over the 65,536 possible sign matrices.

Expected final markers:

```text
SIGN_MATRIX_80_KERNEL_CLASSES_AND_65536_DETERMINANTS_PASS
BASES 1280 ROOT_CLASSES 16 EXCHANGES 7680
```

Both programs require only Python's standard library and have complete source embedded here. They were executed directly and subsequently replayed from extracted final-package paths. These are exact finite enumerations of the fixed five-cube, not an infinite-dimensional result, and their success does not constitute independent external validation. The mathematical manuscript separately proves all necessary lemmas, quantifiers, and reconfiguration statements.
