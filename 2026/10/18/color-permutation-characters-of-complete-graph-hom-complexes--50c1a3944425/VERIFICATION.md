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
# Reproducibility

The three accompanying pure-Python scripts require Python 3 and no third-party packages. From the directory containing `artifacts`, execute:

```
python3 artifacts/check_cells.py
python3 artifacts/verify_chain.py
python3 artifacts/verify_action.py
```

`check_cells.py` exhaustively enumerates every target permutation, cell and signed fixed-cell trace for parameter pairs `(2,2)`, `(2,3)`, `(2,4)`, `(3,3)`, `(3,4)`, `(3,5)`, `(4,4)`, `(4,5)`; its success marker is `CHECK_CELLS_OK`.

`verify_chain.py` constructs the augmented chain complexes and computes exact ranks modulo `1000003` for pairs `(2,2)`, `(2,3)`, `(2,4)`, `(2,5)`, `(3,3)`, `(3,4)`, `(3,5)`, `(3,6)`, `(4,4)`, `(4,5)`; its success marker is `VERIFY_CHAIN_OK`.

`verify_action.py` independently uses a spanning-tree cycle basis of the one-dimensional complex \(\operatorname{Hom}(K_3,K_4)\) and directly tests all \(24\) induced target permutations on first homology. It verifies \(24\) vertices, \(36\) edges and \(13\) fundamental cycles, printing `VERIFY_HOMOLOGY_ACTION_OK`.

The exhaustive finite tests do not prove the statement for arbitrary parameters or rule out torsion in other complexes. The general correctness argument instead uses the published nonequivariant homotopy theorem, the fully stated signed-cell calculation and the representation argument in `RESULT.md`. No independent scientific audit has been performed.
