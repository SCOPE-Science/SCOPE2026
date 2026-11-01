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

# Reproduction and limits

The theorem is proved analytically in `RESULT.md`. `verify_zonotope.py` independently computes exact rational Legendre-weighted beta integrals up to \(m=14\), checks the closed eigenvalue formula, checks the exact mean/variance overlap counts, and compares the determinant sum against the independently triangulated convex hull of all endpoint subsets for samples of 3, 4, 6, and 8 unit vectors. It also tests the series trace and squared spectral mass at a finite cutoff, and tests the finite-\(n\) mean/variance by 18,000 reproducible uniform-sphere trials at \(n=7\). The required Python packages are listed in `requirements.txt`.

Run: `python verify_zonotope.py`. The expected completion marker is `ALL_EXACT_MOMENT_SPECTRAL_AND_HULL_CHECKS_PASSED`.

Finite truncation of a harmonic series and Monte Carlo samples are *not* infinite proofs, nor do they establish exact historical priority. The full infinite-series and remainder justifications appear in the written proof, using an analytic Legendre identity, Funk–Hecke, Hilbert–Schmidt tail control, and orthogonality of canonical U-statistic terms.
