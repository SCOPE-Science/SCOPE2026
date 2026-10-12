# Self-review

## Claim
For integers \(2\le m\le n\) and \(0\le t\le m\), let \(G_{m,n,t}=K_{m,n}-M_t\), where \(M_t\) is a matching of size \(t\). If \(\operatorname{eis}(G)\) denotes the edge independent dom-saturation number, equivalently the maximum over edges \(e\) of the minimum cardinality of a maximal matching containing \(e\), then
\[
\operatorname{eis}(G_{m,n,t})=
\begin{cases}
m-1,&m=n\text{ and }t\ge3,\\
m,&\text{otherwise.}
\end{cases}
\]
Thus a balanced biclique requires deletion of at least three independent edges before \(\operatorname{eis}\) drops, whereas any strict shore imbalance prevents a drop under deletion of a matching. In the balanced regime with \(t\ge3\), every present edge lies in a maximal matching of size \(n-1\); for \(t=1\) or \(t=2\), a present edge incident with all deleted pairs forces local value \(n\).

## Correctness
PASS. A maximal matching is characterized by the absence of an edge between unmatched vertices. Because the deleted nonedges form a matching, any unbalanced instance with an unmatched vertex on the smaller shore leaves at least two unmatched vertices on the larger shore and can still be extended; hence every maximal matching has size \(m\). In the balanced case, the same argument forces every maximal matching to have size at least \(n-1\). For one or two deletions the edge \(a_1b_2\) forces local value \(n\). With at least three deletions, every prescribed edge avoids some deleted index \(i\), and after fixing that edge and leaving \(a_i,b_i\) unmatched, the residual graph is complete bipartite minus a matching and has a perfect matching by Hall's theorem. The finite checker independently confirms all local values for \(2\le m\le n\le6\).

## Originality
PASS. The initiating 2025 paper defines the same invariant and gives only the undeleted complete-bipartite value in the relevant family. Its accessible full text was inspected at Definition 3.1, Observation 3.3(iv), and Theorem 3.6; document-wide searches found no “matching” or “crown” treatment of the new family. Classical edge domination determines only the minimum maximal-matching size, whereas the new theorem determines the maximum over prescribed-edge minimum sizes. Semantic searches using the exact invariant name, matching-deleted biclique notation, crown terminology, and the equivalent prescribed-edge maximal-matching formulation found no covering statement. A prior result on well-edge-domination of the same graph family was compared and is implication-incomparable with the claimed prescribed-edge formula.

## Value
PASS. This identifies a sharp structural resilience threshold for a newly introduced edge invariant: balanced complete bipartite graphs tolerate one or two independent edge deletions without changing \(\operatorname{eis}\), but the third deletion makes every edge fit inside a smaller maximal matching; any shore imbalance suppresses the transition entirely. The result is an exact two-shore, full-deletion-range classification and exposes a regime where the ordinary edge domination number and edge independent dom-saturation diverge.

## Closest literature and limitations
The closest primary source is Muthulakshmi–Subramanian, DOI 10.17654/0974165826003, which introduces \(\operatorname{eis}\) and computes complete bipartite graphs. Yannakakis–Gavril, DOI 10.1137/0138030, supplies the classical minimum-maximal-matching/edge-domination background but not the prescribed-edge maximum. The theorem does not cover arbitrary deleted edge sets.

Self-review: passed. Independent audit: not yet performed.
