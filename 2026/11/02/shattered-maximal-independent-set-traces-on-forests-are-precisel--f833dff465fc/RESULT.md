# Shattered maximal-independent-set traces on forests are precisely induced-matching sides

## Finding
For any finite simple forest \(F=(V,E)\), let \(\mathcal M(F)\) be the family of inclusion-maximal independent vertex sets. Its Boolean traces on a support \(S\subseteq V\) are all \(2^{|S|}\) labelings precisely when there exists an **induced matching** of \(F\) with exactly one endpoint of each edge in \(S\). The empty support is covered by the empty matching. Thus
\[
\operatorname{VCdim}(\mathcal M(F))=\nu_{\mathrm{ind}}(F)
\]
for every finite forest, where \(\nu_{\mathrm{ind}}\) denotes the maximum cardinality of a set of disjoint edges inducing no additional edges on their endpoints.

The acyclicity hypothesis matters: on the five-cycle, \(S=\{0,2\}\) is shattered by maximal independent sets, but \(\nu_{\mathrm{ind}}=1\). In particular, the theorem is about *all shattered supports*, not merely a numerical upper bound.

## Assumptions and scope
Graphs are finite, simple, and undirected. A forest may be disconnected, edgeless, or empty. A set \(I\) is *maximal independent* when it is independent and every vertex outside \(I\) has a neighbor in \(I\). A support \(S\) is *shattered* if for each \(A\subseteq S\), some maximal independent set satisfies \(I\cap S=A\). An *induced matching* is a collection of edges whose union of endpoints induces exactly those edges. Saying it covers \(S\) on one side means each selected edge has exactly one endpoint in \(S\) and no vertex of \(S\) lies outside those selected endpoints. There is no bound on \(|V|\).

## Proof
**Induced matching implies shattering, in every graph.** Let \(M=\{\{s_i,t_i\}:1\le i\le k\}\) be an induced matching with \(S=\{s_1,\ldots,s_k\}\). Given any requested positive set \(A\subseteq S\), take the independent set comprising \(s_i\) if \(s_i\in A\), and \(t_i\) otherwise. It is independent because the matching is induced. Extend it greedily to a maximal independent set \(I\). A chosen \(t_i\) prevents \(s_i\) from entering \(I\), and a chosen \(s_i\) remains in \(I\). Thus \(I\cap S=A\).

**Shattering implies induced matching in a forest.** Induct on \(|V|\). If \(S=\varnothing\), use the empty matching. Assume \(S\ne\varnothing\). An isolated vertex belongs to every maximal independent set, so no isolated vertex can lie in shattered \(S\); delete isolated vertices outside \(S\) without changing traces. Now choose a leaf \(v\) and its unique neighbor \(u\). Since \(S\) is shattered, its full-positive labeling is realized; hence \(S\) is independent.

**Case 1: \(v\in S\).** To realize any \(A\subseteq S\setminus\{v\}\) with \(v\) negative, maximality forces \(u\) positive because \(v\) is a leaf. Taking \(A=S\setminus\{v\}\) shows that \(u\) has no neighbors in \(S\setminus\{v\}\). Each restricted maximal independent set outside the closed neighborhood \(N[u]\) is maximal independent in the induced residual forest \(F-N[u]\). Therefore \(S\setminus\{v\}\) is shattered in this residual forest. Induct and add the edge \(uv\): \(u\) is nonadjacent to the residual vertices and \(v\), being a leaf, has no other neighbors, so the resulting matching is induced and covers \(S\).

**Case 2: \(v\notin S\), but \(u\in S\).** Fix the positive label at \(u\) and prescribe every possible labeling of \(S\setminus\{u\}\). Since \(S\) is independent, all those other support vertices lie outside \(N[u]\). Restricting the witnessing maximal independent sets containing \(u\) to \(F-N[u]\) shows that \(S\setminus\{u\}\) is shattered there. By induction there is a matching covering the residual support. Adding \(uv\) gives an induced matching: every residual vertex is nonadjacent to \(u\), and \(v\) is a leaf. Its chosen support endpoint is \(u\).

**Case 3: \(v,u\notin S\).** Removing \(v\) does not change the available traces on \(S\). Indeed, from any maximal independent set \(I\) of \(F\), if \(v\notin I\) then \(u\in I\) and \(I\) is already maximal independent in \(F-v\). If \(v\in I\), remove it; if \(u\) is no longer dominated, add \(u\), otherwise do nothing. The result is a maximal independent set of \(F-v\) with the same intersection with \(S\). Hence \(S\) is shattered in \(F-v\). Apply induction; its induced matching remains induced in \(F\), since \(v\) was deleted and cannot create an edge between retained vertices.

These exhaustive cases prove the characterization. Taking maximum support cardinalities gives the displayed VC-dimension identity.

**Sharp obstruction beyond forests.** For the cycle \(C_5\) on vertices \(0,1,2,3,4\) modulo five, the five maximal independent sets are \(\{0,2\},\{0,3\},\{1,3\},\{1,4\},\{2,4\}\). Their traces on \(\{0,2\}\) include all four subsets. The cycle has no two-edge induced matching, so its induced-matching number equals one.

## Verification
The self-contained file `verify_forest_mis.py` independently enumerates all labeled forests on at most six vertices, their maximal independent vertex sets, all trace supports, and all possible oriented induced-matching supports. It compares the two support families exactly and checks the five-cycle counterexample. Its recorded standard output appears in `verification_output.txt`. These finite checks supplement rather than establish the unrestricted induction.

## Relationship to prior work
Kahn and Park (arXiv:1909.04283, initial public version 2019-09-10) connect induced matchings with the abundance of maximal independent sets, rather than identifying all shattered supports. Palmer and Patkós (arXiv:2205.04082) obtain extremal enumerative results involving induced matchings and maximal independent sets. Liu, Shangguan, Skokan, and Xu (arXiv:2403.17910, SoCG 2024, Lemma 27) prove an upper bound on the VC dimension of the maximal-independent-set hypergraph using the **bipartite induced matching number**, which does not require either endpoint class to be independent. The present theorem supplies the stronger exact *ordinary induced-matching* characterization specifically for forests. The older bound does not imply it: on \(P_4\), the bipartite induced-matching number is two, but the actual VC dimension and induced-matching number both equal one.

## Limitations
The statement does not assert this characterization for cyclic graphs; \(C_5\) explicitly refutes that extension. It does not determine the Littlestone dimension, and it does not claim novelty for the classical induced-matching-to-many-maximal-independent-sets construction. The publication-priority comparison is based on identified records and inspected literature and may miss unindexed equivalent formulations. Finite verification covers only the stated orders; the all-orders result relies on the leaf argument.

## References
- J. Kahn and J. Park, *The number of maximal independent sets in the Hamming cube*, arXiv:1909.04283, first version 2019-09-10.
- C. Palmer and B. Patkós, *On the number of maximal independent sets: From Moon-Moser to Hujter-Tuza*, arXiv:2205.04082, first version 2022-05-09.
- H. Liu, C. Shangguan, J. Skokan, and Z. Xu, *Beyond chromatic threshold via the \( (p,q) \)-theorem, and a sharp blow-up phenomenon*, arXiv:2403.17910, first version 2024-03-26, SoCG 2024, Lemma 27, DOI 10.4230/LIPIcs.SoCG.2024.71.
