# Geodetic polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), parts \(V_1,\ldots,V_r\), \(n_i=|V_i|\ge1\), and \(N=\sum_i n_i\). For \(S\subseteq V(G)\), put \(s_i=|S\cap V_i|\) and
\[
H(S)=\{i:s_i\ge2\}.
\]
Then \(S\) is a geodetic set if and only if
\[
s_i<n_i\quad\Longrightarrow\quad H(S)\setminus\{i\}\ne\varnothing
\]
for every \(i\). Equivalently, the geodetic sets are exactly those satisfying one of the following mutually exhaustive descriptions: \(|H(S)|\ge2\); \(H(S)=\{i\}\) for some \(i\) and \(S\) contains all of \(V_i\); or every part is a singleton and \(S=V(G)\).

Define
\[
A_i(x)=1+n_i x,
\qquad
B_i(x)=(1+x)^{n_i}-A_i(x).
\]
If \(g_G(x)=\sum_S x^{|S|}\), summed over all geodetic sets \(S\), then
\[
g_G(x)=(1+x)^N-\prod_{i=1}^r A_i(x)
-\sum_{i=1}^r B_i(x)\prod_{j\ne i}A_j(x)
+\sum_{i:n_i\ge2}x^{n_i}\prod_{j\ne i}A_j(x)
+\mathbf 1_{\max_i n_i=1}x^N.
\]
Thus the complete cardinality distribution of geodetic sets is available directly from the part sizes.

As a scalar corollary only, let \(m=\min\{n_i:n_i\ge2\}\) when a non-singleton part exists. Then
\[
g(G)=
\begin{cases}
N,&\max_i n_i=1,\\
m,&\text{exactly one part is non-singleton},\\
\min\{m,4\},&\text{at least two parts are non-singleton}.
\end{cases}
\]
The scalar minimum is not the novelty target here; prior work already provides polynomial algorithms for geodetic number on broader graph classes containing complete multipartite graphs.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A set \(S\) is geodetic when every vertex of \(G\) lies on a shortest path between two vertices of \(S\), with endpoints counted as lying on their own shortest path. The theorem concerns ordinary vertex geodetic sets, not strong geodetic, edge geodetic, strong edge geodetic, hull, Steiner, or monitoring variants.

The formula applies to arbitrary positive part sizes and any \(r\ge2\). The complete graph occurs when every \(n_i=1\).

## Proof
Vertices in distinct parts of a complete multipartite graph are adjacent, so a shortest path between them has length one and has no internal vertex. Two distinct vertices in the same part \(V_j\) have distance two, and every vertex outside \(V_j\) can serve as the middle vertex of a shortest path between them.

Fix \(v\in V_i\setminus S\). Since \(v\notin S\), it must occur internally on a geodesic whose endpoints lie in \(S\). Such a geodesic must have length two, so its two endpoints must lie in one common part \(V_j\). The middle vertex \(v\) is adjacent to both endpoints exactly when \(j\ne i\). Hence \(v\) is geodetically covered by \(S\) if and only if some part \(V_j\) with \(j\ne i\) contains at least two vertices of \(S\). This is exactly
\[
H(S)\setminus\{i\}\ne\varnothing.
\]
Requiring this for every omitted vertex proves the structural criterion.

If \(|H(S)|\ge2\), every omitted part can use a heavy part different from itself. If \(H(S)=\{i\}\), omitted vertices outside \(V_i\) are covered from \(V_i\), while an omitted vertex of \(V_i\) cannot be covered; therefore \(V_i\subseteq S\) is necessary and sufficient. If \(H(S)=\varnothing\), no omitted vertex can be covered at all, so \(S=V(G)\); this has no heavy part precisely when all parts are singletons. This proves the trichotomy.

