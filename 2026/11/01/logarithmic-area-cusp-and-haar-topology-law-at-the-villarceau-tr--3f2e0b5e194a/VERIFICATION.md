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

# Verification record

Analytic proof: the radial discriminant and positive root product establish the topology and exact area integral; two local model integrals supply the same logarithmic coefficient on both sides of the Villarceau angle; Haar normal coordinates yield the density limit. All quantities and normalizations are in `RESULT.md`.

Standalone numerical checker: execute `python check.py` with `numpy` and `mpmath`. It uses high-precision quadrature of the exact radial formula and an independent physical-coordinate planar occupancy raster for three aspect ratios. The script validates endpoint and critical-section areas, logarithmic coefficient estimates, and twelve noncritical areas. It passed on execution. Numerical checks do **not** prove uniform asymptotics, historical priority, or independent scientific validity.

No external independent audit has been performed.
