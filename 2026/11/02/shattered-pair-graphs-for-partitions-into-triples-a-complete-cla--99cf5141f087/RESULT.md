# Shattered-pair graphs for partitions into triples: a complete classification

## Finding

Fix an integer \(m\ge1\), put \(n=3m\), and let \(\mathcal T_m\) contain all partitions of the labeled vertex set \([n]\) into \(m\) unordered three-element blocks. A partition \(\pi\) determines a Boolean concept on unordered vertex pairs by \(c_\pi(\{u,v\})=1\) if and only if \(u\) and \(v\) belong to the same block.

For a support \(S\subseteq\binom{[n]}2\), form the simple graph \(H=([n],S)\). Then \(S\) is VC-shattered by \(\mathcal T_m\) **if and only if** all of the following hold:

1. Every nontrivial connected component of \(H\) is either an isolated edge \(K_2\) or a two-edge path \(P_3\).
2. Writing \(p\) for the number of \(P_3\)-components and \(q\) for the number of \(K_2\)-components, \(p+q\le m\).
3. The pair \((p,q)\) is neither \((m,0)\) nor \((m-1,1)\).

Isolated vertices are allowed. In particular, for every \(m\ge1\),
\[
\operatorname{VCdim}(\mathcal T_m)=2m-2.
\]

More precisely, the complete shattered-support enumerator is
\[
F_m(z)=\sum_{\substack{p,q\ge0,\ p+q\le m\\(p,q)\ne(m,0),(m-1,1)}}
\frac{(3m)!}{2^{p+q}p!q!(3m-3p-2q)!}\,z^{2p+q}.
\]
For \(m\ge2\), the number of maximum-cardinality shattered supports is
\[
[z^{2m-2}]F_m(z)=\frac{(3m)!}{6\,2^{m-1}(m-1)!}+\frac{(3m)!}{2^{m+2}(m-2)!}.
\]
For \(m=1\), the unique shattered support is empty.

## Assumptions and scope

All blocks have size exactly three; they are unlabeled. Queries concern equality of blocks for distinct vertices. Shattering requires a possibly different partition for every binary labeling of all query pairs in \(S\). No assumption is made on geometry, distances, preferred clusters, or a probability distribution. The formulas are valid for every integer \(m\ge1\) and all labeled supports.

## Proof

**Necessity of the component conditions.** If \(S\) is shattered, its all-positive labeling is realized by some triple partition. Every connected component of \(H\) must consequently fit in one three-element block; it has at most three vertices. If a component contained a cycle, deleting any edge of that cycle from the positive constraints would not disconnect its endpoints. The labeling that makes just that edge negative would therefore be impossible. Thus \(H\) is a forest, and every nontrivial component is \(K_2\) or \(P_3\). Different nontrivial components cannot occupy the same triple block because their combined sizes exceed three, so \(p+q\le m\).

If \((p,q)=(m,0)\), the \(m\) path components force all \(m\) triple blocks when the other queried edges are positive, making every edge of \(S\) unavoidable. If \((p,q)=(m-1,1)\), the \(m-1\) paths force \(m-1\) blocks and the two vertices joined by the remaining edge must lie together in the final block. In both cases a negative answer to a selected edge, with the other answers positive, is impossible.

**A relocation lemma.** Suppose a finite collection of three-element boxes has selected movable vertices, with exactly as many vacant positions as movable vertices, and each selected vertex may enter any box other than its box of origin. A perfect placement exists if every box with \(t\) selected vertices has at least \(t\) selected vertices originating in other boxes. Indeed, apply Hall's theorem to the bipartite graph of movable vertices and vacant positions. For a single destination box, Hall's condition is exactly the stated inequality. For at least two distinct destination boxes, each movable vertex is compatible with positions in at least one of them, so the union of their neighborhoods contains all movable vertices and Hall's inequality is automatic. A box declared *free*, whose vertices may return to their origin box, has no prohibition and may be included in the same argument.

**Sufficiency, with an unused box.** Suppose \(p+q\le m-1\). Start with one triple box for each \(P_3\), one triple box containing both endpoints of each \(K_2\) and one unused vertex, and \(m-p-q\ge1\) completely unqueried boxes. There are exactly enough unused vertices for this arrangement. Fix an arbitrary desired labeling of \(S\). From each path box select for relocation precisely its leaves whose queried edge to the center is labeled zero (at most two vertices); from each edge box labeled zero select one of the endpoints (one vertex); select none from a positive edge box. Every entirely unqueried box is free: allow all three of its vertices to be movable and to return to that box. Original positive-edge endpoints stay together; each negative edge will be broken if all selected nonfree vertices are assigned to different boxes. For any nonfree box with \(t\le2\) movable vertices, the free boxes alone provide at least three candidate movable vertices originating elsewhere, so the relocation lemma gives a complete assignment. The remaining positive endpoints and path centers never move. All positive query answers are preserved and all negative answers are realized.

