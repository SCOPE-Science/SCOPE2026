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

`verify.py` contains the complete 112-facet presentation of the twelve-vertex complex and uses only the Python standard library.

It reconstructs the full face vector \((12,66,220,390,336,112)\), verifies that every edge and every triangle is present, and enumerates all \(495\) four-vertex sets. Exactly \(105\) are missing tetrahedra.

Exact bit-vector elimination over \(\mathbf F_2\) gives ranks \(55\) and \(164\) for the degree-two and degree-three boundary maps, hence one-dimensional mod-two middle homology. Every missing tetrahedral boundary is checked to be the unique nonzero class.

The script then checks the displayed integral two-cocycle on all \(390\) tetrahedra. Its evaluations on the \(105\) missing tetrahedral boundaries are exactly \(+1\) in \(57\) cases and \(-1\) in \(48\). These integral unit pairings are the certificate of primitivity.

Exact successful output:

`VERIFY_OK f=12,66,220,390,336,112 H2_F2_dim=1 missing4=105 all_missing4_mod2_nonzero=yes integral_cocycle_support=35 primitive_pairings=+1:57,-1:48 carrier_vertex_degree=35`

The published identification of the manifold with \(S^3\times S^2\) supplies \(H_2(K;\mathbb Z)\cong\mathbb Z\); the primitivity statement itself is checked by the explicit integral cocycle.
