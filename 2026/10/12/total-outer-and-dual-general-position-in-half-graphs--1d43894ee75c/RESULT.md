# Unique maximum dual general-position set of the half graph

## Finding

For every integer \(n\ge4\), let \(H_n\) be the connected half graph with bipartition
\(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where
\[
 a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]
A set \(X\) is in *general position* if no selected vertex is internal to a shortest path between two other selected vertices. It is in *dual general position* if, in addition, \(V(H_n)\setminus X\) is geodesically convex (equivalently: no shortest path between two unselected vertices passes through a selected vertex).

**Theorem (dual general-position rigidity).** For every \(n\ge4\),
\[
 \operatorname{gp}_{\mathrm d}(H_n)=2,
 \qquad\text{and}\qquad
 \{a_n,b_1\}
\]
is the **unique** maximum dual general-position set.

This is a complete infinite-family classification of the dual optimum, not a claim that the three existing general-position variants or the mutually-maximally-distant structure are newly introduced. For context, the already-known general characterizations and previously published chain-graph strong-resolving-graph structure give \(\operatorname{gp}_{\mathrm t}(H_n)=\operatorname{gp}_{\mathrm o}(H_n)=2\): total general position has the same unique leaf-pair optimum, while outer general position has exactly \(\binom n2\) optimum pairs \(\{a_i,b_j\}\) with \(j<i\). These context facts are credited as prior implications, **not presented as new findings**. The contribution here is the explicit dual convex-complement exclusion and uniqueness for all \(n\ge4\).

## Assumptions and scope

All graphs are finite, simple, undirected and connected. A vertex set \(C\) is geodesically convex if **every** shortest path between any two vertices of \(C\) lies entirely within \(C\). The dual condition therefore quantifies over *all* shortest paths between outside vertices, not just the existence of one avoiding \(X\). The theorem covers all \(n\ge4\); at \(n=3\) an additional dual optimum exists and uniqueness as stated does not hold. No assertion about arbitrary chain-graph twin-class sizes is made.

## Proof

The degrees are \(\deg(a_i)=n-i+1\) and \(\deg(b_j)=j\). Thus \(a_n\) and \(b_1\) are precisely the degree-one vertices of \(H_n\); both are simplicial. A simplicial vertex cannot be an internal vertex of a shortest path between two other vertices. Consequently \(X_0=\{a_n,b_1\}\) is in general position, and its complement is geodesically convex: a shortest path between unselected endpoints cannot pass internally through either simplicial selected vertex. Thus \(X_0\) is dual.

We show there is no larger dual set. First, **any general-position set containing three or more vertices is independent**. Suppose it contains an adjacent pair \(a_i,b_j\) (\(i\le j\)) and a third vertex. If the third is \(a_k\), then for \(k\le j\) the length-two path \(a_i-b_j-a_k\) is a geodesic (for distinct \(a_k,a_i\)); for \(k>j\) the path \(b_j-a_i-b_n-a_k\) is a length-three geodesic (the endpoints \(b_j,a_k\) are nonadjacent). Either way, one member of the selected triple is interior to a selected-pair geodesic. If the third vertex lies in \(B\), the same conclusion follows by swapping the shores and reversing their index orders. Therefore a set of size at least three in general position has no adjacent pair.

Let \(X\) be an *independent* dual set. If \(a_i\in X\) for \(i<n\), independence forces \(b_i,b_{i+1}\notin X\), since both are neighbors of \(a_i\). Their distance is two and \(b_i-a_i-b_{i+1}\) is a shortest path crossing the selected vertex \(a_i\). This contradicts convexity of the complement. Thus \(X\cap A\subseteq\{a_n\}\). Dually, if \(b_j\in X\) for \(j>1\), then \(a_{j-1},a_j\notin X\) and their distance-two path \(a_{j-1}-b_j-a_j\) violates complement convexity. Hence \(X\cap B\subseteq\{b_1\}\). An independent dual set therefore has size at most two. Combining this with the preceding independence argument, no dual set has three or more vertices.

To establish *uniqueness* among two-element sets, first consider two distinct vertices on the same shore. For \(i<k\), the unselected endpoints \(b_i,b_k\) have a length-two geodesic \(b_i-a_i-b_k\) crossing a selected vertex of \(\{a_i,a_k\}\). Likewise two selected \(B\)-vertices have an analogous geodesic crossing a selected \(b\)-vertex. Thus no same-shore pair is dual.

For a nonadjacent cross-shore pair \(\{a_i,b_j\}\) with \(i>j\), independence holds. The convexity witnesses from the preceding paragraph force \(i=n\) and \(j=1\), so this pair is \(X_0\).

Finally consider an adjacent cross-shore pair \(\{a_i,b_j\}\), with \(i\le j\). If \(i\le n-2\), then \(a_i\) has at least three distinct neighbors in \(B\), of which at most \(b_j\) is selected. Two others are unselected and joined by a length-two geodesic through \(a_i\), contradicting convexity. Otherwise \(i\ge n-1\), which together with \(n\ge4\) gives \(j\ge n-1\ge3\). Hence \(b_j\) has at least three neighbors in \(A\); two are not the selected \(a_i\) and their length-two geodesic crosses \(b_j\). No adjacent pair is dual. All other two-element possibilities have been excluded; \(X_0\) is the unique dual optimum. \(\square\)

## Finite verification and its limitations

The supplied `verify.py` independently constructs shortest-path distances and tests every vertex subset directly against the definitions of total, outer and dual general position for \(4\le n\le7\). In particular, it checks the dual optimum is \(2\) with exactly one maximizing set, \(\{a_n,b_1\}\), at every tested order. The complete arbitrary-\(n\) dual assertion rests on the geodesic/convexity argument above; testing finitely many graphs does not prove an infinite theorem.

## Relationship to prior work and contribution boundary

Tian and Klavžar, *Variety of General Position Problems in Graphs* (arXiv:2402.17338, 2024; later published 2025), introduced the total/outer/dual distinctions and proved that dual general-position sets are precisely general-position sets with geodesically convex complements. Their general criterion is a premise, not a half-graph classification. Shallcross and coauthors, *Solution to some conjectures on mobile position problems* (arXiv:2507.16622, 2025), explicitly study half graphs for **mobile ordinary general position**, not the dual convex-complement optimum.

The earlier published result *Strong metric bases of chain graphs from the canonical cut* (Resultary, 2026-10-04) already **explicitly determines the complete mutually maximally distant edge relation** of the strong resolving graph for every connected chain graph. Specializing its singleton-class result gives exactly the half-graph cross nonedges \(\{a_i,b_j\}\) with \(j<i\), and Tian--Klavžar's outer characterization then gives the outer optimum and its entire maximum-pair family. These outer facts were thus **prior-covered**; neither the present finding nor its significance claims novelty for them. The total leaf-pair calculation is similarly immediate from the published simplicial-vertex characterization. Neither cited result supplies the convexity case classification above proving uniqueness of the **dual** optimum on every half graph.

The genuinely assessed contribution is the dual-geodesic rigidity argument: within a highly structured infinite graph family, the requirement that the *entire complement* remain convex forces exactly the two degree-one vertices, and excludes all other pairs. It gives a precise benchmark for separating ordinary, outer and dual shortest-path visibility on chain graphs. A differently indexed dual-position classification may exist, so originality remains best-of-knowledge rather than absolute priority certification.

## References

1. J. Tian and S. Klavžar, *Variety of General Position Problems in Graphs*, arXiv:2402.17338, 2024; *Bulletin of the Malaysian Mathematical Sciences Society* 48 (2025), article 5, DOI 10.1007/s40840-024-01788-z.
2. E. Shallcross, J. Tuite, A. Evans, A. Krishnakumar, and S. Boshar, *Solution to some conjectures on mobile position problems*, arXiv:2507.16622, 2025.
3. *Strong metric bases of chain graphs from the canonical cut*, Resultary, published 2026-10-04, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-strong-metric-bases-of-chain-graphs-from-the-canonical-cut--b2ee564f2dc9/RESULT.md.