For the polynomial, \(A_i(x)\) counts choices of at most one selected vertex from \(V_i\), while \(B_i(x)\) counts choices of at least two. Starting from all \((1+x)^N\) subsets, subtract the no-heavy profiles \(\prod_iA_i(x)\) and all exactly-one-heavy profiles \(\sum_i B_i(x)\prod_{j\ne i}A_j(x)\). The valid exactly-one-heavy profiles are precisely those where the heavy part is selected in full, giving \(x^{n_i}\prod_{j\ne i}A_j(x)\) for \(n_i\ge2\). Finally, when every part is a singleton, \(V(G)\) was removed with the no-heavy profiles and must be restored. This yields the displayed formula.

For the minimum-size corollary, every geodetic set either contains an entire non-singleton part, or has two heavy parts and therefore at least four vertices, apart from the complete-graph case. Selecting a smallest non-singleton part gives size \(m\), and when two non-singleton parts exist, selecting two vertices from each gives size four. The stated cases follow.

## Verification
The accompanying `verify.py` constructs each tested complete multipartite graph explicitly, computes all-pairs graph distances, and checks geodeticity from the literal shortest-path condition. It compares that result against the structural criterion for every subset, compares the resulting cardinality counts against the closed polynomial formula, and checks the minimum-size corollary.

The finite computation is a regression check only. The theorem for arbitrary part sizes and arbitrary \(r\) follows from the proof above, not from enumeration.

## Relationship to prior work
Douthat and Kong studied geodetic bases in chordal and split graphs, establishing hardness on chordal graphs and a polynomial algorithm on split graphs. Chartrand, Harary, and Zhang developed the geodetic-number framework. Vijayan and Binu Selin introduced the geodetic polynomial as the cardinality enumerator of geodetic sets and computed it for selected graph families. Kanté and Nourine later gave a linear-time algorithm for the geodetic number on distance-hereditary graphs, a class containing complete multipartite graphs. These minimum-number algorithms do not by themselves enumerate every geodetic set by cardinality.

Later work on complete multipartite graphs has concentrated on strong and edge variants. In particular, Davot, Isenmann, and Thiebaut give a polynomial algorithm for the strong geodetic number of complete multipartite graphs. Those strong-geodetic choices assign particular shortest paths and are not equivalent to ordinary geodetic sets. Searches for ordinary geodetic polynomials, complete multipartite geodetic-set classifications, complete bipartite geodetic polynomials, and geodesic-convexity formulations did not expose the all-set criterion or the displayed ordinary geodetic polynomial.

## Limitations
The result is only for ordinary vertex geodetic sets in complete multipartite graphs. It does not claim a new algorithm for the scalar geodetic number, nor does it cover strong, edge, hull, Steiner, or monitoring variants.

The accessible abstract of the original geodetic-polynomial paper does not enumerate all graph families treated in its full text, and a direct fetch of one later complete-multipartite strong-geodetic full text timed out during comparison. Those are residual bibliographic risks. The claim is therefore limited to the exact statement above and does not assert exhaustive uniqueness across all unpublished or inaccessible literature.

## References
- G. Douthat and Y. Kong, “Computing Geodetic Bases of Chordal and Split Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 22 (1996), 67–77. Public record dated 31 October 1996.
- G. Chartrand, F. Harary, and P. Zhang, “On the Geodetic Number of a Graph,” *Networks* 39 (2002), 1–6, DOI `10.1002/net.10007`.
- A. Vijayan and T. Binu Selin, “An introduction to geodetic polynomial of a graph,” *Bulletin of Pure & Applied Sciences—Mathematics and Statistics* 31E(1) (2012), 25–32; online 11 January 2013.
- M. M. Kanté and L. Nourine, “Polynomial Time Algorithms for Computing a Minimum Hull Set in Distance-Hereditary and Chordal Graphs,” *SIAM Journal on Discrete Mathematics* 30(1) (2016), 311–326, DOI `10.1137/15M1013389`.
- T. Davot, L. Isenmann, and J. Thiebaut, “On the Approximation Hardness of Geodetic Set and Its Variants,” *COCOON 2021*, 76–88, DOI `10.1007/978-3-030-89543-3_7`.
