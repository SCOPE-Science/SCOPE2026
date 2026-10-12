# Edge-independent dom-saturation has a three-deletion threshold on bicliques
## Finding
For integers \(2\le m\le n\) and \(0\le t\le m\), let \(G_{m,n,t}=K_{m,n}-M_t\), where \(M_t\) is a matching of size \(t\). If \(\operatorname{eis}(G)\) denotes the edge independent dom-saturation number, equivalently the maximum over edges \(e\) of the minimum cardinality of a maximal matching containing \(e\), then
\[
\operatorname{eis}(G_{m,n,t})=
\begin{cases}
m-1,&m=n\text{ and }t\ge3,\\
m,&\text{otherwise.}
\end{cases}
\]
Thus a balanced biclique requires deletion of at least three independent edges before \(\operatorname{eis}\) drops, whereas any strict shore imbalance prevents a drop under deletion of a matching. In the balanced regime with \(t\ge3\), every present edge lies in a maximal matching of size \(n-1\); for \(t=1\) or \(t=2\), a present edge incident with all deleted pairs forces local value \(n\).

## Assumptions and scope
All graphs are finite and simple. Let the bipartition of \(G_{m,n,t}\) be \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), with deleted matching \(M_t=\{a_i b_i:1\le i\le t\}\). A maximal edge-independent set is a maximal matching. For a present edge \(e\), write \(\operatorname{eis}(e,G)\) for the minimum cardinality of a maximal matching containing \(e\), and \(\operatorname{eis}(G)=\max_{e\in E(G)}\operatorname{eis}(e,G)\).

The theorem covers the full matching-deletion family with \(2\le m\le n\) and \(0\le t\le m\), including the disconnected boundary \(K_{2,2}-M_2\). It makes no assertion for deleted edge sets that are not matchings.

## Proof
A matching is maximal exactly when no edge joins two unmatched vertices. In \(G_{m,n,t}\), each vertex has at most one nonneighbor on the opposite shore, and the only cross-shore nonedges are the deleted pairs \(a_i b_i\).

First suppose \(m<n\). If a matching has size at most \(m-1\), then some vertex of \(A\) is unmatched and at least
\[
n-(m-1)=n-m+1\ge2
\]
vertices of \(B\) are unmatched. Since an \(A\)-vertex has at most one nonneighbor in \(B\), it is adjacent to an unmatched vertex of \(B\), so the matching is not maximal. Hence every maximal matching has exactly \(m\) edges. Every edge can be extended greedily to a maximal matching, so every local value is \(m\), giving \(\operatorname{eis}(G_{m,n,t})=m\).

Now suppose \(m=n\). If a matching has size at most \(n-2\), at least two vertices on each shore are unmatched. Any unmatched \(A\)-vertex is nonadjacent to at most one of the unmatched \(B\)-vertices, so an augmenting edge can be added. Thus every maximal matching has size at least \(n-1\).

If \(t=0\), the graph is complete bipartite and every maximal matching is perfect, so \(\operatorname{eis}=n\). If \(t=1\), the present edge \(a_1b_2\) cannot lie in a maximal matching of size \(n-1\): such a matching would leave exactly one vertex on each shore unmatched, and maximality forces those two vertices to be the sole deleted pair \(a_1,b_1\), impossible because \(a_1\) is already used by the prescribed edge. Hence its local value is \(n\). If \(t=2\), the present edge \(a_1b_2\) again cannot lie in a size-\(n-1\) maximal matching, because the unmatched pair would have to be either \(a_1,b_1\) or \(a_2,b_2\), while the prescribed edge uses \(a_1\) and \(b_2\). Thus \(\operatorname{eis}=n\) for \(t\le2\).

It remains to take \(t\ge3\). Fix any present edge \(e=a_p b_q\). Choose a deleted index \(i\le t\) distinct from both \(p\) and \(q\). We construct a matching of size \(n-1\) that contains \(e\) and leaves exactly \(a_i,b_i\) unmatched. After reserving \(e\) and deleting \(a_i,b_i,a_p,b_q\), the residual bipartite graph has \(n-2\) vertices on each shore and is a complete bipartite graph with a matching deleted. When \(n-2\ge2\), Hall's condition is immediate: a singleton has at least \(n-3\ge1\) neighbors, while any subset of at least two left vertices collectively misses no right vertex because the missing edges form a matching. Hence the residual graph has a perfect matching. When \(n=3\), necessarily \(t=3\), and the one residual cross-edge is off the deleted diagonal and is present. Therefore the desired size-\(n-1\) matching exists. It is maximal because its two unmatched vertices \(a_i,b_i\) form a deleted nonedge. Since no maximal matching is smaller than \(n-1\), every local value equals \(n-1\), proving the formula.

## Verification
The standalone checker `verify.py` enumerates every maximal matching for every parameter triple \(2\le m\le n\le6\), \(0\le t\le m\). For each present edge it computes the minimum size of a maximal matching containing that edge, takes the maximum over edges, and compares the result with the stated formula. It also checks the stronger proof assertions: in the unbalanced case every maximal matching has size \(m\), while in the balanced \(t\ge3\) case every edge has local value \(n-1\).

The replay output is recorded in `verification_output.txt`. This finite computation is a stress test of boundary cases and does not replace the universal proof.

## Relationship to prior work
Muthulakshmi and Subramanian introduced the edge independent dom-saturation number in their 2025 online publication and defined it through maximal edge-independent sets. Their Observation 3.3(iv) gives \(\operatorname{eis}(K_{r,s})=\min\{r,s\}\), which is exactly the \(t=0\) boundary of the theorem above. Their Theorem 3.6 places \(\operatorname{eis}\) within one unit of the edge domination number, but does not determine which side occurs for matching-deleted bicliques. Document-wide inspection of the accessible full text found no occurrence of “matching” or “crown” in the edge-independent dom-saturation treatment.

The classical edge-domination literature identifies the edge domination number with the minimum cardinality of a maximal matching. That scalar does not determine the present invariant, which maximizes a prescribed-edge minimum. The distinction is substantive here: for balanced \(n\ge3\) and \(t=1\) or \(t=2\), a maximal matching of size \(n-1\) exists, but the theorem proves \(\operatorname{eis}=n\) because some prescribed edges cannot belong to any such minimum maximal matching.

A separate published analysis of the same family \(K_{m,n}-M_t\) classifies when it is well-edge-dominated. That property concerns cardinalities of all inclusion-minimal edge-dominating sets and does not imply the prescribed-edge maximal-matching minima used here.

## Limitations
The theorem uses essentially that the deleted edges form a matching, so each vertex has at most one cross-shore nonneighbor. It does not determine \(\operatorname{eis}\) for arbitrary near-complete bipartite graphs. The originality assessment is based on full-text inspection of the initiating paper, classical edge-domination comparison, semantic literature searches under maximal-matching and prescribed-edge formulations, and overlap checks against prior records. An older result phrased entirely in matching-theory language could remain undiscovered.

## References
1. T. Muthulakshmi and M. Subramanian, “On the Independent Dom-Saturation Number of a Graph,” Advances and Applications in Discrete Mathematics 43(1) (2026), 33–47, DOI 10.17654/0974165826003; published online 2025-11-17.
2. M. Yannakakis and F. Gavril, “Edge Dominating Sets in Graphs,” SIAM Journal on Applied Mathematics 38(3) (1980), 364–372, DOI 10.1137/0138030.
