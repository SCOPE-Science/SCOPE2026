# Minimum-sum vertex cover on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge 2\) and
\[
1\le n_1\le\cdots\le n_r.
\]
Write \(N=\sum_{i=1}^r n_i\), \(S_i=\sum_{j=1}^i n_j\), and \(S_0=0\). For a vertex ordering \(\sigma\), the cover time of an edge is the smaller of the positions of its endpoints, and \(\operatorname{msvc}(G)\) is the minimum total cover time over all orderings. Then
\[
\operatorname{msvc}(G)=\sum_{i=1}^{r-1}(N-S_i)\,\frac{n_i(2S_{i-1}+n_i+1)}{2}.
\]
In particular, an optimal ordering is obtained by taking the multipartition classes as contiguous blocks in nondecreasing order of their sizes. Equal-sized blocks may be permuted, and vertices within a block may be permuted.

For example,
\[
\operatorname{msvc}(K_{1,2,4})=26.
\]
For \(r=2\), the formula becomes
\[
\operatorname{msvc}(K_{a,b})=\frac{ba(a+1)}{2}\qquad(a\le b),
\]
recovering the previously known complete-bipartite formula.

## Assumptions and scope
Graphs are finite and simple. The multipartition has at least two nonempty classes, so the graph is connected. Positions in an ordering are numbered starting at \(1\). The result is an exact statement for complete multipartite graphs only; it does not claim an exact formula for arbitrary cographs, perfect graphs, or general graphs.

## Proof
For an ordering \(\sigma=(v_1,\ldots,v_N)\), let \(G_k\) be the subgraph induced by the vertices remaining after the first \(k\) positions have been removed, with \(G_0=G\). Every edge whose cover time is \(t\) remains uncovered after exactly the prefixes of lengths \(0,1,\ldots,t-1\). Therefore
\[
\operatorname{cost}(\sigma)=\sum_{k=0}^{N-1} |E(G_k)|.
\]

Fix a prefix length \(k\). Let \(r_i\) be the number of remaining vertices in part \(i\), and let \(R=N-k=\sum_i r_i\). Since edges join exactly the vertices in distinct parts,
\[
|E(G_k)|=\sum_{i<j}r_ir_j
=\frac12\left(R^2-\sum_{i=1}^r r_i^2\right).
\]
For fixed \(k\), the number \(R\) is fixed, so minimizing the number of uncovered edges is equivalent to maximizing \(\sum_i r_i^2\) subject to
\[
0\le r_i\le n_i,\qquad \sum_i r_i=R.
\]
The maximum is obtained by packing the remaining vertices into the largest-capacity parts first. An elementary two-part operation proves this. If \(i<j\), \(r_i>0\), and \(r_j<n_j\), move as much remaining mass as possible from part \(i\) to part \(j\). If \(r_i+r_j\le n_j\), the pair changes to \((0,r_i+r_j)\) and its squared sum increases by \(2r_ir_j\). If \(r_i+r_j>n_j\), the pair changes to \((r_i+r_j-n_j,n_j)\), and its squared sum changes by
\[
2(n_j-r_i)(n_j-r_j)\ge0,
\]
because \(r_i\le n_i\le n_j\). Repeating the operation yields a maximizer with all smaller parts empty, at most one part partially filled, and all larger parts full.

Thus, for every prefix length \(k\), the least possible number of still-uncovered edges is attained by removing vertices from the parts in nondecreasing order of part size, exhausting each part before proceeding to a larger part. One and the same block ordering attains these termwise minima simultaneously for every \(k\). Summing the termwise lower bounds in the cost identity proves global optimality.

In such an ordering, the vertices of part \(i\) occupy positions \(S_{i-1}+1,\ldots,S_i\). Each of these vertices first covers exactly \(N-S_i\) edges whose other endpoints lie in later blocks. Hence the contribution of part \(i\) is
\[
(N-S_i)\sum_{t=S_{i-1}+1}^{S_i}t
=(N-S_i)\frac{n_i(2S_{i-1}+n_i+1)}{2}.
\]
The last block contributes zero because all edges have already been covered. Summing over \(i=1,\ldots,r-1\) gives the stated formula.

## Verification
The accompanying standard-library program `verify_complete_multipartite_msvc.py` exhaustively checks every integer multipartition of every order from \(2\) through \(8\). For each of the \(58\) multipartite types it enumerates every labeled vertex ordering, directly computes every edge cover time, and compares the exact optimum with the formula. It checks \(925310\) orderings in total. It also checks, in this finite range, that the optimal orderings are exactly the nondecreasing contiguous block orderings and verifies the published complete-bipartite specialization. The saved output is `verification_output.txt` and ends with `ALL CHECKS PASSED`.

The exhaustive computation is a stress test, not the infinite proof; the proof above establishes the formula for every finite choice of part sizes.

## Relationship to prior work
Biniaz, De Carufel, Maheshwari, Odak, and Smid introduced a September 2026 vertex-cover-based treatment of minimum-sum vertex cover, including new approximation and exact algorithms. Its inspected full text discusses previously solved structured graph families and the complete-bipartite exact result, but no complete-multipartite exact formula was located and the text contains no occurrence of “multipartite.”

Gera, Rasmussen, Stănică, and Horton proved in 2006 that for \(a\le b\),
\[
\operatorname{msvc}(K_{a,b})=\frac{ba(a+1)}{2}.
\]
The present theorem strictly extends that two-part formula to an arbitrary number of parts. Targeted searches for the aliases “minimum sum vertex cover,” “min-sum vertex cover,” “complete multipartite,” and “cograph” did not locate a stronger published statement covering the theorem. Search failure is not itself a novelty proof; the strongest directly relevant exact-value paper was inspected at its complete-bipartite theorem.

## Limitations
The argument uses the complete-multipartite structure essentially through the identity for the uncovered induced edge count. No analogous formula is claimed for arbitrary multipartite graphs with missing cross-edges. The finite verifier covers orders through \(8\) only and is not used as evidence for the infinite quantifier. A residual originality risk is unindexed or obscure older work on minimum-sum orderings of cographs or complete multipartite graphs; no such source was located in the targeted searches.

## References
1. A. Biniaz, J.-L. De Carufel, A. Maheshwari, S. Odak, and M. Smid, *Minimum Sum Vertex Cover via Minimum Vertex Cover*, arXiv:2609.27117, first submitted 22 September 2026.
2. R. Gera, C. Rasmussen, P. Stănică, and S. Horton, *Results on the min-sum vertex cover problem*, Congressus Numerantium 178 (2006), 161–172. The paper lists AMS Subject Classification 05C15 and 05C69 and proves the complete-bipartite formula in Corollary 5.3.
