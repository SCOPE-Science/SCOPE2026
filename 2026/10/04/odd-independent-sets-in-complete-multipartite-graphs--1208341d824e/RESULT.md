# Odd independent sets in complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), and let \(M=\max_i n_i\). The odd independent sets of \(G\) are exactly the empty set and the odd-cardinality subsets contained in a single part. Consequently, if \(I_{\mathrm{od}}(G;x)=\sum_S x^{|S|}\) ranges over odd independent sets, then \(I_{\mathrm{od}}(G;x)=1+\frac12\sum_{i=1}^r((1+x)^{n_i}-(1-x)^{n_i})\), and \(\alpha_{\mathrm{od}}(G)=M\) for odd \(M\) while \(\alpha_{\mathrm{od}}(G)=M-1\) for even \(M\). In particular, within complete multipartite graphs, \(\alpha_{\mathrm{od}}(G)=\alpha(G)\) if and only if the largest part size is odd.

## Assumptions and scope
All graphs are finite, simple, and undirected. Write \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) and partite sets \(V_1,\ldots,V_r\), where \(|V_i|=n_i\ge1\). Following Caro, Petruševski, Škrekovski, and Tuza, an odd independent set \(S\) is an independent set such that for every \(v\notin S\), either \(N(v)\cap S=\varnothing\) or \(|N(v)\cap S|\) is odd. The empty set is included. The polynomial \(I_{\mathrm{od}}(G;x)\) in the finding counts all such sets by cardinality.

## Proof
Every nonempty independent set of a complete multipartite graph is contained in a unique part, say \(S\subseteq V_i\), because vertices in distinct parts are adjacent. For a vertex \(v\in V_i\setminus S\), there are no edges from \(v\) to \(S\), hence \(N(v)\cap S=\varnothing\). For every vertex \(v\in V_j\) with \(j\ne i\), all vertices of \(S\) are adjacent to \(v\), so \(|N(v)\cap S|=|S|\). Since \(r\ge2\), at least one such outside part exists. Therefore a nonempty independent set is odd independent if and only if its cardinality is odd. This proves the structural classification.

For every odd integer \(k\ge1\), the number of odd independent sets of size \(k\) is therefore \(\sum_i\binom{n_i}{k}\), and there are no positive even-sized odd independent sets. Using the odd part of the binomial expansion gives
\[
I_{\mathrm{od}}(G;x)=1+\sum_{i=1}^r\sum_{k\ge1,\ k\text{ odd}}\binom{n_i}{k}x^k
=1+\frac12\sum_{i=1}^r\left((1+x)^{n_i}-(1-x)^{n_i}\right).
\]
The maximum possible cardinality is the largest odd integer not exceeding \(M=\max_i n_i\), hence it equals \(M\) when \(M\) is odd and \(M-1\) when \(M\) is even. Ordinary independence in a complete multipartite graph has value \(\alpha(G)=M\), so equality \(\alpha_{\mathrm{od}}(G)=\alpha(G)\) holds exactly when \(M\) is odd.

## Verification
The accompanying verifier enumerates every vertex subset of every complete-multipartite isomorphism type with at least two parts through order \(11\). It checks the defining odd-independence condition directly from the adjacency matrix, compares the entire cardinality distribution with the closed polynomial coefficients, and compares the maximum size with the stated formula. The replay covers \(183\) multipartite types and \(177556\) subsets and returns `ALL CHECKS PASSED`. This finite computation is a stress test only; the universal theorem is proved above.

## Relationship to prior work
Caro, Petruševski, Škrekovski, and Tuza introduced the odd independence number and asked for structural understanding of when \(\alpha_{\mathrm{od}}(G)=\alpha(G)\). Their paper treats many classical classes and proves, among other things, a general statement for bipartite graphs whose degrees are all odd and an exact equality result for odd-regular bipartite graphs. The inspected full text contains no occurrence of “multipartite” and does not state the classification above. The present theorem gives the complete answer to their equality question inside the broad class of complete multipartite graphs, including all irregular complete bipartite graphs.

Targeted searches for “odd independence number” together with complete multipartite, complete bipartite, and equivalent odd-independent-set terminology found no prior formula matching the structural classification or enumerator. A semantic research-index search likewise returned no covering record; the closest complete-multipartite hit concerns the different invariant of odd chromatic number.

## Limitations
The proof relies essentially on the fact that every independent set in a complete multipartite graph lies inside one part. It does not directly extend to graphs obtained by deleting cross-part edges. The originality assessment is based on the inspected primary paper and targeted literature/index searches; older work using different terminology for this recently named invariant remains a residual literature risk.

## References
1. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “The odd independence number of graphs, I: Foundations and classical classes,” arXiv:2509.20763v1, first submitted 25 September 2025. Primary MSC: 05C15; additional MSC: 05C69, 05C76.
