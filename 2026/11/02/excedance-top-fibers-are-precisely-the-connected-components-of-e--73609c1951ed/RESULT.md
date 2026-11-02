# Excedance-top fibers are precisely the connected components of Eulerian adjacent-swap graphs

## Finding

For every integer \(n\geq 2\) and every \(0\leq k\leq n-1\), let \(G_{n,k}\) have as vertices the permutations \(\pi\in S_n\) with exactly \(k\) excedances, and join two permutations if one is obtained from the other by interchanging entries at consecutive positions while retaining exactly \(k\) excedances. An excedance is an index \(i\) with \(\pi_i>i\). Define the *excedance-top set* \(T(\pi)=\{\pi_i:\pi_i>i\}\), a set of values, not of indices.

**Theorem.** Two vertices of \(G_{n,k}\) belong to the same connected component if and only if they have the same excedance-top set. Every \(k\)-subset of \(\{2,\ldots,n\}\) occurs, and therefore

\[
\#\operatorname{components}(G_{n,k})=\binom{n-1}{k}.
\]

Exactly one vertex of \(G_{n,k}\) is isolated, namely

\[
(2,3,\ldots,k+1,1,k+2,\ldots,n),
\]

where the sequence is interpreted as the identity when \(k=0\). Thus there are exactly \(n\) isolated permutations over the disjoint union of all excedance strata.

If \(A(n,k)\) denotes the Eulerian number counting permutations of length \(n\) with \(k\) excedances (defined as zero when \(k<0\) or \(k\ge n\)), the exact number of graph edges is

\[
|E(G_{n,k})|=\frac{n-1}{2}\bigl(A(n,k)-A(n-1,k)-A(n-1,k-1)\bigr).
\]

Each component has a canonical representative, and any two of its vertices can be joined by a path of at most \(n(n-1)\) legal swaps.

## Assumptions and scope

Only ordinary permutations of \(\{1,\ldots,n\}\) and exchanges at *adjacent positions* are considered. A move is legal if the total excedance number is unchanged; no separate preservation of the excedance-top set is imposed. The results hold for every \(n\ge2\), including \(k=0\) and \(k=n-1\). The Eulerian numbers in the edge formula use the excedance convention and satisfy \(A(1,0)=1\).

## Proof

**Local move rule.** Consider exchanging \(a=\pi_i\) and \(b=\pi_{i+1}\) at positions \(i,i+1\). The local change in excedance count is

\[
\bigl[ b>i\bigr]+\bigl[a>i+1\bigr]-\bigl[a>i\bigr]-\bigl[b>i+1\bigr]
=\bigl[b=i+1\bigr]-\bigl[a=i+1\bigr],
\]

where brackets denote indicator functions. Since \(a\ne b\), a legal move occurs exactly when neither entry equals \(i+1\). For such a move, both entries individually retain their excedance/nonexcedance status when their positions are exchanged. Hence the set \(T(\pi)\) is invariant on every connected component.

**Realizability of every top set.** Fix \(T=\{t_1<\cdots<t_k\}\subseteq\{2,\ldots,n\}\), and list the other values as \(q_1<\cdots<q_{n-k}\). Let

\[
\rho_T=(t_1,\ldots,t_k,q_1,\ldots,q_{n-k}).
\]

Because \(t_j\ge j+1\), each entry \(t_j\) at position \(j\) is an excedance. Because \(q_j\le k+j\), every \(q_j\) at position \(k+j\) is a nonexcedance. Thus \(T(\rho_T)=T\). This includes \(T=\varnothing\) and \(T=\{2,\ldots,n\}\).

**Connectivity of each fiber.** Order the symbols by listing the elements of \(T\) increasingly and then the elements of its complement increasingly. Whenever two adjacent entries are inverted relative to this total order, their exchange is legal. Indeed, if both entries lie in \(T\), write \(a>b\) in positions \(i,i+1\). Since \(b\) is an excedance at position \(i+1\), both \(a,b\) exceed \(i+1\). If both lie outside \(T\), then \(a>b\) and \(a\le i\), so both are smaller than \(i+1\). Finally, if \(a\notin T\) and \(b\in T\), then \(a\le i\) and \(b\ge i+2\). Thus in every case neither value equals \(i+1\). Bubble-sorting the finite word reaches \(\rho_T\), by at most \(\binom n2\) legal exchanges. Hence a fiber is connected, and the two directed sorting paths through \(\rho_T\) give the claimed diameter bound.

