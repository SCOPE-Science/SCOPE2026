# Edge-open packing profiles of matching-deleted bicliques

## Finding
Let \(m,n\ge 2\), and let \(0\le t\le\min\{m,n\}\) be integers. From the complete bipartite graph with parts \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), delete the \(t\) independent edges \(a_ib_i\), \(1\le i\le t\), obtaining \(H_{m,n,t}\). For a graph \(H\), let \(P_H(x)=\sum_{S}x^{|S|}\), with the sum over all edge-open packing sets \(S\subseteq E(H)\), including the empty set.

Every edge-open packing set of \(H_{m,n,t}\) containing at least two edges is **exactly one** of the following: (i) a subset of at least two edges incident to a common vertex; or (ii) the two-edge set \(\{a_ib_j,a_jb_i\}\) for a unique pair \(1\le i<j\le t\). No set of the second kind can be enlarged to a three-edge packing.

Consequently, with \(\binom{d}{k}=0\) when \(k>d\),
\[
P_{H_{m,n,t}}(x)=1+(mn-t)x+\sum_{k\ge2}\left[t\binom{n-1}{k}+(m-t)\binom{n}{k}+t\binom{m-1}{k}+(n-t)\binom{m}{k}+\mathbf{1}_{k=2}\binom{t}{2}\right]x^k.
\]
The sum is finite, ending at \(\max\{m,n\}\). In particular, deletion of a matching introduces exactly \(\binom{t}{2}\) non-star two-edge packing sets and introduces no larger non-star packings.

## Assumptions and scope
All graphs here are finite, simple, and undirected; connectivity is not assumed. Distinct edges \(e,f\) have a *common edge* if there exists a third edge \(g\notin\{e,f\}\) with one endpoint in \(e\) and the other endpoint in \(f\). An *edge-open packing* is an edge set in which no two edges have a common edge. The empty set is included only to make the enumerator's constant coefficient equal to one. An injective edge coloring partitions edges into edge-open packing classes, so the same formula counts possible individual monochromatic classes by size, without asserting a formula for complete colorings.

The index range includes \(t=0\), the undeleted complete bipartite graph, as a boundary case, and includes full matched deletions \(t=\min\{m,n\}\). The two parts may have unequal sizes.

## Proof
First consider two disjoint edges \(e=a_ib_j\) and \(f=a_kb_\ell\), with \(i\ne k\), \(j\ne\ell\). Because the graph is bipartite, the only potential third edges joining their endpoints are \(a_ib_\ell\) and \(a_kb_j\). Hence the pair \(\{e,f\}\) is an edge-open packing exactly when **both** cross edges are missing. Every missing edge in \(H_{m,n,t}\) has form \(a_rb_r\) with \(r\le t\). It follows that \(i=\ell\le t\), \(k=j\le t\), and \(i\ne j\). Conversely, each such crossed pair is feasible because its only two potential third edges were deleted.

Suppose a packing contains the crossed pair \(e=a_ib_j\), \(f=a_jb_i\). A third selected edge \(g\) cannot be disjoint from \(e\), since the preceding characterization would force \(g=f\); similarly it cannot be disjoint from \(f\). Thus \(g\) would need to meet both disjoint edges. The only bipartite edges between their endpoints are \(a_ib_i\) and \(a_jb_j\), which are missing. Consequently no such \(g\) exists.

If a packing contains no disjoint pair, its edges are pairwise incident. In a simple bipartite graph, any family of at least two pairwise incident edges shares one vertex: choose two edges meeting at \(v\); an edge meeting both but not \(v\) would complete a triangle, impossible. Hence the packing is a star subset. Conversely, any two edges in a bipartite star have no third edge joining their endpoints: the only possible cross-edges between their endpoints are the two selected edges themselves. Therefore every star subset is feasible.

The \(t\) vertices of \(A\) incident with a removed edge each have degree \(n-1\), and its other \(m-t\) vertices have degree \(n\). Likewise, the corresponding counts in \(B\) are \(t\) vertices of degree \(m-1\) and \(n-t\) of degree \(m\). For size \(k\ge2\), a star subset has a **unique** center, so summing \(\binom{\deg(v)}{k}\) over all vertices counts every star packing once. The exceptional crossed pairs are indexed by the \(\binom{t}{2}\) unordered deleted-edge pairs, each counted once and none a star. Finally, there are \(mn-t\) singleton edges and one empty set. This proves the classification and polynomial coefficient formula for every allowed \(m,n,t\).

## Verification
Run the standard-library-only script `python3 verify.py`. It independently enumerates every one of the \(144444\) edge subsets in the \(32\) cases \(2\le m,n\le4\), \(0\le t\le\min\{m,n\}\), comparing both feasibility and all polynomial coefficients. It separately enumerates all \(2^{20}=1048576\) subsets of the crown graph \(H_{5,5,5}\), obtaining coefficients \(1,20,70,40,10\), and independently compares the endpoint-scanning common-edge test against the bipartite cross-edge rule for \(5062\) selected-edge pairs. These finite checks do not replace the preceding all-parameter proof.

For example, on the full matching-deleted \(H_{5,5,5}\), the coefficient of \(x^2\) equals \(70\): \(60\) star pairs and \(10\) crossed pairs. For \(t=0\), the exceptional term vanishes, recovering the direct star-only count on complete bipartite graphs.

## Relationship to prior work
Chelladurai, Kalimuthu, and Soundararajan introduced edge-open packing in 2022. Their Proposition 2.3 determines the **maximum cardinality** for complete multipartite graphs, including undeleted bicliques. It does not give an all-cardinality enumerator for bicliques with a deleted matching. Brešar and Samadi (2024, Theorem 4.2) give general bounds for the effect of deleting one edge on the maximum packing number; neither bounds nor general induced-star decomposition specify the exact family of crossed pairs or the complete coefficient profile here. Cardoso, Cerdeira, Dominic, and Cruz (2019, Proposition 2.2) characterize injective edge-color classes as induced star forests, a general structural statement compatible with our specialization but not an enumeration for this matching-deletion family. Brešar, Dravec, Hedžet, and Samadi (2024, Section 4) also study lower bounds for the edge-open packing number of direct graph products, sometimes involving perfect-matching deletions in illustrative induced-matching constructions. Their full paper does not give this all-cardinality enumeration. The contribution here is the precise exceptional-pair classification and its exact whole-polynomial count, not a claim of priority for those earlier definitions, product bounds, or scalar results.

## Limitations
No formula for the full injective edge chromatic polynomial or the number of partitions into several EOP classes is claimed. The polynomial counts single feasible edge subsets, with fixed labeled vertices, and the theorem is restricted to deleting an actual matching from a complete bipartite graph; arbitrary sparse bipartite graphs can admit larger non-star packings. The literature comparison is not a proof of global priority; unindexed independent derivations remain possible. The proof is self-contained; finite enumeration is only a corroboration.

## References
1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, Proposition 2.3; DOI `10.1051/ro/2022171`, first published online 1 November 2022.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv `2403.00750v1` (1 March 2024), Theorem 4.2; primary MSC2020 `05C70`.
3. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv `2406.04020v2` (2024), Section 4.
4. D. M. Cardoso, J. O. Cerdeira, C. Dominic, and J. P. Cruz, *Injective Edge Coloring of Graphs*, Filomat 33 (2019), 6411–6423, Propositions 2.1–2.2.
