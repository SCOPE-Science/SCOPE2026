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

# Reproducible verification and scientific limits

The self-contained `verify.py` requires only the Python standard library. Invoke `python3 verify.py` in the directory containing the file. Its exact-rational procedure builds 110 finite normalized monotone submodular functions from sums of representable matroid-rank functions and modular functions in dimensions one to five. It tests every submodularity and monotonicity condition for those finite instances, the density-tight subset union/intersection and residual conditions, the uniform-density equivalence, and reflection containment at 2,348 greedy-generated vertices for 178 proposed centers. It tests the graphic triangle-plus-bridge case separately, confirming maximal density \(3/2\) and one free coordinate.

Observed output:

`EXACT_VERIFY_PASS polymatroids 110 greedy_vertices_checked 2348 centers_checked 178 triangle_bridge_density 3/2 triangle_bridge_free_coordinates 1`

The exact mathematical proof uses: (i) the necessary and sufficient scaled-center inequalities derived from \(0\) and every axis intercept \(w_e\mathbf e_e\); (ii) normalization, monotonicity and nonnegativity to prove sufficiency; (iii) submodularity of \(\rho f-w\) to prove closure of tight subsets; and (iv) contraction to a positive residual submodular packing region to determine the center-space dimension. None of these steps extrapolates from the finite checker.

Limits: the test suite is finite and does not enumerate all polymatroids, and arbitrary real submodular functions are handled only by the proof. The external fractional-arboricity identity is an established result attributed to the literature. The literature search does not independently certify mathematical novelty. Independent audit was not performed.
