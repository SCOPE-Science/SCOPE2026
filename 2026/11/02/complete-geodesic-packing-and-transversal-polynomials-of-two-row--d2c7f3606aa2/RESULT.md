# Complete geodesic-packing and transversal polynomials of two-row rook graphs

## Finding

For every integer \(n\geq 2\), let \(G_n=K_2\square K_n\), with vertices \((r,j)\), where \(r\in\{0,1\}\) and \(j\in[n]\). Vertices are adjacent exactly when their row or their column agrees. Count a geodesic up to reversal, and count a geodesic packing as an unordered collection of vertex-disjoint **maximal** geodesics, including the empty packing. Define the packing polynomial
\[
P_n(z)=\sum_{\mathcal P}z^{|\mathcal P|}.
\]
Then
\[
\boxed{P_n(z)=\sum_{k=0}^{\lfloor2n/3\rfloor}
\frac{n!}{(n-k)!}\binom{2(n-k)}{k}z^k.}
\]
Its positive coefficients are strictly log-concave. In particular, the geodesic-packing number is \(\lfloor 2n/3\rfloor\). If \(n=3q+r\) with \(r\in\{0,1,2\}\), the exact number of maximum packings is
\[
\boxed{\frac{n!}{q!}\begin{cases}
1,&r=0,\\
2q+1,&r=1,\\
2,&r=2.
\end{cases}}
\]

A geodesic transversal is a vertex set meeting every maximal geodesic. Let \(T_n(z)=\sum_{S\,\mathrm{transversal}}z^{|S|}\) count all transversals, including any redundant ones. Then
\[
\boxed{T_n(z)=z^n(z+2)^n+nz^{2n-2}.}
\]
Thus the geodesic-transversal number is \(n\). The number of minimum transversals is \(2^n\) for \(n\geq3\), and is \(6\) when \(n=2\). The inclusion-minimal transversals are exactly the complements of (a) the \(2^n\) sets choosing one vertex from each two-vertex column and (b) the \(n\) full two-vertex columns. There are \(2^n+n\) of them; their sizes are respectively \(n\) and \(2n-2\), which coincide when \(n=2\).

## Assumptions and scope

The graphs are finite, simple, unweighted and undirected; \(n\ge2\). A *maximal geodesic* is a shortest path not properly contained as a consecutive subpath of another shortest path. Because \(G_n\) has diameter two and every edge extends to a shortest two-edge path, its maximal geodesics are precisely its shortest two-edge paths. Reversal of a path is identified. The two adjacent path edges do not become two separately counted objects.

A geodesic packing is a set of such paths with pairwise disjoint **vertex sets**. A geodesic transversal meets every such path. The polynomial \(T_n\) counts vertex subsets, whereas \(P_n\) counts collections of paths; the two sample spaces are different. The results do not assert formulas for more than two clique layers, arbitrary graphs, weighted geodesics, or edge-disjoint rather than vertex-disjoint packings.

## Proof

**Classification of maximal geodesics.** Every distance-two pair has the form \((0,i),(1,j)\) with \(i\ne j\). Its two possible shortest paths have respective vertex sets
\[
\{(0,i),(0,j),(1,j)\},\qquad
\{(0,i),(1,i),(1,j)\}.
\]
Each consists of both vertices of one column (its uniquely determined *full column*) and a single vertex of a different column (its uniquely determined *singleton cell*). Conversely every choice of a full column \(c\), singleton row \(r\) and a different singleton column \(j\) gives exactly one maximal geodesic, with vertices \((0,c),(1,c),(r,j)\). Its endpoints are \((1-r,c)\) and \((r,j)\), at distance two. No length-zero or length-one geodesic is maximal because every edge extends to one of these paths.

**Packing bijection.** In any packing of \(k\) paths, the \(k\) full columns are distinct, and none of the \(k\) singleton cells may belong to a full column. Moreover all singleton cells are distinct. Conversely, choose \(k\) full columns; choose \(k\) distinct cells in the remaining \(n-k\) columns (two possible row positions per column); biject those cells to the \(k\) full columns. The resulting \(k\) paths are vertex-disjoint, and every packing is recovered exactly once by this construction. There are
\[
\binom nk\binom{2(n-k)}k k!
=\frac{n!}{(n-k)!}\binom{2(n-k)}k
\]
choices. Feasibility is exactly \(k\le 2(n-k)\), namely \(k\le\lfloor2n/3\rfloor\). All these values are attained because the displayed count is positive. Substituting \(k=\lfloor2n/3\rfloor\) in the coefficient gives the three residue-class formulas: for \(n=3q\), the remaining cells equal \(2q\); for \(n=3q+1\), the remaining cells equal \(2q+2\) and one chooses \(2q\); for \(n=3q+2\), the remaining cells equal \(2q+2\) and one chooses \(2q+1\).

