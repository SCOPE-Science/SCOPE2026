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

# Reproducibility of the central section law

Run `python verify_truncated_tetra.py` using Python 3, NumPy, and mpmath. The self-contained program defines the twelve exact vertices from the original four tetrahedral vertices and derives the eighteen edges by squared edge length eight. It verifies the four critical vertex-sign lines and partitions the normal chamber into six polygons with rational vertices. Testing rational interior centroids determines the section side count rigorously on each open cell because all sign-change boundaries have been listed. Exact shoelace areas prove that the six cells exhaust the planar chamber without positive-area overlap.

The checker evaluates each spherical polygon by triangulation using the closed spherical solid-angle formula, separately tests the two radical denominators for the hexagonal cells, and checks that direct six-cell probabilities agree with the expectation from the eighteen identical endpoint angles. Numerical calculations use high precision for displayed values; exact statements are established symbolically in the accompanying proof. A separate direct experiment samples 240000 independent Gaussian directions and counts edge crossings as a diagnostic only. The observed counts are 51993 quadrilaterals, 124711 pentagons, and 63296 hexagons.

The executable prints `EXACT_VERTEX_AND_CHAMBER_PARTITION_PASSED`, `EXACT_SOLID_ANGLE_AND_EDGE_CROFTON_IDENTITIES_PASSED`, `INDEPENDENT_ALL_SIX_SPHERICAL_CELL_AREAS_PASSED`, `RATIONAL_PENTAGON_MAJORITY_CERTIFICATE_PASSED`, `INDEPENDENT_HAAR_NORMAL_MONTE_CARLO_PASSED`, and `ALL_CHECKS_PASSED` on successful completion.

The verification does not establish novelty, independent proof certification, extension to off-center sections, or unexamined literature coverage.
