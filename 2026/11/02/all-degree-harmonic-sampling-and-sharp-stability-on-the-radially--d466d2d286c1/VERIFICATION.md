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

The standard-library `rhombic_dodecahedron_exact_check.py` constructs exact Legendre recurrences at rational arguments and their quadratic irrational counterpart. It checks spectral ranks for all degrees \(0\le k<120\), exact expressions for the degree-seven extremum, and exact rational envelopes proving every other nonsingular finite-range condition number less than \(11/2\). Its expected success message begins `RHOMBIC_DODECAHEDRON_EXACT_CERTIFICATE_OK`.

The supplementary SymPy script `rhombic_geometry_crosscheck.py` constructs the complete seven-point Legendre Gram matrix directly from coordinates and checks the characteristic-polynomial identity for eighteen degrees. Its expected success prefix is `RHOMBIC_DODECAHEDRON_GEOMETRY_CROSSCHECK_OK`.

These scripts are finite checks only. The distinct proof of the unbounded range uses Bernstein's Legendre inequality \(|P_k(\cos\theta)|<\sqrt{2/(\pi k\sin\theta)}\), equation (56) of Gautschi–Giordano (2008), together with a six-off-diagonal Gershgorin estimate for all \(k\ge120\). The remaining scholarly uncertainty is whether an equivalent theorem has appeared in older cubature or harmonic-representation literature. No external independent audit or validation has been performed.
