# Five actors are the first strict rank reversal between triangle balance and frustration balance
## Finding
Consider a complete undirected signed network
\[
G=(V,E,\sigma),
\]
where every edge has sign \(+1\) or \(-1\).

A triangle is balanced when the product of its three edge signs is positive. Let
\[
U(G)
\]
be the number of unbalanced triangles, and define the triangle index
\[
T(G)=1-\frac{U(G)}{\binom{|V|}{3}}.
\]

Let \(L(G)\) be the frustration index: the minimum number of edges whose deletion makes the signed graph balanced, equivalently the minimum number of frustrated edges over all bipartitions of the vertices. Following the standard normalization for a graph with \(m\) edges, define
\[
F(G)=1-\frac{2L(G)}{m}.
\]

Both \(T\) and \(F\) are invariant under switching, so it is natural to compare their rankings on switching-isomorphism classes.

For complete signed graphs on at most \(4\) vertices, the two measures induce the same strict ordering of switching-isomorphism classes.

This fails first at \(5\) vertices, and there is exactly one unordered pair of switching-isomorphism classes giving a strict rank reversal.

Choose the unique switching representative in which every edge incident with vertex \(0\) is positive.

For the first class, let the negative edges be
\[
\{12,14,23\}.
\]
The negative subgraph on vertices \(1,2,3,4\) is a path on four vertices. This signing has
\[
U=5,\qquad L=3,
\]
hence
\[
T=\frac12,\qquad F=\frac25.
\]

For the second class, let the negative edges be
\[
\{14,23\}.
\]
The negative subgraph on vertices \(1,2,3,4\) is a matching of size \(2\). This signing has
\[
U=6,\qquad L=2,
\]
hence
\[
T=\frac25,\qquad F=\frac35.
\]

Therefore
\[
T_{\mathrm{path}}>T_{\mathrm{matching}}
\]
but
\[
F_{\mathrm{path}}<F_{\mathrm{matching}}.
\]
The triangle index judges the path-type signing more balanced, while the frustration measure judges the matching-type signing more balanced.

The path-type reversal class contains \(12\) labeled switching classes, and the matching-type class contains \(15\). Since each switching class of a complete signed graph on \(5\) labeled vertices contains
\[
2^{5-1}=16
\]
raw sign assignments, the two types comprise respectively
\[
192
\]
and
\[
240
\]
raw signings.

## Assumptions and scope
The underlying graph is complete, finite, simple, undirected, and signed.

Balance is the classical Cartwright--Harary notion: every cycle has positive sign, equivalently the vertices admit a bipartition with positive edges inside parts and negative edges between parts.

The triangle index is the relative \(3\)-balance
\[
T(G)=D_3(G).
\]

The normalized frustration measure is
\[
F(G)=1-\frac{2L(G)}{|E|}.
\]

The theorem compares strict ordinal judgments between distinct switching-isomorphism classes. Equalities under one measure are not counted as rank reversals.

The result is only a smallest-order statement for complete signed networks. It does not claim that the two measures agree on sparse signed graphs of the same order.

## Proof
Switching a vertex subset reverses exactly the signs on the corresponding cut. Cycle signs are switching-invariant, so \(T\) is switching-invariant. The frustration index is also switching-invariant because switching simply relabels which bipartition realizes a given number of frustrated edges.

For a complete signed graph on \(n\) vertices, every switching class has a unique representative in which all edges incident with vertex \(0\) are positive. Thus there are
\[
2^{\binom{n-1}{2}}
\]
switching classes on labeled vertices.

The verifier exhausts these normalized classes and then quotients by vertex relabeling using the switching-invariant pattern of unbalanced triangles.

For \(n=3\), the switching-isomorphism classes have
\[
(U,L)\in\{(0,0),(1,1)\}.
\]

For \(n=4\), they have
\[
(U,L)\in\{(0,0),(2,1),(4,2)\}.
\]

Thus through four vertices, increasing \(U\) always increases \(L\). Since \(T\) is strictly decreasing in \(U\) and \(F\) is strictly decreasing in \(L\) for fixed \(n\), the two measures have the same strict ordering.

