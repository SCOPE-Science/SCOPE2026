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

# Reproducibility and limitations

Put `verify.py` and `cells.csv` in the same directory and run `python verify.py` using any recent Python 3 installation. The standard-library exact-arithmetic program reconstructs the icosahedral adjacency and faces, checks the sixty one-third-truncation vertices and their supporting facets, and exhausts every open direction chamber by nested infinitesimal perturbations of every arrangement intersection. The last step is exhaustive because each chamber's boundary contains an arrangement vertex and every incident local sector touches one of the tested tangent rays. The code reads and checks the bundled complete table of 152 unique sign vectors rather than relying on an absent external file.

Actual execution of the bundled program before delivery produced:

`EXACT_OK normals=32 great_circles=16 cells=152 spectrum_20=132 spectrum_21=20 max=21 fractional=20/7`

For \(a+b\varphi\), all signs are decided by comparing integers \((2a+b)^2\) and \(5b^2\) when the rational and irrational terms oppose. Neither floating-point tolerance nor statistical sampling enters the final certificate. The program's finite certificate and the mathematical arrangement-exhaustiveness proof together establish the uniform upper bound for all generic directions. Geometric normal-fan invariance extends the result to the entire continuous range \(0<t<1/2\); endpoint cases are excluded. Independent audit: not performed.
