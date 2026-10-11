# All seventy-six empty triangles are primitive systoles in the twelve-vertex twisted \(S^3\)-bundle
## Finding
Let \(K={}^{4}12^{54}_{1}\) be the Köhler--Lutz vertex-transitive twelve-vertex triangulation of the nonorientable sphere bundle
\[
S^3\widetilde{\times}S^1.
\]
The published complex has
\[
f(K)=(12,66,144,150,60)
\]
and full simplicial automorphism group of order \(96\).

The one-skeleton is complete, so it has
\[
\binom{12}{3}=220
\]
three-vertex cliques. Exactly \(144\) are triangular faces and the remaining \(76\) are nonfacial triangular cycles.

Every one of those \(76\) cycles represents a primitive generator of
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]
Consequently the simple integral homology \(1\)-systole has edge length \(3\), and its complete carrier set consists of all \(76\) empty triangles.

The full automorphism group has exactly three orbits on these systoles, of sizes
\[
12,\qquad48,\qquad16,
\]
represented by
\[
\{1,2,3\},\qquad\{1,2,6\},\qquad\{1,4,8\}.
\]
Its induced action on \(H_1(K;\mathbb Z)\) is the full group \(\{\pm1\}\): exactly \(48\) automorphisms preserve a chosen primitive generator and \(48\) reverse it.

## Assumptions and scope
The complex is the labelled `manifold_4_12_54_1` data set. Vertices are \(1,\ldots,12\), and the \(60\) facets are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in integral first homology is nonzero. A primitive class in \(H_1\cong\mathbb Z\) is a generator up to sign.

For an increasing triple \(a<b<c\), the verifier orients its triangular cycle as
\[
a\to b\to c\to a.
\]
The split of these chosen orientations into positive and negative evaluations is label-dependent; primitivity and the three unoriented carrier orbits are intrinsic to the labelled simplicial complex.

## Proof
The \(60\)-facet presentation reconstructs all \(66=\binom{12}{2}\) edges, \(144\) triangles, and \(150\) tetrahedra.

Contract the spanning tree consisting of the eleven edges from vertex \(1\) to the other vertices. The graph cycle lattice then becomes \(\mathbb Z^{55}\). Each of the \(144\) triangular faces supplies one integral relation.

The verifier performs only unimodular integral row and column operations on this \(144\times55\) relation matrix. It produces an identity block of size \(54\) and a zero residual block. Hence
\[
H_1(K;\mathbb Z)\cong
\mathbb Z^{55}/\operatorname{im}\partial_2
\cong\mathbb Z.
\]

An explicit integral cocycle \(y\) on the \(55\) non-tree edges is stored in `verify.py`. It annihilates every one of the \(144\) facial boundary relations and evaluates to a unit on the cycle \(1\to2\to3\to1\). Because the quotient has already been proved free of rank one, evaluation against \(y\) is an isomorphism
\[
H_1(K;\mathbb Z)\longrightarrow\mathbb Z.
\]

There are \(220-144=76\) nonfacial three-vertex subsets. Exhaustive evaluation gives \(+1\) on \(30\) increasing-label orientations and \(-1\) on \(46\). Therefore every empty triangle is nonzero and primitive. No simple cycle has fewer than three edges, so these are exactly all simple integral homology \(1\)-systoles.

For symmetry, the verifier exhausts all vertex permutations that preserve triangular-face membership by backtracking and then checks the complete facet set at every leaf. It finds exactly \(96\) simplicial automorphisms, agreeing with the published group order. Their action on the \(76\) carrier sets has orbit sizes \(12,48,16\). Applying every automorphism to an oriented primitive triangular cycle and evaluating with \(y\) gives \(48\) actions by \(+1\) and \(48\) by \(-1\).

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs every face from the complete facet list, performs the integral unimodular reduction, verifies the cocycle against every facial relation, exhausts every three-vertex subset, enumerates the full automorphism group by finite backtracking, and computes the carrier orbits and induced \(H_1\)-actions.

Exact successful output:

`VERIFY_OK f=12,66,144,150,60 H1_Z=Z all_triangles=220 facial3=144 empty3=76 all_empty3_primitive=yes oriented_pairings=+1:30,-1:46 aut=96 carrier_orbits=12,48,16 reps=123|126|148 H1_action=+1:48,-1:48`

The integral claim is not inferred from a finite-field calculation or from the published homology table.

## Relationship to prior work
Köhler and Lutz enumerate the exact vertex-transitive complex as \({}^{4}12^{54}_{1}\), identify its topological type as the twisted \(S^3\)-bundle over \(S^1\), record the face vector \((12,66,144,150,60)\), and give its automorphism group as `t12n54(96)`. The companion manifold data supply the complete \(60\)-facet presentation and record the integral homology.

Those published facts determine the ambient group \(H_1\cong\mathbb Z\) and the symmetry order, but they do not state which of the \(76\) missing triangular faces represent the generator, nor the complete \(12,48,16\) orbit decomposition of the shortest homology carriers.

Focused semantic searches using the exact data-set label, twisted-bundle aliases, empty-triangle language, primitive-generator language, shortest-loop language, and the numerical fingerprint \(76\) did not locate a covering statement.

## Limitations
The theorem concerns simple simplicial cycles in this fixed twelve-vertex triangulation. It does not compare other triangulations of the twisted sphere bundle or a geometric metric systole.

The signs \(30\) versus \(46\) obtained from increasing-label orientations are not asserted as an intrinsic invariant; only the fact that all \(76\) cycles are primitive is used in the finding.

A 2004 preprint version of the vertex-transitive census is bibliographically attested only at year resolution. The machine-readable public-source date is therefore the earliest inspected day-resolved release of that census, its 2005-06-24 arXiv submission; no day was invented for the earlier preprint.

An unindexed historical computation may contain the same finite carrier-orbit census.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24; Table 5.
2. F. H. Lutz, *The Manifold Page*, data entries `manifold_4_12_54_1` in the four-manifold facet, homology, and topological-type tables.
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:`math/0506372v1`, Section 5.
