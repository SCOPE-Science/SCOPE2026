# Integral multipath homology and rotation character of the seven-vertex cyclic tournament

## Finding
Let \(T\) be the directed tournament on \(\mathbb Z/7\mathbb Z\) with \(i\longrightarrow j\) exactly when \((j-i)\bmod 7\in\{1,2,3\}\). Let \(X(T)\) be its *multipath complex*: the vertices of \(X(T)\) are the 21 directed arcs of \(T\), and an arc subset is a face precisely if its directed spanning subgraph is a disjoint union of simple directed paths and isolated vertices.

Its complete reduced **integral** homology is
\[
\widetilde H_k(X(T);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{13},&k=3,\\
\mathbb Z^{43},&k=4,\\
\mathbb Z^{17},&k=5,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, no integral torsion occurs. Moreover, let \(\rho:i\mapsto i+1\) act on arcs and on \(X(T)\), and let \(W=\mathbb Q(\zeta_7)\) be the six-dimensional irreducible rational representation of \(C_7=\langle\rho\rangle\), where a generator acts by multiplication by a primitive seventh root of unity. Then
\[
\widetilde H_k(X(T);\mathbb Q)\cong
\begin{cases}
\mathbb Q\oplus W^{\oplus2},&k=3,\\
\mathbb Q^{\oplus7}\oplus W^{\oplus6},&k=4,\\
\mathbb Q^{\oplus5}\oplus W^{\oplus2},&k=5,\\
0,&\text{otherwise}
\end{cases}
\]
as rational \(C_7\)-modules. The displayed trivial summands carry the identity action.

## Assumptions and scope
The tournament is exactly the specified orientation, not an arbitrary regular tournament, and the complex is the **arc-subset multipath complex**, not path homology, a directed flag complex, or a tournaplex. All homology is reduced, in the usual simplicial grading: an arc set with \(r\) arcs is an \((r-1)\)-simplex. The homology calculation is integral; the symmetry decomposition is over \(\mathbb Q\). No homotopy-wedge classification or result for other tournament orders is asserted.

## Proof
**Finite model.** Order the 21 arcs lexicographically by their ordered vertex pairs. A subset of arcs is a face if and only if every vertex has in-degree and out-degree at most one in the subset, and no directed cycle occurs. Exhaustive traversal using this criterion yields the face counts in dimensions \(0,1,2,3,4,5\):
\[
(21,168,630,1113,819,175).
\]
There are no larger faces, since a directed path forest on seven vertices has at most six arcs. The complete face set therefore has 2,927 faces including the empty face.

**Integral reduction.** Apply successive face/coface matchings, in lexicographic arc order: at each stage pair every still-unmatched face not containing the current arc with its coface obtained by adding that arc, whenever the coface is still unmatched. The complete directed Hasse diagram (all unmatched covering relations directed downward, matched relations upward) is acyclic; an exhaustive topological ordering verifies this. The matching has 1,415 pairs and leaves exactly one critical vertex, 24 critical three-cells, 54 critical four-cells, and 17 critical five-cells.

For oriented simplicial boundaries use increasing arc order and the sign \((-1)^j\) on deletion of the arc in zero-based position \(j\). Algebraic Morse elimination follows all gradient paths with these exact signs. The only potentially nonzero positive-degree Morse differentials are
\[
\partial_4:\mathbb Z^{54}\longrightarrow\mathbb Z^{24},\qquad
\partial_5:\mathbb Z^{17}\longrightarrow\mathbb Z^{54}.
\]
The second is identically zero. Exact rational elimination establishes \(\operatorname{rank}(\partial_4)=11\), and the matrix contains an \(11\)-by-\(11\) minor of determinant \(-1\). With critical faces in increasing bitmask order, the zero-based indices of its selected rows are
\[
(3,2,12,13,11,14,5,4,20,10,1)
\]
and its selected columns are
\[
(5,9,14,15,17,23,25,27,32,46,47).
\]
Therefore all 11 nonzero Smith factors of \(\partial_4\) equal one, and all other differentials vanish. The critical-cell counts give the stated free integral homology in degrees three, four and five, and zero reduced homology elsewhere.

**Rotation representation.** Every nonempty simplex has a free orbit of length seven under \(\rho\): a fixed nonempty arc subset would be a union of full seven-element arc orbits, whereas every face contains at most six arcs. The ordinary oriented chain complex, modulo the signed rotation relation, has orbit-chain ranks
\[
(3,24,90,159,117,25)
\]
in degrees zero through five. Using orbit representatives chosen by least arc-subset bitmask, the signed boundary matrices of this coinvariant complex have **exact rational** ranks
\[
(2,22,68,90,20)
\]
in degrees one through five. In degree zero the quotient complex is connected. Its positive-degree rational homology consequently has dimensions \(1,7,5\) in degrees three, four and five respectively, zero otherwise.

Because the group has order seven, rational invariants, coinvariants and the homology of the quotient chain complex have equal dimensions. The only rational irreducible representations of \(C_7\) are the one-dimensional trivial module and \(W\), of dimension six. Combining invariant dimensions \((1,7,5)\) with total dimensions \((13,43,17)\) uniquely gives the asserted module multiplicities.

## Verification
The accompanying standalone programs `verify_integral.py` and `verify_independent.py` require Python 3.9 or later and only its standard library; run from the directory containing the files with `python verify_integral.py` and `python verify_independent.py`. The first reconstructs every face, every matching pair and the complete directed Hasse graph, verifies acyclicity, performs signed Morse elimination, calculates the exact rational boundary rank, and checks the stated unimodular minor by integer-preserving determinant elimination. The second uses **independent combinations-based enumeration** and direct signed simplicial boundaries, checks the ordinary chain ranks over four finite fields, constructs rotation-orbit boundary matrices, and checks their ranks over two finite fields and exactly over \(\mathbb Q\).

The direct unsigned homology checks give ordinary Betti numbers \((1,0,0,13,43,17)\) in degrees zero through five, hence the reduced ranks stated above. Nonidentity rotation has reduced Lefschetz number \(-1\): the representation formula yields \(-(-1)+1-3=-1\), consistently with the absence of any fixed nonempty face.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith introduced the multipath-complex framework, studied several directed-graph families, and proved a wedge-of-spheres theorem specifically for **transitive** tournaments. The present \(T\) contains directed cycles and is not transitive; that theorem does not compute this example. Caputi, Collari and Di Trani previously related multipath cohomology to the shifted homology of the associated simplicial complex, but did not provide these seven-vertex regular-tournament groups. Govc, Levi and Smith studied tournaplexes and directionality filtrations on vertex-subtournaments; those are different complexes from arc-subset multipath complexes. The present result concerns the full integral groups and their rotation representation for one precisely specified nontransitive regular tournament.

## Limitations
No full homotopy type, higher homotopy operation, integral equivariant splitting, or general formula for regular tournaments of other orders is asserted. The proof is a complete finite calculation with an explicit reproducible signed integral certificate; independently checking the public computation is encouraged. Existing publications and indexed mathematical records were searched, but an unindexed equivalent calculation cannot be ruled out. No independent mathematical audit has been performed.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first submitted 9 August 2022), subsequently *Mathematika* **70** (2024), e12235. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, *Journal of Algebraic Combinatorics* (2022), DOI 10.1007/s10801-022-01180-9. https://doi.org/10.1007/s10801-022-01180-9
3. D. Govc, R. Levi, J. P. Smith, *Complexes of tournaments, directionality filtrations and persistent homology*, *Journal of Applied and Computational Topology* **5** (2021), 313–337. https://doi.org/10.1007/s41468-021-00068-0
