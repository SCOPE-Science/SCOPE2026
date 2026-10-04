# All k-Steiner general position sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), \(N=\sum_i n_i\), and fix \(2\le k\le N-1\). For \(A\subseteq V(G)\), write \(a_i=|A\cap X_i|\), where \(X_i\) is the \(i\)-th part. Then \(A\) is a \(k\)-Steiner general position set if and only if either \(A\subseteq X_i\) for some \(i\), or \(a_i\le k-1\) for every \(i\). Consequently, with \(c_i=\min\{n_i,k-1\}\), the exact size enumerator is \[\Phi_{k,G}(z)=\prod_{i=1}^r\left(\sum_{j=0}^{c_i}\binom{n_i}{j}z^j\right)+\sum_{i=1}^r\sum_{j=k}^{n_i}\binom{n_i}{j}z^j.\] In particular, if \(M=\max_i n_i\) and \(S_k=\sum_i c_i\), then \(\operatorname{sgp}_k(G)=\max\{M,S_k\}\). If \(L=|\{i:n_i=M\}|\) and \(C_k=\prod_i\binom{n_i}{c_i}\), the number of maximum \(k\)-Steiner general position sets is \(L\) when \(M>S_k\), \(C_k\) when \(M<S_k\), and \(L+C_k\) when \(M=S_k\).

## Assumptions and scope
All graphs are finite and simple. Let \\(G=K_{n_1,\\ldots,n_r}\\) have partite sets \\(X_1,\\ldots,X_r\\), with \\(r\\ge2\\), every \\(n_i\\ge1\\), and \\(N=\\sum_i n_i\\). Fix an integer \\(k\\) with \\(2\\le k\\le N-1\\). A set \\(A\\subseteq V(G)\\) is a \\(k\\)-Steiner general position set when, for every \\(k\\)-subset \\(B\\subseteq A\\) and every minimum Steiner tree \\(T_B\\) connecting \\(B\\), one has \\(V(T_B)\\cap A=B\\).

The polynomial \\(\\Phi_{k,G}(z)\\) used here is simply the size enumerator of all \\(k\\)-Steiner general position sets; no claim is made that this notation is standard.

## Proof
Put \\(a_i=|A\\cap X_i|\\).

Suppose first that \\(A\\) is not contained in one part and that \\(a_i\\ge k\\) for some \\(i\\). Choose a \\(k\\)-set \\(B\\subseteq A\\cap X_i\\) and a vertex \\(y\\in A\\setminus X_i\\). The vertices of \\(B\\) are pairwise nonadjacent, so every connected subgraph containing \\(B\\) needs at least one additional vertex and therefore any Steiner \\(B\\)-tree has at least \\(k\\) edges. The star with center \\(y\\) and leaves \\(B\\) has exactly \\(k\\) edges, hence is a minimum Steiner \\(B\\)-tree. It contains \\(y\\in A\\setminus B\\), so \\(A\\) is not a \\(k\\)-Steiner general position set. This proves necessity of the stated dichotomy.

Conversely, assume first that \\(A\\subseteq X_i\\). For any \\(k\\)-set \\(B\\subseteq A\\), a minimum Steiner \\(B\\)-tree has exactly \\(k\\) edges and exactly one vertex outside \\(B\\): one outside-part center is necessary and sufficient. Hence its unique nonterminal vertex lies outside \\(X_i\\), so it does not belong to \\(A\\). Thus \\(V(T_B)\\cap A=B\\).

Now assume instead that \\(a_i\\le k-1\\) for every \\(i\\). Every \\(k\\)-subset \\(B\\subseteq A\\) then meets at least two parts. Consequently \\(G[B]\\) is connected, so a spanning tree of \\(G[B]\\) has \\(k-1\\) edges. No tree connecting \\(k\\) prescribed terminals can use fewer than \\(k-1\\) edges. Therefore every Steiner \\(B\\)-tree has exactly the \\(k\\) vertices of \\(B\\), and again \\(V(T_B)\\cap A=B\\). This proves the characterization.

For counting, the family with \\(a_i\\le k-1\\) for all \\(i\\) contributes
\\[
\\prod_{i=1}^r\\left(\\sum_{j=0}^{c_i}\\binom{n_i}{j}z^j\\right),
\\qquad c_i=\\min\\{n_i,k-1\\}.
\\]
The only additional sets are one-part sets of cardinality at least \\(k\\), contributing
\\[
\\sum_{i=1}^r\\sum_{j=k}^{n_i}\\binom{n_i}{j}z^j.
\\]
These two families are disjoint, giving the displayed enumerator.

The largest capped-profile set has size \\(S_k=\\sum_i c_i\\), and the largest one-part set has size \\(M=\\max_i n_i\\), so \\(\\operatorname{sgp}_k(G)=\\max\\{M,S_k\\}\\). Capped-profile sets of size \\(S_k\\) must choose exactly \\(c_i\\) vertices from each part, giving \\(C_k=\\prod_i\\binom{n_i}{c_i}\\) such sets. One-part sets of size \\(M\\) are exactly the full largest parts, giving \\(L\\) such sets. If \\(M=S_k\\), then necessarily \\(M\\ge k\\), so the two maximum-set families are disjoint and their counts add.

## Verification
The included `verify.py` constructs every complete multipartite graph of order at most eight from its adjacency relation. For every admissible \\(k\\), it enumerates every candidate set \\(A\\), computes minimum Steiner-tree sizes by exhaustive connected-superset search, tests whether an additional selected vertex occurs in any minimum Steiner tree, and compares the result with the structural criterion. It also compares the observed size distribution with the closed enumerator. The recorded run checks 264 graph-parameter instances and 44,496 candidate sets without mismatch.

## Relationship to prior work
Klavžar, Kuziak, Peterin, and Yero introduced \\(k\\)-Steiner general position in 2021. Their join theorem expresses \\(\\operatorname{sgp}_k(G\\vee H)\\) through auxiliary invariants, and Corollary 4.4 gives an explicit formula for complete bipartite graphs. The present theorem does not claim novelty for that bipartite maximum-value specialization. Instead, it gives a direct all-set characterization for arbitrary complete multipartite graphs, an exact size enumerator, a uniform maximum formula, and the exact number of maximum sets.

The 2026 general-position survey restates the tree, cycle, join, and complete-bipartite Steiner results, but its Steiner-general-position section does not state an arbitrary complete-multipartite classification. Exact and semantic searches using “Steiner general position complete multipartite,” “k-Steiner general position complete multipartite,” and “Steiner general position polynomial complete multipartite” did not locate an equivalent all-set theorem.

For \\(k=2\\), the characterization reduces to the well-known description of ordinary general-position sets in complete multipartite graphs: a set lies in one part or contains at most one vertex from each part. Thus the new uniform statement is consistent with the classical boundary case.

## Limitations
The theorem is specific to complete multipartite graphs. The size enumerator is introduced only as a convenient count and is not asserted to be a previously standardized invariant. The finite exhaustive computation is corroborative and does not replace the all-orders proof. Search coverage cannot exclude differently phrased or non-indexed prior work, and the complete-bipartite maximum-value case is already covered by the 2021 source.

## References
1. S. Klavžar, D. Kuziak, I. Peterin, I. G. Yero, “A Steiner general position problem in graph theory,” arXiv:2105.08391v1 (18 May 2021); Computational and Applied Mathematics 40 (2021), Article 223, DOI 10.1007/s40314-021-01619-y.
2. U. Chandran S. V., S. Klavžar, J. Tuite, “The General Position Problem: A Survey,” arXiv:2501.19385v5 (2026), Section 3.7.

