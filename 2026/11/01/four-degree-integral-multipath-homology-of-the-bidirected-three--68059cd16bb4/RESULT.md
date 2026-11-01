# Four-degree integral multipath homology of the bidirected three-cube

## Finding
Let \(D=\overleftrightarrow{Q_3}\) be obtained from the three-dimensional cube by replacing each undirected edge with both directed arcs. The multipath complex \(X(D)\) has the integral reduced homology
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^6,&i=3,\\
\mathbb Z^{45},&i=4,\\
\mathbb Z^{36},&i=5,\\
\mathbb Z^{12},&i=6,\\
0,&\text{otherwise}.
\end{cases}
\]
Moreover, \(X(D)\) is 2-connected, so the Hurewicz map identifies \(\pi_3(X(D))\) with \(\mathbb Z^6\). All integral homology groups are torsion-free. The assertion is an integral homology and connectivity classification, **not** a homotopy-equivalence-to-a-wedge assertion.

## Assumptions and scope
The vertices of the underlying cube are \(\{0,1,\ldots,7\}\), regarded as three-bit strings. For each vertex \(u\) and each \(k\in\{0,1,2\}\), the digraph has the arc \(u\to u\mathbin\oplus 2^k\), where \(\oplus\) is bitwise exclusive-or. Hence there are 24 directed arcs. A face of \(X(D)\) is a set of arcs with in-degree and out-degree at most one at every vertex, and without directed cycles. Equivalently, the selected arcs are disjoint unions of directed simple paths and isolated vertices. Only the ordinary simplicial homology of this finite complex is considered, with integer coefficients.

## Proof
**Finite reconstruction.** Index the arcs lexicographically by their ordered source-target pairs. The recursive enumeration in `verify.py` adds arcs only when no source or target repeats and no cycle appears. Independently, the checker enumerates all partial injective maps from the eight vertices to their allowed cube neighbors, discarding cycles; these two independent routes agree. They produce exactly 6,496 nonempty faces with the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)
=(24,216,928,2016,2160,1008,144).
\]
There are 29,136 codimension-one incidences.

**Integral discrete-Morse reduction.** Apply sequential elementary toggling matchings in the following explicit order of arc indices (indices begin at zero):
`[6,16,21,14,1,5,19,10,9,13,23,12,3,8,20,22,0,2,15,11,4,17,18,7]`.
At each index, pair every still-unpaired nonempty face not containing that arc with the face obtained by adding the arc, whenever both are still unpaired. The resulting 3,196 disjoint pairs leave the critical-cell vector
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)
=(1,0,0,7,47,37,12).
\]
The checker reconstructs all incidences, orients unmatched incidences downward and matched incidences upward, and verifies by an exhaustive topological sort of all 6,496 cells that the resulting directed Hasse graph is acyclic. Therefore the matched faces can be eliminated by unit integral boundary pivots, yielding an integral Morse chain complex with the critical-cell ranks just displayed.

**Exact Morse boundary.** For each matched lower face \(a\) paired with upper face \(b\), write its boundary incidence as \(\epsilon(a,b)=\pm1\). Replace \(a\), in every boundary computation, by
\[
-\epsilon(a,b)\sum_{t\subset b,\,|t|=|a|,\,t\ne a}\epsilon(t,b)\,t,
\]
recursively, discarding cells paired as uppers and retaining critical cells. Acyclicity makes this finite recursion well founded; it is precisely the usual integral unit-pivot reduction. With critical cells sorted by their arc bitmasks, the only potentially nonzero boundary matrices are
\[
\partial_4:\mathbb Z^{47}\to\mathbb Z^7,
\quad\partial_5:\mathbb Z^{37}\to\mathbb Z^{47},
\quad\partial_6:\mathbb Z^{12}\to\mathbb Z^{37}.
\]
The checker verifies that \(\partial_6=0\), while both \(\partial_4\) and \(\partial_5\) have rank exactly one and contain an entry equal to \(1\) or \(-1\). In fact, it checks every entry against a rank-one factorization through an explicit unit pivot, which certifies that all two-by-two minors vanish. Their complete nonzero integral Smith invariant-factor lists are thus respectively \((1)\) and \((1)\). The checker also verifies that consecutive Morse differentials compose to zero, without floating-point arithmetic or an external computer algebra dependency.

**Homology and connectivity.** From the critical-cell ranks and the two unit boundary pivots, the reduced integer Betti ranks in degrees three through six are \((6,45,36,12)\), with no torsion. The zero-, one-, and two-dimensional Morse skeleton consists of a single vertex. Thus \(X(D)\) is 2-connected, and the Hurewicz theorem gives \(\pi_3(X(D))\cong\mathbb Z^6\). This proves the finding.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It independently constructs the face set twice, validates all 29,136 incidences, checks the complete acyclic pairing, computes integral Morse boundaries by recursive elimination, checks the exact unit rank-one matrices, and independently obtains the ranks of the unreduced simplicial boundary maps over \(\mathbb F_2\). Expected output includes `VERIFY_OK`, 6,496 faces, 3,196 pairs, and the integral Betti vector \((1,0,0,6,45,36,12)\) in nonreduced degree-zero notation.

## Relationship to prior work
Caputi, Collari, and Smith (2026) study the bidirectional path and polygon digraphs and prove connectivity/homology theorems for cycles. The cube differs substantially: every underlying vertex has valence three, there are multiple intersecting four-cycles, and the result has nonzero reduced homology in four consecutive degrees rather than the one or two characteristic degrees in the polygon formula. Caputi, Collari, Di Trani, and Smith (2022/2024) treat directed paths, polygons and grid products with specified *one-way* edge orientations; those grid statements do not evaluate the fully bidirected cube. Also, the Morse complex of an undirected cube, the ordinary matching complex of the cube, and the multipath complex of a bidirected cube are distinct complexes, so their known homology does not imply this calculation.

## Limitations
The result does not determine the full homotopy type or attaching maps in dimensions greater than three. In particular, torsion-free integral homology is not evidence that the complex is a wedge of spheres. The computation is specific to the eight-vertex three-cube and does not give a formula for higher-dimensional hypercubes or for arbitrary bidirected regular graphs. The exact finite checker provides a reproducible proof but is not an independently authored certification.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09. https://arxiv.org/pdf/2601.05670
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, first posted 2022-08-09; published in *Mathematika* (2024). https://arxiv.org/pdf/2208.04656
3. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
