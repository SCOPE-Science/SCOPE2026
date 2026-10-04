# Exact random-greedy maximal-independent-set law on chain graphs
## Finding
Let \(G\) be a connected chain graph with bipartition \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_n\}\), and canonical nested neighborhoods \(N(a_h)=\{b_1,\ldots,b_{d_h}\}\) with \(1\le d_1\le\cdots\le d_m=n\). Put \(d_0=0\) and \(\mathcal C=\{0,m\}\cup\{i:1\le i<m,\ d_i<d_{i+1}\}\). Then the uniformly random-order greedy maximal-independent-set algorithm has support exactly \(M_i=\{a_1,\ldots,a_i\}\cup\{b_{d_i+1},\ldots,b_n\}\) for \(i\in\mathcal C\). Define \(\Phi\) on a finite nondecreasing sequence of nonnegative integers by deleting zero entries, setting \(\Phi(\varnothing)=1\), and, for positive \(q_1\le\cdots\le q_s=t\), \[\Phi(q_1,\ldots,q_s)=\frac{1}{s+t}\sum_{h=1}^{s}\Phi(q_{h+1}-q_h,\ldots,q_s-q_h).\] For \(i\in\mathcal C\), let \(c_j=|\{h>i:d_h\ge j\}|\) and \(R_i=(c_n,c_{n-1},\ldots,c_{d_i+1})\). Then \[\Pr(\mathbf I=M_i)=\Phi(d_1,\ldots,d_i)\,\Phi(R_i),\] with the empty factor interpreted as \(1\). Consequently \[\mathbb E[x^{|\mathbf I|}]=\sum_{i\in\mathcal C}\Pr(\mathbf I=M_i)x^{i+n-d_i}.\]

This determines the complete finite output distribution of the random-order greedy maximal-independent-set process from the Ferrers degree sequence of the chain graph. The recurrence is exact and terminates because every recursive call removes at least one positive entry and decreases the largest remaining degree.

## Assumptions and scope
The graph is finite, simple, connected, bipartite, and a chain graph. The canonical ordering is chosen so that
\[
N(a_h)=\{b_1,\ldots,b_{d_h}\}
\]
with \(1\le d_1\le\cdots\le d_m=n\). Connectivity excludes isolated vertices and ensures the last degree is \(n\). The random greedy algorithm scans a uniformly random permutation of all vertices and accepts the current vertex exactly when it has no previously accepted neighbor.

The theorem concerns the full law of the greedy output, not merely its expectation. It does not claim a corresponding formula for general bipartite graphs or for quasi-chain graphs.

## Proof
First classify the maximal independent sets. Let \(M\) be maximal independent. If \(a_j\in M\) and \(i<j\), then \(N(a_i)\subseteq N(a_j)\). Every selected vertex of \(B\) is a nonneighbor of \(a_j\), hence also a nonneighbor of \(a_i\). Therefore \(a_i\) can be added unless it already lies in \(M\). Thus \(M\cap A\) is a prefix \(\{a_1,\ldots,a_i\}\). Independence then forces \(M\cap B\subseteq\{b_{d_i+1},\ldots,b_n\}\), and maximality forces equality. If \(0<i<m\) and \(d_i=d_{i+1}\), then \(a_{i+1}\) has no neighbor in this set and could be added, contradicting maximality. Conversely, when \(i=0\), \(i=m\), or \(d_i<d_{i+1}\), every omitted vertex has a neighbor in the displayed set. Hence the maximal independent sets are exactly the \(M_i\) with \(i\in\mathcal C\).

Now use independent continuous priorities, one per vertex, instead of an explicit random permutation. For any fixed maximal independent set \(M\), greedy outputs \(M\) exactly when every vertex outside \(M\) has an earlier-priority neighbor in \(M\). Indeed, all vertices of \(M\) are pairwise nonadjacent, so if each outside vertex is blocked by an earlier member of \(M\), no outside vertex is ever accepted and every vertex of \(M\) is accepted.

Fix \(M_i\). The blocking requirements for vertices \(b_j\) with \(j\le d_i\) involve only
\[
\{a_1,\ldots,a_i\}\cup\{b_1,\ldots,b_{d_i}\},
\]
whereas the blocking requirements for vertices \(a_h\) with \(h>i\) involve only
\[
\{a_{i+1},\ldots,a_m\}\cup\{b_{d_i+1},\ldots,b_n\}.
\]
These two vertex blocks are disjoint, and the induced priority orders on disjoint blocks are independent. Therefore the desired probability factors into a left probability and a right probability.

