# Complete VC-shattering profiles of rank-two Kneser geodesic convexity

## Finding

For every integer \(n\ge5\), let \(G_n=KG(n,2)\) have the \(\binom n2\) edges of \(K_n\) as its vertices, with two vertices adjacent exactly when their corresponding edges are disjoint. Let \(\mathcal C_n\) be *all* geodesically convex vertex subsets of \(G_n\), including the empty and full vertex sets. A support \(S\subseteq V(G_n)\) is VC-shattered if \(\{C\cap S:C\in\mathcal C_n\}=2^S\), and let \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\). Then:

\[
\begin{aligned}
\Phi_5(z)&=1+10z+45z^2+90z^3+15z^4,\\
\Phi_6(z)&=1+15z+105z^2+255z^3,\\
\Phi_n(z)&=1+\binom n2 z+\binom{\binom n2}{2}z^2
+\sum_{k=3}^{\lfloor n/2\rfloor}\frac{n!}{2^k k!(n-2k)!}z^k\qquad(n\ge7).
\end{aligned}
\]

For \(n\ge7\), supports with at least three vertices are shattered **if and only if** their constituent edges in \(K_n\) form a matching; every support with at most two vertices is shattered. For \(n=6\), the nonshattered three-element supports are exactly the triples of vertices lying within some \(T_A=\binom A2\cup\binom{[6]\setminus A}2\) with \(|A|=3\). For \(n=5\), the fifteen shattered four-element supports are precisely the edge sets of four-cycles of \(K_5\). In particular,
\[
\operatorname{VCdim}(\mathcal C_n)=
\begin{cases}4,&n=5,\\3,&n=6,\\\lfloor n/2\rfloor,&n\ge7.\end{cases}
\]
The dimension drops from four to three when the underlying Kneser parameter increases from five to six; it returns to four at eight.

## Assumptions and scope

All graphs are finite, simple, undirected, unweighted, with graph distance defined by shortest-path length. A set of graph vertices is geodesically convex when it contains every vertex lying on every shortest path between any two of its elements. Equivalently, it is closed under the entire geodesic interval of each contained pair, not just one selected shortest path. The Kneser convention is \(KG(n,2)\) with \(n\ge5\), so the graph has diameter two. There is no claim concerning larger subset-rank Kneser graphs, Littlestone dimension, or graph convexity with a different path convention.

## Proof

**Diameter-two interval rule.** Vertices \(ab\) and \(ac\), regarded as two-element subsets of \([n]\), are nonadjacent and at graph distance two. Their geodesic interval consists of these endpoints and all vertices \(de\) with \(\{d,e\}\subseteq[n]\setminus\{a,b,c\}\). Disjoint pairs are adjacent, and their interval consists only of the two endpoints. These descriptions follow immediately from Kneser adjacency and the existence of a two-element subset disjoint from any intersecting pair when \(n\ge5\).

**Stable classification for \(n\ge7\).** Fix intersecting vertices \(ab,ac\) and write \(U=[n]\setminus\{a,b,c\}\), so \(|U|\ge4\). Their interval contains \(\binom U2\). Every further vertex \(xy\) outside \(\binom U2\) has at most one endpoint in \(U\). Hence three distinct elements \(p,q,r\in U\setminus\{x,y\}\) exist. The vertices \(pq\) and \(pr\), already included, intersect, and \(xy\) is disjoint from both. Thus \(xy\) lies on the length-two shortest path \(pq,xy,pr\). Closure in at most two rounds from any intersecting pair therefore equals the whole of \(G_n\). A proper convex set cannot contain intersecting vertices, so it is a matching in the base complete graph; conversely any matching is a clique of the Kneser graph and is geodesically convex. Thus the complete concept class consists of all matchings, viewed as vertex subsets, and one additional full-graph hypothesis.

Every two-element support is shattered by the empty set, its two singleton sets and the full graph. A matching support of arbitrary size is shattered by its own submatchings. If a support of size at least three contains intersecting vertices \(e,f\) and a third \(g\), the labeling selecting \(e,f\) but not \(g\) cannot be realized, because every convex set containing \(e,f\) equals the full graph. Therefore, for \(k\ge3\), the number of shattered \(k\)-supports is precisely the number of \(k\)-edge matchings in \(K_n\), namely \(n!/(2^k k!(n-2k)!)\). The support sizes zero, one, and two give the stated initial coefficients. This proves the all-order formula and VC dimension for \(n\ge7\).

