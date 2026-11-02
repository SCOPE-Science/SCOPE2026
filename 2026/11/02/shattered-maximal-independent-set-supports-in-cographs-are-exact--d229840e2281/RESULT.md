# Shattered maximal-independent-set supports in cographs are exactly induced-matching transversals

## Finding

**Theorem.** Let \(G\) be any finite simple undirected \(P_4\)-free graph (a cograph), and let \(\mathcal M(G)\) be the family of inclusion-maximal independent subsets of its vertex set. A set of query vertices \(S\subseteq V(G)\) is **shattered**, meaning \(\{I\cap S:I\in\mathcal M(G)\}=2^S\), if and only if \(S\) can be obtained by choosing one endpoint from each edge of an induced matching in \(G\). The matching and set may both be empty. In particular,
\[
\operatorname{VCdim}(\mathcal M(G))=\nu_{\mathrm{ind}}(G).
\]
Here \(\nu_{\mathrm{ind}}(G)\) is the largest number of edges in an induced matching (the graph induced by their endpoints has exactly those edges).

The theorem determines **the entire support family**, not just its maximum size. Write the shattering polynomial as \(\Phi_G(z)=\sum_{S\text{ shattered}}z^{|S|}\), and let \(i(G)\) denote the number of isolated vertices. For nonempty cographs \(A,B\), the exact cotree recurrences are
\[
\begin{aligned}
\Phi_{K_1}(z)&=1,\\
\Phi_{A\sqcup B}(z)&=\Phi_A(z)\Phi_B(z),\\
\Phi_{A\vee B}(z)&=\Phi_A(z)+\Phi_B(z)-1+(i(A)+i(B))z.
\end{aligned}
\]
The empty graph also has polynomial \(1\). Consequently the VC dimension and the complete polynomial are calculable from a union/join decomposition, with at most quadratic arithmetic operations for the polynomial using ordinary coefficient convolution.

**Sharp boundary of the class statement.** There is no graph on at most four vertices with \(\operatorname{VCdim}(\mathcal M(G))>\nu_{\mathrm{ind}}(G)\). Exactly three five-vertex graph isomorphism types have a strict inequality: the five-cycle, the house (a four-cycle with a fifth vertex adjacent to two consecutive cycle vertices), and the gem (the complete join of one vertex with a four-vertex path). All three have \(\operatorname{VCdim}=2\) and \(\nu_{\mathrm{ind}}=1\). They occur in respectively \(12,60,60\) of the \(1024\) labeled five-vertex graphs. In particular, the gem is chordal, so the identity does not extend to every chordal graph.

## Assumptions and scope

All graphs are finite, simple, undirected; a maximal independent set is inclusion-maximal, not necessarily maximum-cardinality. A singleton query \(v\) is shattered exactly when some maximal independent set contains \(v\) and some does not; equivalently \(v\) has a neighbor. A cograph is constructed from isolated vertices using disjoint union \(\sqcup\) and complete join \(\vee\), where all cross edges are present. The induced matching definition forbids **all** additional edges between endpoints of distinct matching edges, including edges joining two endpoints on the same chosen side.

## Proof

**Lemma 1 (matching transversals always shatter).** Suppose a graph contains an induced matching with edges \(s_it_i\), with no edge among any pair of distinct selected endpoints except each paired edge. Given any Boolean labeling of \(S=\{s_i\}\), choose \(s_i\) for a positive label and \(t_i\) for a negative label. The chosen vertices form an independent set. Extend it greedily to a maximal independent set \(I\). Every negative \(s_i\) is excluded because its adjacent mate \(t_i\) already belongs to \(I\); every positive \(s_i\) is included. Hence \(I\cap S\) realizes the prescribed labeling. The empty matching represents the empty query set.

**Lemma 2 (the missing-empty-pattern property for cographs).** Let \(G\) be a cograph and \(S\subseteq V(G)\) have at least two elements. If maximal independent sets realize every *nonempty* subset of \(S\) as a trace, they also realize the empty subset.

Induct on a cograph decomposition. For a disjoint union \(G=A\sqcup B\), every maximal independent set is \(I_A\cup I_B\) with each \(I_A,I_B\) maximal in its factor. If \(S\) lies entirely in one factor, use the induction hypothesis there and choose any maximal independent set in the other factor. If it meets both factors, pick a positive query vertex in the other factor to realize each possible local trace, including the empty local trace, and then combine the two empty local traces. If \(G=A\vee B\), every maximal independent set is wholly in exactly one factor and maximal there. If \(S\) meets both, the all-positive trace is impossible, so the premise cannot hold. If \(S\) lies entirely in one factor, each nonempty trace must be realized by maximal independent sets of that factor; by induction they also realize the empty trace. This proves the lemma. The singleton and empty bases have no qualifying \(S\).

