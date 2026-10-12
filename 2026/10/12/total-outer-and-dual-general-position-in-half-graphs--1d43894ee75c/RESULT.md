# Total, outer, and dual general position in half graphs
## Finding
For every integer \(n\ge4\), let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency
\[
a_i b_j\in E(H_n)
\quad\Longleftrightarrow\quad
i\le j.
\]

Then
\[
\operatorname{gp}_{\mathrm t}(H_n)
=
\operatorname{gp}_{\mathrm o}(H_n)
=
\operatorname{gp}_{\mathrm d}(H_n)
=
2.
\]

The unique maximum total general-position set and the unique maximum dual general-position set are both
\[
\{a_n,b_1\}.
\]

The mutually maximally distant pairs are exactly
\[
\{a_i,b_j\},
\qquad
1\le j<i\le n.
\]
Equivalently, the strong resolving graph of \(H_n\) has precisely those edges. Hence the maximum outer general-position sets are exactly these pairs, and their number is
\[
\binom n2.
\]

## Assumptions and scope
For \(X\subseteq V(G)\), vertices \(u,v\in V(G)\) are \(X\)-positionable when every shortest \(u,v\)-path meets \(X\) only in possible endpoints.

A total general-position set requires every pair of vertices of \(G\) to be \(X\)-positionable. An outer general-position set requires this for pairs inside \(X\) and for pairs with one endpoint in \(X\). A dual general-position set requires it for pairs inside \(X\) and for pairs outside \(X\).

The proof uses three established characterizations: total general-position sets are exactly subsets of the simplicial vertices; outer general-position sets are exactly sets whose vertices are pairwise mutually maximally distant; and a general-position set is dual exactly when its complement is convex.

## Proof
The degrees in \(H_n\) are
\[
\deg(a_i)=n-i+1,
\qquad
\deg(b_j)=j.
\]
Because \(H_n\) is bipartite, a vertex of degree at least two cannot be simplicial. Hence the only simplicial vertices are
\[
a_n\quad\text{and}\quad b_1.
\]
The total-general-position characterization therefore gives
\[
\operatorname{gp}_{\mathrm t}(H_n)=2,
\]
with unique maximum set \(\{a_n,b_1\}\).

For outer general position, first note that
\[
d(a_i,b_j)=3
\qquad
\text{when }i>j.
\]
The half graph has diameter \(3\), so every such pair is diametral and therefore mutually maximally distant.

No other pair is mutually maximally distant. If \(i<k\), then
\[
d(a_i,a_k)=2
\]
but \(b_i\) is a neighbor of \(a_i\) and
\[
d(b_i,a_k)=3,
\]
so \(a_i\) is not maximally distant from \(a_k\). The same argument, with the bipartition classes interchanged, excludes same-side \(B\)-pairs.

Now let \(a_i b_j\) be an edge, so \(i\le j\). If \(i<n\), then \(a_i\) has at least two neighbors; choose a neighbor \(b_\ell\ne b_j\). Since distinct \(B\)-vertices are at distance \(2\),
\[
d(b_\ell,b_j)=2>d(a_i,b_j)=1,
\]
so \(a_i\) is not maximally distant from \(b_j\). If \(i=j=n\), then \(b_n\) has another neighbor \(a_\ell\ne a_n\) and
\[
d(a_\ell,a_n)=2>1,
\]
so \(b_n\) is not maximally distant from \(a_n\).

Thus the strong resolving graph has edge set
\[
\big\{a_i b_j:1\le j<i\le n\big\}.
\]
It is bipartite and has edges, so its clique number is \(2\). Hence
\[
\operatorname{gp}_{\mathrm o}(H_n)=2,
\]
and its maximum sets are exactly the \(\binom n2\) displayed pairs.

It remains to prove the dual statement. The pair
\[
\{a_n,b_1\}
\]
is dual because both vertices are simplicial.

