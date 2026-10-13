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

# Reproduction and limitations

Run `python3 verify.py` using Python 3.10+ and the standard library, with no external files or network. The script is included in full and reconstructs every value it tests from elementary trigonometric definitions.

Observed output:

`VERIFY_OK spectra=2446 feasible_grid_comparisons=30996 eigenvector_entries=3281 asymptotic_cases=5`

It covers sizes \(5\le n\le99\) for Fourier contacts and feasibility; sizes \(5\le n\le40\) for alternative stochastic edge-class weight grids; and sizes \(5\le n\le21\) for direct physical-matrix/Fourier eigenvector identities. It also tests five larger sizes for the spectral-gap asymptotic and exact six-vertex rational special values.

A separate finite-dimensional linear-programming check using SciPy's HiGHS solver for all sizes \(5\le n\le100\) returned optimal values agreeing with the stated formula to within \(3\times10^{-16}\). SciPy is not required by the included checker.

These numerical and finite-size validations do not independently certify the analytical proof for every integer size. The argument's nonstandard points are the location of the maximum sampled concave quadratic, the four-class holding-probability positivity calculation, and the three-contact affine optimality argument; all are written explicitly in `RESULT.md`.

An independent mathematical audit has not been performed.
