# The Grötzsch \(4\)-cut complex is a mixed-dimensional sphere wedge

## Finding
Let \(G=\mu(C_5)\) be the Grötzsch graph. Its ordinary \(4\)-cut complex has the integral homotopy type
\[
\Delta_4(G)\simeq\bigvee^4 S^5\vee\bigvee^5 S^6.
\]
In particular, its only nonzero reduced integral homology groups are \(\widetilde H_5\cong\mathbb Z^4\) and \(\widetilde H_6\cong\mathbb Z^5\). The complex is pure of dimension \(6\), but is **not shellable**: the nonzero reduced homology in dimension \(5\) is an obstruction to shellability of a pure six-dimensional complex.

## Assumptions and scope
All graphs are finite, simple and undirected. Number the graph vertices \(0,\ldots,10\), with indices in the five-cycle interpreted modulo \(5\). The original five-cycle has edges \(\{i,i+1\}\); the twin vertex \(5+i\) has edges to the original vertices \(i-1\) and \(i+1\); the apex \(10\) has edges to every twin. These are all \(20\) edges. In particular this is the usual \(11\)-vertex, triangle-free, four-chromatic Mycielski graph.

The ordinary \(4\)-cut complex \(\Delta_4(G)\) is the simplicial complex on the graph's vertex set whose facets are \(V(G)\setminus S\) for all four-element sets \(S\) such that the induced graph \(G[S]\) is disconnected. This is *not* the total cut complex, whose four-element sets must be independent.

## Proof
**Finite face reconstruction.** Exactly \(180\) of the \(\binom{11}{4}=330\) four-element induced subgraphs are disconnected. Their seven-element complements produce the complete facet set. The nonempty face numbers by dimension \(0,1,\ldots,6\) are
\[
(11,55,165,330,462,431,180).
\]
Thus there are \(1,634\) nonempty faces and the complex is pure of dimension \(6\).

**An explicit acyclic matching.** Identify faces with bit masks, including the empty mask, and process pivot vertices in the order
`(0,3,8,4,9,5,7,6,2,10,1)`.
For each pivot \(i\), pair each still-unmatched face \(F\) not containing \(i\) with \(F\cup\{i\}\) when both are still available; scan faces first by increasing cardinality and then by integer bit mask. This gives \(813\) pairs on the augmented face poset, including \((\varnothing,\{0\})\), and leaves precisely four critical five-faces and five critical six-faces. Delete the single augmented pair to obtain an ordinary matching with \(812\) pairs and one additional critical vertex \(\{0\}\).

Reverse the arrows for matched face/coface incidences in the usual downward-directed Hasse diagram. The companion verifier constructs every one of the \(8,081\) incidences among nonempty faces and applies topological sorting to the directed graph. Every one of the \(1,634\) faces is removed, proving the matching **acyclic**, not merely locally consistent. The corresponding CW Morse complex therefore has one cell in dimension \(0\), four in dimension \(5\), five in dimension \(6\), and no others.

**Integral attaching degrees.** Orient each simplex by increasing vertex order. Write \(\epsilon(\sigma,\tau)\in\{+1,-1\}\) for its signed facet incidence. To compute the Morse boundary, define for a five-simplex \(\sigma\) its projection \(R(\sigma)\) into the free abelian group on the four critical five-simplices. It is the corresponding basis vector if \(\sigma\) is critical, zero if not critical and not matched upward, and otherwise, if \(\sigma\) is matched with a six-simplex \(\tau\),
\[
R(\sigma)=-\epsilon(\sigma,\tau)^{-1}
\sum_{\substack{\sigma'\subset\tau\\\dim\sigma'=5,\ \sigma'\ne\sigma}}
\epsilon(\sigma',\tau)R(\sigma').
\]
Acyclicity ensures this gradient-path recursion terminates. For each of the five critical six-cells \(\tau\), sum \(\epsilon(\sigma,\tau)R(\sigma)\) over its five-dimensional facets. The exact **integral** four-by-five Morse differential is the zero matrix. The verifier performs this signed recursion using arbitrary-precision integers.

**Homotopy conclusion.** The five-skeleton of the Morse CW complex is a wedge of four five-spheres. A six-cell attaches by a map from \(S^5\) to this five-skeleton. The Hurewicz map \(\pi_5(\bigvee^4S^5)\to H_5(\bigvee^4S^5;\mathbb Z)\cong\mathbb Z^4\) is an isomorphism. The attaching map is therefore nullhomotopic exactly when its degree column is zero. All five degree columns vanish, establishing the stated wedge decomposition integrally.

## Verification
Run the standalone standard-library program `verify_groetzsch_four_cut.py` with Python 3. It independently regenerates the graph, all facets and faces, the complete matching, directed Hasse acyclicity, the signed integral Morse boundary and all original simplicial boundary ranks over \(\mathbb F_2\). Its exact success marker is
`GROETZSCH_4CUT_180_FACETS_1635_FACES_812_ACYCLIC_PAIRS_4S5_5S6_EXACT_OK`.

Original boundary ranks in dimensions \(1\) through \(6\), computed independently over \(\mathbb F_2\), are \((10,45,120,210,252,175)\), giving reduced Betti ranks \(4\) and \(5\) in degrees \(5\) and \(6\). These finite checks are exhaustive because the ground set has exactly eleven vertices. The integral homotopy conclusion also uses the standard discrete Morse and Hurewicz theorems, as detailed above.

## Relationship to prior work
Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue introduce and analyze ordinary cut complexes and determine homotopy types for several graph families, including cycles, complete multipartite graphs and prisms over cliques. Their subsequent work treats disjoint unions, squared paths and grids. Neither cited set of graph-family theorems contains the eleven-vertex Mycielski graph. Their work on **total** cut complexes studies a different facet condition for \(k>2\).

The present calculation concerns precisely the ordinary \(4\)-cut complex of the canonical triangle-free four-chromatic graph. Its nonzero next-to-top integral homology distinguishes it from the top-dimensional wedges found for several familiar graph families, and provides a concrete non-shellability obstruction. Other complexes built from the Grötzsch graph, such as its matching complex or Čech nerve, have different simplex sets and do not determine this cut-complex homotopy type.

## Limitations
This is an exact result for one named finite graph, not a classification for all Mycielski graphs or all four-chromatic graphs. The result does not determine the integral automorphism representation, cup products or the complete cut filtration. No independent audit has been performed. Although no covering result was found in the specifically examined literature and indexed records, unindexed or inaccessible prior work, including the 2018 preliminary report cited by the foundational authors, remains a bibliographic risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first public 2022-09-27).
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26); SIAM J. Discrete Math. 38 (2024), 1630–1675.
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first public 2024-07-11); SIAM J. Discrete Math. 39 (2025), 1123–1157.
4. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008 (discrete Morse background).
