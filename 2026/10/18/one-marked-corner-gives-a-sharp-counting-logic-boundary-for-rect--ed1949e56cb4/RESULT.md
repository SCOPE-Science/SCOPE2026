# One marked corner gives a sharp counting-logic boundary for rectangular grids

## Finding

Let \(2\le m\le n\) be integers. Write \(G_{m,n}=P_m\square P_n\) for the finite simple undirected graph with vertex set \(\{(i,j):0\le i<m,\ 0\le j<n\}\), in which two distinct vertices are adjacent exactly when their Manhattan distance is one. Give \((0,0)\) one distinguished unary colour and every other vertex the other colour. Then the following are equivalent:

1. The coloured grid \(G_{m,n}\) is uniquely identified, among **all finite vertex-coloured simple graphs**, by two-variable first-order logic with counting, \(C^2\).
2. Ordinary vertex colour refinement distinguishes the coloured grid from every nonisomorphic finite vertex-coloured graph.
3. Either \(m<n\), or \(m=n\le3\).

More precisely, if \(m<n\), the stable refinement partition of the corner-coloured grid is discrete. If \(m=n=s\), its classes are exactly \(\{(i,j),(j,i)\}\), with singletons on the diagonal. When \(s\le3\), this partition and its edge-count quotient determine the entire graph up to coloured isomorphism. For every \(s\ge4\), changing two matching edges between stable classes produces a connected nonisomorphic graph on the same vertices with the same complete colour-refinement invariant. The obstruction is sharp at the \(4\times4\) grid.

## Assumptions and scope

Graphs are finite, simple, undirected and carry exactly one named unary predicate, true at the indicated corner and false elsewhere. Isomorphisms and logical equivalence preserve that predicate. Competing graphs are arbitrary finite graphs in the same signature; they are not assumed planar, connected, grids, or of bounded degree. The parameters satisfy \(2\le m\le n\). The phrase 'identified by \(C^2\)' means that there is a \(C^2\) sentence having that coloured graph as its only finite isomorphism type. Standard counting quantifiers may use integer constants. All statements concern unrestricted logical depth, not a claimed uniform depth bound.

## Proof

**Lemma 1 (distance and singleton landmarks).** In a vertex-coloured graph whose initial colour distinguishes a vertex \(r\), distinct distances from \(r\) are distinguishable by stable colour refinement. Indeed, at stage \(t\) a vertex's colour determines whether its distance from \(r\) is at most \(t\): this follows by induction from the neighbour-colour multiset. Consequently, once a vertex becomes a singleton stable class, its distance function is also constant on every stable class. Vertex degrees are available after the first round.

**Lemma 2 (the nonsquare case).** Suppose \(m<n\). The degree-two vertices of \(G_{m,n}\) are precisely its four corners. Their distances from the initially marked corner are \(0\), \(m-1\), \(n-1\), and \(m+n-2\); these numbers are pairwise distinct. Thus \(a=(m-1,0)\) is itself a singleton stable class. The two distances of a vertex \((i,j)\) to the individually recognized landmarks \((0,0)\) and \(a\) are
\[
 d_0=i+j,\qquad d_a=(m-1-i)+j.
\]
They determine \(i=(m-1+d_0-d_a)/2\) and \(j=d_0-i\). Therefore every stable class is a singleton. If another graph has the same refinement invariant, the unique vertices of corresponding stable colours, together with their adjacency counts into singleton classes, give an isomorphism.

**Lemma 3 (the square case).** Suppose \(m=n=s\). The diagonal reflection \((i,j)\mapsto(j,i)\) fixes the distinguished corner and preserves all refinement colours, so each orbit \(X_{i,j}=\{(i,j),(j,i)\}\), for \(0\le i\le j<s\), lies within a single stable class. Conversely, Lemma 1 separates the shells of constant \(i+j\). Proceed outward by induction on the shell index \(t=i+j\). A vertex \((i,j)\), \(i\le j\), has in shell \(t-1\) the predecessor-class multiset
\[
 \begin{cases}
 \{X_{0,j-1}\},& i=0,\\
 \{X_{i-1,j},X_{i,j-1}\},&0<i<j,\\
 \{X_{i-1,i},X_{i-1,i}\},&i=j>0.
 \end{cases}
\]
Here a symbol with reversed coordinates denotes the same unordered-pair class. The multiset uniquely determines \(i\) on that shell: for \(i=0\) it has one element, whereas for \(i>0\) the smallest first coordinate among the unordered predecessor indices equals \(i-1\). Every predecessor exists because decreasing a positive coordinate remains inside the grid. By induction the predecessor classes are already distinguished, hence so are the displayed orbit classes. This proves the precise stable partition.

