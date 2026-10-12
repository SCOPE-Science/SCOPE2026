# Correcting the general position polynomial of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the connected crown graph, with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where the deleted perfect matching is \(\{a_ib_i:1\le i\le n\}\).

The ordinary general position polynomial is
\[
\psi(\operatorname{Cr}_n;z)=2(1+z)^n-1+n^2z^2.
\]

Every ordinary general position set of cardinality at least three is contained entirely in \(A\) or entirely in \(B\).

By contrast, the polynomial
\[
2(1+z)^n-1+n^2z^2+2n(n-1)z^3+\binom{n}{2}z^4
\]
is the cardinality enumerator of the general \(2\)-position sets of \(\operatorname{Cr}_n\). Since crown graphs are triangle-free, these are exactly the dissociation sets.

The 2024 formula stated for \(T^*(n,2)\), which that paper identifies as a complete bipartite graph with a perfect matching removed, is exactly this general-\(2\)-position polynomial rather than the ordinary general position polynomial.

Consequently,
\[
\operatorname{gp}_2(\operatorname{Cr}_n)=\max\{n,4\}.
\]
For \(n=3\), the maximum general-\(2\)-position sets are the three unions of two deleted matched pairs. For \(n=4\), there are eight maximum sets: the two bipartition classes and the six unions of two deleted matched pairs. For \(n\ge5\), the only maximum sets are \(A\) and \(B\).

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A set is in ordinary general position if no three selected vertices lie on a common geodesic. It is in general \(2\)-position if no three selected vertices lie on a common geodesic of length at most \(2\).

The theorem concerns connected crown graphs, hence \(n\ge3\). The disconnected graph obtained at \(n=2\) is excluded.

## Proof
First consider ordinary general position. In any bipartite graph, a general position set of size at least three cannot contain an edge. Indeed, let \(uv\) be an edge and let \(w\) be a third selected vertex. The integers \(d(w,u)\) and \(d(w,v)\) have opposite parity and differ by at most one, hence differ by exactly one. The farther endpoint of \(uv\) therefore lies on a shortest path from \(w\) to the nearer endpoint, contradicting general position.

Thus every ordinary general position set of size at least three in \(\operatorname{Cr}_n\) is independent. An independent set of size at least three cannot contain vertices from both bipartition classes: if it contains a cross-part nonedge \(a_i,b_i\), any third vertex is adjacent to one of these two vertices. Hence every such set lies wholly in \(A\) or wholly in \(B\).

Every set of cardinality at most two is automatically in general position. Therefore the union of all one-sided subsets contributes
\[
2(1+z)^n-1,
\]
and the mixed two-sets contribute the \(n^2\) cross-part pairs. This proves
\[
\psi(\operatorname{Cr}_n;z)=2(1+z)^n-1+n^2z^2.
\]

Now classify general \(2\)-position sets. Write
\[
I=\{i:a_i\in S\},\qquad J=\{j:b_j\in S\}.
\]
For distinct \(i,j\in I\), a selected vertex \(b_k\) lies on a length-two geodesic from \(a_i\) to \(a_j\) exactly when
\[
k\notin\{i,j\}.
\]
Therefore every pair of indices in \(I\) forces
\[
J\subseteq\{i,j\}.
\]
Symmetrically, every pair of indices in \(J\) forces
\[
I\subseteq\{i,j\}.
\]

These two conditions give the complete mixed classification:
\[
(|I|,|J|)=(1,1);
\]
\[
(|I|,|J|)=(2,1)\quad\text{with }J\subseteq I;
\]
the symmetric \((1,2)\) case; and
\[
(|I|,|J|)=(2,2)\quad\text{with }I=J.
\]
If one of \(I,J\) is empty, the subset on the other side is arbitrary.

Counting these cases gives
\[
2(1+z)^n-1+n^2z^2+2n(n-1)z^3+\binom{n}{2}z^4.
\]

The foundational general-\(d\)-position result proves that, in every triangle-free graph, general \(2\)-position sets are exactly dissociation sets. Hence the same polynomial is also the dissociation polynomial of the crown graph.

Finally, the 2024 paper defines \(T^*(r,2)\) as a complete bipartite graph with a perfect matching removed, so \(T^*(n,2)=\operatorname{Cr}_n\). Its displayed polynomial is exactly the general-\(2\)-position polynomial just derived. The ordinary polynomial differs by the positive correction
\[
2n(n-1)z^3+\binom{n}{2}z^4.
\]
For \(n=3\), this discrepancy is already forced by \(\operatorname{Cr}_3=C_6\): the same 2024 paper's cycle formula gives only two ordinary general-position triples, whereas its \(T^*(3,2)\) table gives fourteen.

## Verification
The included checker constructs \(\operatorname{Cr}_n\), computes all-pairs shortest-path distances, and tests both ordinary general position and general \(2\)-position directly from the geodesic definition.

For every \(3\le n\le9\), it enumerates every vertex subset, independently checks the two structural classifications, compares all coefficients with the two closed polynomials, and verifies that the 2024 displayed \(T^*(n,2)\) formula agrees exactly with the general-\(2\)-position polynomial and disagrees with the ordinary polynomial.

## Relationship to prior work
General \(d\)-position was introduced in 2020. The defining source proves that on triangle-free graphs general \(2\)-position sets are precisely dissociation sets and notes the scalar equality
\[
\operatorname{gp}_2(K_{m,n})=\max\{m,n\}
\]
for complete bipartite graphs. It does not treat crown graphs.

The general position polynomial was introduced in 2024. That paper defines the family \(T^*(r,a)\); for \(a=2\) it explicitly identifies \(T^*(r,2)\) as a complete bipartite graph without a perfect matching and displays a polynomial for it as an ordinary general position polynomial. The present result shows that the displayed expression instead counts general \(2\)-position sets.

The correction does not affect the definition of the general position polynomial or the other graph families in that paper. It is specific to the \(T^*(r,2)\) crown specialization and its resulting table and unimodality argument.

## Limitations
The theorem does not reassess the remaining \(T^*(r,a)\) formulas for \(a\ne2\). It corrects only the connected crown case \(n\ge3\).

The finite enumeration is corroborative only. The all-\(n\) correction follows from the bipartite edge obstruction for ordinary general position and the explicit index-pair classification for general \(2\)-position.

## References
1. S. Klavžar, D. F. Rall, I. G. Yero, “General \(d\)-position sets,” arXiv:2005.08095v1, 16 May 2020; Ars Mathematica Contemporanea 21 (2021), 33–44, DOI 10.26493/1855-3974.2384.77d.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General Position Polynomials,” arXiv:2401.05696v1, 11 January 2024; Results in Mathematics 79 (2024), Article 110, DOI 10.1007/s00025-024-02133-3.
