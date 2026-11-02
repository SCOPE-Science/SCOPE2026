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

# Verification and reproducibility

With Python 3, NumPy and SciPy installed, run:

```sh
python check.py
```

Successful execution prints two PASS lines comprising 97 tests. The tests compare cycle-Laplacian eigenvectors and norms, algebraic susceptibility ratios, nonlinear planar-spin minimizations for odd rings of lengths 3, 5, 7, 9 and 11, energy-gap tests on odd cycles 5, 7 and 9, and explicitly constructed planar saturation on even rings 4, 6, 8 and 10.

The proof is analytical: it uses Fourier diagonalization of the cyclic interaction matrix, a constant-modulus trigonometric polynomial rigidity argument, and a local quadratic expansion on the compact zero-field minimizer manifold. Finite optimizations or numerical tolerances are not claimed to certify the all-size theorem. The comparison source fixes a bond normalization twice the one used here, an explicit factor that is accounted for in the proof.

Independent audit has not been performed.
