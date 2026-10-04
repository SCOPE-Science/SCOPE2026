# Packing-total criticality of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\). Then \(G\) is packing-total chromatic critical—meaning \(\chi_\rho^{\prime\prime}(H)<\chi_\rho^{\prime\prime}(G)\) for every proper subgraph \(H\subsetneq G\)—if and only if \(G\not\cong K_{n,1,1}\) for every integer \(n\ge2\). For the exceptional family, if \(e\) is the edge joining the two singleton parts, then \(G-e\cong K_{n,2}\) and \(\chi_\rho^{\prime\prime}(G-e)=\chi_\rho^{\prime\prime}(G)=2n+3\).

An auxiliary exact value used in the proof is the following. Write the part sizes in nonincreasing order as \(n_1\ge n_2\ge\cdots\ge n_r\), put \(N=\sum_i n_i\), \(S=N-n_1\), and let \(m=|E(G)|\). Then
\[
\chi_\rho^{\prime\prime}(G)=m+1+\max\left\{n_2,\left\lceil\frac{S}{2}\right\rceil\right\}.
\]
The criticality classification is the finding; the numerical identity is used as a supporting lemma and is not asserted here to be new independently of earlier work on total independence and edge domination.

## Assumptions and scope
Graphs are finite, simple, and undirected. A packing total coloring assigns a positive integer color to every element of \(V(G)\cup E(G)\), and two distinct elements with color \(i\) must be at distance greater than \(i\). Equivalently, it is a packing coloring of the total graph \(T(G)\). The packing total chromatic number is denoted by \(\chi_\rho^{\prime\prime}(G)\).

A graph is packing-total chromatic critical when every proper subgraph has strictly smaller packing total chromatic number. The theorem concerns connected complete multipartite graphs with at least two parts. The one-edge graph \(K_2\) is included and is critical.

## Proof
For a connected complete multipartite graph \(G\), every two elements of \(V(G)\cup E(G)\) are at distance at most two. Indeed, two vertices in different parts are adjacent and two vertices in one part have a common neighbor; a vertex and a nonincident edge have an endpoint in a different part from the vertex; and two disjoint edges have endpoints in different parts. Hence \(\operatorname{diam}T(G)\le2\). It follows that every color greater than \(1\) is used at most once, so
\[
\chi_\rho^{\prime\prime}(G)=|V(G)|+|E(G)|-\alpha(T(G))+1.
\]

We next describe \(\alpha(T(G))\). An independent set of \(T(G)\) is a total independent set in \(G\): its selected graph vertices lie in a single part, its selected graph edges form a matching, and no selected edge is incident with a selected vertex. If its selected vertices lie in a part \(P\), then replacing every selected matching edge incident with an unselected vertex of \(P\) by that unselected vertex never decreases the size, because a matching uses each such vertex at most once. Thus some maximum total independent set has the form
\[
P\;\cup\;M,
\]
where all vertices of \(P\) are selected and \(M\) is a maximum matching of \(G-P\). Therefore
\[
\alpha(T(G))=\max_P\bigl(|P|+\nu(G-P)\bigr).
\]

A largest part \(V_1\) attains this maximum. To see this, let \(P\) have size \(p\le n_1\), and let \(M\) be a maximum matching of \(G-P\). If \(P\ne V_1\), let \(k\) be the number of edges of \(M\) incident with \(V_1\). Delete those \(k\) edges. In \(G-V_1\), restore \(\min\{k,p\}\) edges by joining distinct vertices of \(P\) to distinct other endpoints of the deleted edges. This gives a matching of size at least \( |M|-(n_1-p)\), because \(k\le n_1\). Hence
\[
n_1+\nu(G-V_1)\ge p+\nu(G-P).
\]
For the complete multipartite graph \(G-V_1\), which has order \(S\) and largest part \(n_2\),
\[
\nu(G-V_1)=\min\left\{\left\lfloor\frac S2\right\rfloor,S-n_2\right\}.
\]
The first bound is the endpoint bound, the second follows because every matching edge uses a vertex outside a largest part, and both are attained by pairing across parts. Substitution gives the displayed formula for \(\chi_\rho^{\prime\prime}(G)\).

Now fix an edge \(e\) of \(G\). If one endpoint of \(e\) lies in a largest part \(V_1\), then a maximum total independent set consisting of all of \(V_1\) together with a maximum matching of \(G-V_1\) automatically avoids the edge-element \(e\).

Suppose instead that neither endpoint part of \(e\) is largest, and put \(J=G-V_1\). If \(J\) has at least three vertices, then \(J\) has a maximum matching avoiding the prescribed edge \(e\). If an endpoint part of \(e\) has another vertex, swap that endpoint with its twin in any maximum matching containing \(e\). If both endpoint parts are singleton parts and a third singleton part exists, swap one endpoint with that third singleton. In the remaining case, every other part has size at least two. Then a maximum matching containing \(e\) has size at least two; replacing \(e=uv\) and another matching edge \(xy\) by \(ux\) and \(vy\) preserves the matching size and avoids \(e\). Thus the only case in which the matching argument can force \(e\) is \(J\cong K_2\), which is exactly \(G\cong K_{n,1,1}\) with \(n\ge2\) and \(e\) joining the singleton parts.

