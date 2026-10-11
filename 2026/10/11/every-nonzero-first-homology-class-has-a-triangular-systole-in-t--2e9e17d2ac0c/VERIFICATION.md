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

`verify.py` embeds the complete \(121\)-tetrahedron presentation and uses only the Python standard library.

It reconstructs
\[
f=(18,139,242,121)
\]
and checks that every triangular face belongs to exactly two tetrahedra.

After contracting a spanning tree, the graph-cycle lattice has rank
\[
122.
\]
A \(122\times122\) facial-relation minor has exact determinant of absolute value
\[
25,
\]
and the complete relation matrix has rank
\[
120
\]
modulo \(5\). Therefore its Smith quotient is
\[
(\mathbb Z/5)^2.
\]

Two exact mod-five cocycles then coordinate this quotient. Exhaustion of all three-vertex cliques finds
\[
619=242+377,
\]
where the \(242\) facial triangles are boundaries and all \(377\) nonfacial triangles have nonzero homology coordinates.

Up to orientation, all twelve nonzero class pairs occur, with multiplicity multiset
\[
\{11,15,15,17,19,30,33,39,45,49,52,52\}.
\]
All six projective order-five directions occur, with total carrier multiplicities
\[
\{50,50,60,64,71,82\}.
\]

Exact successful output:

`VERIFY_OK f=18,139,242,121 H1_Z=Z5^2 graph_triangles=619 facial3=242 empty3=377 all_empty3_nonzero=yes simple_integral_1_systole=3 minimizers=377 all_nonzero_H1_classes_hit=yes nonzero_classes=24 unoriented_class_pairs=12 pair_profile=11,15,15,17,19,30,33,39,45,49,52,52 projective_directions=6 direction_profile=50,50,60,64,71,82 maximal_minor_absdet=25 rank_mod5=120`
