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

# Computational and analytic verification

The standalone file `VERIFY.py` was executed against the identities in `RESULT.md` using SymPy and NumPy. It reported PASS for the three exact eigenvector identities, exact Gram determinant, exact unit-diagonal Gram reconstruction, even-subspace eigenvalue identities, and the symbolic limit of the Jacobi-to-optimal conditioning ratio, \(9/8\). A seeded supplementary sweep checked \(3,200\) positive diagonal scales across eight nondegenerate correlations, confirming the candidate's condition numbers and never finding a sample below the claimed optimum.

The tested calculations do not establish the universal minimization over infinitely many positive diagonal matrices. That statement and uniqueness are proved analytically using equal squared coordinate moduli of the two extremal eigenvectors and Rayleigh–Ritz. The source full texts were checked for the mathematical definitions and the distinction between the known Gram matrix and the new proposed diagonal optimum. The numerical sweep is not a certificate of historical novelty.

To reproduce: `python VERIFY.py` (Python 3, NumPy and SymPy). The result concerns only positive diagonal congruence scaling, not arbitrary basis transformations or polynomial chaos degrees other than two.
