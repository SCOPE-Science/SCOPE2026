# Cone-fillability detects the null empty-triangle orbit in a neighborly ten-vertex \(S^2\times S^1\)
## Finding
Let \(K\) be the ten-vertex simplicial complex obtained from the four cyclic tetrahedron orbits represented by \(1236\), \(1237\), \(1257\), and \(1368\) under the shift \(i\mapsto i+1\pmod{10}\). This is the neighborly vertex-transitive triangulation of \(S^2\times S^1\) listed as the class \(N^{10}_{3611}\), later as type \(2_{10}\), and in the public manifold data as `manifold_3_10_1_2`.

The exact complex has
\[
f(K)=(10,45,70,35)
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]
Because its one-skeleton is complete, every three vertices form a graph triangle. Of the \(120\) graph triangles, \(70\) are faces and \(50\) are empty triangles. Exactly \(40\) of the empty triangles represent nonzero homology classes, and every one of those classes is primitive. The other \(10\) empty triangles are null-homologous.

Under the published cyclic shift, the \(50\) empty triangles form five orbits of size \(10\), represented by
\[
124,\qquad 128,\qquad 129,\qquad 135,\qquad 147.
\]
After choosing a generator \(g\) of \(H_1(K;\mathbb Z)\), the corresponding oriented values are respectively \(g,0,g,g,-g\). Thus the orbit of \(128\) is the unique null-homologous empty-triangle orbit.

There is also a local characterization of that orbit. Call an empty triangle \(abc\) *cone-fillable* if some vertex \(v\notin\{a,b,c\}\) makes all three triangles \(vab\), \(vbc\), and \(vca\) faces of \(K\). Then an empty triangle is null-homologous if and only if it is cone-fillable. Every null empty triangle has exactly three cone apices. For the representative \(128\), they are \(3\), \(6\), and \(7\).

Consequently the simple integral homology \(1\)-systole of the one-skeleton, measured by number of edges in a simple cycle, equals \(3\), and it has exactly \(40\) minimizing cycles.

## Assumptions and scope
The claim concerns this exact combinatorial triangulation, with the cyclic labeling above. An *empty triangle* means a three-cycle in the one-skeleton whose three vertices do not span a \(2\)-simplex. A *simple integral homology \(1\)-systole* means the minimum edge length of a simple graph cycle representing a nonzero class in \(H_1(K;\mathbb Z)\). The statement is combinatorial; it does not assert a metric-geometric systole for any Riemannian realization.

## Proof
Contract the spanning tree consisting of the nine edges \(1j\) with \(2\le j\le10\). The integral graph-cycle lattice then has rank \(45-10+1=36\). Express the boundaries of the \(70\) triangular faces in the resulting chord basis, giving an integer relation matrix \(R\) of size \(70\times36\).

The supplied verification constructs a nonzero primitive integer vector \(w\in\mathbb Z^{36}\) with \(Rw=0\). Hence \(\operatorname{rank}R\le35\). It also exhibits a \(35\times35\) minor of \(R\) with determinant \(-1\). Therefore \(\operatorname{rank}R=35\), and the rank-\(35\) relation lattice is primitive in \(\mathbb Z^{36}\). It follows that
\[
\mathbb Z^{36}/\operatorname{rowspan}_{\mathbb Z}(R)\cong\mathbb Z,
\]
which is \(H_1(K;\mathbb Z)\).

The vector \(w\) is an integral cocycle coordinate for this quotient. Evaluating it on all \(50\) empty triangular cycles gives the exact distribution
\[
30\text{ with value }+1,\qquad 10\text{ with value }-1,\qquad 10\text{ with value }0.
\]
Thus the \(40\) nonzero empty triangles are primitive generators up to orientation. Since a simple cycle has at least three edges and such nonzero three-cycles exist, the simple integral homology \(1\)-systole is \(3\), with exactly \(40\) minimizers.

Direct orbit enumeration under the cyclic shift gives the five representatives \(124,128,129,135,147\), each with orbit size \(10\). Their cocycle values are constant up to the stated orientation convention and equal \(+1,0,+1,+1,-1\), respectively.

If an empty triangle has a cone apex \(v\), its oriented boundary is the sum of the three facial triangle boundaries \(vab+vbc+vca\), so it is null-homologous. Conversely, exhaustive examination of the ten possible vertex labels shows that the only empty triangles admitting such an apex are precisely the ten members of the \(128\) orbit. Each has exactly three apices; the representative \(128\) has apices \(3,6,7\). Since the cocycle computation already shows that this orbit is exactly the null orbit, cone-fillability is equivalent to null-homology among empty triangles.

## Verification
Run `artifacts/verify.py` with a standard Python \(3\) interpreter. The script contains the full \(35\)-tetrahedron facet list, reconstructs every face, builds the exact integral relation matrix, checks the unimodular minor and cocycle, enumerates all \(120\) graph triangles and all cyclic empty-triangle orbits, and verifies every cone apex. The recorded output is in `artifacts/verification_output.txt`.

The decisive checks are: \(f=(10,45,70,35)\); a rank-\(35\) unimodular relation minor; quotient \(H_1\cong\mathbb Z\); \(50\) empty triangles split as \(40\) primitive nonzero plus \(10\) null; five cyclic orbits of size \(10\); and cone-fillability exactly on the null orbit, with three apices per null triangle.

## Relationship to prior work
Altshuler's 1977 census contains the exact class \(N^{10}_{3611}\) among the orientable Class VI neighborly ten-vertex \(3\)-manifolds, records fundamental group \(\mathbb Z\) for Class VI, and states that these triangulate \(S^2\times S^1\). Kühnel and Lassmann's 1985 cyclic census lists the same complex as type \(2_{10}\), with the four generating tetrahedron orbits. Köhler and Lutz's 2005 vertex-transitive census identifies the same complex as a minimal \(S^2\times S^1\) triangulation with face vector \((10,45,70,35)\), cyclic automorphism group, and the same orbit representatives.

Those sources determine the object, topology, symmetry, and ambient first-homology type, but the inspected texts do not state the partition of its empty triangles into \(40\) primitive nonzero and \(10\) null cycles, the five-orbit homology spectrum, or the cone-fillability characterization of the null orbit.

## Limitations
The theorem is specific to this triangulation and this notion of edge-length systole. It does not classify empty-triangle homology shells for all ten-vertex triangulations of \(S^2\times S^1\), nor does it assert that cone-fillability detects null-homology in arbitrary simplicial \(3\)-manifolds. The originality comparison covers the indexed and directly inspected sources listed below; an unindexed historical finite computation could still contain the same census.

## References
A. Altshuler, *Neighborly 4-Polytopes and Neighborly Combinatorial 3-Manifolds with Ten Vertices*, Canadian Journal of Mathematics 29 (1977), 400--420, DOI `10.4153/CJM-1977-043-5`.

W. Kühnel and G. Lassmann, *Neighborly combinatorial 3-manifolds with dihedral automorphism group*, Israel Journal of Mathematics 52 (1985), 147--166, DOI `10.1007/BF02776088`.

E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv `math/0506520v1` (2005).

F. H. Lutz, *The Manifold Page*, dataset entry `manifold_3_10_1_2`.
