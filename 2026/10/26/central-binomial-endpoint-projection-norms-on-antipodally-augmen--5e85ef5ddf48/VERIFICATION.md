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

Run `python3 verify_folded_cube.py` beside this document. The program uses only the Python standard library and exact `fractions.Fraction` arithmetic. The successful test output is:

```
FOLDED_CUBE_EXACT_OK dimensions=9 spectral_edge_currents=22520 full_grounded_columns=6 full_grounded_currents=304
```

The spectral calculation checks every edge of the actual augmented-cube graph for integer dimensions \(3\) through \(11\) (22,520 edges total), using an independent explicit finite-character representation of the potential. It separately checks exact vertexwise current conservation, the edge diagonal and both endpoint formulas.

The grounded-Laplacian calculation constructs the actual integer graph Laplacian, deletes a ground vertex, and performs rational Gaussian elimination for six source edges (two edge directions across dimensions \(3,4,5\)), checking 304 reconstructed edge-current coefficients. These solves do not depend on the Fourier or beta-integral construction.

These finite calculations are checks, not an exhaustive or computer-assisted proof of the unbounded dimension range. The written proof establishes the quotient representation, monotonicity, character diagonalization, exact current counts, binomial identity and trace correction for all \(n\ge5\). No independent mathematical audit has been performed.
