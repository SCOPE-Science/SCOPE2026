# Shortest octahedral cycles and an index-three orbit lattice in the Bidiakis matching complex

## Finding
Let \(B\) be the twelve-vertex Bidiakis cube graph and let \(K=\mathcal M(B)\) be its ordinary matching complex. There is an integral homotopy equivalence
\[
K\simeq\bigvee^{10}S^3.
\]
The smallest number of vertices of an induced subcomplex of \(K\) with nonzero third homology is eight. Exactly **39** eight-vertex induced subcomplexes attain this bound. All are boundaries of four-dimensional crosspolytopes, equivalently joins \((S^0)^{*4}\); each is induced by four mutually vertex-disjoint two-edge paths of \(B\). Every one of their fundamental classes is nonzero and primitive in \(H_3(K;\mathbb Z)\), and the 39 classes together generate \(H_3(K;\mathbb Z)\cong\mathbb Z^{10}\) integrally. Ten explicitly indexed classes form an integral basis.

The graph automorphism group has eight elements. On the 39 shortest spheres it has nine orbits, with sizes
\[
(4,8,8,8,4,1,2,2,2).
\]
In that orbit order, their integral homology-span ranks are
\[
(4,8,8,5,3,1,2,2,2),
\]
and their saturation indices inside their respective rational spans in \(H_3(K;\mathbb Z)\) are
\[
\boxed{(1,3,1,1,1,1,1,1,1).}
\]
Thus one eight-element symmetry orbit has an **index-three obstruction to integral saturation** although all eight of its individual sphere classes are primitive. All other orbit-generated sublattices are saturated. The exact orbit order is the reproducible lexicographic order specified below.

## Assumptions and scope
Number the vertices of \(B\) by \(0,1,\ldots,11\), modulo 12. Include the cycle edges \(\{i,i+1\}\) and the chords \(\{i,i+s_i\}\), where \((s_0,s_1,s_2)=(-6,4,-4)\) is repeated four times. Unordered edges are included only once. This is the LCF description of the Bidiakis cube and gives exactly 18 edges. An \(r\)-simplex of \(K\) is a set of \(r+1\) pairwise vertex-disjoint edges of \(B\).

For reproducibility, sort the 18 graph edges as ordered pairs \((u,v)\) with \(u<v\), lexicographically, and identify each simplex with its 18-bit edge mask. Enumerate every two-edge path by ascending center vertex and ascending pair of its neighbors; choose quadruples of such paths in lexicographic order, retaining those using all twelve graph vertices. These give carrier indices \(0,1,\ldots,38\). Graph automorphism orbits are ordered by the smallest carrier index they contain. The displayed ranks and indices refer to that convention.

For a sublattice \(L\le H_3(K;\mathbb Z)\), its saturation index is \([\,(L\otimes\mathbb Q)\cap H_3(K;\mathbb Z):L\,]\), finite when \(L\) has the stated rank. All homology groups and lattice indices above are **integral**, not merely rational or modular.

## Proof
**1. An explicit perfect discrete-Morse matching.** Enumerate all nonempty simplices; the face vector in dimensions zero through five is
\[
(18,117,336,418,184,12).
\]
For pivot edge-vertices \(p=17,16,\ldots,0\), in increasing bit-mask order, pair any two presently unpaired faces \(\sigma\) and \(\sigma\cup\{p\}\) when the latter is a face and \(p\notin\sigma\). The resulting matching contains 537 disjoint Hasse pairs. Directly orient every matched Hasse edge upward and every unmatched edge downward. The entire directed graph has 1,085 nodes and is acyclic, as checked by an exhaustive topological ordering in `verify.py`. Exactly one zero-dimensional and ten three-dimensional faces remain critical. Forman's discrete-Morse theorem therefore gives a CW complex with one 0-cell and ten 3-cells, with no positive-dimensional cells in degrees one or two. All attaching maps are constant; consequently \(K\simeq\bigvee^{10}S^3\) and \(H_3(K;\mathbb Z)\cong\mathbb Z^{10}\). This proves integral torsion-freeness and excludes hidden higher-dimensional homology.

**2. Sharp minimal induced support.** For any flag complex \(L\) with \(\widetilde H_d(L;\mathbb Z)\ne0\), at least \(2d+2\) vertices are necessary. To see this, restrict to a vertex-minimal induced subcomplex with nonzero \(d\)-homology. For every vertex \(v\), deletion has zero \(d\)-homology; the deletion–star–link long exact sequence forces \(\widetilde H_{d-1}(\operatorname{lk}(v);\mathbb Z)\ne0\). By induction each link needs at least \(2d\) vertices. There must also be a nonneighbor of \(v\), since a flag complex with a universal vertex is a cone. Therefore there are at least \(1+2d+1\) vertices. Equality forces every vertex to have precisely one nonneighbor, so the one-skeleton is the complement of a perfect matching and \(L=(S^0)^{*(d+1)}\). The initial case \(d=0\) is two disconnected vertices. Applying this lemma with \(d=3\), any eight-vertex induced third-homology carrier is octahedral.

In a matching complex, the eight graph edges underlying such an octahedron split into four pairs of incident edges, with every edge in one pair disjoint from every edge in another. Thus the graph edges make four mutually vertex-disjoint paths of length two. The converse also holds: each such packing induces \((S^0)^{*4}\). Exhaustively checking the 36 two-edge paths of \(B\) yields exactly 39 such packings, hence exactly 39 induced eight-vertex octahedral three-spheres.

**3. Integral classes and spanning.** Orient the paths within each packing by their lexicographically ordered edge indices and orient the join of four zero-spheres by the ordered path pairs, with the shuffle sign needed to put every selected four-edge matching into increasing edge order. The resulting 16-term chain for each octahedron has integral boundary zero. All 39 boundaries are checked coefficient by coefficient.