**Lemma 4 (small squares).** At \(s=2\), only the cell \(X_{0,1}\) has two vertices. At \(s=3\), the three two-vertex cells are \(X_{0,1}\), \(X_{0,2}\), \(X_{1,2}\); all induce empty graphs, and their only nonempty pairwise bipartite interactions are perfect matchings from \(X_{0,1}\) to \(X_{0,2}\) and from \(X_{0,2}\) to \(X_{1,2}\). All interactions involving singleton classes are forced by the per-cell neighbour counts. For bipartite interactions between two-vertex classes the counts force either the empty graph, a perfect matching, or the complete bipartite graph. The graph formed by the matching interactions is a path, so all possible matching orientations are isomorphic: fix an orientation at one two-vertex class and propagate along the path. The same observation holds trivially at \(s=2\). Therefore any graph sharing the entire refinement invariant is isomorphic as a coloured graph, even without a grid hypothesis.

**Lemma 5 (all larger squares).** For \(s\ge4\), denote \(a=(0,2)\), \(a'=(2,0)\), \(b=(0,3)\), \(b'=(3,0)\). Delete the grid edges \(ab\) and \(a'b'\) and insert \(ab'\) and \(a'b\), obtaining \(H_s\). Both inserted edges are new. The deletion removes one edge from each of the two perfect matchings between \(X_{0,2}\) and \(X_{0,3}\), replacing their pairing by the other perfect matching. Every vertex retains exactly the same number of neighbours in every stable class of the grid. Since the classes of Lemma 3 form a common equitable partition of both graphs and were obtained by refinement from the initial unary colours on the grid, induction on refinement rounds shows that the two graphs have identical colour histograms at every round. Thus they are \(C^2\)-equivalent.

The four successive classes \(X_{0,2}\), \(X_{0,3}\), \(X_{1,3}\), and \(X_{1,2}\) each have two vertices; their induced eight-vertex subgraph in \(G_{s,s}\) is the disjoint union of two four-cycles, whereas in \(H_s\) it is one eight-cycle. Any colour-preserving isomorphism must preserve each stable class, and therefore these four classes, so no such isomorphism exists. The remaining grid after the two deletions is still connected: each removed boundary edge has a three-edge detour around its adjacent unit square not involving the other removed edge. Hence \(H_s\) is also connected.

Finally, the classical equivalence of graph colour refinement and \(C^2\)-equivalence, together with finiteness of the refinement quotient, converts the positive identification statements into \(C^2\) characteristic sentences; the explicit competitors establish failure in the other cases. This proves the theorem.

## Verification

The standalone program `verify_corner_grids.py` checks stable orbit partitions for \(88\) pairs \(2\le m\le12\), \(m\le n\le14\); for squares \(4\le s\le12\), it additionally checks joint-colour-refinement equivalence, connectivity and the \(2\)-versus-\(0\) colour-sensitive four-cycle witness under the indicated switch. The independent program `verify_small_square_forcing.py` enumerates all equitable matching completions for the small square cases: exactly one at side \(2\) and four labelled choices at side \(3\), all isomorphic by classwise flips. Both scripts were executed successfully with standard-library Python. The all-size statements are proved above, not inferred from the finite tests.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015) give a complete general graph-amenability criterion in terms of stable equitable cells and an acyclic anisotropic-cell graph. Kiefer, Schweitzer and Selman (2015) independently characterize graphs identified by \(C^2\), including the global flip/bouquet-forest criterion. Arvind, Fuhlbrück, Köbler, Kuhnert and Rattan (2016) investigate individualization before colour refinement. Those results establish the broad framework and imply a decision procedure for each particular marked grid. The contribution here is the explicit *uniform* boundary for the two-parameter family and a direct geometric explanation through a uniquely distinguishable second corner, orbit-pair propagation, and a switched matching around the first orbit-cell cycle. The paper's general criteria are not attributed as new. Earlier explicit specializations are possible; priority has not been independently established.

## Limitations

The theorem requires precisely one marked **corner** and \(m,n\ge2\); it makes no assertion about an interior marker, multiple markers, higher-dimensional products, or the minimum possible quantifier rank. The negative competitors are simple and connected but are not asserted planar. Computations through finite sizes supplement, rather than replace, the uniform proofs. Because general published amenability characterizations could support an alternative derivation of this grid-specific corollary, the priority of the closed-form specialization carries residual risk. No independent scientific validation is claimed.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, Theorem 9. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30, Theorem 17. https://arxiv.org/abs/1503.08792
3. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383, first posted 2016-06-14, Section 1. https://arxiv.org/abs/1606.04383
