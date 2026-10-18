# Sharp freezing and bounded token-sliding distances on \(\operatorname{KG}(n,2)\)

## Finding
For every integer \(n\ge5\), consider the Kneser graph \(G_n=\operatorname{KG}(n,2)\). Let \(R_{n,k}\) be the token-sliding graph on its independent sets of size \(k\), for \(1\le k\le n-1\). There is a sharp transition at four tokens:

* \(R_{n,1}\) is connected of diameter \(2\).
* \(R_{n,2}\) is connected, vertex-transitive, and has radius and diameter \(4\). Its order is \(n\binom{n-1}{2}\) and degree is \(2(n-3)\).
* \(R_{n,3}\) is a connected bipartite graph between \(\binom n3\) triangle configurations and \(n\binom{n-1}{3}\) three-edge star configurations. The two degrees are respectively \(3(n-3)\) and \(3\). Its radius and diameter are
\[
(\operatorname{rad},\operatorname{diam})(R_{n,3})=
\begin{cases}(4,4)&n=5,\\(5,6)&n=6,\\(7,7)&n=7,\\(7,8)&n\ge8.\end{cases}
\]
* Every state of \(R_{n,k}\) for \(4\le k\le n-1\) is isolated, and there are precisely \(n\binom{n-1}{k}\) such states. There are no states for \(k>n-1\).

Remarkably, \(R_{n,2}\) and \(R_{n,3}\) have the **same** number of edges, namely \(\frac{n(n-1)(n-2)(n-3)}2\), despite their different geometry.

More precisely, \(R_{n,3}\) has an exact intrinsic distance rule. For a triangle-state \(T_A\) on three labels \(A\), put \(\mathcal A(T_A)=\{A\}\). For a star-state \(S_{a;B}\), with center \(a\) and three distinct leaves \(B\), put
\[\mathcal A(S_{a;B})=\{\{a\}\cup X:X\in\tbinom B2\}.\]
For distinct states \(X,Y\) in \(R_{n,3}\), one has
\[
d(X,Y)=2\left(3-\max_{U\in\mathcal A(X),\,V\in\mathcal A(Y)}|U\cap V|\right)
+\mathbf{1}_{X\text{ is a star}}+\mathbf{1}_{Y\text{ is a star}}.
\]
Of course \(d(X,X)=0\).

## Assumptions and scope
The vertex set of \(G_n\) consists of the unordered two-element subsets of \([n]=\{1,\ldots,n\}\); two vertices of \(G_n\) are adjacent precisely when the underlying two-element subsets are **disjoint**. Consequently, an independent set in \(G_n\) is a pairwise-intersecting family of edges of the complete graph on \([n]\). A token slide replaces one of these edges by a new edge disjoint from the removed edge, keeping all remaining edges fixed and preserving pairwise intersection. Tokens are indistinguishable; state counts do not quotient by automorphisms. Distances refer to the ordinary unweighted shortest-path metric within a connected component. The classification is for all integers \(n\ge5\) and all permissible integer occupancies \(k\ge1\); the empty state is not considered.

## Proof
**1. Shape of independent sets.** A pairwise-intersecting family of three distinct two-subsets is either the three edges of a triangle or three edges of a star. If a pairwise-intersecting family contains at least four edges, they must share a center: take two members \(\{a,b\}\) and \(\{a,c\}\). Any member not containing \(a\) must be \(\{b,c\}\); then no fourth distinct edge can intersect all three. Thus the independence number is \(n-1\). All counts of star and triangle states follow by choosing centers, leaf sets, or triangle triples.

**2. Frozen region.** In a star-family of size \(k\ge4\), each of its \(k-1\) edges retained after a proposed slide contains the old center \(a\), and their leaves are distinct. The replacement edge must avoid \(a\), because it is disjoint from the removed edge, yet must meet at least three retained edges. A two-element set cannot contain three distinct leaves. Hence no slide exists, proving every higher-occupancy state is isolated.

