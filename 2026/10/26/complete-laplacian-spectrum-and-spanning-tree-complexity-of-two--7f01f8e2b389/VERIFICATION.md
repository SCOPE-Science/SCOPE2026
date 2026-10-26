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

# Reproducibility checks

Run `python verify.py` with Python 3 and NumPy installed. The executable independently creates the graph directly from allowed token moves, computes an unweighted integer Laplacian matrix, compares its eigenvalues with the stated complete multiset to tolerance \(10^{-7}\), and computes exact determinant residues of a principal Laplacian minor modulo two different primes. Its output on the checked package was:

```text
VERIFY_OK spectra_pairs=14 exact_modular_matrix_tree_pairs=9
```

The spectral tests cover \(3\le m\le6\) with \(m\le n\le7\); the exact modular determinant tests cover \(3\le m\le5\) with \(m\le n\le6\). The source code in this package, rather than an external run log or a cached computation, produces these checks. Modular determinant agreement in finitely many cases does not establish the full formula. The proof in `RESULT.md` establishes the infinite theorem through orthogonal invariant subspaces, complete dimension accounting, and the matrix-tree theorem. No independent audit has been performed.
