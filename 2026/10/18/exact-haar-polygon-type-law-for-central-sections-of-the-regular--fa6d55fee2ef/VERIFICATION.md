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

# Verification of the exact spherical chamber census

Execute `python3 check_truncated_tetra_sections.py` with a standard Python 3 installation. No packages, network access, or external data are needed. This program regenerates all twelve integer vertices and all eighteen edges, verifies that every triple of vertex normals has nonzero determinant, constructs the \(528\) sign witnesses surrounding \(132\) spherical great-circle crossings, and deduplicates them to \(134\) convex spherical sign cells. It finds every cell corner by testing all pairwise great-circle intersections against all hemisphere signs, computes each cell's exact area coefficient vector in the basis \((\pi,\arccos(1/11),\arccos(5/11),\arccos(7/11),\arccos(9/11))\), and checks the expected complete six-class census. It verifies that the three aggregated section-count areas sum to \(4\pi\) and that their first moment matches the independent eighteen-edge formula.

The final stdout line must be `EXACT_CHAMBERS_OK 134_cells 18_edges 3_support_values`. The `math.acos` calculations print only decimal approximations for orientation; the exact-check assertions use integer arithmetic exclusively.

The certificate is a finite exhaustive computation for the specified coordinates; its completeness depends on the proved arrangement characterization and spherical excess formula in RESULT.md. A finite checker is not a proof of a broader theorem about arbitrary polytopes. No independent audit has been performed.
