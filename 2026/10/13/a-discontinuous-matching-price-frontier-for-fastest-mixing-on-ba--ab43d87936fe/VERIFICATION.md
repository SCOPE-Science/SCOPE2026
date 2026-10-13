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

The finite checker in `verify_matching_spectral.py` uses only the Python standard library (`fractions`, `random`). Run it as follows:

```text
python3 verify_matching_spectral.py
```

Successful output observed from the included source file:

```text
VERIFY_OK 693 exact eigenvector equations; 126 projector bounds; 1260 feasible-allocation certificates; 28 critical-family spectra
```

The code forms the actual \(2n\)-vertex Laplacian in exact rational arithmetic. It tests independent eigenvectors spanning the constant, bipartition-sign, symmetric zero-sum and antisymmetric zero-sum subspaces. It separately computes the two global trace bounds for nonsymmetric positive feasible allocations, checks their budget constraints, and verifies the optimal rate formulas and critical continuum for several exact rational prices and graph sizes.

**Analytical proof obligations.** The full theorem additionally relies on the Rayleigh minimum inequality for each orthogonal zero-sum subspace, the exact calculation of projected incidence-vector lengths, scalar optimization of the resulting envelope for every real \(t>0\), and the equality-case rigidity of the antisymmetric subspace. The script does not exhaust all real parameters, independently prove those lemmas, or supply an external audit.
