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

# Reproducibility and checks

Run `python3 verify_cube_geodesic_law.py` in the same folder. No packages beyond the Python standard library are required.

The script constructs all six faces and their adjacency graph from cube vertex coordinates. It enumerates 28 simple top-to-bottom face sequences and 26 simple top-to-a-fixed-side sequences. For each unfolding, it calculates the image of the marked top-face center in the target plane, verifies that a canonical candidate is at most as far from each of the square's four corners, and thereby proves dominance across the whole target square (the squared-distance difference is affine). The four canonical bottom candidates and direct side candidate are also explicitly seen among the generated unfoldings. These exact-fraction checks are exhaustive over the required finite set of face paths.

It then expands and integrates the polynomial formulas for the first five even moments, checking exact results \(1,23/18,451/180,331/56,389423/25200\). Finally, it checks CDF continuity and monotonicity at 3001 radii and compares a deterministic sample of 180000 points from the cube surface against the proposed CDF, obtaining maximum observed discrepancy about \(0.001375\). Random sampling checks are corroborative only; they do not prove the formula. The exact CDF integration and two-term tail asymptotic are derived in RESULT.md and are not independently machine-certified. No external mathematical audit has been performed.