**The six-point exceptional structure.** For an intersecting pair \(ab,ac\), write \(B=\{a,b,c\}\) and \(D=[6]\setminus B\). Its geodesic closure is exactly \(T_B=\binom B2\cup\binom D2\): the first interval supplies the entire triangle on \(D\); either triangle of edges forces the other, and \(T_B\) is convex by the interval rule. Any additional mixed edge between \(B\) and \(D\) together with \(T_B\) yields every mixed edge on repeated interval closure, hence the full graph. This can also be checked directly with the exhaustive closure evaluator below. Consequently all proper convex sets are matchings or the ten distinct \(T_B\), indexed by unordered partitions of \([6]\) into two triples. There are \(1+15+45+15=76\) matchings of \(K_6\), so there are \(76+10+1=87\) convex hypotheses, counting the full graph.

A triple \(S\) contained in some \(T_B\) contains two intersecting constituent edges in one block, by pigeonhole. Their hull is \(T_B\), so the trace containing those two but excluding the third is impossible. Conversely, if a triple lies in no \(T_B\), every one- or two-element requested positive trace can be realized by its convex hull, and the all-positive and all-negative traces are realized by the full and empty sets. Thus it is shattered. Each triple contained in a \(T_B\) has an intersecting pair that uniquely determines that \(T_B\); therefore the ten families of \(\binom63=20\) bad triples do not overlap. Exactly \(\binom{15}3-200=255\) triples are shattered. The exhaustive finite verifier checks all \(\binom{15}4\) four-element supports and finds none shattered; the same holds for larger supports by heredity. All one- and two-element supports are shattered, proving \(\Phi_6\).

**The five-point exceptional structure.** There are only \(\binom52=10\) vertices. The fully specified exhaustive algorithm in the two independent verification programs constructs the graph from disjointness, reconstructs all pairwise shortest-path intervals, enumerates every one of its \(2^{10}\) vertex subsets and tests convexity, and enumerates every possible query support and trace. It finds exactly 79 convex hypotheses and the full coefficient sequence \((1,10,45,90,15,0,\ldots)\). An additional direct graph-theoretic equality check in `verify_kneser_convexity.py` compares all fifteen shattered four-element supports with the edge sets of the fifteen four-cycles of \(K_5\) and verifies equality, not merely equal counts. This finite exhaustive proof is independent of extrapolation and completely establishes the exceptional \(n=5\) statement.

## Verification

Execute `python3 verify_kneser_convexity.py` and `python3 verify_kneser_hull_traces.py` in the directory containing both scripts. Both are self-contained standard-library Python programs. The first reconstructs shortest-path distances by breadth-first search; its exhaustive convexity and trace census gives \(\Phi_5\) and \(\Phi_6\), checks all thirty-two thousand-plus six-point candidate convex subsets, verifies their exact structural classification, independently checks bad triples, and tests intersecting-pair full hulls at \(n=7,8,9\). The second uses Floyd–Warshall shortest paths and convex-hull avoidance for every target trace, without referring to a precomputed concept-family list. Recorded execution outputs include `ALL_RANK_TWO_KNESER_SHATTERING_CHECKS_PASS` and `ALL_INDEPENDENT_HULL_TRACE_CHECKS_PASS`. The infinite-family proof is the interval and closure argument above; small-case tests alone do not establish it.

## Relationship to prior work

Bedo, Leite, Oliveira and Protti study geodetic convexity and the *geodetic hull number* of diameter-two Kneser graphs, determining minimal sizes of sets whose hull is full. The present statement classifies **all** geodesically convex hypotheses in the rank-two family, then determines every VC-shattered query support and its generating polynomial. A hull-number statement about the existence of a generating pair does not itself imply the universal pair-hull classification or the shattering counts. Iršič, Klavžar, Rus and Tuite determine *general-position polynomials* for rank-two Kneser graphs, but a geodesic general-position support (no selected three on one geodesic) is not the same as a set VC-shattered by the graph's convex subsets. The polynomial and degree differ already for the Petersen graph. Research on online learning of graph-convex sets supplies a general conceptual setting but no exact Kneser VC-shattering theorem was verified in the material available. Priority under other terminologies remains an explicitly unresolved risk.

## Limitations

The classification is only for two-element Kneser vertices and \(n\ge5\). The two exceptional orders are proved by complete finite enumeration, with runnable independently formulated algorithms; their verification is not an infinite-parameter argument. The stable \(n\ge7\) claim has a closed-form mathematical proof. No exact online learning or Littlestone dimension is asserted. Self-review is not an independent audit. The full text of the closest general online graph-convex-learning paper was not accessible, and comprehensive historical priority is not certified.

## References

1. M. Bedo, J. V. S. Leite, R. A. Oliveira, F. Protti, *Geodetic convexity and Kneser graphs*, arXiv:2203.03406 (first public 7 March 2022), later *Applied Mathematics and Computation* 449 (2023).
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (11 January 2024), *Results in Mathematics* 79, 110 (2024), DOI:10.1007/s00025-024-02133-3.
3. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, 2022 conference paper; abstract/preview consulted, complete text not verified.
