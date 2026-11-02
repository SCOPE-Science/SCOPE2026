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

The reproducibility script `check_theta_projection.py` was executed after finalizing the theorem statement. Output:

`CHECK_OK rational_parameter_cases=6336 mesh_checks= 82368 regimes= {'short': 1944, 'balanced': 2975, 'saturated': 1417} unrestricted_LP_cases= 8 LP_edge_counts= [6, 7, 11, 8, 12, 14, 15, 22]`

The rational test checks the formula, coefficient ranges, full edge-column norms, and multiple independent rational inputs for each parameter triple. The eight unrestricted linear programs optimize over every matrix of an \(\ell_1(E)\) projection onto the circulation space; no symmetry constraints are imposed in those numerical linear programs. Their computed optima agree with the proposed exact formulas to within \(10^{-8}\).

These finite computations do not establish the theorem for all integer parameters. The proof uses symmetry averaging, exact operator-column algebra, monotonicity outside the optimization interval, and the minimum of two affine functions, as detailed in RESULT.md. The independent mathematical audit remains unperformed.
