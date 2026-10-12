# Total bondage number of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where the missing perfect matching is \(\{a_i b_i:1\le i\le n\}\). Then
\[
\gamma_t(\operatorname{Cr}_n)=4
\qquad\text{and}\qquad
b_t(\operatorname{Cr}_n)=2n-3.
\]
Here \(b_t(G)\) is the minimum number of edges whose removal, without creating an isolated vertex, strictly increases the total domination number.

## Assumptions and scope
Graphs are finite and simple. Total domination is considered only for graphs with no isolated vertices. The theorem concerns ordinary total bondage, equivalently the \(k=1\) case of \(k\)-total bondage, and starts from the crown graph itself rather than from the complete bipartite graph.

## Proof
For a bipartite graph \(H\) with bipartition \(A\cup B\) and no isolated vertices, let \(\tau_A(H)\) be the least number of vertices of \(A\) whose open neighborhoods cover \(B\), and define \(\tau_B(H)\) symmetrically. A set \(D\) is total dominating exactly when \(D\cap A\) covers \(B\) and \(D\cap B\) covers \(A\). Therefore
\[
\gamma_t(H)=\tau_A(H)+\tau_B(H).
\]
In \(\operatorname{Cr}_n\), no single vertex covers the opposite shore, while any two distinct vertices on one shore cover the other shore. Hence \(\tau_A=\tau_B=2\) and \(\gamma_t(\operatorname{Cr}_n)=4\).

We use the following pair-cover lemma. If proper subsets \(C_1,\ldots,C_m\subsetneq [n]\), each of size at least two, cover every two-element subset of \([n]\), then
\[
\sum_{i=1}^m (|C_i|-1)\ge 2n-3.
\]
For \(n=3\), every proper block has size at most two, so all three pairs are required and the bound is exact. Assume \(n\ge4\) and let \(s=\max_i|C_i|\). If \(s=n-1\), choose \(C_0=[n]\setminus\{x\}\). Every pair \(\{x,y\}\) with \(y\in C_0\) must lie in another block containing \(x\). The sets obtained from those blocks by removing \(x\) cover \(C_0\), so their total cardinality, which is exactly their total contribution \(\sum(|C_i|-1)\), is at least \(n-1\). Adding the contribution \(n-2\) of \(C_0\) gives \(2n-3\). If \(s\le n-2\), fix any \(x\in[n]\), restrict all blocks to \([n]\setminus\{x\}\), and discard restrictions of size below two. These restricted proper blocks still cover every pair of the remaining \(n-1\) points, so induction gives cost at least \(2n-5\). Returning to the original family adds one unit for every block containing \(x\). At least two blocks contain \(x\), because a unique such block would have to contain every other point in order to cover all pairs \(\{x,y\}\), contradicting properness. Thus the original cost is at least \(2n-3\).

Now delete a set \(F\) of crown edges and write \(H=\operatorname{Cr}_n-F\), assuming \(H\) has no isolated vertices. For each \(b_j\in B\), define
\[
Z_j=\{i\in[n]:a_i b_j\notin E(H)\}.
\]
The built-in missing matching gives \(j\in Z_j\), while nonisolation makes every \(Z_j\) proper. If \(\tau_A(H)\ge3\), then no pair of vertices of \(A\) covers \(B\); equivalently, every pair \(\{p,q\}\subseteq[n]\) is contained in at least one \(Z_j\). After singleton \(Z_j\)'s are ignored, the pair-cover lemma yields
\[
|F|=\sum_{j=1}^n(|Z_j|-1)\ge2n-3.
\]
The same argument with the shores reversed applies if \(\tau_B(H)\ge3\). Since each shore-cover number is always at least two in a subgraph of a crown, any strict increase of \(\gamma_t(H)=\tau_A(H)+\tau_B(H)\) above four forces one of these two cases. Hence \(b_t(\operatorname{Cr}_n)\ge2n-3\).

