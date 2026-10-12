# Three-periodic rigidity of maximum edge open packings in ladder graphs

## Finding

Let \(L_n=P_2\square P_n\) be the ordinary two-rail ladder with \(n\ge2\) rungs, and let \(\rho_e^o(G)\) denote the largest number of edges in an **edge open packing** of \(G\): an edge set whose endpoints induce a disjoint union of nontrivial stars, with all edges of those induced stars selected. Let \(M_n\) count distinct maximum edge open packings as edge subsets (not modulo graph automorphisms). Then, for every integer \(n\ge2\),

\[
\rho_e^o(L_n)=n,\qquad
M_n=\begin{cases}
4,&n\equiv2\pmod 3,\\
2,&n\equiv0,1\pmod 3.
\end{cases}
\]

Moreover, **all** maximum sets have an explicit classification. Choose one of the two checkerboard bipartition classes \(B=\{b_1,\ldots,b_n\}\) of the ladder, ordered by rung; write \(A=\{a_1,\ldots,a_n\}\) for its other class, so \(a_j\) lies in the same rung as \(b_j\). Form the indexed intervals
\[
I_j=[\max(1,j-1),\min(n,j+1)]\cap\mathbb Z\qquad(1\le j\le n).
\]
Choose a set \(T\subseteq\{1,\ldots,n\}\) for which the intervals \(\{I_j:j\in T\}\) partition \(\{1,\ldots,n\}\). Then take all edges \(a_jb_i\) with \(j\in T\) and \(i\in I_j\). Every maximum edge open packing arises in **exactly one** such way, and all such choices are maximum.

## Assumptions and scope

Graphs are finite, undirected and simple. The vertices of \(L_n\) are \((r,j)\) for \(r\in\{0,1\}\) and \(1\le j\le n\); two vertices are adjacent if they share their rung and differ in rail, or share their rail and occupy consecutive rungs. An edge open packing is an edge subset \(F\) for which the subgraph induced by the endpoints of \(F\) is a vertex-disjoint union of stars \(K_{1,t}\) with \(t\ge1\), and its edge set equals \(F\). This standard equivalent formulation is stated as Observation 1 in Das–Santra [1]. Distinct maxima are counted as labeled edge subsets of this fixed ladder. For \(n=2\), the two boundary intervals have the same underlying set but different labels/centres.

## Proof

**Upper bound and equality constraint.** In any edge open packing \(F\), orient each induced star from a chosen centre towards its leaves; for a single-edge star choose either endpoint as its centre. The union \(B_F\) of all leaves is an independent vertex set of the original graph: leaves of one star are independent, and different induced components have no edges between them. There is precisely one leaf per selected edge, so \(|B_F|=|F|\). Every rung of \(L_n\) is a two-vertex clique, hence \(|B_F|\le n\) and \(|F|\le n\). If equality holds, \(B_F\) contains exactly one vertex of every rung. Because vertices on the same rail in consecutive rungs are adjacent, these choices must alternate rails. Thus \(B_F\) is one of precisely two checkerboard classes.

**Classification.** Fix this checkerboard class \(B=\{b_1,\ldots,b_n\}\), with the complementary class \(A=\{a_1,\ldots,a_n\}\). Its vertex \(a_j\) is adjacent to exactly \(b_i\) for \(i\in I_j\): to \(b_j\) along the rung, and to the available \(b_{j-1},b_{j+1}\) along the rail. If \(|F|=n\), every vertex \(b_i\) is a leaf of an induced star of \(F\), therefore has exactly one neighbour among the selected star centres. The centres all lie in \(A\), and selecting \(a_j\) necessarily gives all edges to \(b_i\) for \(i\in I_j\); otherwise an unselected edge would occur inside the induced endpoint graph. Hence the intervals of the selected centre indices partition \(\{1,\ldots,n\}\). Conversely, if these intervals partition the index set, each \(b_i\) has exactly one selected neighbour, every selected \(a_j\) has at least one leaf, there are no edges inside either checkerboard class, and all selected components are stars. Their edge set therefore is an edge open packing of exactly \(n\) edges. This also proves existence of equality once the interval partitions are enumerated.

