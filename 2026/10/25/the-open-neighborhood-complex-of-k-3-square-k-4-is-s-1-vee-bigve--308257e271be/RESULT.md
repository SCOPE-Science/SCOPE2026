# The open neighborhood complex of \(K_3\square K_4\) is \(S^1\vee\bigvee^{18}S^2\)

## Finding
Let \(R=K_3\square K_4=L(K_{3,4})\) be the twelve-vertex rook graph. Its **open Lovász neighborhood complex** has the exact integral homotopy type
\[
\boxed{\mathcal N(R)\simeq S^1\vee\bigvee^{18}S^2.}
\]
In particular, \(\pi_1(\mathcal N(R))\cong\mathbb Z\); its reduced integral homology is \(\mathbb Z\) in degree one, \(\mathbb Z^{18}\) in degree two, and zero in every other degree. The complex has dimension four, despite admitting this two-dimensional Morse model.

Equivalently, \(R=K_4\square C_3\). This is the shortest-cycle boundary excluded from the published \(K_m\square C_n\) neighborhood-complex wedge formula for \(m\ge4\) and \(n\ge5\). The numerical specialization of that formula to three cycle positions happens to agree, but its published proof uses a unique-common-center property that fails for \(C_3\). The present homotopy classification is proved independently by a complete integral discrete-Morse certificate.

## Assumptions and scope
Write the rook-graph vertex set as \(V=\{0,1,2\}\times\{0,1,2,3\}\), with index \(4a+b\) for the vertex \((a,b)\). Distinct vertices are adjacent precisely when they share a coordinate. The open neighborhood \(N_R(v)\) consists of the other three cells in the same row and the other two cells in the same column. A nonempty set \(\sigma\subseteq V\) is a face of \(\mathcal N(R)\) exactly when \(\sigma\subseteq N_R(v)\) for at least one center \(v\). The center is not itself included in its neighborhood; this is neither the closed-neighborhood complex nor the nonattacking-rooks independence complex.

The twelve open neighborhoods, each of size five, generate every nonempty face. Exhaustive deduplication yields \(270\) nonempty faces with face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(12,66,120,60,12).
\]
The assertion concerns this specified finite graph and ordinary, nonequivariant homotopy equivalence.

## Proof
**Complete finite model.** Each face is encoded by its twelve-bit vertex-incidence mask. Enumerating the nonempty subsets of all twelve five-element open neighborhoods is exhaustive by the definition of the complex. The preceding face counts follow from that enumeration; the standalone verifier independently reconstructs the graph, neighborhoods, and faces from the coordinate rule.

**An acyclic matching with twenty critical faces.** Use the vertex order
`(1, 7, 10, 0, 6, 11, 4, 5, 2, 8, 9, 3)`.
For each vertex index \(j\) in this order, process the nonempty faces in increasing mask order; whenever both still-unmatched faces \(\sigma\) and \(\sigma\cup\{j\}\) exist and \(j\notin\sigma\), match the pair and remove it from further stages. There are exactly \(125\) pairs and \(20\) unmatched faces, with dimensions: one vertex, one edge, and eighteen triangles.

For a fully independent acyclicity check, orient each matched codimension-one incidence from its lower face to its upper face and every unmatched incidence in the opposite direction. The resulting oriented Hasse graph has \(270\) nodes and \(792\) incidence arcs. The verifier topologically sorts all \(270\) nodes, so no directed cycle exists. By Forman's discrete Morse theorem, \(\mathcal N(R)\) is homotopy equivalent to a CW complex with precisely one \(0\)-cell, one \(1\)-cell, and eighteen \(2\)-cells. Its one-skeleton is \(S^1\).