We next show that no dual general-position set has size at least three. Any general-position set of size at least three in \(H_n\) is independent: if it contains an edge \(a_i b_j\) with \(i\le j\), then every third selected vertex lies with that edge on a shortest path. Indeed, a third \(a_k\) with \(k\le j\) gives the geodesic
\[
a_i-b_j-a_k,
\]
while \(k>j\) gives the geodesic
\[
b_j-a_i-b_n-a_k.
\]
The cases of a third \(B\)-vertex are symmetric.

Let \(X\) now be an independent dual general-position set. If \(a_i\in X\) with \(i<n\), independence forces every selected \(B\)-vertex to have index less than \(i\). Hence \(b_i,b_{i+1}\notin X\), while
\[
b_i-a_i-b_{i+1}
\]
is a shortest path. Thus \(H_n-X\) is not convex. Therefore every selected \(A\)-vertex must be \(a_n\). Symmetrically, every selected \(B\)-vertex must be \(b_1\). Hence an independent dual set has size at most two.

Finally consider arbitrary two-vertex sets. Two vertices from the same bipartition class cannot be dual: for \(a_i,a_k\) with \(i<k\), the complement contains \(b_i,b_k\), and
\[
b_i-a_i-b_k
\]
is a shortest path through a deleted vertex; the \(B\)-side argument is symmetric.

For a nonadjacent cross pair \(\{a_i,b_j\}\) with \(i>j\), the preceding convexity witnesses force \(i=n\) and \(j=1\). For an adjacent pair \(\{a_i,b_j\}\) with \(i\le j\), if \(i\le n-2\), then \(a_i\) has at least two unselected neighbors in \(B\), whose distance-\(2\) geodesic passes through \(a_i\). If \(i\ge n-1\), then \(j\ge3\) because \(n\ge4\), and \(b_j\) has at least two unselected neighbors in \(A\), whose distance-\(2\) geodesic passes through \(b_j\). Thus no adjacent pair is dual.

Therefore
\[
\operatorname{gp}_{\mathrm d}(H_n)=2,
\]
and \(\{a_n,b_1\}\) is its unique maximum set.

## Verification
The included checker constructs \(H_n\) for
\[
4\le n\le7
\]
and exhausts every vertex subset. It tests the defining \(X\)-positionability condition directly for total, outer, and dual general position, without using the structural characterizations from the proof.

For each order, it verifies the three maximum values and compares the complete maximum-set families with the theorem.

## Relationship to prior work
The total, outer, and dual variants were introduced together in 2024. The introducing paper proves the three structural characterizations used above and lists Mathematics Subject Classification \(05C12\), \(05C69\), and \(05C76\). Its full searchable text contains no half-graph or chain-graph specialization.

A later paper on mobile position problems uses the same half graph and proves mobile and completely mobile ordinary general-position results. It records the ordinary general-position value
\[
\operatorname{gp}(H_n)=n,
\]
but does not study total, outer, or dual general position.

A recent result on strong metric bases of chain graphs determines the strong metric dimension and all minimum strong resolving sets. This is related because strong metric dimension is governed by the strong resolving graph, but a vertex-cover optimum of that graph does not determine its clique number or the complete set of mutually maximally distant pairs. The outer statement here therefore requires the explicit strong-resolving-graph calculation above.

## Limitations
The theorem is stated for \(n\ge4\). Small half graphs have exceptional dual maximum sets: the boundary \(n=3\) case has an additional maximum dual pair.

The exhaustive verification through \(n=7\) is corroborative only. The arbitrary-order theorem follows from the explicit simplicial, mutually-maximally-distant, and convex-complement arguments.

A differently phrased or non-indexed treatment of these variants on half graphs may exist.

## References
1. J. Tian and S. Klavžar, “Variety of General Position Problems in Graphs,” arXiv:2402.17338v1, 27 February 2024; Bulletin of the Malaysian Mathematical Sciences Society 48 (2025), article 5, DOI 10.1007/s40840-024-01788-z.
2. E. Shallcross, J. Tuite, A. Evans, A. Krishnakumar, and S. Boshar, “Solution to some conjectures on mobile position problems,” arXiv:2507.16622v1, 22 July 2025.
