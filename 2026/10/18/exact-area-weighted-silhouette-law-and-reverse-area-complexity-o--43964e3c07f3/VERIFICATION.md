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
# Verification of the exact icosahedral mixed-shadow law

The theorem has an analytic spherical-flux proof with a finite exact algebraic chamber certificate. The standard-library checker `ico_weighted_check.py` constructs all twenty facets from the twelve edge-two icosahedral vertices in \(\mathbb Q(\sqrt5)\). It verifies thirty facet adjacencies, forty-five great-circle pairs without triple intersection, ninety signed arrangement vertices, all ninety-two open chambers, all chamber types and exact angular and boundary-flux coefficient lists. Its terminal line is `EXACT_ICO_SHADOW_FLUX_CERTIFICATE_OK cells=92 plane_intersections=90`.

The independent rational-angle checker `ico_shadow_signs.py` proves the strict descending conditional projected-area means and negative covariance with a finite Taylor bound for cosine, alternating-series bounds for arctangent, and Machin's identity for \(\pi\). It reports the covariance strictly within the rational interval represented approximately as \((-0.119267326469,-0.119267284635)\). No floating-point values are used in its inequality proofs.

The optional numerical checker `ico_shadow_numeric.py` uses NumPy and SciPy to reconstruct 1,800 actual projected convex hulls from the twelve geometric vertices, compare area with the independent facet-normal Cauchy sum and silhouette count with thirty facet-edge horizon tests, then compare the three mixed moments against 300,000 Haar-sphere samples. The deterministic fixed-seed run passed. These simulated directions are diagnostics, not an exhaustive geometric proof.

Limitations: the historical-priority search and source-comparison are not an independent verification, and the complete area distribution conditioned on each vertex count is not established. All relevant independent-audit channels remain not performed.
