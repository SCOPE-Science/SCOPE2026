# Exact arclength-distance separation of the Shrikhande and rook metric graphs

## Finding

Let \(R=K_4\square K_4\) be the \(4\times4\) rook graph and let \(S\) be the Shrikhande graph on \(\mathbb Z_4^2\), where two vertices differ by one of \((\pm1,0),(0,\pm1),(\pm1,\pm1)\) with matching signs in the last pair. Give each graph edge length one. Independently sample two points by normalized arclength over its 48 edges, and let \(F_R(t)\) and \(F_S(t)\) denote the cumulative distributions of their intrinsic shortest-path distances.

Then, for every real \(t\),
\[
 F_S(t)-F_R(t)=
 \begin{cases}
 0,&t\le 2,\\
 (t-2)^2/24,&2\le t\le5/2,\\
 (3-t)^2/24,&5/2\le t\le3,\\
 0,&t\ge3.
 \end{cases}
\]
In particular,
\[
 F_R(5/2)=29/32,\qquad F_S(5/2)=11/12,
 \qquad F_S(5/2)-F_R(5/2)=1/96.
\]
Thus these two nonisomorphic, cospectral, strongly regular graphs have identical continuous arclength-distance distributions through radius two but are distinguishable at every radius strictly between two and three.

More generally, let \(G\) be **any finite connected simple unit-edge graph with vertex-graph diameter at most two**, let \(m=|E(G)|\ge1\), and let \(M_2(G)\) count unordered induced two-edge matchings (induced \(2K_2\) subgraphs). For independent normalized-arclength points with intrinsic distance \(D_G\),
\[
 \mathbb P(D_G>t)=\frac{4M_2(G)}{m^2}(3-t)^2
 \quad (5/2\le t\le3).
\]
Consequently \(\mathbb P(D_G>5/2)=M_2(G)/m^2\). In this class the full distance law also determines \(m\), since its right derivative at zero is \(2/m\). Hence it determines the exact induced-two-edge-matching count. Specifically, \(M_2(R)=216\) and \(M_2(S)=192\).

## Assumptions and scope

A metric edge is the unit interval with its endpoints identified with graph vertices; distance is length of a shortest path in the resulting one-dimensional length space, **not Euclidean distance in an embedding**. Arclength sampling assigns equal probability to each original edge and uniform conditional position on that edge. The endpoint-identification events have probability zero. Graphs are labeled only to construct and verify an invariant law; all conclusions are graph-isomorphism invariant. The general tail identity requires connectedness, simplicity, unit edge lengths, and vertex diameter at most two. The exact two-graph identity is limited to the two specified graphs.

## Proof

