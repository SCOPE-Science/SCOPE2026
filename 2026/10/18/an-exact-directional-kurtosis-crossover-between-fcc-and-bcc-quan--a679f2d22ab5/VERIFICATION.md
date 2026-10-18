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

# Exact verification and boundaries

Execute `python verify.py` with SymPy, NumPy, and SciPy installed. The program (1) integrates symmetric polynomials on a directly parameterized FCC simplex chamber and a BCC simplex-minus-three-corners decomposition; (2) independently constructs the complete convex hull of both rational vertex sets; (3) triangulates their boundary, evaluates the exact rational determinant of each origin pyramid, and integrates the same polynomial moments on those tetrahedra. Both methods produce the following exact values:

- FCC: 14 vertices, 24 triangular hull boundary pieces, volume \(2\), radial moments \(3/8\), \(41/240\), \(1397/16128\), component fourth moment \(3/80\), distinct-component mixed fourth moment \(7/720\).
- BCC: 24 vertices, 44 triangular hull boundary pieces, volume \(4\), radial moments \(19/32\), \(409/960\), \(27217/80640\), component fourth moment \(89/960\), distinct-component mixed fourth moment \(71/2880\).

Exact rational assertions then check the radial gaps and symbolic identity \(K_F(u)-K_B(u)=4(74w(u)-29)/5415\). The independent triangulation's facet discovery uses floating-point hull software with exact-rational determinants and polynomial integration afterward; the independent direct simplex decomposition and Voronoi inequalities in the written proof remove reliance on floating-point completeness. The executable does not prove historical priority or external validation.
