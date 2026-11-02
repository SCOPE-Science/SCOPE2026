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

# Verification

The standalone `checker.py` uses SymPy to reproduce the three trace identities, common determinant, two characteristic-polynomial difference identities, and exact positive trace gaps; it also enumerates all twenty six-step words and verifies characteristic-polynomial equivalence within their three dihedral orbits.

For the rational parameter case, the checker verifies the positive eigenvector at \(\beta=3/10\), its strict componentwise subeigenvector inequality at \(\beta=149/500\), and the exact negative sign of \(\det(I-M)\). The paper's argument converts these certificates into the strict Perron inequalities and the invasion-threshold split. No external formal proof or independent validation is claimed; the conclusions do not extend to a finite stochastic SIS chain.
