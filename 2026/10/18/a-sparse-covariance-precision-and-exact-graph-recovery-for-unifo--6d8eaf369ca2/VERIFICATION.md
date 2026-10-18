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

The accompanying `check.py` is self-contained aside from SymPy. Run `python check.py` in the directory containing this file. It computes cycle constants as exact rational evaluations of finite binomial sums, constructs the claimed weighted Laplacian, and independently reconstructs continuous covariances from leading coefficients of integer lattice counts and coordinate moments of dilated graph Lipschitz polytopes. It verifies all matrix entries, covariance determinants and reconstruction support. The observed output ends with `NONCACTUS_K23_EXACT_BOUNDARY_OK 8 -3/8` and `CHECKS_PASSED 7 NONCACTUS_BOUNDARIES 1`.

Graphs checked: three-cycle, four-cycle, triangle with bridge, square with bridge, two triangles sharing a vertex, four-vertex path, and two triangles joined by a bridge. Seven distinct cactus graphs and a contrasting non-cactus \(K_{2,3}\) were tested exactly. The latter has a missing-edge precision entry \(-3/8\), also obtained by direct conditional integration. The mathematical derivation of independence, cycle isotropy, congruence inversion, exact density constants and determinant is in `RESULT.md`; the checker does not establish any general theorem by enumeration.

The public data do not assert peer review, independent verification, or computer certification of the general case. Full-text reading covered the primary 2018 finite-metric graph-space paper, the primary 2019 graph-circle basis paper, the published cactus coordinate-projection theorem, and the distinct discrete random-height-function model. A bibliographic alias may remain undiscovered.
