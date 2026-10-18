# Integral homology and antipodal action of the octahedral directed-linear-forest complex

## Finding
Let \(O=K_{2,2,2}\) be the one-skeleton of a regular octahedron, with three opposite-vertex pairs, and let \(\overleftrightarrow O\) contain both orientations of its twelve edges. Let \(X=\operatorname{Dlf}(\overleftrightarrow O)\) be the simplicial complex whose vertices are the 24 directed arcs and whose faces are precisely those arc sets forming vertex-disjoint directed paths, with directed cycles forbidden. Then
\[
\widetilde H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&k=2,\\
\mathbb Z^{92},&k=3,\\
\mathbb Z^{32},&k=4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, all integral homology is torsion-free. The central antipodal automorphism \(\iota\) interchanges the endpoints of each of the three opposite pairs. Its induced action on rational homology has eigenspace dimensions
\[
\begin{array}{c|cc}
 k &\dim H_k(X;\mathbb Q)^{+}&\dim H_k(X;\mathbb Q)^{-}\\\hline
2&2&1\\3&49&43\\4&12&20
\end{array}
\]
with \(H_0\) one-dimensional and antipodal-even. Thus its reduced homological Lefschetz traces are \(1\), \(6\), and \(-8\) in degrees two, three, and four respectively.

## Assumptions and scope
Vertices of \(O\) are \(0,1,2,3,4,5\), with opposite pairs \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5\}\). There is a directed arc \((u,v)\) for every ordered pair with \(\lfloor u/2\rfloor\ne\lfloor v/2\rfloor\). Face dimension is the number of arcs minus one. An admissible arc set has in-degree and out-degree at most one at each graph vertex and contains no directed cycles, including two-cycles. The antipodal map is \(u\mapsto u\mathbin{\mathrm{xor}}1\), acting on each arc's two endpoints. All homology has integral coefficients unless otherwise specified. No assertion concerning the full homotopy type, cup products, or the entire octahedral group representation is made.

## Proof
List arcs lexicographically by ordered endpoint pair and identify arc subsets with 24-bit integers. Starting with the empty face, adjoin an arc exactly when the new source has no outgoing arc, the target has no incoming arc, and following the present successor chain from the target does not reach the source. Exhaustive recursion terminates after five arcs because an acyclic directed path forest on six graph vertices has at most five arcs. It produces exactly \(24,192,616,744,240\) nonempty simplices in dimensions \(0,1,2,3,4\), respectively.

Perform the sequential vertex-toggle matching with the fixed arc-index order
\[
(6,16,21,14,1,5,19,10,9,13,23,12,3,8,20,22,0,2,15,11,4,17,18,7).
\]
At each step pair every still-unpaired face not containing the selected arc with its still-unpaired coface obtained by adjoining the selected arc. There are 843 disjoint pairs and critical-cell counts \((1,0,4,93,32)\). Orient every face by increasing arc index. Direct every cover relation downwards except matching edges, which point upwards. All 6,408 nonempty-face cover relations admit a directed topological ordering of all 1,816 faces, proving this is an acyclic Forman matching.

The integral Morse differential is computed by eliminating each paired lower face using the signed boundary equation of its matched upper face. With \(p\) the coefficient \(\pm1\) of the paired face, replace its formal chain by \(-p\) times the sum of the remaining signed boundary faces. The absence of closed gradient paths makes the recursive expansion finite. The differential from critical three-cells to four critical two-cells is a \(4\times93\) integer matrix of rank one, with every nonzero entry \(\pm1\) and all nonzero rows equal up to sign. Its unique nonzero Smith factor is therefore one. The differential from the 32 critical four-cells to the 93 critical three-cells is identically zero. Other reduced Morse differentials vanish for dimension reasons. Consequently, integral homology has ranks \(4-1=3\), \(93-1=92\), and \(32\) in degrees two, three, and four and has no torsion.

For the symmetry, let \(C_k^{\pm}\) be the eigenspaces of the involution on rational simplicial chains. Signed fixed-simplex enumeration gives their dimensions \((12,12),(90,102),(308,308),(384,360),(120,120)\) for degrees zero through four. For the boundary maps in degrees one through four, the ranks of the \(+\) and \(-\) images are respectively \((11,12),(79,90),(227,217),(108,100)\). These ranks are determined by exact elimination over \(\mathbb F_{1009}\) of the projected columns \((1\pm\iota)\partial\). Their sums are \(23,169,444,208\), which also are the exact rational full-boundary ranks from the integral Morse calculation. Since reduction modulo a prime cannot increase rational rank, each projected finite-field rank is its rational rank. Subtract the two adjacent image ranks from the corresponding chain eigenspace dimension to obtain the displayed homology eigenspace table.

## Verification
The accompanying `verify_complex.py` regenerates every simplex from the graph definition, checks downward closure, constructs the matching, topologically sorts every directed cover relation, computes the signed integral Morse differential, and independently computes all mod-two simplicial boundary ranks. Its observed nonempty-face counts are \((24,192,616,744,240)\), Morse critical counts \((1,0,4,93,32)\), and mod-two boundary ranks \((23,169,444,208)\). The `verify_antipodal.py` script reproduces the full signed involution, the rationally sharp finite-field rank lower bounds, and the eigenspace table. Run both scripts with Python 3 from the same directory; neither requires third-party packages. Recorded outputs are included.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (2022, arXiv:2208.04656) define multipath complexes and analyze several families, including one-way oriented complete bipartite digraphs and complete bidirected graphs, but do not evaluate the bidirected octahedral graph. Caputi, Collari and Smith (2026, arXiv:2601.05670) study bidirected paths and polygons and their homology; the octahedral graph is neither such a path nor a polygon. Deshpande and Sawant (2026, arXiv:2602.14936) introduce the terminology directed linear-forest complex and provide structural criteria and open problems for digraphs with cycles; they do not give the integral homology or antipodal representation of this example. Available indexed exact results for the octahedral graph concern ordinary matching or ordinary discrete-Morse complexes, which are different complexes. The present calculation distinguishes a three-part complete multipartite digraph from previously treated one-way or bipartite configurations.

## Limitations
The classification concerns this specific six-vertex digraph and the antipodal subgroup, not arbitrary complete multipartite digraphs or the full automorphism representation. The finite exact verification establishes integral homology and the rational involution character, not a wedge-of-spheres homotopy equivalence. Literature search cannot exclude unindexed equivalent work; a direct complete prior classification would supersede originality. The computation relies on ordinary discrete Morse theory and exact finite matrix operations, not on inference from numerical samples.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first submitted 9 August 2022), Sections 1, 3, and 4.
2. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first submitted 9 January 2026), introduction and Theorems 2.8 and 2.10.
3. P. Deshpande and R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first submitted 16 February 2026), Sections 3, 5, and Problem 6.3.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
