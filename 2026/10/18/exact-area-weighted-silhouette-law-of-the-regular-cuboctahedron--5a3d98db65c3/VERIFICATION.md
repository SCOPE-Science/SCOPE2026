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

# Reproduction of internal mathematical checks

The bundled `verify_cuboctahedron.py` evaluates exact formulas against independently computed orthogonal projections, deterministic quadrature and seeded sampling. It requires Python, NumPy and SciPy; run with `python verify_cuboctahedron.py`.

The source uses all twelve vertices of the standard cuboctahedron, calculates two-dimensional convex hulls in 500 directions and confirms area and vertex count. It integrates the spherical triangle over the gnomonic coordinates \((s,t)\) satisfying \(0\le s\le1\), \(0\le t\le1-s\), with area element \((1+s^2+t^2)^{-3/2}\,ds\,dt\). It also uses 240,000 seeded uniform-sphere samples as a stochastic check. The recorded successful output is:

`CUBOCTAHEDRON_SILHOUETTE_OK quadrature_nodes=5184 direct_hulls=500 monte_carlo=240000 p_octagon=0.649040687816 mean_oct_area=4.622206367513 mean_hex_area=4.935189771122 covariance=-0.142587021853`

The exact conclusions rest on analytic finite face enumeration and the spherical boundary-flux calculation. Neither a sampling run nor numerical quadrature proves an exact equality for all viewing directions. Degenerate viewing directions lie on finitely many great circles and have Haar measure zero.