Outside that exceptional case, choose a maximum independent set of \(T(G)\) avoiding the edge-element \(e\), color that set with \(1\), and give every other element a distinct color. The edge-element \(e\) therefore has a unique color. After deleting \(e\) from \(G\), all remaining element-distances can only stay the same or increase, so restricting the coloring and then lowering unused color labels gives a packing total coloring of \(G-e\) with one fewer color. Hence
\[
\chi_\rho^{\prime\prime}(G-e)<\chi_\rho^{\prime\prime}(G)
\]
for every edge \(e\) unless \(G\cong K_{n,1,1}\) and \(e\) joins its singleton parts.

Because a connected complete multipartite graph has no isolated vertices, strict decrease under every single edge deletion implies strict decrease for every proper subgraph: any proper subgraph is contained in \(G-e\) for some edge \(e\) absent from that subgraph, and packing total chromatic number is monotone under taking subgraphs.

Finally let \(G=K_{n,1,1}\) with \(n\ge2\), and let \(e\) join the singleton parts. Then \(G-e\cong K_{n,2}\). The total graph of \(G\) has \(3n+3\) vertices and independence number \(n+1\), while the total graph of \(K_{n,2}\) has \(3n+2\) vertices and independence number \(n\). Both total graphs have diameter two, so
\[
\chi_\rho^{\prime\prime}(G)=3n+3-(n+1)+1=2n+3
\]
and
\[
\chi_\rho^{\prime\prime}(G-e)=3n+2-n+1=2n+3.
\]
Thus these and only these complete multipartite graphs fail criticality.

## Verification
The accompanying `verify.py` reconstructs each complete multipartite graph, its total graph, all total-graph distances, and the packing total chromatic number from the definitions for every multipartite isomorphism type of order at most \(8\). For edge-deleted instances, each connected total-graph component has diameter at most three in the tested range; the checker therefore enumerates every admissible color-2 packing and computes the largest compatible color-1 independent set by an exact recursive maximum-independent-set solver. It does not use the criticality classification to decide the optimum.

The replay result is:

`ALL CHECKS PASSED; multipartite_types=58; edge_deletions=813; max_order=8; exceptional_equalities=5`

The five equalities are exactly the singleton-part edge deletions in \(K_{n,1,1}\) for \(2\le n\le6\). This finite computation is a stress test only; the theorem above is proved for all admissible part sizes.

## Relationship to prior work
Ferme and Mesarič Štesl introduced packing total coloring in arXiv:2508.08691. Their full preprint proves the equivalence with packing coloring of the total graph and the hereditary property, and its open-problem section explicitly introduces packing-total chromatic critical graphs and states that they had not yet been studied. The same section asks for identification of graphs in this class. The present theorem gives a complete answer inside the broad complete-multipartite family.

Ferme, Hedžet, Melicharová, and Mesarič Štesl subsequently introduced \(S\)-packing total coloring in arXiv:2609.10107. Its publicly available abstract states results for complete bipartite graphs, paths, and cycles; it does not state a critical-graph classification or a complete-multipartite theorem. The full text was not available through the accessible primary/open route used for this comparison, so this source remains a residual overlap risk rather than being treated as whole-document negative evidence.

Brešar and Ferme, arXiv:1904.10212, classify ordinary packing-chromatic critical graphs of diameter two. That result concerns \(\chi_\rho(G)\) under deletion inside \(G\). Packing-total criticality concerns \(\chi_\rho(T(G))\) while deleting an underlying edge changes the total graph by removing the edge-element and also changing adjacencies and distances among surviving elements. Their theorem therefore does not imply the classification above.

Stanton's arXiv:2206.04395 studies total independent sets, and Song, Miao, Wang, and Zhao determine edge-domination parameters of complete multipartite graphs (DOI:10.1080/00207160.2013.818668). Those works can account for the auxiliary total-independence value used in the numerical formula, but they do not study packing-total criticality. Accordingly, novelty is claimed for the criticality classification, not for the auxiliary numerical identity in isolation.

## Limitations
The theorem is restricted to finite connected complete multipartite graphs. It does not classify packing-total critical graphs outside this family, and it does not address criticality for arbitrary \(S\)-packing total colorings. The full text of arXiv:2609.10107 was not available in the accessible route used here; its abstract was checked and does not state the present result, but an unobserved full-text discussion remains a residual literature risk.

## References
1. J. Ferme and D. Mesarič Štesl, *On packing total coloring*, arXiv:2508.08691, first public 12 August 2025.
2. J. Ferme, J. Hedžet, P. Melicharová, and D. Mesarič Štesl, *On \(S\)-packing total colorings*, arXiv:2609.10107, 2026.
3. B. Brešar and J. Ferme, *Graphs that are critical for the packing chromatic number*, arXiv:1904.10212; Discussiones Mathematicae Graph Theory 42 (2022), 569–589.
4. L. Stanton, *Structure of a Maximal Total Independent Set*, arXiv:2206.04395.
5. W. Song, L. Miao, H. Wang, and Y. Zhao, *Maximal matching and edge domination in complete multipartite graphs*, International Journal of Computer Mathematics 91 (2014), 857–862, DOI:10.1080/00207160.2013.818668.