It remains to compute one generic factor. Consider a chain graph with selected side \(x_1,\ldots,x_s\), opposite side \(y_1,\ldots,y_t\), and
\[
N(x_h)=\{y_1,\ldots,y_{q_h}\},\qquad 0<q_1\le\cdots\le q_s=t.
\]
Let \(\Phi(q_1,\ldots,q_s)\) be the probability that greedy selects every \(x_h\) and no \(y_j\). The earliest vertex among these \(s+t\) active vertices must be some \(x_h\); if a \(y_j\) is earliest, the event fails. If \(x_h\) is earliest, then \(y_1,\ldots,y_{q_h}\) are permanently blocked, while \(x_1,\ldots,x_{h-1}\) have no neighbors among the unblocked opposite vertices and hence become irrelevant guaranteed selections. The remaining active chain graph has degree sequence
\[
(q_{h+1}-q_h,\ldots,q_s-q_h),
\]
after zero entries are discarded. Conditioning on the identity of the earliest active vertex leaves a uniform relative order on the remaining active vertices. Summing over the \(s\) possible earliest selected vertices gives
\[
\Phi(q_1,\ldots,q_s)=\frac{1}{s+t}\sum_{h=1}^s
\Phi(q_{h+1}-q_h,\ldots,q_s-q_h).
\]

For the left block of \(M_i\), this is exactly \(\Phi(d_1,\ldots,d_i)\). For the right block, order the selected \(B\)-vertices as \(b_n,b_{n-1},\ldots,b_{d_i+1}\) and the rejected \(A\)-vertices in reverse order. The corresponding nested degrees are
\[
R_i=(c_n,c_{n-1},\ldots,c_{d_i+1}),
\qquad
c_j=|\{h>i:d_h\ge j\}|.
\]
Multiplying the independent left and right factors proves the probability formula. Summing the probabilities with the monomial determined by
\[
|M_i|=i+n-d_i
\]
gives the probability-generating function.

## Verification
A standalone exact-rational checker exhaustively tested every connected canonical chain graph with at most eight vertices. It enumerated all nondecreasing degree sequences with \(d_1\ge1\) and \(d_m=n\), then every vertex permutation, computed greedy directly, and compared the entire support and every probability to the theorem. The executed package artifact reported:

`VERIFY_OK degree_sequences=127 permutations=2754350 support_points=383 max_total=8`

This finite computation is a stress test, not the proof of the general theorem.

## Relationship to prior work
Boyacı, Ekim, and Shalom give the nested-neighborhood formulation of bipartite chain graphs and use the corresponding degree structure in their 2015 study of co-bipartite chain graphs. Alecu, Atminas, Lozin, and Malyshev later note explicitly that a chain graph has only linearly many inclusion-wise maximal independent sets and exploit that support structure algorithmically for quasi-chain graphs. Those structural results account for the support side of the present theorem.

Krivelevich, Mészáros, Michaeli, and Shikhelman study the same uniformly random-order greedy maximal-independent-set process in broad graph families and give exact analyses in several settings, notably trees. Their full accessible text contains no chain-graph or Ferrers-graph specialization. Targeted searches under the aliases chain graph, Ferrers graph, difference graph, and \(2K_2\)-free bipartite graph did not locate the factorized exact law above.

The closest mathematical-results database hit found in the stochastic direction is an exact random-greedy theorem for complete multipartite graphs. Complete bipartite graphs form a special subfamily of chain graphs, and the present formula specializes correctly there, but that result does not imply the law for arbitrary nested-neighborhood chain graphs.

## Limitations
The theorem is restricted to connected chain graphs. Isolated vertices can be incorporated separately, but that extension is not claimed here. The literature comparison was targeted rather than exhaustive across every historical use of the term “difference graph”; older Ferrers/difference-graph literature is therefore a residual indexing risk. The exhaustive computation covers only graphs of order at most eight and is corroborative rather than logically necessary.

## References
1. A. Boyacı, T. Ekim, and M. Shalom, “The Maximum Cut Problem in Co-bipartite Chain Graphs,” arXiv:1504.03666, first submitted 14 April 2015.
2. B. Alecu, A. Atminas, V. Lozin, and D. Malyshev, “Combinatorics and Algorithms for Quasi-Chain Graphs,” Algorithmica, DOI: 10.1007/s00453-022-01019-6; arXiv:2104.04471.
3. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” Random Structures & Algorithms, DOI: 10.1002/rsa.21200.
