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

`verify.py` embeds all seventy-two tetrahedra and uses only the Python standard library.

After contracting a spanning tree, the graph-cycle group is \(\mathbb Z^{73}\). A fixed \(73\times73\) facial-relation minor has determinant \(5\), while the full relation matrix has rank \(72\) modulo \(5\). These two facts together force the integral quotient to be exactly \(\mathbb Z/5\).

The verifier constructs the unique nonzero cocycle line over \(\mathbf F_5\), enumerates all \(308\) graph triangles, and checks that the \(164\) nonfacial triangles have no zero homology values. The oriented values occur as \(41,44,38,41\) in classes \(1,2,3,4\), giving the intrinsic \(82/82\) split up to orientation.

For automorphisms, a vertex invariant partitions the vertices into cells of sizes \(2,4,4,4\). Exhausting all \(27{,}648\) cell-preserving permutations finds exactly four simplicial automorphisms, with element orders \(1,2,4,4\). Their induced homology multipliers are exactly \(1,2,3,4\).

Exact successful output:

`VERIFY_OK f=14,86,144,72 H1_Z=Z/5 det_minor=5 rank_mod5=72 graph_triangles=308 facial3=144 empty3=164 all_empty3_generators=yes unoriented_class_counts=82,82 aut=C4 aut_H1_units=1,2,3,4 carrier_orbits=39x4+4x2`
