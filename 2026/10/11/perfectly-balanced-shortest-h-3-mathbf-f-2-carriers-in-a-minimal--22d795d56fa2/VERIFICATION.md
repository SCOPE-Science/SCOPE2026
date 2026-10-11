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

`verify.py` embeds the complete \(208\)-facet presentation of the thirteen-vertex complex and uses only the Python standard library.

It reconstructs the face vector
\[
(13,78,286,715,1014,728,208),
\]
checks that every four-set is a tetrahedron, and computes exact mod-two boundary ranks
\[
\operatorname{rank}\partial_3=220,\qquad
\operatorname{rank}\partial_4=493.
\]
Thus \(H_3\) has dimension \(2\).

The script enumerates all \(1287\) five-vertex sets. For each one it builds the tetrahedral boundary chain. All \(1014\) present four-simplices reduce to zero modulo \(\operatorname{im}\partial_4\). All \(273\) missing four-simplex boundaries are nonzero. Their reduced quotient representatives form exactly three classes, each with multiplicity \(91\).

Exact successful output:

`VERIFY_OK f=13,78,286,715,1014,728,208 H3_F2_dim=2 missing5=273 all_missing5_nonzero=yes class_counts=91,91,91 reps=12357|12358|12378 class_relation=alpha+beta=gamma carrier_vertex_degree=105`

The verifier also checks the displayed class representatives, the relation \(\alpha+\beta\), and the uniform incidence count of \(105\) shortest carriers through each vertex.
