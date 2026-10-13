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

The standalone checker `verify.py` uses exact arithmetic only. It reconstructs the four matrices printed in Bonnafé--Sarti Remark 5.8, reduces the generated action projectively, verifies that the orbit of the displayed conic has 16 distinct planes, checks preservation of the three-quadrics defining the surface, and computes normalized Plücker coordinates in the exact quotient ring \(\mathbb Z[i,r]/(r^4-r^2-1)\).

It then exhausts the four automorphisms of \(\mathbb Q(r,i)/\mathbb Q(\sqrt5)\). Complex conjugation has cycle type \(1^8 2^4\) on the 16 components, while each automorphism changing \(r\) has zero overlap with the original 16-component set. The fixed-field conclusions in the finding follow directly.

Expected terminal line:
`VERIFY_OK projective_A=16 planes=16 ci_fixed=8 ci_pairs=4 r_conjugate_overlap=0 both_overlap=0 config_field=Q(r) component_fields=8xQ(r)+8xQ(r,i) minpoly_r=r^4-r^2-1`

The checker does not attempt to classify other Nikulin configurations or projectively different models of the surface.
