# Positive semidefinite zero forcing polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), partite sets \(A_1,\ldots,A_r\), and \(N=\sum_i n_i\). For an initially blue set \(S\subseteq V(G)\), put \(w_i=|A_i\setminus S|\), \(b_i=n_i-w_i\), and \(I=\{i:w_i>0\}\). Then \(S\) is a positive semidefinite zero forcing set if and only if one of the following holds:

1. \(|I|\le1\); or
2. \(I=\{i,j\}\) and \((w_j=1\text{ and }b_i>0)\) or \((w_i=1\text{ and }b_j>0)\).

Consequently, if
\[
\mathcal Z_+(G;x)=\sum_{S\text{ PSD zero forcing}}x^{|S|},
\]
then
\[
\begin{aligned}
\mathcal Z_+(G;x)={}&x^N+\sum_{i=1}^r\sum_{a=1}^{n_i}\binom{n_i}{a}x^{N-a}\\
&+\sum_{1\le i<j\le r}\Bigg[
 n_j\sum_{a=1}^{n_i-1}\binom{n_i}{a}x^{N-a-1}
+n_i\sum_{b=1}^{n_j-1}\binom{n_j}{b}x^{N-b-1}\\
&\hspace{42mm}-\mathbf 1_{\{n_i\ge2,\ n_j\ge2\}}n_in_jx^{N-2}
\Bigg].
\end{aligned}
\]
The least exponent with nonzero coefficient is \(N-\max_i n_i\), recovering the known formula for \(Z_+(G)\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. A positive semidefinite zero forcing step uses the standard component rule: with current blue set \(B\), consider the connected components of the white-induced graph \(G-B\); a blue vertex may force a white vertex when that white vertex is its unique neighbor in one such white component. The theorem classifies every initial blue set, not merely minimum sets.

## Proof
Let \(W=V(G)\setminus S\). If all white vertices lie in one part \(A_i\), then \(G[W]\) is an independent graph, so every white vertex is its own white component. Since \(r\ge2\), every vertex outside \(A_i\) is blue and is adjacent to every white vertex. Thus the whites can be forced one at a time. This proves sufficiency when \(|I|\le1\).

Assume now that white vertices occur in at least two parts. Then \(G[W]\) is connected. Write \(W_0=|W|=\sum_i w_i\). A blue vertex in part \(A_i\) has exactly \(W_0-w_i\) white neighbors, while a blue vertex in a part containing no white vertex has exactly \(W_0\) white neighbors. Hence an initial positive semidefinite force exists exactly when some blue vertex lies in a white-support part \(A_i\) and there is exactly one white vertex outside \(A_i\).

If \(|I|\ge3\), then every white-support part has at least two white vertices outside it, so no force is possible and the process is stalled. If \(I=\{i,j\}\), a force is possible exactly when \(b_i>0\) and \(w_j=1\), or symmetrically when \(b_j>0\) and \(w_i=1\). After such a force, all remaining white vertices lie in a single part. The preceding one-part argument then finishes the process. This proves the classification and its necessity.

For the generating function, the term \(x^N\) counts the all-blue set. The first double sum counts nonempty white subsets contained in one part. For a fixed pair \(i<j\), successful two-part white sets have either one white vertex in \(A_j\) and between one and \(n_i-1\) white vertices in \(A_i\), or the symmetric pattern. These give the first two sums inside the brackets. When \(n_i,n_j\ge2\), the case of one white vertex in each part is counted twice, so the final term removes one copy. The cases are disjoint across their white-support sets, proving the polynomial formula.

Finally, a one-part white set may contain all vertices of a largest part, so \(Z_+(G)\le N-\max_i n_i\). Conversely, the classification never permits more than \(\max_i n_i\) white vertices: in the two-part case, the unique-white side contributes one vertex while the other side omits at least one vertex from its part. Hence \(Z_+(G)=N-\max_i n_i\).

## Verification
A standalone verifier independently simulates the positive semidefinite color-change rule by recomputing white components after every force. For every integer-partition type of connected complete multipartite graph of order \(2\) through \(10\), it checks every initial blue subset against the structural criterion, compares the resulting cardinality histogram with the closed polynomial, and verifies the minimum exponent. The exact replay output is `VERIFY_OK graph_types=128 subset_checks=64916 classification_checks=64916 coefficient_checks=1179 max_order=10`.

## Relationship to prior work
Barioli, Barrett, Fallat, Hall, Hogben, Shader, van den Driessche, and van der Holst introduced the positive semidefinite zero forcing number in the 2010 paper *Zero forcing parameters and minimum rank problems*. Peters later proved for \(n_1\ge n_2\ge\cdots\ge n_r>0\) that \(Z_+(K_{n_1,\ldots,n_r})=n_2+\cdots+n_r\), equivalently \(N-n_1\), and linked this value to positive semidefinite maximum nullity. The result here does not claim that scalar minimum formula as new; it refines it to an exact characterization of every positive semidefinite zero forcing set and the complete size-generating polynomial.

Ordinary zero forcing on complete multipartite graphs has a different forcing rule and a much smaller feasible-set family near full size. Its results do not imply the positive semidefinite classification above because the component rule can split an independent white part into singleton components and enable forces that ordinary zero forcing cannot perform.

## Limitations
The proof is specific to complete multipartite graphs and uses their exact white-component structure. The finite verifier corroborates the theorem only through order \(10\); the infinite statement rests on the proof, not on enumeration. The literature comparison is best-of-knowledge and may miss poorly indexed work that explicitly enumerates all positive semidefinite zero forcing sets, although the directly relevant complete-multipartite scalar theorem was inspected.

## References
1. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, and H. van der Holst, *Zero forcing parameters and minimum rank problems*, Linear Algebra and its Applications 433 (2010), 401–411, arXiv:1003.2028v1, https://doi.org/10.1016/j.laa.2010.03.008.
2. T. Peters, *Positive semidefinite maximum nullity and zero forcing number*, Electronic Journal of Linear Algebra 23 (2012), 815–830, https://doi.org/10.13001/1081-3810.1559.
