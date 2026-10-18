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

## Reproducibility
Run `python3 check_tetrahedral_support.py` with Python 3 and no third-party libraries. Exact integer checks establish group closure, Schur orthogonality, all seven witness cardinalities and the Fourier-transform rank-one identity. The limited integer-grid enumeration is supporting evidence only.

## Analytic verification
The proof uses the four-sign pattern on each of three cosets. All-nonzero vector coordinates give at most one zero value per coset; the existence of any zero coordinate makes the coset nonzero counts even. Together with the known uncertainty product bound, this excludes all unlisted cardinalities without a computational completeness assumption.

## Limits
No finite computation establishes originality, the theorem for arbitrary finite groups, or independent validation. These are not claimed.
