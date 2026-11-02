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

# Verification and reproducibility

Run `python VERIFY.py` in a directory containing this package. The script uses only the Python standard library, constructs the two-layer transition matrix from genuine graph adjacency matrices, checks exact row sums and zero diagonals, and matches all characteristic-polynomial coefficients by verifying the first \(2|V(H)|\) integer power-sum traces against the predicted spectrum. It independently tests exact-rational one-dimensional feasible grids and the sharp no-holding penalty identity for complete, Johnson, Petersen, cube and small-cycle graph bases.

The actual execution completed with `PASS: 1177 exact assertions, including full characteristic-polynomial certificates`. The universal optimality assertion relies on the explicit convex symmetrization and affine minimax proof in `RESULT.md`, not on a finite enumeration, a floating-point matrix spectrum or a solver log.

The manuscript has not been independently audited. The specialized historical-literature comparison is necessarily incomplete; missing or unindexed equivalent work is a residual originality risk.
