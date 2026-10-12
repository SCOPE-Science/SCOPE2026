# All monophonic position sets of half graphs
## Finding
Let \(H_n\), \(n\ge2\), have bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with
\[
a_i b_j\in E(H_n)\iff i\le j.
\]
Then \(S\subseteq V(H_n)\) is in monophonic position exactly when \(|S|\le2\) or \(S\) is independent. For \(|S|\ge3\), if both sides are represented, this is equivalent to
\[
\max\{j:b_j\in S\}<\min\{i:a_i\in S\}.
\]
Consequently the complete cardinality enumerator is
\[
\mathcal P_n(z)=1+2nz+\binom{2n}{2}z^2+\sum_{k=3}^{n}(k+1)\binom{n}{k}z^k.
\]
Thus \(\operatorname{mp}(H_n)=n\). For \(n\ge3\), the \(n+1\) maximum sets are
\[
\{b_1,\ldots,b_t\}\cup\{a_{t+1},\ldots,a_n\},\qquad 0\le t\le n.
\]
For \(n=2\), all six two-vertex sets are maximum.

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A monophonic position set meets every induced path in at most two vertices. The half graph is the canonical twin-free chain graph.

## Proof
Every set of size at most two is admissible.

The half graph is \(2K_2\)-free. Any induced path on at least five vertices contains an induced \(2K_2\), using its first and last edges. Hence every induced path of \(H_n\) has at most four vertices. An independent subset of such a path has size at most two, so every independent set is in monophonic position.

Conversely, let \(|S|\ge3\) and suppose \(S\) contains an edge \(a_i b_j\), so \(i\le j\). Choose a third vertex. If it is \(a_k\), then for \(k\le j\) the path \(a_k-b_j-a_i\) is induced, while for \(k>j\) the path \(a_k-b_k-a_i-b_j\) is induced. If the third vertex is \(b_\ell\), then for \(i\le\ell\) use \(b_\ell-a_i-b_j\), while for \(\ell<i\) use \(b_\ell-a_\ell-b_j-a_i\). Thus every non-independent set of size at least three fails.

For \(k\ge3\), admissible sets are independent. Fix \(r\), the number selected from \(B\). Choose indices \(t_1<\cdots<t_k\) in \([n]\). There is exactly one independent set with these indices and this value of \(r\):
\[
\{b_{t_1},\ldots,b_{t_r}\}\cup\{a_{t_{r+1}},\ldots,a_{t_k}\}.
\]
Hence for each \(r=0,\ldots,k\) there are \(\binom nk\) sets, giving \((k+1)\binom nk\). Sizes zero, one, and two contribute \(1\), \(2n\), and \(\binom{2n}{2}\). The maximum-set statement follows by setting \(k=n\), with the separate \(n=2\) boundary.

## Verification
The included checker constructs \(H_n\) for \(2\le n\le8\), enumerates induced paths directly, and exhaustively tests every vertex subset against the definition. It compares the result with the structural criterion, every polynomial coefficient, and the maximum-set classification. It checks \(87{,}376\) subsets and \(1{,}001\) induced paths.

## Relationship to prior work
Monophonic position was introduced in 2020. The defining paper proves a triangle-free upper bound and exact results for several families, including unicyclic graphs, complements of bipartite graphs, joins, coronas, and split graphs. Its inspected searchable text contains no half-graph or chain-graph treatment.

The scalar equality \(\operatorname{mp}(H_n)=n\) lies close to the published triangle-free theory and is not the originality basis. The new content is the exact classification of every admissible subset, the full cardinality enumerator, and the complete maximum-set description. Targeted searches under half graph, chain graph, Ferrers graph, and induced-path terminology did not locate an equivalent theorem.

## Limitations
The theorem does not classify arbitrary chain graphs with repeated twin classes. The finite computation is corroborative only; the all-\(n\) result follows from the structural proof. A differently phrased or non-indexed chain-graph result may exist.

## References
1. E. J. Thomas, S. V. Ullas Chandran, J. Tuite, G. Di Stefano, “On monophonic position sets in graphs,” arXiv:2012.10330v1, 18 December 2020; DOI 10.1016/j.dam.2023.02.021.
