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
# Reproducible verification and limits

Run `python3 check_brightness.py` from the directory containing the associated mathematical files. Only the Python standard library is needed. The checker enumerates all projection-body candidate normals and their integer pair products, computes planar projected convex-hull areas directly from the 24 solid vertices in 800 independent orientations, compares 300,000 Haar-normal samples with the two explicit upper CDF branches, and checks the three-halves overlap coefficient on four decreasing scales. Every seeded check completed successfully.

The key exact proof steps are in RESULT.md: facet-area normalization, the cap incidence threshold from dot products 196 and 188, spherical Gauss--Bonnet for the equal-cap lens, the local rescaling at cap tangency, and the local cone-area computation for 12 brightness minima. Experiments alone do not prove those continuum or asymptotic statements. The analytic upper branch starts at brightness 14, not at the lower endpoint. A complete elementary middle density and independent external scientific audit are not asserted.
