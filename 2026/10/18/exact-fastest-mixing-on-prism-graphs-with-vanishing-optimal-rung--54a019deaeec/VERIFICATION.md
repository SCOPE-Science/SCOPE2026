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

## Reproduction
Run `python3 verify_prism.py`. The exact rational characteristic-polynomial checks for \(n=3,4,6\) need only Python's standard library. With NumPy and SciPy installed, the script constructs and diagonalizes the complete \(2n\)-by-\(2n\) matrices, and solves the symmetry-reduced LP independently for every integer \(3\le n\le60\).

## Observations
The script prints `EXACT_RATIONAL_CHARPOLY: 3 cases (6, 8, 12 vertices) passed`, `MATRIX_SPECTRA_AND_LP: 58 sizes, 6 to 120 vertices, passed`, and `PRISM_VERIFICATION_OK`. The exact tests use integer/rational entries; the additional comparisons use numerical tolerance and cannot constitute proof for every \(n\).

## Analytical boundary
The all-\(n\) guarantee rests on the Fourier spectral decomposition, the three-active-mode weighted lower bound, feasible explicit transition weights, and convex symmetrization. No numerical extrapolation or exhaustive claim beyond the tested sizes is used. Independent assessment has not been performed.
