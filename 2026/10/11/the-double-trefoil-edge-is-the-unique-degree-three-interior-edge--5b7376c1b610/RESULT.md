# The double-trefoil edge is the unique degree-three interior edge of \(B_{15,66}\)
## Finding
Let \(B_{15,66}\) be the Benedetti--Lutz 15-vertex, 66-tetrahedron 3-ball obtained from \(S_{16,92}\) by deleting the entire star of vertex \(1\). Among its \(54\) interior edges, the tetrahedron-incidence degrees have distribution: one edge of degree \(3\), fourteen of degree \(4\), twenty-one of degree \(5\), thirteen of degree \(6\), and five of degree \(7\). The unique degree-three interior edge is \(\{2,3\}\), exactly the spanning edge proved in the source to carry the double-trefoil knot; its link is the three-cycle on vertices \(4,13,15\). Thus the double-trefoil obstruction is supported on the smallest possible local degree of an interior edge in a triangulated 3-manifold, and no other interior edge of this ball has that minimum degree.

## Assumptions and scope
The complex is the labeled simplicial \(3\)-ball \(B_{15,66}\) of Benedetti and Lutz. Their construction starts from the \(92\)-tetrahedron sphere \(S_{16,92}\) in Table 6 and removes the entire star of vertex \(1\), leaving \(66\) tetrahedra on vertices \(2,\ldots,16\). For an edge \(e\), its degree means the number of tetrahedra of \(B_{15,66}\) containing \(e\). An edge is called interior when it is not contained in the boundary \(2\)-sphere.

The source proves that \(\{2,3\}\) is a spanning interior edge and that a boundary path from \(2\) to \(3\), together with this edge, forms a double-trefoil knot. The present statement concerns the local incidence degree of this edge relative to every other interior edge of the same fixed triangulation.

## Proof
Reconstruct the \(92\) facets of \(S_{16,92}\) from Table 6 and discard exactly those containing vertex \(1\). The remaining complex has face vector
\[
(15,93,145,66).
\]
A triangle of the ball is a boundary triangle exactly when it occurs in one tetrahedron. This test gives the same \(26\) boundary triangles printed in the source. Their edges comprise \(39\) boundary edges. The ball has \(93\) edges in total, so the other \(54\) are interior.

Counting incident tetrahedra for each of these \(54\) interior edges gives the degree distribution
\[
1\cdot 3,\qquad 14\cdot 4,\qquad 21\cdot 5,\qquad 13\cdot 6,\qquad 5\cdot 7.
\]
The sole degree-three edge is \(\{2,3\}\). It occurs in exactly the tetrahedra
\[
\{2,3,4,13\},\qquad \{2,3,4,15\},\qquad \{2,3,13,15\}.
\]
Therefore its link has vertices \(4,13,15\) and edges \(\{4,13\},\{4,15\},\{13,15\}\), hence is the three-cycle.

Finally, the link of an interior edge in a triangulated \(3\)-manifold is a triangulated circle. A simplicial circle has at least three edges, so degree \(3\) is the smallest possible local degree for an interior edge. Thus the source's double-trefoil spanning edge is not only degree-minimal but uniquely so inside \(B_{15,66}\).

## Verification
The bundled `verify.py` parses the published compact facet notation without a pre-expanded face list, reconstructs the source sphere and ball, checks the face vector and the published boundary-triangle list, classifies boundary versus interior edges, counts every tetrahedron incidence, and verifies the exact link of \(\{2,3\}\). Running `python3 verify.py` must end with a single `VERIFY_OK` line reporting the counts in the finding.

## Relationship to prior work
Benedetti and Lutz introduce \(B_{15,66}\), prove that \(\{2,3\}\) is a double-trefoil knotted spanning edge, use that knot to prove non-collapsibility, print the complete parent facet table, and print the \(26\) boundary triangles. Their statement does not give the degree of \(\{2,3\}\), compare it with the other interior edges, or give the interior-edge degree distribution. A full-text search of the exact source found no edge-degree statement.

General literature on knotted spanning edges explains their topological obstruction to shellability, local constructibility, or collapsibility, but does not force a particular local edge degree. The new point is therefore specific and structural: the globally complicated double-trefoil obstruction in this canonical small example sits on the unique locally degree-minimal interior edge.

## Limitations
This is an exact statement about the fixed labeled triangulation \(B_{15,66}\), not a theorem that every double-trefoil spanning edge can be realized at degree \(3\). The result does not classify how the edge degree changes under bistellar moves or subdivisions. The originality search cannot rule out an unindexed finite observation of the same incidence counts.

## References
B. Benedetti and F. H. Lutz, “Knots in collapsible and non-collapsible balls,” arXiv:1303.2070v1, first public 2013-03-08; *Electronic Journal of Combinatorics* 20(3) (2013), P31, DOI 10.37236/3319.

B. Benedetti, “Discrete Morse Theory for Manifolds with Boundary,” arXiv:1007.3175; *Transactions of the American Mathematical Society* 364 (2012), 6631–6670.