**Sufficiency, no unused box.** Suppose \(p+q=m\) and \(q\ge2\). Begin with \(p\) path boxes and \(q\) edge boxes, where each edge box also contains a different unqueried singleton (there are exactly \(q\) such vertices). For each path box select each leaf whose edge to the center is negative, leaving its positive-connected vertices stationary. For each edge box select exactly one vertex: the unqueried singleton if its edge is positive, or one endpoint if its edge is negative. The selection size from a path box is \(0\), \(1\), or \(2\), while every edge box contributes exactly one movable vertex. A path box with two selected vertices has at least two movable vertices from the other \(q\ge2\) edge boxes; a path box with one selected vertex has at least two, and an edge box with one selected vertex has at least one from another edge box. The relocation lemma therefore supplies a permutation of the movable vertices among the vacancies in which no vertex returns to its original box. In every path box the center and any positive leaves remain together, and the negative leaves have moved. In each edge box the positive endpoints remain together if that edge was positive; if negative, one endpoint has moved while the other stays. Hence the chosen labeling is realized. These two cases exhaust all nonexceptional possibilities.

**Dimension and enumerator.** A support with \(p\) paths and \(q\) edges has \(2p+q\) queried pairs. Under \(p+q\le m\), the only possibilities with more than \(2m-2\) pairs are \((m,0)\) and \((m-1,1)\), both excluded. The value \(2m-2\) is attained for \(m\ge2\) by \((p,q)=(m-1,0)\) or \((m-2,2)\); the empty support gives the \(m=1\) case. For specified \(p,q\), choose disjoint labeled triples and pairs and, for each triple, one of its three two-edge paths. The number of such graphs is
\[
\frac{(3m)!}{(3!)^p p!\,(2!)^q q!\,(3m-3p-2q)!}\,3^p
=\frac{(3m)!}{2^{p+q}p!q!(3m-3p-2q)!}.
\]
Summing over permitted profiles proves \(F_m(z)\). Only \((m-1,0)\) and \((m-2,2)\) contribute to the top coefficient, giving the displayed count.

## Verification

The standalone standard-library program `verify.py` directly enumerates triple partitions and their pair-label traces whenever the elementary cardinality upper bound does not already rule out shattering. It checks all \(34\) isomorphism profiles \((m,p,q)\) with \(1\le m\le4\), and also every one of the \(8\) possible supports when \(n=3\) and all \(32,768\) supports when \(n=6\), checking the predicted enumerator coefficients. The recorded command is `python3 verify.py`, and its output is in `verification_output.txt`. These exhaustive *finite* tests corroborate—but do not replace—the unrestricted Hall-theorem proof.

For example \(F_2(z)=1+15z+105z^2\), \(F_3(z)=1+36z+630z^2+5040z^3+18900z^4\), and \(F_4(z)\) has top coefficient \(5,405,400\).

## Relationship to prior work

Pairwise same-cluster queries are a standard model in active clustering. Ailon–Begleiter–Ezra (JMLR 2014, Section 5.2) explicitly bound the VC dimension for the **larger** class of all equivalence relations having at most a prescribed number of classes: their \(\Theta(n)\) bounds and forest/cycle argument do not characterize shattered supports when every block must have exactly three elements. In that class, a full matching is shattered; this can fail for the present fixed-size class because the unmatched filler must be packed into triples. Ailon–Bhattacharya–Jaiswal–Kumar (arXiv:1704.01862; ITCS 2018) study approximation algorithms for geometric clustering, and Mazumdar–Saha (arXiv:1706.07719) study recovery query complexity with side information. Saha–Subramanian (arXiv:1908.04976; ESA 2019) study query efficiency for correlation clustering. These works motivate the same pair-oracle but their inspected statements concern algorithmic recovery under different constraints, not the exact static shattering supports of partitions into prescribed triple blocks. This finding does not assert that those papers established—or that the search exhaustively excludes—related older combinatorial classifications.

## Limitations

The theorem applies only to partitions all of whose blocks have size three; unequal-size or larger-block variants are not settled here. It determines VC shattering and its full support enumerator, not Littlestone dimension, statistical sample complexity, or the minimum number of queries needed to identify an unknown partition. Historical priority beyond the inspected sources has not been independently certified.

## References

1. N. Ailon, R. Begleiter, E. Ezra, *Active Learning Using Smooth Relative Regret Approximations with Applications*, J. Mach. Learn. Res. 15 (2014), 885–920, Section 5, especially p. 902. https://www.jmlr.org/papers/volume15/ailon14a/ailon14a.pdf
2. N. Ailon, A. Bhattacharya, R. Jaiswal, A. Kumar, *Approximate Clustering with Same-Cluster Queries*, arXiv:1704.01862 (first posted 2017-04-06), ITCS 2018, DOI:10.4230/LIPIcs.ITCS.2018.40. https://arxiv.org/abs/1704.01862
3. A. Mazumdar, B. Saha, *Query Complexity of Clustering with Side Information*, arXiv:1706.07719 (2017). https://arxiv.org/abs/1706.07719
4. B. Saha, S. Subramanian, *Correlation Clustering with Same-Cluster Queries Bounded by Optimal Cost*, arXiv:1908.04976, ESA 2019, DOI:10.4230/LIPIcs.ESA.2019.81. https://arxiv.org/abs/1908.04976
