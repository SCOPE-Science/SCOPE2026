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

# Verification and scope

To reproduce, run `python verify.py` in a Python 3 environment with NumPy and SciPy installed. The checker uses exact rational arithmetic for all 60 planar polygon hulls and 950 coefficient-profile instances. It also independently computes higher-dimensional convex hulls in 27 cases. Its expected success line is:

`FRUSTUM_EXACT_OK planar_hulls=60 rational_profiles=950 independent_high_dim_hulls=27`

If NumPy or SciPy is missing, the exact rational tests still run, but the higher-dimensional field reports `scipy-unavailable`, which is not evidence for those cases. The general theorem is proved in `RESULT.md` by explicit section identities, elementary integration, coefficient extraction, and a strict derivative argument; a finite checker cannot certify all convex bases or dimensions. The proof permits arbitrary full-dimensional centrally symmetric convex bases and parameter \(0\le a\le1\). Independent scientific audit remains unperformed.