For \(n=5\), there are seven switching-isomorphism classes. Their complete invariant table is
\[
\begin{array}{c|c|c}
U & L & \text{number of labeled switching classes}\\ \hline
0&0&1\\
3&1&10\\
4&2&15\\
5&3&12\\
6&2&15\\
7&3&10\\
10&4&1
\end{array}
\]

Only the pair
\[
(5,3)\quad\text{and}\quad(6,2)
\]
reverses the strict order, because
\[
5<6\qquad\text{but}\qquad 3>2.
\]

The displayed representatives realize exactly these two rows.

For the path-type signing, direct triangle-sign multiplication gives five unbalanced triangles. Exhaustion of all \(2^{4}=16\) vertex bipartitions gives frustration \(3\).

For the matching-type signing, direct triangle-sign multiplication gives six unbalanced triangles, while the best bipartition has frustration \(2\).

The verifier independently recomputes frustration both as the minimum number of frustrated edges over all bipartitions and as the minimum number of negative edges over all switchings. The two values agree for every raw signing through \(K_5\).

## Verification
The embedded `verify_signed_balance_rank_reversal.py` uses only the Python standard library.

It performs two complementary exhaustive checks.

First, it enumerates all raw edge-sign assignments on
\[
K_3,\quad K_4,\quad K_5,
\]
namely
\[
8,\quad64,\quad1024
\]
signings. For each signing it computes:
- the number of unbalanced triangles directly from edge-sign products;
- frustration by exhaustive vertex bipartitions;
- frustration independently as the minimum negative-edge count over all switchings.

Second, it normalizes every signing by switching so that all edges incident with vertex \(0\) are positive, then canonically quotients the normalized switching classes under all vertex permutations using the unbalanced-triangle pattern.

It verifies the exact class tables
\[
K_3:\ (0,0),(1,1),
\]
\[
K_4:\ (0,0),(2,1),(4,2),
\]
and
\[
K_5:\ (0,0),(3,1),(4,2),(5,3),(6,2),(7,3),(10,4),
\]
with labeled switching-class multiplicities
\[
1,10,15,12,15,10,1
\]
at order five.

It then verifies that the unique strict reversal is the pair
\[
(5,3)\leftrightarrow(6,2),
\]
with the two displayed normalized negative-edge sets and raw-signing counts \(192\) and \(240\).

Run:

`python3 verify_signed_balance_rank_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Aref and Wilson formalize partial balance in signed social networks and compare several measures because complete balance is rare in empirical data. Their paper explicitly defines the triangle index as the fraction of balanced \(3\)-cycles and defines the normalized frustration index
\[
F(G)=1-\frac{2L(G)}{m}.
\]
It also reports that cycle-based and frustration-based measures can produce substantially different assessments of partial balance.

The same paper treats switching as balance-preserving, explains frustration as a minimum over vertex two-colorings or switchings, and recommends frustration-based measurement as a global alternative to cycle-based indices.

Its analytical complete-graph discussion considers special signing families and notes that different measures can identify different extremal configurations. The inspected text does not give the smallest complete network on which \(T\) and \(F\) make opposite strict pairwise judgments, nor a complete switching-isomorphism census of that first reversal layer.

Targeted searches using triangle-index, frustration-index, complete signed graph, switching, five-vertex, \(K_5\), and rank-reversal formulations did not locate this exact minimality statement or the unique reversal pair.

## Limitations
The result concerns complete signed networks only.

The finite classification stops at \(5\) vertices because that is the first reversal order; it does not enumerate larger orders.

The triangle index and normalized frustration index are only two of several proposed measures of partial structural balance.

A switching-class atlas, thesis appendix, software test corpus, or teaching note not indexed by the searches could contain the same \(K_5\) comparison.

## References
1. S. Aref and M. C. Wilson, “Measuring Partial Balance in Signed Networks,” arXiv:1509.04037, first submitted 14 September 2015; *Journal of Complex Networks* 6(4), 566–595. DOI: 10.1093/comnet/cnx044.
2. D. Cartwright and F. Harary, “Structural Balance: A Generalization of Heider's Theory,” *Psychological Review* 63(5), 277–293, 1956. DOI: 10.1037/h0046049.
