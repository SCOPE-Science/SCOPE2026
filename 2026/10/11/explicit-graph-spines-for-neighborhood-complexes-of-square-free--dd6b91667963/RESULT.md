# Explicit graph spines for neighborhood complexes of square-free bipartite graphs
## Finding
Let \(G\) be a finite connected simple bipartite graph with bipartition \(X\sqcup Y\), at least one edge, and no \(4\)-cycle. For every \(y\in Y\), choose a root \(r_y\in N_G(y)\). Write \(K_X\) for the connected component of the Lovász neighborhood complex \(\mathcal N(G)\) supported on \(X\). Define a graph \(T_X\) on vertex set \(X\) by
\[
E(T_X)=\bigl\{{{\{r_y,x\}}}:y\in Y,\ x\in N_G(y)\setminus{{\{r_y\}}}\bigr\}.
\]
Then \(K_X\) simplicially collapses onto \(T_X\). The graph \(T_X\) is exactly the graph obtained from \(G\) by contracting the forest \(F_Y=\{{yr_y:y\in Y\}}\). The same construction with the two bipartition classes exchanged gives a collapse \(K_Y\searrow T_Y\). Hence
\[
\mathcal N(G)=K_X\sqcup K_Y,
\qquad K_X\simeq G,
\qquad K_Y\simeq G.
\]
For a \(d\)-regular example with \(|X|=|Y|=n\), each spine has \(n\) vertices and \(n(d-1)\) edges, so each component is homotopy equivalent to
\[
\bigvee^{{n(d-2)+1}}S^1.
\]

## Assumptions and scope
The graph is finite, simple, connected, bipartite, has at least one edge, and contains no \(4\)-cycle. The neighborhood complex uses the standard convention that its vertices are the non-isolated vertices of \(G\), and a nonempty vertex set is a simplex exactly when its vertices have a common neighbor. Connectivity eliminates isolated vertices. The conclusion is a simplicial-collapse statement, stronger than merely identifying a homotopy type.

## Proof
Every simplex of \(\mathcal N(G)\) lies wholly in \(X\) or wholly in \(Y\), because all vertices sharing a neighbor in a bipartite graph lie on the side opposite that neighbor. Thus \(\mathcal N(G)=K_X\sqcup K_Y\). An alternating path in the connected graph \(G\) gives an edge path between any two vertices on the same side, so both nonempty side complexes are connected.

Consider \(K_X\). It is the union of the simplices on the sets \(N_G(y)\subseteq X\), with \(y\in Y\). Square-freeness implies that two distinct vertices of \(X\) have at most one common neighbor. Equivalently, every face of \(K_X\) having at least two vertices is contained in the neighborhood simplex of a unique \(y\in Y\).

Fix \(y\in Y\). For every subset \(\sigma\subseteq N_G(y)\setminus\{{r_y\}}\) with \(|\sigma|\ge 2\), process these subsets in decreasing cardinality and remove the elementary collapse pair
\[
\bigl(\sigma,\ \sigma\cup\{{r_y\}}\bigr).
\]
At the moment this pair is removed, all larger faces in the same neighborhood simplex have already disappeared. No face of size at least two belongs to a different neighborhood simplex, so \(\sigma\) has the unique remaining strict coface \(\sigma\cup\{{r_y\}}\), and the latter is maximal. Therefore every removal is a legal elementary simplicial collapse. The procedures for different \(y\) interact only through vertices and can be concatenated in any order. What remains is exactly the union of the rooted stars on \(N_G(y)\), namely \(T_X\).

Now select in \(G\) the edge \(yr_y\) for every \(y\in Y\). In the selected subgraph every vertex of \(Y\) has degree one, so the selected edges form a forest \(F_Y\). Contracting all edges of \(F_Y\) identifies \(y\) with \(r_y\). Every other edge \(yx\) becomes the edge \(r_yx\). Two different vertices of \(Y\) cannot create the same resulting edge, since that would give two common neighbors of the same pair of vertices in \(X\) and hence a \(4\)-cycle. Thus the contracted graph is precisely \(T_X\). Contracting a forest is a graph homotopy equivalence, yielding \(T_X\simeq G\). The proof for \(K_Y\) is symmetric.

For the regular corollary, \(T_X\) has \(n\) vertices and \(n(d-1)\) edges. Since it is connected, its cycle rank is \(n(d-1)-n+1=n(d-2)+1\), and a connected finite graph is homotopy equivalent to a wedge of that many circles.

## Verification
A standalone exhaustive checker enumerates every connected labeled bipartite square-free graph on at most six vertices. For each side of every graph, it reconstructs the neighborhood complex, replays the stated descending-cardinality collapse sequence, checks at each step that the proposed free face has exactly one strict coface and that the paired coface is maximal, compares the final complex with the claimed rooted-star spine, and checks that the spine and original graph have equal cycle rank. It reports \(1501\) graphs checked without failure. This finite computation is a sanity check only; the proof above is uniform and does not depend on enumeration.

## Relationship to prior work
Donovan and Scoville develop star-cluster and acyclic-matching methods for graph-derived simplicial complexes and use collapses as a central tool; their paper supplied the literature-led collapse direction here. Shukla determines homotopy types of neighborhood complexes for graphs of maximum degree at most three and certain regular circulants, but does not state the all-degree square-free bipartite rooted-spine collapse above. Matsushita proves a substantially broader abstract homotopy classification for Hom complexes with square-free codomain; specializing its homotopy classification to the \(K_2\) domain covers the homotopy-type consequence in the appropriate components, but the inspected full text does not state a simplicial collapse onto the explicit forest-contraction minor \(T_X\). The new content claimed here is this constructive collapse/minor model, not the abstract homotopy equivalence alone.

## Limitations
The square-free hypothesis is used exactly to make every face with at least two vertices belong to a unique neighborhood simplex. When a \(4\)-cycle is present, two neighborhood simplices can share an edge and the displayed local collapse pairs need not be free. No claim is made that the construction extends unchanged beyond the square-free bipartite case. A residual literature risk remains that the same elementary collapse observation may have appeared under incidence-complex or Dowker-complex terminology not located in the searches reported in the review file.

## References
1. C. Donovan and N. A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780, first posted 2022-07-27; published as “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” New York J. Math. 29 (2023), 1393–1412.
2. S. Shukla, “Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs,” arXiv:1802.04526; Electron. J. Combin. 26(2) (2019), P2.4, DOI 10.37236/7549.
3. T. Matsushita, “Hom complexes of graphs whose codomains are square-free,” arXiv:2412.19144; J. Combin. Theory Ser. B 178 (2026), 267–293, DOI 10.1016/j.jctb.2026.01.005.
