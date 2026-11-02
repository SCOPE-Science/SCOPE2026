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

# Reproducibility and established limits

Run `python3 verify.py` with the Python standard library. The checker computes the exact adjacency matrix of the line graph of \(GP(10,2)\), checks its 30 vertices and 60 edges, verifies the degree-seven annihilating polynomial, and tests every one-site and distinct two-site Krylov rank by rational row reduction.

The complete two-site distance/path/rank table comprises \(60+120+60+60+120+15=435\) unordered pairs. Exactly 15 antipodal pairs have rank 8, exactly 60 two-geodesic distance-three pairs have rank 12, and the remaining 360 pairs have rank 13. These assertions use no floating-point tolerances, random sampling, precomputed files, or external network data.

The physical absorption conclusion additionally uses the analytic fact that the dissipative evolution is unitary on the dark invariant subspace and strictly decaying on its orthogonal bright subspace. An enumerated rank alone would not establish the asymptotic limit without that argument. The result applies only to the given finite graph, exact homogeneous hopping, two distinct positive-rate sinks and a single excitation; independent scientific validation has not been performed.
