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
The proof establishes the piecewise projection through Moreau orthogonality; differentiates the smooth middle branch; computes row/column sums; proves uniqueness and the dimension-five strict cutoff by elementary inequalities. The global Lipschitz bound follows by integrating derivatives and sharpness by limiting local derivative witnesses.

Run `python3 check_soc_projection.py` with Python 3.9 or newer. The packaged implementation was run successfully without third-party packages, yielding `OK 130484 assertion groups` and exhibiting the spatial/axial transition between dimensions four and five. Finite tests check arithmetic and derivative consistency but cannot establish the full infinite-dimensional-parameter theorem. Historical general Jacobian theorems are used only as related literature; the critical row optimization and dimension cutoff are proved in RESULT.md. The manuscript has not undergone independent mathematical validation.