**Isolated vertices.** For \(T=\{2,3,\ldots,k+1\}\), the representative \(\rho_T\) has at each boundary \(i\) the entry \(i+1\) in one of its two positions, so no exchange is legal. Conversely, if \(T=\{t_1<\cdots<t_k\}\) is not that initial segment, choose the least \(j\) such that \(t_j>j+1\). If \(j<k\), the adjacent top entries \(t_j,t_{j+1}\) at positions \(j,j+1\) can be exchanged legally. If \(j=k\), the adjacent entries \(t_k,1\) at positions \(k,k+1\) can be exchanged legally. Thus this representative lies in a nontrivial connected component. Since every fiber is connected, all its vertices then have positive degree; only the single initial-segment fiber is isolated. The case \(k=0\) is the identity singleton directly.

**Degrees and edge count.** The local rule gives

\[
\deg_{G_{n,k}}(\pi)=(n-1)-\#\{i<n:\pi_i=i+1\}-\#\{2\le j\le n:\pi_j=j\}.
\]

The two forbidden events at a given boundary are disjoint. Fixing \(\pi_j=j\) and deleting this entry, while reducing larger labels by one, bijects length-\(n\) permutations with \(k\) excedances and a prescribed fixed point with length-\(n-1\) permutations with \(k\) excedances. Similarly, fixing \(\pi_i=i+1\) and deleting this entry bijects permutations with \(k\) excedances and the prescribed unit excedance with length-\(n-1\) permutations with \(k-1\) excedances. Therefore the total number of legal ordered boundary incidences is \((n-1)(A(n,k)-A(n-1,k)-A(n-1,k-1))\). Divide by two for undirected edges.

## Verification

The standalone `verify_primary.py` enumerates every permutation for \(2\le n\le8\); it checks the local move equivalence, top-set invariance, exact connected-component labels, the binomial component count, one isolated vertex per stratum, canonical realizability, and the Eulerian edge identity. The separately implemented `verify_alt.cpp` uses factorial-ranking plus disjoint-set unions instead of direct graph traversal and checks the component signatures, isolation counts, and edge incidences for \(2\le n\le9\). Both were run successfully from extracted files of the completed package. These finite tests corroborate but do not replace the proof.

## Relationship to prior work

Classical work on the excedance *position* set enumerates permutations with specified excedance indices, not the reconfiguration connected components indexed by excedance *values*. Permutation tableaux encode (weak) excedance statistics but do not assert this local adjacency-swap classification. The equivalence relation of Baril, Mansour and Petrossian requires agreement at individual excedance positions, so it is finer than agreement of the top-value set and does not imply fiber connectivity. Pierrot, Rossin and West study position-independent replacements of consecutive order patterns, whereas the legal moves here depend on the absolute boundary position \(i+1\). The component invariant and constructive fiber connectivity distinguish the present result from these prior frameworks.

## Limitations

The formula classifies the components, but does not give a closed expression for the size or internal diameter of each component. In particular, the induced reconfiguration metric is not always the unrestricted adjacent-swap distance: for \(n=5\), the top set \(\{4,5\}\) contains \((1,4,3,5,2)\) and \((4,2,3,5,1)\), whose legal shortest-path distance is \(8\) although their ordinary adjacent-swap distance is \(6\). Novelty comparisons are based on the inspected literature and available searchable records; equivalents under alternative terminology or in unindexed sources remain possible. No independent mathematical audit has been performed.

## References

1. R. Ehrenborg and E. Steingrímsson, *The Excedance Set of a Permutation*, Advances in Applied Mathematics 24 (2000), 284–299. DOI: 10.1006/aama.1999.0671.
2. E. Steingrímsson and L. K. Williams, *Permutation Tableaux and Permutation Patterns*, first arXiv version July 7, 2005, arXiv:math/0507149.
3. A. Pierrot, D. Rossin and J. West, *Adjacent transformations in permutations*, DMTCS Proceedings (2011), 765–776. DOI: 10.46298/dmtcs.2951.
4. J.-L. Baril, T. Mansour and A. Petrossian, *Equivalence classes of permutations modulo excedances*, Journal of Combinatorics 5 (2014), 453–469. DOI: 10.4310/joc.2014.v5.n4.a4.
