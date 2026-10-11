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

`verify.py` embeds all \(70\) five-simplices and uses only the Python standard library.

It reconstructs
\[
f=(14,84,210,280,210,70).
\]
Contracting a spanning tree leaves \(71\) graph-cycle generators. Unimodular integral reduction of the \(210\) facial triangle relations gives \(70\) unit pivots and one zero column, hence
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]

The explicit primitive cocycle annihilates every facial relation. Exhaustion of all three-vertex cliques finds \(280\) graph triangles, of which \(210\) are faces and \(70\) are nonfaces. Every nonface, oriented by increasing labels, evaluates to \(1\).

The natural cyclic shift preserves the complete facet set, acts by \(+1\) on \(H_1\), and splits the \(70\) carriers into five orbits of size \(14\). The natural reflection also preserves the facet set, acts by \(-1\) on \(H_1\), and combines the carriers into four dihedral orbits of sizes
\[
14,\quad28,\quad14,\quad14.
\]

Exact successful output:

`VERIFY_OK f=14,84,210,280,210,70 H1_Z=Z graph_triangles=280 facial3=210 empty3=70 all_empty3_primitive_same_oriented_generator=yes simple_integral_1_systole=3 minimizers=70 C14_orbits=14x5 D14_orbits=14,28,14,14 shift_action_H1=+1 reflection_action_H1=-1 missing_graph_edges=7_antipodal smith=1^70,0`