**Counting indexed interval partitions.** The endpoint tiles \(I_1\) and \(I_n\) have length two, and all other indexed tiles have length three. For \(n=2\), the two endpoint tiles share their underlying interval but designate distinct centres. A partition may choose neither endpoint tile, exactly the left endpoint tile, exactly the right endpoint tile, or both; in these four cases respectively the total length is \(3k\), \(2+3k\), \(3k+2\), or \(4+3k\), where \(k\ge0\), subject to the obvious valid placement. All interior tiles of length three are then forced consecutively, with centre at their middle rung. For \(n\ge2\), the possibilities are: one partition if \(n\equiv0\pmod3\), using neither endpoint tile; one if \(n\equiv1\pmod3\), using both; and two if \(n\equiv2\pmod3\), using exactly one endpoint tile. Each interior three-block has exactly one centre index, so there are no additional tilings.

Finally the two checkerboard classes produce distinct packings. Indeed, if an edge packing were represented using both as its leaf class, every vertex of the ladder would be an endpoint of a selected edge; but the full ladder has a cycle and so is not an induced star forest, for \(n\ge2\). Multiplying the partitions-per-class by two gives the stated \(M_n\) and the constructed packings attain the upper bound.

## Verification

The accompanying standalone `verify.cpp` enumerates all nonempty vertex subsets for each \(2\le n\le11\), retaining precisely those whose induced graph has no isolated vertices and no edge joining two vertices of induced degree at least two. This is equivalent to being an induced disjoint union of nontrivial stars; its edges are an edge open packing. Every such edge subset uniquely determines its endpoint subset, so the exhaustive optimum count is exact at each tested order. The program checks both the optimum value and number of distinct maxima against the theorem. It tested **5,592,390** nonempty endpoint subsets, with all ten parameter values passing. Compile with `g++ -std=c++17 -O3 verify.cpp -o verify` and execute `./verify`; expected stdout is provided in `verify_output.txt`. The infinite conclusion rests on the proof, not on extrapolation from these checks.

## Relationship to prior work

Chelladurai–Kalimuthu–Soundararajan [4] introduced edge open packing and investigated its value on several elementary graph families. Brešar–Samadi [3] established algorithmic aspects and general bounds. Brešar–Dravec–Hedžet–Samadi [2] studied graph products, proving general Cartesian-product bounds and the existing general bound \(\rho_e^o(G)\le\alpha(G)\); neither that bound nor the induced-star characterization is new here. Das–Santra [1], first public on 1 October 2026, proves algorithms for broad graph classes, including convex bipartite graphs, but its stated results do not classify maximum packings or their number on the ordinary ladder. The contribution here is a complete extremal classification and exact period-three count for this natural Cartesian-product family, rather than a new general algorithm or a new general inequality.

## Limitations

The result concerns the ordinary two-rail ladder only, not wider grids, cylindrical ladders or weighted packings. It counts labeled edge subsets, not automorphism orbits or all suboptimal packings. General algorithms in [1] already permit optimization on the graph class. Some recent algorithmic preprints by related authors were available only through summaries at inspection; equivalent specialized results in inaccessible, unindexed or differently named literature cannot be excluded. No independent external review has occurred.

## References

[1] G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275v1 (1 October 2026), https://arxiv.org/abs/2610.02275.

[2] B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v2 (2024), https://arxiv.org/abs/2406.04020.

[3] B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1 (2024), https://arxiv.org/abs/2403.00750.

[4] A. Chelladurai, C. Kalimuthu and A. Soundararajan, *Edge open packing sets in graphs*, RAIRO—Operations Research (2022), DOI:10.1051/ro/2022171.