In the discrete-Morse matching, precisely 172 pairs have lower faces of dimension three and upper faces of dimension four. Their unit signed incidence coefficients permit integral cancellation. The directed dependency graph between these lower three-faces is acyclic. Cancel these 172 pairs in a topological order and project a remaining cycle onto the ten critical three-faces. The 236 other remaining three-faces are paired as uppers with two-faces. The corresponding restricted third-boundary matrix has **full column rank 236 over \(\mathbb F_2\)**, checked independently by exact bit elimination; hence it is injective over \(\mathbb Z\). Consequently a three-cycle with all ten critical coefficients zero becomes zero after the 172 integral upper-degree cancellations, so these critical coordinates define an injective integral homomorphism \(H_3(K;\mathbb Z)\hookrightarrow\mathbb Z^{10}\). The later degree-three/two cancellations yield the same integral Morse coordinate map. The full acyclic matching also proves the target rank is ten.

The 39 resulting ten-component vectors all have coefficient gcd one. Hence every fundamental class is primitive. Moreover, the coordinate matrix of the ten carriers with **zero-based indices**
\[
(0,6,10,14,19,22,23,25,28,30)
\]
has exact determinant \(-1\). They form an integral basis, and all 39 carriers generate \(H_3(K;\mathbb Z)\).

**4. Symmetry orbits and the exceptional lattice.** Exhaustive incidence-preserving backtracking produces exactly eight graph automorphisms. They act on the 39 path packings in the nine orbits listed under Finding. For every orbit, construct the integer matrix whose columns are the corresponding Morse coordinates. Its exact rational rank gives the listed span rank. The gcd of all maximal minors equals the index of that column lattice in its saturation. These gcds are \((1,3,1,1,1,1,1,1,1)\), computed by exact fraction-free determinants. In particular, the unique nonsaturated orbit is an eight-element orbit of rank eight and index three; the other rank-eight orbit is saturated. These full-rank-minor computations are finite and exhaustive, not extrapolations from sampled determinants.

## Verification
Run `python3 verify.py` with Python 3.10 or later; no third-party modules, downloads, or network access are required. It independently constructs all 1,085 faces from the 18 graph edges; verifies the entire acyclic Morse matching and its critical dimensions; certifies full rank 236 for the matched-upper-three restricted boundary over \(\mathbb F_2\); checks the 39 signed octahedral boundaries; computes their integral Morse coordinates; verifies primitiveness and the indicated determinant \(-1\); enumerates all eight graph automorphisms; and verifies every orbit's rank and saturation index using exact rational arithmetic and integer determinants. The program terminates only after all assertions pass and prints `VERIFY_OK_BIDIAKIS_MATCHING_SHORTEST_SPHERES`.

The finite enumeration is exhaustive for this fixed graph because the entire finite edge set, simplex poset, path families, and automorphism search tree are traversed. The wedge conclusion uses the discrete-Morse theorem and its verified acyclicity; no finite experiment is promoted to an infinite-family theorem.

## Relationship to prior work
The named Bidiakis cube and its LCF graph structure are classical, not new. Kelmans and Mubayi proved a general lower bound for disjoint two-edge paths in cubic graphs. That theorem is an existence/packing result, not an enumeration or homology theorem for the Bidiakis cube. Bayer, Goeckner, and Jelić Milutinović classified graph matching complexes that are homology manifolds; their description of joins of small sphere matching complexes explains the geometric octahedral building blocks, but does not determine the Bidiakis matching-complex homotopy type or which of its induced octahedral classes generate the integral homology. Jelić Milutinović, Jenne, McDonough, and Vega developed discrete-Morse techniques for matching complexes of trees and honeycomb families; the Bidiakis cube does not fall under their asserted homotopy classifications. Matsushita treats small grid families, not this graph.

The contribution is the **complete Bidiakis-specific shortest-carrier classification, integral generation, and the exceptional index-three symmetry-orbit lattice**, not the generic existence of disjoint paths or the generic octahedral sphere construction. No previously published result inspected here entails these exact Bidiakis conclusions. An equivalent computation in difficult-to-search or nonindexed sources remains possible.

## Limitations
The theorem concerns only the explicitly defined twelve-vertex graph and its ordinary matching complex. It does not classify matching complexes of arbitrary cubic graphs, and its integral orbit indices are not asserted to extend to other graphs. The 39 induced octahedral spheres are minimal by **number of vertices in the matching complex**; there is no claim about minimizing the number of simplicial facets among arbitrary chains representing a class. The finite verifier is a checkable computational proof for this finite graph, not independent human validation. Literature searching cannot establish absolute publication priority, and an independent scientific audit has not been performed.

## References
1. *Bidiakis cube*, House of Graphs, graph 6632, graph data and submission recorded 28 November 2012: https://houseofgraphs.org/graphs/6632 ; also the classical LCF description of the Bidiakis cube.
2. A. Kelmans and D. Mubayi, *How many disjoint 2-edge paths must a cubic graph have?*, Journal of Graph Theory 45 (2004), 57–79; first published online 15 December 2003: https://doi.org/10.1002/jgt.10136 .
3. M. Bayer, B. Goeckner, and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328, 2019: https://arxiv.org/abs/1906.03328 .
4. M. Jelić Milutinović, H. Jenne, A. McDonough, and J. Vega, *Matching complexes of trees and applications of the matching tree algorithm*, arXiv:1905.10560, 2019: https://arxiv.org/abs/1905.10560 .
5. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26 (2019), P3.1: https://doi.org/10.37236/8480 .
