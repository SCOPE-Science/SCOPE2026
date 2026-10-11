# Octahedral puncture blocks local vertex elimination in the 16-vertex Poincaré sphere
## Finding
Let \(K=\Sigma^3_{16}\) be Björner–Lutz’s 16-vertex triangulation of the Poincaré homology 3-sphere. Vertex \(16\) is the unique vertex contained in only \(8\) tetrahedra; every other vertex is contained in at least \(18\). Its link is the octahedral \(2\)-sphere on vertices \(\{9,10,11,13,14,15\}\), whose three nonedges are \(\{9,13\}\), \(\{10,14\}\), and \(\{11,15\}\). All three pairs are edges of the deletion \(K-\{16\}\). Consequently no triangulated \(3\)-ball on exactly those six boundary vertices can replace \(\operatorname{st}_K(16)\) while meeting \(K-\{16\}\) exactly in \(\operatorname{lk}_K(16)\): every tetrahedron on four vertices of an octahedron contains at least one opposite pair, so every such filling necessarily uses an edge already present in the deletion but absent from the octahedral boundary. Thus the unique minimum-tetrahedron vertex is locally non-eliminable by any no-new-vertex retriangulation of its closed star. Moreover, \(K-\{16\}\) is a 15-vertex homology \(3\)-ball with octahedral boundary and the same binary-icosahedral fundamental group as the Poincaré sphere.


## Assumptions and scope
Let \(K\) denote the labeled simplicial complex in Björner and Lutz's published 90-tetrahedron list. The topological identification of \(K\) with the Poincaré homology 3-sphere is taken from their construction. A *no-new-vertex local retriangulation at vertex \(16\)* means replacing the closed star \(\operatorname{st}_K(16)\) by a triangulated 3-ball whose vertex set is exactly the six vertices of \(\operatorname{lk}_K(16)\), with intersection with the unchanged deletion \(K-\{16\}\) equal to that link.

The assertion is local to this labeled triangulation. It does not prove that 16 vertices are globally minimal for the Poincaré homology sphere and does not rule out simplifications that first alter simplices away from the closed star or introduce temporary vertices.

## Proof
The published facet list has face vector \( (16,106,180,90) \). Counting tetrahedra through each vertex gives the sorted tetrahedron-incidence degrees
\[
8,18,18,20,22,24,24,24,24,24,24,26,26,26,26,26.
\]
The unique degree-\(8\) vertex is \(16\).

The eight tetrahedra through \(16\) have opposite triangular faces
\[
91011,\;91015,\;91114,\;91415,\;101113,\;101315,\;111314,\;131415,
\]
where a digit string denotes its set of vertex labels. These triangles form the octahedral 2-sphere on \(\{9,10,11,13,14,15\}\). Its three opposite pairs, equivalently its three missing graph edges, are
\[
\{9,13\},\qquad \{10,14\},\qquad \{11,15\}.
\]
Each is nevertheless an edge of the deletion \(K-\{16\}\): for example they occur respectively in the tetrahedra \(\{2,4,9,13\}\), \(\{2,6,10,14\}\), and \(\{2,4,11,15\}\).

Now consider any tetrahedron whose four vertices are chosen from the six vertices of an octahedron. The octahedral graph is \(K_{2,2,2}\), whose clique number is \(3\); hence those four vertices contain at least one opposite pair. Therefore every triangulated 3-ball filling the octahedral boundary without adding vertices contains at least one of the three opposite edges as an interior edge. Here all three such edges already belong to \(K-\{16\}\) but not to the boundary link. Thus the filling would meet the unchanged deletion in more than the octahedral boundary, contradicting the definition of a local star replacement. This proves local non-eliminability.

Finally, deleting a vertex from a closed combinatorial 3-manifold removes the interior of its vertex star and leaves a compact 3-manifold with boundary equal to the vertex link. Since \(K\) is the Poincaré integral homology sphere, the deletion has the integral homology of a 3-ball by Mayer–Vietoris (equivalently by excision for a punctured homology sphere). Removing an open 3-ball does not change the fundamental group, so the deletion retains the binary-icosahedral fundamental group of the Poincaré sphere.

## Verification
The accompanying `verify.py` reconstructs all 90 tetrahedra, checks \(f=(16,106,180,90)\), computes all 16 tetrahedron-incidence degrees, reconstructs the link and boundary of the deletion, finds the three octahedral opposite pairs, verifies that all three are edges of the deletion, and exhausts all 15 four-subsets of the six link vertices to confirm that every possible tetrahedron contains an opposite pair. The recorded replay output is included in `verification_output.txt`.

## Relationship to prior work
Björner and Lutz construct the 16-vertex triangulation and print the complete facet list. Their discussion records the face vector, trivial automorphism group, and several equivalence classes of vertex links, but does not identify vertex \(16\) as the unique minimum-incidence vertex, identify its link as octahedral, or state the diagonal obstruction to a no-new-vertex star replacement. Lutz's later survey discusses vertex-minimal triangulations and cites this Poincaré triangulation, but likewise does not give this local obstruction.

The result is therefore a statement-level refinement of the exact triangulation, not a new construction of the Poincaré sphere and not a proof of its conjectured global vertex minimality.

## Limitations
The obstruction concerns a single local replacement with the deletion fixed. A sequence of bistellar or other retriangulation moves that first changes the deletion may remove the vertex later; the result does not exclude that possibility. The integral homology and fundamental-group conclusions use the published topological identification of the facet complex with the Poincaré homology sphere rather than recomputing a full group presentation in the verifier.

For source dating, the 1999 dissertation is an earlier public scientific source but the inspected copy provides only year-level dating. The machine date field therefore uses the earliest inspected day-resolved public source, arXiv:math/0506372v1, submitted 2005-06-18; no calendar day has been invented for the 1999 item.

## References
1. Anders Björner and Frank H. Lutz, *Simplicial Manifolds, Bistellar Flips and a 16-Vertex Triangulation of the Poincaré Homology 3-Sphere*, Experimental Mathematics 9 (2000), 275–289, DOI 10.1080/10586458.2000.10504652.
2. Frank H. Lutz, *Triangulated Manifolds with Few Vertices and Vertex-Transitive Group Actions*, dissertation, TU Berlin, 1999, Chapter 1, Theorem 1.5 and its complete facet list.
3. Frank H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, submitted 2005-06-18; MSC 57Q15, 52B05, 05C30, 52B70.
4. SageMath, `PoincareHomologyThreeSphere`, `src/sage/topology/simplicial_complex_examples.py`, reproducing the Björner–Lutz facet complex.
