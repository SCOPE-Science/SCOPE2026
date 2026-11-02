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

# Verification details

The theorem is proved by an exact radial flux identity, Fourier sine coefficients on regular facets, the Neumann harmonic-energy identity on the disk, dominated convergence, and an operator-norm density argument.

Execute `python3 verify_polygon_neumann.py` using only Python's standard library. It reports 34 successful finite Fourier/consistency checks, including independent midpoint quadrature, two equivalent series formulas, two-frequency limit scaling, and tangent-versus-sine bounds. The checks are not exhaustive and do not certify the theorem independently.

The Sobolev endpoint is limited to radial extensions; for general physical flux, the stated proof assumes a smooth collar and homogeneous Neumann data. Historical priority is not certified.
