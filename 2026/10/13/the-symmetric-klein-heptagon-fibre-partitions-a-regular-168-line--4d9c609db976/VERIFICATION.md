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

The attached `verify_heptagon_line_orbit.py` performs exact symbolic checks with SymPy 1.14.0. It works over \(\mathbf Q(\zeta_7,a)\), proves the defining degree-seven polynomial for \(a\) is irreducible over \(\mathbf Q(\zeta_7)\), and verifies the explicit seven-line heptagon and all \(14\) residual points.

It independently closes the displayed projective generators of the Klein quartic automorphism group to exactly \(168\) elements and checks their invariance of the quartic. The order-seven element \(\phi\) cycles the seven sides and generates a subgroup with exactly \(24\) left cosets. Applying every group element to one side through the dual projective action finds exactly one stabilizing element. Therefore the side orbit has size \(168\), and the \(24\) cosets yield disjoint seven-line blocks.

Fresh replay output:

`VERIFY_OK field_degree=42 group=168 residual_points=14 line_stabilizer=1 line_orbit=168 heptagon_partition=24x7`

The computation is finite and exact. It does not use floating-point evidence as proof. The \(24\)-heptagon identification with the symmetric-theta fibre uses the cited theorem of Agostini--Plaumann--Sinn--Wesner; the script verifies the additional line-level claim and the exact group/coset geometry.
