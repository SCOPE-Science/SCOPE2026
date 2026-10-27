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

The analytic proof reconstructs the inverse difference matrix, partitions all vertex functions into orthogonal invariant radial/contrast subspaces, computes the full characteristic polynomial of each Jacobi block, identifies the extremizing radial mode using a strictly positive kernel, and uses matching variational estimates for the asymptotic constant. The path case is checked by the elementary sine diagonalization.

The supplied `check_tree.py` builds the full incidence-difference matrix separately from the predicted tridiagonal spectral blocks. It checks complete eigenvalue multisets for branching 2, 3, 4 and depths 1 through 4, and tests the scaled smallest eigenvalue for depths 8, 12, 16. The finite checks cannot prove an all-depth theorem; the proof above does that. Requires NumPy and SciPy. The closest inaccessible historical full text remains an originality limitation, not a proven instance of coverage. Independent audit has not been performed.