**Universal tail.** For two points on the same edge their distance is at most one; for points on edges sharing a vertex it is at most two. Suppose instead they lie on distinct vertex-disjoint edges \(e=ab\), \(f=cd\). Write their positions as proportions \(x,y\in[0,1]\) from \(a,c\), respectively. Their distance is
\[
\min\{d(a,c)+x+y,\ d(a,d)+x+1-y,\ d(b,c)+1-x+y,\ d(b,d)+2-x-y\},
\]
where the \(d\)'s denote vertex-graph distances. If any endpoint pair across the edges is adjacent, orient both edges to make \(a,c\) adjacent. Because the graph has diameter at most two, the two routes through \(a,c\) and through \(b,d\) give
\[
D_G\le\min\{1+x+y,\ 4-x-y\}\le5/2.
\]
If instead no cross-endpoint pair is adjacent, the four cross-distances are all two. The minimum then simplifies to
\[
 D_G=2+\min(x,1-x)+\min(y,1-y).
\]
The two minima are independent uniform random variables on \([0,1/2]\). Their sum has upper tail \(2(1-s)^2\) for \(1/2\le s\le1\), so a single ordered induced-matching edge pair contributes \(2(3-t)^2\) to \(\mathbb P(D_G>t)\) for \(5/2\le t\le3\). There are \(2M_2(G)\) such ordered edge pairs out of \(m^2\), proving the formula. The equal-edge contribution \(m(2r-r^2)/m^2\) for small positive \(r\), and all distinct-edge contributions \(O(r^2)\), show \(F'_G(0+)=2/m\).

**Exact graph-pair comparison.** Represent both graphs on the 16 labeled pairs in \(\mathbb Z_4^2\). The rook graph connects pairs with exactly one equal coordinate; Shrikhande adjacency uses the six differences specified above. Direct degree/common-neighbor calculation gives \((v,k,\lambda,\mu)=(16,6,2,2)\) for both, and each graph has 48 edges and vertex diameter two. For two **distinct** unordered metric edges \((a,b)\), \((c,d)\), encode the four vertex-distances by \((d(a,c),d(a,d),d(b,c),d(b,d))\), modulo reversal of either edge and interchange of the two edges. Enumeration of all \(\binom{48}{2}=1128\) pairs in each graph gives:

| Canonical four-distances | Rook count | Shrikhande count |
|---|---:|---:|
| (0,1,1,1) | 96 | 96 |
| (0,1,1,2) | 144 | 144 |
| (1,1,1,1) | 24 | 0 |
| (1,1,1,2) | 0 | 96 |
| (1,1,2,2) | 288 | 192 |
| (1,2,2,1) | 72 | 24 |
| (1,2,2,2) | 288 | 384 |
| (2,2,2,2) | 216 | 192 |

All other classes have count zero. The \((2,2,2,2)\) class is precisely an induced two-edge matching; it yields the claimed values 216 and 192. The two graphs have no difference from identical-edge pairs, since both have 48 edges.

For any class \(abcd\), let \(T_{abcd}(t)\) be the area in \([0,1]^2\) where **all four** endpoint routes listed above have length greater than \(t\). This is the area of a convex polygon obtained by intersecting the unit square with four explicitly given halfplanes. The table reduces the difference of *unordered* distinct-edge upper-tail contributions to \(24Q(t)\), where
\[
 Q=T_{1111}-4T_{1112}+4T_{1122}+2T_{1221}-4T_{1222}+T_{2222}.
\]
Elementary halfplane clipping yields
\[
 Q(t)=\begin{cases}
 0,&t\le2,\\
 2(t-2)^2,&2\le t\le5/2,\\
 2(3-t)^2,&5/2\le t\le3,\\
 0,&t\ge3.
 \end{cases}
\]
For example, writing \(s=t-2\in[0,1/2]\), the only nonzero contributing upper-tail areas from these six classes are
\[
 T_{1122}=(1/2-s)^2,\quad T_{1222}=1/2-s,\quad
 T_{2222}=1-2s^2,
\]
which give \(Q=2s^2\). In the interval \([5/2,3]\), only \(T_{2222}=2(3-t)^2\) survives. On \([0,2]\) direct clipping gives exact cancellation. The supplementary verifier exhausts the edge pairs and checks this cancellation at three exact rational controls on every half-unit interval; these controls suffice because all region-boundary intersections have coordinates affine in \(t\) between consecutive half-integers, so each polygon area is a quadratic polynomial there.

There are \(48^2\) ordered edge pairs and each unordered pair occurs twice. Therefore
\[
F_R(t)-F_S(t)=-\frac{48}{48^2}Q(t)=-\frac{Q(t)}{48},
\]
which proves the complete identity. At \(t=5/2\), the universal tail gives \(F_R=1-216/2304=29/32\) and \(F_S=1-192/2304=11/12\).

## Verification

Run `python3 verify.py` with the Python standard library. It independently constructs both graphs from their adjacency definitions, verifies the 16-vertex strongly regular parameters and graph distances, enumerates all 1128 unordered edge pairs for each graph, and checks the exact integer pattern tables and induced-matching counts. Convex-polygon clipping uses rational arithmetic only. Exact-rational checks at the endpoints and midpoint of each of six half-unit intervals, together with the proved quadratic-piece property, verify the full difference identity without floating-point approximation. Additional exact checks verify the diagnostic radius and upper-tail areas. These checks are exhaustive for the two explicitly defined finite graphs. The universal diameter-two statement is proved by the route comparison above, not extrapolated from graph tests.

## Relationship to prior work

Wei, Walteros and Batta (2019; published online November 27) give a general forward framework for distance distributions of random edge-location events on arbitrary networks. That substantially broader computational framework is acknowledged: no novelty is claimed for the ability to calculate a distance law on a given graph. The claim here is the **exact inverse induced-matching identity for diameter-two graphs** and the **sharp explicit difference law** for the classical strongly regular pair, not a new general graph distance algorithm. Gamble et al. (first public arXiv version February 16, 2010) analyze strongly regular graph distinguishability via quantum walks, an invariant with different definitions and outputs. Existing analysis of Shrikhande/rook graph Čech and independence complexes concerns topological complexes, not edge-uniform intrinsic two-point distance laws. The exact polynomial difference and its onset at radius two were not found in the inspected comparisons. This is a best-knowledge priority statement, not a claim of exhaustive historical uniqueness.

## Limitations

The universal tail formula does not extend as written to graphs of vertex diameter three or more, or to arbitrary unequal edge lengths. It determines one induced-matching count, not a whole graph. The pair separation holds for intrinsic continuous-arclength sampling, not for uniformly sampled *vertices*: the two graphs share all standard vertex-distance parameters. The full short-distance identity is a finite exact comparison, not a general classification of strongly regular graphs. Other equivalent formulations in earlier graph-invariant or network-distance literature remain a historical-priority risk.

## References

1. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003v1 (first submitted 2010-02-16), subsequently Phys. Rev. A 81, 052313 (2010), https://arxiv.org/abs/1002.3003 .
2. N. Wei, J. L. Walteros and R. Batta, *On the distance between random events on a network*, first published online 2019-11-27, Networks 75 (2020), 203–231, DOI:10.1002/net.21919; openly displayed author text https://www.researchgate.net/publication/337598607_On_the_distance_between_random_events_on_a_network .
3. *Shrikhande graph* data overview, https://jaanos.github.io/tables/graphs/Shrikhande.html (historical background identifying the classical 1959 classification).
