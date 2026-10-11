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

`verify.py` embeds all \(169\) tetrahedra and uses only the Python standard library.

After contracting a spanning tree, the graph-cycle lattice has rank \(170\). A deterministic \(170\times170\) facial-relation minor has determinant
\[
-125,
\]
while the full relation matrix has rank \(167\) modulo \(5\). These two facts force
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^3.
\]

The verifier constructs a basis of the mod-\(5\) cocycle space and uses it as exact coordinates on the proved quotient. Exhaustion yields \(984\) graph triangles, \(338\) facial triangles, and \(646\) nonfacial triangles. Every nonfacial triangle has nonzero coordinates.

The \(646\) coordinates meet all \(31\) one-dimensional subspaces of \(\mathbf F_5^3\). Up to orientation, they represent \(40\) of the \(62\) nonzero inverse-pair classes. Nine projective directions contain both inverse-pair types and twenty-two contain one.

The explicit order-three vertex permutation is checked against the full facet set. Its induced homology map is reconstructed from the cocycle coordinates and verified on every graph triangle. On projective directions it has one fixed point and ten three-cycles. The fixed direction has \(16\) carriers, and the ten three-cycles have per-direction carrier totals
\[
2,\ 7,\ 8,\ 19,\ 21,\ 25,\ 26,\ 28,\ 35,\ 39.
\]

Exact successful output:

`VERIFY_OK f=21,190,338,169 H1_Z=Z5^3 graph_triangles=984 facial3=338 empty3=646 all_empty3_nonzero=yes projective_directions=31 all_directions_hit=yes unoriented_class_pairs_hit=40of62 direction_pair_profile=double9+single22 order3_symmetry=yes projective_orbits=1+10x3 fixed_direction_carriers=16 triple_direction_totals=2,7,8,19,21,25,26,28,35,39 maximal_minor_det=-125 rank_mod5=167`
