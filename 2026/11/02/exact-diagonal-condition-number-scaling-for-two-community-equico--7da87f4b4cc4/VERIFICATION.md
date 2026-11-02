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

# Reproduction and limits

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The code is standalone and constructs all matrices directly; it does not rely on network calls, cached eigenvalue tables, or pre-existing artifacts. In the final package it returned `PASS: 17287 exact, grid, spectral, saturation and randomized assertions`.

The checks include an exact six-dimensional rational case with quotient eigenvalues `1/2` and `5/2`, an exact parameter family across increasing community size, direct full-matrix versus quotient eigenvalue comparisons, local and distant scalar perturbations, seeded randomized scalar minimization and independent diagonal optimization attempts. The finite set of checked sizes/parameters and the randomized numerical searches do not establish global uniqueness or infinitely many cases. The analytical proof of those facts is given in `RESULT.md`.

The reported originality assessment compares accessible published work and semantic records; it is not independent publication priority confirmation. External audit has not been performed.
