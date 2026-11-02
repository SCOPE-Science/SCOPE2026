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

The exact proof is contained in `RESULT.md` and does not depend on numerical extrapolation. The standalone checker `check_defect_cages.py` constructs the signed Hamiltonian, confirms the finite-dimensional Clifford identity by exact integer arithmetic, factors the four-dimensional characteristic polynomial symbolically, compares full Hermitian spectra for dimensions 2 through 8 and three strength assignments per geometry, and checks local support, sector rank and pairwise orthogonality. It also calculates contrasting three-cube characteristic polynomials for an induced and a non-induced two-edge pattern.

The recorded checker output is `checks.txt`. These computations are supplementary. The all-dimension conclusion and all-real-strength quantifiers rest on the written invariant-subspace argument, not on finite enumeration. Historical novelty remains subject to independent literature review. No independent audit was performed.