For the matching upper bound, when \(n=3\) delete \(a_1b_2,a_2b_3,a_3b_1\). The remaining graph is a perfect matching, so it has no isolated vertices and its total domination number is six.

For \(n\ge4\), prescribe the sets of nonneighbors of the \(A\)-vertices by
\[
W_1=[n]\setminus\{n\},\qquad
W_2=[n]\setminus\{n-1\},\qquad
W_{n-1}=\{n-1,n\},
\]
and \(W_i=\{i\}\) for all other \(i\). Starting from the crown, delete precisely the edges \(a_i b_j\) with \(j\in W_i\setminus\{i\}\). The number of deleted edges is
\[
(n-2)+(n-2)+1=2n-3.
\]
Every vertex remains nonisolated. The family \(W_1,W_2,W_{n-1}\) covers every pair of indices: all pairs except \(\{n-1,n\}\) lie in at least one of the first two sets, and the exceptional pair lies in \(W_{n-1}\). Therefore no two vertices of \(B\) cover \(A\), so \(\tau_B(H)\ge3\), and consequently \(\gamma_t(H)>4\). This proves \(b_t(\operatorname{Cr}_n)\le2n-3\) and completes the proof.

## Verification
The bundled checker evaluates the definitions directly. It exhaustively tests every edge-deletion set of size below \(2n-3\) for \(n=3,4,5\), independently computes the pair-cover minimum for \(n=3,4,5,6\), and checks the explicit upper-bound construction through \(n=30\). Its replay result is:

`ALL CHECKS PASSED; exhaustive_orders=[3,4,5]; deletion_subsets_below_target=61276; lemma_orders=[3,4,5,6]; lemma_minima=[3, 5, 7, 9]; witness_range=3..30`

The finite computation is a stress test only; the theorem for all \(n\ge3\) follows from the analytic pair-cover lemma and the explicit construction above.

## Relationship to prior work
Appel, Fischberg, Kelley, Shank, and Sosis introduced \(k\)-total bondage and, in their 2025 preprint, obtained exact values for several standard classes including complete bipartite graphs. The earlier total-bondage literature gives
\[
b_t(K_{m,n})=m\qquad(2\le m\le n).
\]
Thus the balanced undeleted baseline is \(b_t(K_{n,n})=n\). The inspected Appel et al. text treats complete bipartite graphs but contains no crown-graph or perfect-matching-deletion theorem.

Hemalatha and Jeyanthi computed the ordinary bondage number for crown graphs in 2016. That result concerns ordinary domination, not total domination, and therefore does not imply the present theorem. The present result shows a different perturbation phenomenon: deleting one perfect matching from \(K_{n,n}\) changes the subsequent total-bondage threshold from \(n\) to \(2n-3\).

## Limitations
The theorem is specific to ordinary total bondage of crown graphs. It does not classify \(k\)-total bondage for \(k\ge2\), nor arbitrary starting deletions from complete bipartite graphs. The original 1991 Kulli--Patwari paper was not used as the sole source for a noncoverage claim; the comparison relies on later survey statements and the inspected 2025 treatment. A poorly indexed equivalent crown result under an alternate graph name remains a residual literature risk.

## References
1. J.-P. Appel, G. Fischberg, K. Kelley, N. Shank, and E. Sosis, *The \(k\)-Total Bondage Number of a Graph*, arXiv:2506.07000v1, first public 2025-06-08.
2. J.-M. Xu, *On Bondage Numbers of Graphs: A Survey with Some Comments*, International Journal of Combinatorics (2013), Article 595210, DOI 10.1155/2013/595210.
3. V. R. Kulli and D. K. Patwari, *The total bondage number of a graph*, Advances in Graph Theory (1991), 227--235.
4. G. Hemalatha and P. Jeyanthi, *Results on Domination Number and Bondage Number for Some Families of Graphs*, International Journal of Pure and Applied Mathematics 107(3) (2016), 565--577, DOI 10.12732/ijpam.v107i3.5.