**The integral attaching degrees vanish.** Orient each simplex by increasing vertex index; deleting its vertex in position \(p\) gives incidence \((-1)^p\). Let \(e_*\) denote the unique critical edge, indexed by the vertices \((7,10)\). Define an integer projection \(E\) on oriented edges: \(E(e_*)=1\); \(E(e)=0\) if \(e\) is matched downward to a vertex; and if \(e\) is matched upward to a triangle \(t\), recursively set
\[
E(e)=-[t:e]\sum_{e'\subset t,\ e'\ne e}[t:e']E(e').
\]
Here all displayed incidences are \(\pm1\). This is integral elementary elimination along the matched edge–triangle pairs. The recursion is well-founded because the matching is acyclic. For each critical triangle \(c\), its attaching degree onto the critical circle is
\[
d(c)=\sum_{e\subset c}[c:e]E(e).
\]
The verifier computes all eighteen values from the actual signed incidences and obtains \(d(c)=0\) for every critical triangle. This identity is an exact integer certificate, not a finite-field inference.

Every attaching loop of a two-cell to the unique circle is classified up to homotopy by its degree, since \(\pi_1(S^1)\cong\mathbb Z\). All eighteen maps are therefore null-homotopic. Attaching eighteen disks by nullhomotopic maps wedges on eighteen two-spheres. This proves the claimed homotopy equivalence and the asserted complete integral homology and fundamental group.

## Verification
Run `python3 artifacts/verify_rook34.py` with Python 3.10 or newer; only the standard library is used. It reconstructs all faces, checks every matching pair, independently verifies acyclicity of the full oriented Hasse graph, performs the exact signed recursive Morse boundary calculation, and independently checks the original simplicial boundary ranks over \(\mathbb F_2\) in degrees one through four: \((11,54,48,12)\). It checks the Euler characteristic \(18\) and exits with `ROOK34_HOMOTOPY_CERTIFICATE_OK`; its recorded output is `artifacts/verification_output.txt`. The integral homotopy conclusion relies on the verified matching and signed attaching-degree calculation, not on extrapolation or only on mod-two ranks.

## Relationship to prior work
Shukla [1] studies the same open-neighborhood functor, classifying graphs of maximum degree at most three and selected four-regular circulants; the five-regular graph \(K_3\square K_4\) is not in those classes. Matsushita's graph-theoretic fundamental-group comparison [2] is general, but does not itself identify the rook graph's attaching maps. Matsushita–Wakatsuki [3] relate neighborhood and dominance complexes through Alexander duality; their general duality alone does not determine this homotopy type.

The closest public all-parameter rook-graph result [4] identifies a quotient by a row–column core and homology above degree two, while explicitly not determining the first or second homology or full homotopy type. The published complete-graph–cycle-product theorem [5] assumes at least five cycle positions; its proof's unique-center lemma does not apply to the three-cycle, so substitution is not an implication of that theorem. The two-row rook-graph classification [6] assumes a two-row factor, whereas here both factors have at least three vertices. The known \(4\)-by-\(4\) open-rook case [7] instead has projective-plane two-torsion, so it is not an equivalent computation. A search under the alternative descriptions \(K_3\square K_4\), \(K_4\square C_3\), \(L(K_{3,4})\), and the three-by-four rook graph found no statement covering the present integral wedge decomposition. This is an evidence-bound comparison, not a proof of universal priority.

## Limitations
This does not classify the other rectangular rook graphs, determine symmetry actions, or extend the complete-graph–cycle-product theorem to every omitted short cycle. The matching is a complete certificate only for the stated twelve-vertex graph, with no inference about infinitely many graphs. Equivalent results under unindexed graph-Hom or neighborhood terminology remain possible.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13; *Electronic Journal of Combinatorics* 26(2) (2019), P2.4.
[2] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public 2012-10-10; *Journal of Mathematical Sciences, the University of Tokyo* 24 (2017), 321–353.
[3] T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first public 2023-12-05.
[4] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, public published-finding corpus research record, 2026-10-11, identifier `f09a20a3ee45`, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45`.
[5] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, public published-finding corpus research record, 2026-10-11, identifier `3a53c8927b3c`, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c`.
[6] *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, public published-finding corpus record, 2026-10-11, identifier `9b16e10ce620`.
[7] *The Kummer biplane block complex has an integral projective-plane summand*, public published-finding corpus record, 2026-10-11, identifier `6184c6679525`.
[8] R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