**3. Two tokens.** Represent the two-edge state \(\{\{a,b\},\{a,c\}\}\) as \(P(a;b,c)\), where \(b,c\) are unordered. A slide keeps one edge, say \(\{a,c\}\), and replaces \(\{a,b\}\) by \(\{c,d\}\), where \(d\notin\{a,b,c\}\). Therefore \(P(a;b,c)\) has exactly \(2(n-3)\) neighbors, all with a different center. All states are equivalent under label permutations.

For the diameter upper bound, it suffices to check \(n=5\) and \(n=6\): any two states on more labels involve at most six labels, and the induced six-label Kneser graph contains both with exactly the same legal slides. Fix \(P(0;1,2)\). Under exchanges of labels \(1,2\) and arbitrary permutations of unused labels, a complete set of target-orbit representatives is given below. The columns give orbit multiplicity for five and six labels and the exact distance to the fixed start. A dash means the type requires six labels. Their multiplicities sum to \(30\) and \(60\), respectively. Each distance is reproduced by the exhaustive state-and-slide enumeration in `verify.py`.

| Target representative | Five-label multiplicity | Six-label multiplicity | Distance |
| --- | ---: | ---: | ---: |
| `P(0;1,2)` | 1 | 1 | 0 |
| `P(0;1,3)` | 4 | 6 | 2 |
| `P(0;3,4)` | 1 | 3 | 4 |
| `P(1;0,2)` | 2 | 2 | 3 |
| `P(1;0,3)` | 4 | 6 | 1 |
| `P(1;2,3)` | 4 | 6 | 3 |
| `P(1;3,4)` | 2 | 6 | 3 |
| `P(3;0,1)` | 4 | 6 | 3 |
| `P(3;0,4)` | 2 | 6 | 3 |
| `P(3;1,2)` | 2 | 3 | 2 |
| `P(3;1,4)` | 4 | 12 | 2 |
| `P(3;4,5)` | – | 3 | 3 |

To see that diameter four is necessary for every \(n\ge5\), compare \(P(a;b,c)\) with \(P(a;d,e)\), where all five letters are distinct. Their edges are disjoint as states and neither target edge can be created by the first slide, because every first-slide replacement avoids \(a\). A hypothetical three-step path must create a target edge on its second slide. The first intermediate state is of the form \(\{\{a,t\},\{t,u\}\}\), and the second slide can introduce an edge containing \(a\) only by replacing \(\{t,u\}\), leaving \(\{a,t\}\). The resulting state has center \(a\), so its next slide necessarily leaves center \(a\) and cannot equal \(P(a;d,e)\). Hence the distance is at least four; the finite six-label bound supplies the matching upper bound.

**4. Three tokens and exact distances.** A three-star \(S_{a;\{b,c,d\}}\) has precisely the triangle-state neighbors \(T_{\{a,b,c\}}\), \(T_{\{a,b,d\}}\) and \(T_{\{a,c,d\}}\). Conversely, a triangle \(T_{\{a,b,c\}}\) has \(3(n-3)\) star neighbors, obtained by retaining two triangle edges and sliding the third to a new edge through their common endpoint. Thus \(R_{n,3}\) is bipartite with the asserted degrees and edge count.

Two triangle vertices are linked by a two-step path exactly when their underlying triples differ in one label. Indeed, their common intermediate star is supported on their four-label union, with center one of their two shared labels; conversely any two triangle neighbors of a star share two labels. Therefore the triangle-to-triangle distance in \(R_{n,3}\) is exactly twice the distance in the Johnson graph \(J(n,3)\), namely \(2(3-|A\cap B|)\). Any path with a star endpoint begins or ends at one of that star's three adjacent triangles. Minimizing over these forced choices proves the displayed formula for all distinct states. It also proves connectivity, since \(J(n,3)\) is connected and every star has neighbors.

