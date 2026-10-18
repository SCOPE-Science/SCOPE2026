# The \(2\times2\times3\) honeycomb perfect-matching complex is a wedge of two four-spheres

## Finding
Let \(H_{2\times2\times3}\) denote the honeycomb graph dual to the subdivision of a lattice hexagon with consecutive side lengths \(2,2,3,2,2,3\) into elementary equilateral triangles. Let \(\mathcal M_p(H)\) be the simplicial complex whose vertices are graph edges that occur in perfect matchings and whose facets are the perfect matchings. Then
\[
\mathcal M_p(H_{2\times2\times3})\simeq S^4\vee S^4.
\]
Equivalently, its reduced integral homology is \(\widetilde H_4\cong\mathbb Z^2\) and vanishes in all other degrees. This is a homotopy equivalence, not merely a homology computation.

## Assumptions and scope
The graph is finite, simple and undirected. A perfect matching covers every vertex exactly once. The triangular hexagonal region has \(32\) elementary triangles, and its dual graph has \(32\) vertices and \(41\) edges; each perfect matching corresponds to a lozenge tiling. This is the standard \(H_{2\times2\times3}\) convention of Bayer, Jelić Milutinović and Vega. The theorem concerns that one graph, not the family of all honeycombs.

For an explicit finite specification, enumerate the \(2\times2\) matrices \(h=(h_{i,j})\), with indices \(i,j\in\{0,1\}\), entries in \(\{0,1,2,3\}\), weakly decreasing along rows and columns. Put \(c_j(t)=\#\{i:h_{i,j}>t\}\) and \(r_i(t)=\#\{j:h_{i,j}>t\}\) for \(t\in\{0,1,2\}\). For each such matrix, the associated perfect matching contains the following \(16\) labeled rhombi:
\[
\begin{aligned}
& (z,i-h_{i,j},j-h_{i,j}) && (i,j\in\{0,1\}),\\
& (x,c_j(t)-t,j-t) && (j\in\{0,1\},\ t\in\{0,1,2\}),\\
& (y,i-t,r_i(t)-t) && (i\in\{0,1\},\ t\in\{0,1,2\}).
\end{aligned}
\]
Here a label \((a,u,v)\) denotes the lozenge formed by two adjacent elementary triangles when the pair of side vectors is, respectively, \((e_y,e_z)\) for \(a=x\), \((e_x,e_z)\) for \(a=y\), and \((e_x,e_y)\) for \(a=z\), where \(e_x=(1,0)\), \(e_y=(0,1)\), and \(e_z=(-1,-1)\). The offset is \((u,v)\). These are exact lattice coordinates, not numerical approximations.

## Proof
**Facets.** The weakly decreasing matrices yield precisely \(50\) distinct rhombus tilings. Each contributes one \(15\)-simplex, and its subfaces are exactly the partial perfect matchings extendible to complete perfect matchings. The independent dual-triangle enumeration in `verify_triangular_dual.py` constructs the region from its all-zero height tiling, joins pairs of elementary triangles sharing a side, recursively lists all perfect matchings of this graph, and verifies exact equality of the resulting \(50\) facets with the coordinate-parametrized facets above. Thus the enumeration is complete, not a sample of tilings.

**Acyclic element pairings.** Number the \(41\) distinct rhombus labels by sorting the triples lexicographically, with orientation labels ordered \(x,y,z\), starting at index zero. Encode a face by the integer sum of the powers of two indexed by its rhombi. Start with every nonempty subface of every facet. For each pivot index in the ordered tuple
\[
(24,1,17,12,40,6,7,28,34),
\]
pair every currently unmatched face \(\sigma\) not containing the pivot with \(\sigma\cup\{p\}\) when both remain unmatched; then delete both from the unmatched set. These pairs differ by exactly one vertex and are mutually disjoint within each stage.

For clarity, the *stagewise element-pairing lemma* states that distinct pivots applied successively in this way give an acyclic matching on the original face poset. In a hypothetical closed gradient path, take the earliest pivot-stage used, say stage \(j\), with pivot \(p_j\). Traversing one stage-\(j\) matched pair in the gradient direction inserts \(p_j\). A descending step from a matched upper face of stage \(j\) cannot remove \(p_j\), since that would traverse its own matched edge backward. Neither can a descending step from a later-stage matched upper face remove \(p_j\): its upper and putative lower faces both survived to stage \(j\), so they would have formed a stage-\(j\) pair, a contradiction. Later-stage matched edges use different pivots and cannot remove \(p_j\). Thus the path cannot return to its stage-\(j\) lower face, contradicting cyclicity. This also handles matching stages after the survivor set is no longer a simplicial subcomplex.

**Exhaustion and critical dimensions.** Complete enumeration of the nonempty face poset gives \(2,517,787\) faces. The nine pairing stages leave respectively \(495177,133,73,21,15,9,7,5,3\) unmatched faces, with numbers of pairs \(1011305,247522,30,26,3,3,1,1,1\). The final three critical face masks are
\[
16777216,\quad 2155873346,\quad 137439215754.
\]
Their numbers of vertices are \(1,5,5\), so their simplicial dimensions are \(0,4,4\). The remaining complex has no other critical cells.

Discrete Morse theory therefore gives a CW complex with one zero-cell and precisely two four-cells. Every attaching map of a four-cell into a point is null, yielding \(S^4\vee S^4\). This proves the claimed integral homotopy type.

## Verification
Run `python3 verify_plane_partitions.py` and `python3 verify_triangular_dual.py` with Python 3; no nonstandard dependencies are needed. The two programs use different facet generators: monotone plane partitions versus a recursive perfect-matching search on the \(32\)-vertex dual graph. They agree on all \(50\) facets, \(41\) edge labels, the complete face vector and every pairing-stage count. The full face vector in dimensions \(0\) through \(15\) is
\[
(41,706,6186,31566,104477,241386,407750,517618,501141,371866,210600,89700,27900,6000,800,50).
\]
The programs verify all \(2,517,788\) faces including the empty face, then reduce the nonempty face poset. Independent enumeration also checks the known control \(H_{2\times2\times2}\simeq S^3\vee S^3\); the plane-partition verifier separately checks \(H_{2\times2\times1}\simeq S^1\). The recorded exact outputs are `plane_partitions_output.txt` and `triangular_dual_output.txt`.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega (arXiv:2209.02803v1, first public September 6, 2022) proved the complete one-unit-width cases and \(\mathcal M_p(H_{2\times2\times2})\simeq S^3\vee S^3\), explicitly identifying wider honeycombs as a further direction (their Theorem 17 and Section 5). These statements do not imply the new homotopy type. The classical plane-partition enumeration determines the number of maximal simplices, not the attaching maps or homotopy type.

Chandrakar and Singh (arXiv:2407.05809v2) studied perfect-matching complexes of polygonal *line* tilings and ladder grid graphs. Those graphs are not the two-dimensional hexagonal honeycomb considered here, so their wedge-of-spheres theorem does not subsume this computation. Relevant published matching-complex calculations on other graphs also do not determine this complex.

## Limitations
The theorem is an exact, reproducible, finite combinatorial classification for a single next-size honeycomb. No formula for all \(H_{2\times2\times n}\) and no assertion about the full ordinary matching complex are claimed. Its proof relies on exhaustive integer/set enumeration together with the mathematical acyclicity lemma, not on numerical sampling.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (September 6, 2022); Electronic Journal of Combinatorics 30(2) (2023), P2.45. https://arxiv.org/abs/2209.02803
2. H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v2. https://arxiv.org/abs/2407.05809
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