**Strict log-concavity.** Write \(p_{n,k}=[z^k]P_n(z)>0\) on its support. Using the factorial expression gives, for \(0\le k<\lfloor2n/3\rfloor\),
\[
\frac{p_{n,k+1}}{p_{n,k}}=
\frac{(2n-3k)(2n-3k-1)(2n-3k-2)}{2(2n-2k-1)(k+1)}.
\]
These successive ratios strictly decrease. Indeed write \(s=2n-3k\), \(t=n-k\); on moving from \(k\) to \(k+1\), the factor \(s/(2t-1)\) strictly decreases because
\[
s(2t-3)-(s-3)(2t-1)=2n-3>0.
\]
The positive factors \((s-1)(s-2)\) and \(1/(k+1)\) likewise strictly decrease. Hence \(p_{n,k}^2>p_{n,k-1}p_{n,k+1}\) for each internal index; when the support has fewer than three terms this assertion is vacuous. This establishes strict log-concavity and therefore unimodality; real-rootedness is not claimed.

**Transversal polynomial and inclusion-minimality.** The complement \(U=V(G_n)\setminus S\) of a geodesic transversal contains no maximal geodesic in full. If \(U\) contains both vertices of a column \(c\), any additional vertex in a different column creates the maximal geodesic consisting of that full column and the additional singleton cell. Consequently such a \(U\) must be exactly the two vertices of one column. Otherwise \(U\) contains at most one vertex from each column; every such selection is valid, because every maximal geodesic contains a full column. Thus the polynomial of geodesic-free sets is
\[
Q_n(y)=(1+2y)^n+ny^2.
\]
Taking set complements yields
\[
T_n(z)=z^{2n}Q_n(z^{-1})=z^n(z+2)^n+nz^{2n-2}.
\]
The inclusion-maximal geodesic-free sets are precisely one-choice-per-column selections (\(2^n\) of size \(n\)) and the \(n\) entire columns (of size \(2\)). Their complements are exactly the inclusion-minimal transversals. The smallest transversal cardinality is \(n\) for \(n\ge2\); at \(n=2\) both structural classes have size \(2\), yielding \(4+2=6\) minimum transversals, while for \(n\ge3\) only the first class is minimum.

## Verification

The standalone `verify.py` reconstructs the graph adjacency and all-pairs distances independently, enumerates all diameter-two geodesics by triples, then recursively enumerates their vertex-disjoint packings without using the displayed counting bijection. It separately scans **every vertex subset** to test whether it contains a maximal geodesic, and checks the exact transversal and inclusion-minimality claims. Complete finite checks cover \(2\le n\le8\). For each \(n\) the observed coefficients equal those given above; the maximum-packing counts and transversal class counts agree. Additional exact-integer arithmetic checks cover \(2\le n\le150\), including the strict log-concavity inequalities. Execute `python3 verify.py` with Python 3; successful execution ends with `VERIFY_OK`.

These computations provide independent finite checks, not an exhaustive infinite-parameter certificate. The all-parameter statements follow from the bijections and ratio argument in the proof.

## Relationship to prior work

Manuel, Brešar and Klavžar (first public preprint 27 October 2022, arXiv:2210.15325) introduced geodesic packing as the vertex-disjoint maximal-geodesic problem and studied its relationship to geodesic transversals. Their Lemma 2.3 gives the general packing upper bound; their Proposition 2.6 evaluates the geodesic transversal of **square** rook graphs, and their proof describes the maximal two-edge geodesics in those graphs. Their numerical result for the **complete bipartite graph** \(K_{n,n}\) concerns a different graph from \(K_2\square K_n\). Their general bound implies the upper bound \(\lfloor2n/3\rfloor\) here, but does not supply the matching construction, all-set packing polynomial, extremal counts, log-concavity or complete transversal polynomial. These general facts and definitions are credited, not presented as new.

Wild (arXiv:2409.16955) develops algorithms to enumerate individual graph geodesics. Such enumeration does not give the above closed enumeration of *pairwise vertex-disjoint collections* of maximal geodesics. Equivalent descriptions here are packings of induced three-vertex paths and path-hypergraph matchings in two cliques connected by a perfect matching. The exact formula could conceivably have appeared under one of these descriptions. Indexed searches and comparisons with accessible mathematical records identified no such earlier statement, but do not prove publication priority.

## Limitations

Only two-row rook graphs, \(n\ge2\), are treated. The identification of paths up to reversal and of a packing as an unordered set is essential to the coefficients. The log-concavity assertion is proved but stronger properties such as real-rootedness are not claimed. The result does not solve geodesic-packing enumeration for arbitrary rectangular rook graphs, and publication-priority uncertainty remains where equivalent induced-path packing counts might exist under different names. No independent external mathematical audit has been performed.

## References

1. P. Manuel, B. Brešar and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325 (first submitted 27 October 2022), subsequently *Applied Mathematics and Computation* 459 (2023), article 128277, DOI:10.1016/j.amc.2023.128277. Public preprint: https://arxiv.org/abs/2210.15325 ; accessible full text: https://users.fmf.uni-lj.si/klavzar/preprints/2210.15325.pdf.
2. M. Wild, *Enumerating all geodesics*, arXiv:2409.16955 (first submitted 25 September 2024), https://arxiv.org/abs/2409.16955.