**5. Sharp radii and diameters.** Triangle-to-triangle distance is at most six, with maximum four when \(n=5\). A triangle versus a star has distance at most seven; it attains seven precisely when a triangle can be disjoint from the star's four-label support, possible when \(n\ge7\). For \(n=6\), their supports meet and the maximum is five, attained by exactly one common label; for \(n=5\), their supports meet in at least two labels, giving a maximum of three.

For two distinct stars, the distance is at most eight. Every pair of labels in the support of a star belongs to at least one of its three adjacent triangles. Hence if the two four-label star supports intersect in at least \(r\) labels for \(r=1,2\), adjacent triangles can be chosen with at least \(r\) labels in common, giving star-to-star distance at most \(8-2r\). In particular, for \(n=5\) it is at most four, for \(n=6\) at most four, and for \(n=7\) at most six. At \(n=5\), two stars with distinct centers and supports sharing their three leaves have no common adjacent triangle, and their distance is four. For \(n\ge8\), disjoint four-label star supports exist and give distance eight. Combining these extrema produces the listed typewise eccentricities and the radii and diameters.

**6. One token and edge counts.** For one token, two disjoint two-subsets are adjacent, while two intersecting two-subsets have a common disjoint two-subset when \(n\ge5\), proving diameter two. For two tokens, multiplying the number \(n\binom{n-1}2\) of states by degree \(2(n-3)\) and halving gives \(\frac{n(n-1)(n-2)(n-3)}2\). For three tokens, multiplying the \(n\binom{n-1}3\) stars by degree three gives the same edge count.

## Verification
Run `python3 verify.py` using only Python's standard library. The program independently enumerates all pairwise-intersecting families of sizes two and three for \(5\le n\le9\), constructs moves directly from the disjoint-replacement rule, checks connectivity, all-source shortest-path distances, the exact triangle/star metric formula and the predicted eccentricities. For \(5\le n\le7\), it also enumerates every independent family at occupancies \(4\le k\le n-1\) and verifies that all have degree zero and the predicted number of states. The run's output is included in `CHECKS.txt`. The infinite-family statements use the proofs above, not extrapolation from these finite tests. The compact orbit table used for the two-token bound is also reproduced by exact finite enumeration over at most six labels.

## Relationship to prior work
Demaine and collaborators (arXiv:1406.6576, first publicly submitted 2014-06-25) study sliding tokens on trees and give algorithms and quadratic-length examples. Avis and Hoang (arXiv:2203.16861) study structural properties and realizability of general independent-set token-sliding graphs; their appendix summarizes diameters for trees, paths, chordal and other special graph classes. The present classification instead gives an explicit uniform formula for an infinite non-tree Kneser graph family, including all occupancies, a star-triangle Johnson incidence metric, and a sharp transition to completely frozen states. These formulas are not consequences of the restricted-tree results or the cited generic structural statements. The elementary fact that pairwise-intersecting two-subsets form stars or triangles is used as a starting lemma and is not claimed as new.

## Limitations
Novelty cannot be certified against every unindexed work; an equivalent unpublished classification could exist. The two-token diameter proof uses a small, explicitly enumerable finite six-label case with a standalone checker, whereas the remaining infinite-dimensional claims are proved combinatorially. The move rule is strictly *token sliding* along edges of \(\operatorname{KG}(n,2)\), not token jumping or unrestricted one-element exchanges. The argument does not apply to higher-uniformity Kneser graphs \(\operatorname{KG}(n,r)\) with \(r>2\), nor does it claim independent external validation.

## References
1. E. D. Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576 (first public submission 2014-06-25), https://arxiv.org/abs/1406.6576 .
2. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, https://arxiv.org/abs/2203.16861 .
3. D. Avis and D. A. Hoang, *A Note On Acyclic Token Sliding Reconfiguration Graphs of Independent Sets*, arXiv:2301.00317, https://arxiv.org/abs/2301.00317 .
