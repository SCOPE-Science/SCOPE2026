# Homology misses one of two triangular systole types in the 15-vertex octahedral space
## Finding
Let \(K\) be the exact 15-vertex complex named `octahedron_space` in Lutz's spherical 3-manifold data. It triangulates the spherical octahedral space \(S^3/T^*\), where \(T^*\) is the binary tetrahedral group of order \(24\). The simple noncontractible combinatorial \(1\)-systole, measured by the number of edges in a simple cycle of the \(1\)-skeleton, has length \(3\).

There are exactly \(243\) systolic cycles. They are precisely the boundaries of the three-vertex cliques that are not triangular faces. Up to unoriented free homotopy, these \(243\) cycles realize exactly two types. Exactly \(215\) represent elements of order \(6\); they map to the two nonzero classes of \(H_1(K;\mathbb Z)\cong\mathbb Z/3\). The remaining \(28\) represent elements of order \(4\) in the commutator subgroup and are nullhomologous. Hence homology misses an entire shortest noncontractible free-homotopy type.

## Assumptions and scope
The object is the labeled complex in the cited facet table, not an arbitrary triangulation of \(S^3/T^*\). “Simple cycle” means a cycle with distinct vertices in the \(1\)-skeleton. Length is edge count. “Unoriented free homotopy” identifies a conjugacy class with its inverse, as appropriate when the orientation of the simple cycle is forgotten.

The literature identifies this exact small triangulation as a triangulation of \(S^3/T^*\), gives \(f(K)=(15,102,174,87)\), gives \(H_1(K;\mathbb Z)\cong\mathbb Z/3\), and identifies \(T^*\) as a group of order \(24\).

## Proof
The 87 listed tetrahedra reconstruct a complex with 15 vertices, 102 edges, 174 triangles, and 87 tetrahedra. Among the \(\binom{15}{3}\) vertex triples, exactly \(417\) span all three edges. Of these, 174 are triangular faces, leaving exactly \(243\) missing triangles.

Collapse the spanning tree consisting of the edges \(\{1,i\}\) for \(2\le i\le14\), together with \(\{2,15\}\), in the \(1\)-skeleton. The remaining edges generate the standard edge-path presentation of \(\pi_1(K)\), with one relator for each triangular face. The verifier assigns every non-tree edge an explicit word in two permutations \(A,B\) of 24 points. It checks all 174 face relators and verifies that \(A,B\) generate a group of order \(24\). Since the cited topology gives \(|\pi_1(K)|=24\), this surjective representation is an isomorphism.

Evaluating every missing-triangle boundary in this exact 24-element group gives 215 elements of order \(6\) and 28 elements of order \(4\); none is the identity. Therefore every missing triangle is noncontractible. No simple cycle can have fewer than three edges, so these 243 cycles are exactly all simple noncontractible systolic cycles.

The used group elements occupy three conjugacy classes: two inverse conjugacy classes of order-six elements, hit 110 and 105 times, and one inverse-stable conjugacy class of order-four elements, hit 28 times. Hence, after forgetting cycle orientation, there are exactly two free-homotopy types.

Finally, the exact generated group's commutator subgroup has order \(8\), with element-order profile one identity, one involution, and six elements of order \(4\). All 28 order-four systoles lie in this subgroup, while all 215 order-six systoles lie outside it. Because abelianization is \(H_1(K;\mathbb Z)\cong\mathbb Z/3\), the former are nullhomologous and the latter represent the two nonzero homology classes.

## Verification
Run `python verify.py` with Python 3. The verifier uses only the standard library. It reconstructs the complex from the full tetrahedron list, checks the face vector, verifies the 24-element fundamental-group representation against every triangular relator, enumerates all three-edge simple cycles, computes element orders and conjugacy classes, computes the commutator subgroup, and checks the stated homology split.

The recorded successful output is included as `artifacts/verification_output.txt`.

## Relationship to prior work
Lutz's geometric 3-manifold paper constructs the spherical octahedral space, identifies its fundamental group as the binary tetrahedral group \(T^*\) of order \(24\), proves the existence of the 15-vertex triangulation, and gives its homology and face vector. The associated online data provide the exact 87 tetrahedra.

The inspected primary text does not state an empty-triangle census, a combinatorial systole, or a free-homotopy classification of short cycles. Searches using the exact object name, the counts \(243\), \(215\), and \(28\), order-four/order-six formulations, and the “homology misses shortest loops” formulation found no statement implying this result.

## Limitations
This is a finite exact theorem about one labeled triangulation. It does not claim that every 15-vertex triangulation of the octahedral space has the same systolic spectrum, nor that the displayed triangulation is vertex-minimal. The 1999 dissertation is earlier bibliographic prior art for small triangulations, but an accessible day-resolved full text was not available for a line-by-line comparison; this remains a residual originality risk.

## References
1. Frank H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:math/0311116v1, 2003. Section 4 identifies \(S^3/T^*\), gives \(|T^*|=24\), and Table 7 gives homology and \(f\)-vector.
2. Frank H. Lutz, `spherical_3manifolds.txt`, exact facet data for `octahedron_space`.
3. Frank H. Lutz, `spherical_3manifolds_hom.txt`, homology table for `octahedron_space`.