**Lemma 3 (support characterization).** Induct on cograph construction. For a disjoint union, maximal-independent-set traces form a Cartesian product. Thus \(S\) is shattered precisely when each \(S\cap V(A)\) and \(S\cap V(B)\) is shattered in its factor. By induction their induced matchings combine without cross edges.

For a nonempty join \(G=A\vee B\), a shattered set \(S\) cannot meet both factors because its all-positive trace would then be impossible. If \(|S|\ge2\) and \(S\) is wholly in \(A\), all its nonempty traces must come from the \(A\) factor; Lemma 2 supplies the empty trace in \(A\). By induction \(S\) is an induced-matching transversal in \(A\), and this matching remains induced in the join. The same argument holds for \(B\). If \(|S|=1\), the lone vertex can be paired with any vertex of the opposite nonempty factor, making a one-edge induced matching. The empty set uses the empty matching. Lemma 1 proves every such transversal is shattered, completing the equivalence.

**Polynomial identities.** For a union, shattered supports are independent choices in the two factors, giving the product. For a join, the supports of size at least two belong wholly to one factor and are exactly the shattered supports from that factor. Every one-vertex subset of the join is shattered, because each vertex has a cross-factor neighbor, whereas isolated vertices in a factor were not previously shattered. Both factors contribute the empty support but the join only once. Therefore \(\Phi_{A\vee B}=\Phi_A+\Phi_B-1+(i(A)+i(B))z\). The leading nonzero degree gives the induced matching number and VC dimension. The stated complexity follows by processing a cotree, maintaining coefficient arrays and isolated-vertex counts; at most \(O(|V|^2)\) coefficient-pair multiplications occur over the full decomposition (even a naive quadratic bound per multiply gives an elementary polynomial-time algorithm).

**Smallest failure outside cographs.** The separate standalone verifier enumerates every simple labeled graph of orders zero through five, computes all maximal independent sets, determines every shattered query support and every induced-matching transversal, and classifies the exceptional five-vertex types under all vertex permutations. Exhaustive certificates establish that orders at most four have no gap and exactly the three stated five-vertex types have \(\operatorname{VCdim}=2>1=\nu_{\mathrm{ind}}\). This finite boundary is independent of the all-order induction.

## Verification

Run `python3 verify_cograph.py` using Python's standard library. The verifier checks every labeled simple graph on at most five vertices, independently computes maximal independent sets and all trace patterns, exhaustively enumerates induced matchings and orientations, checks the cotree polynomial recurrence for every small cograph, and classifies the complete five-vertex obstruction census. Expected success markers: `COGRAPH_COMPLETE_SMALL_GRAPH_CENSUS_PASS`, `INDUCED_MATCHING_SUPPORTS_AND_POLYNOMIALS_PASS`, `SMALLEST_FIVE_VERTEX_GAP_PASS`. Finite enumeration checks the small-domain consequences only; the universal theorem is proved by the preceding induction.

## Relationship to prior work

Liu, Shangguan, Skokan and Xu (2024, Lemma 27) prove a general bound for the VC dimension of maximal independent sets by a **bipartite induced matching number**. Their bipartite matching condition is weaker than the ordinary induced matching used here; their inequality therefore does not imply this theorem. For example the four-cycle has two crossing matching edges satisfying the bipartite condition, but no two-edge ordinary induced matching, while its maximal-independent-set VC dimension is one. Kahn and Park (2020) study maximal-independent-set counts and induced matchings, without the present shattering-support characterization. Bhaskar (2017) and Walker (2022) provide general static and adaptive shattering frameworks rather than this exact cograph classification. The decomposition proof uses the standard \(P_4\)-free characterization of cographs.

## Limitations

No formula is claimed for arbitrary non-cographs, and the theorem concerns **maximal independent sets**, not independent sets of all sizes or maximal cliques. The polynomial counts distinct shattered *query supports*, not the number of distinct maximal independent sets or their traces with multiplicity. The finite five-vertex census is exhaustive only through five vertices. The present literature comparison does not establish absolute historical priority, and there has been no independent mathematical audit.

## References

- Siddharth Bhaskar, *Thicket Density* (2017), arXiv:1702.03956, first publicly posted 2017-02-13.
- Hong Liu, Chong Shangguan, Jozef Skokan and Zixuan Xu, *Beyond Chromatic Threshold via (p,q)-Theorem, and Blow-Up Phenomenon* (2024), arXiv:2403.17910, in particular Lemma 27, first publicly posted 2024-03-26.
- Jeff Kahn and Jinyoung Park, *Stability for Maximal Independent Sets* (2020), DOI:10.37236/8530.
- Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy* (2022), arXiv:2203.12211.
