# A three-state multivariate \(P_3\)-convexity polynomial for block graphs

## Finding

For a finite simple graph \(G\), a vertex set \(S\) is \(P_3\)-convex if no vertex outside \(S\) has two neighbors in \(S\). Define its multivariate convex-set polynomial by
\[
\mathcal C_G(\mathbf y)=
\sum_{\substack{S\subseteq V(G)\\\forall v\notin S:\ |N_G(v)\cap S|\le1}}
\prod_{v\in S}y_v.
\]
The empty product is \(1\). Substituting \(y_v=x\) for every vertex gives the complete cardinality enumerator \(C_G(x)\); substituting arbitrary numerical weights gives the weighted count.

**Theorem.** On every block graph \(G\), including disconnected graphs and isolated vertices, \(\mathcal C_G\) has an exact positive arithmetic circuit with three states at each directed vertex–block incidence. The circuit uses \(O(|V(G)|)\) additions and multiplications after the vertex–block incidence forest is constructed. This is independent of the sizes of the clique blocks. Its univariate specialization can be expanded with \(O(|V(G)|^3)\) naive coefficient arithmetic, while any fixed numerical evaluation takes \(O(|V(G)|+|E(G)|)\) arithmetic operations including block decomposition.

For the generalized windmill with \(t\ge1\) blades, each a clique of \(m+1\) vertices sharing a center, where \(m\ge2\), one obtains the closed specialization
\[
\boxed{C_{K_1\vee tK_m}(x)=1+tm\,x+x(1+x^m)^t.}
\]
Consequently the total number of convex sets on this graph is \(1+tm+2^t\).

## Assumptions and scope

A **block graph** is a finite simple graph in which every nontrivial biconnected block is a clique; bridges count as two-vertex clique blocks. Its bipartite incidence graph between original vertices and nontrivial maximal blocks is a forest. Different blocks meet in at most one vertex. Isolated vertices have no incident block.

The source convention \(P_3\) means **every path with three vertices**, not merely induced three-vertex paths. Precisely, a set \(S\) is \(P_3\)-convex if every vertex \(v\notin S\) has \(\lvert N_G(v)\cap S\rvert\le1\). This distinction matters in clique blocks.

All polynomial variables commute. Operation counts refer to arithmetic operations on polynomial circuits or numerical weights, not bit-level complexity of the possibly exponential-size coefficients. No polynomial-size expanded multivariate output is asserted.

## Proof

Fix a connected component, choose an original vertex \(r\) as root, and direct each incidence edge of its vertex–block tree away from \(r\). The construction below counts every selection by multiplying one factor \(y_v\) for each selected original vertex \(v\), exactly once.

**Vertex messages.** For a vertex \(v\) with one parent block (or no parent when \(v=r\)), let \((P_v,Q_v,R_v)\) be the generating functions for valid selections in the rooted descendant branch, with three boundary states:

- \(P_v\): \(v\) is omitted and has no selected neighbor in descendant blocks;
- \(Q_v\): \(v\) is omitted and has exactly one selected neighbor in descendant blocks;
- \(R_v\): \(v\) is selected.

The status of a selected vertex requires no bound on its selected neighbors. Initially, before incorporating child blocks,
\[
(P_v,Q_v,R_v)=(1,0,y_v).
\]
Suppose a child block \(B\) sends \((L_B^{00},L_B^{01},L_B^1)\), in which the superscripts respectively indicate that \(v\) is omitted with zero selected neighbors inside \(B\), omitted with one, or selected. Since different child blocks are disjoint away from \(v\), the omitted vertex may have at most one selected neighbor over **all** its child blocks. Thus, evaluating the right side using the old values, update
\[
\boxed{(P_v,Q_v,R_v)\longleftarrow
(P_vL_B^{00},\ Q_vL_B^{00}+P_vL_B^{01},\ R_vL_B^1).}
\]

**Block messages.** Let \(B\) be a clique block rooted at its parent vertex \(v\). Every other vertex \(w\in B\setminus\{v\}\) sends a vertex message \((P_w,Q_w,R_w)\). Maintain four accumulators initialized by
\[
(Z,T,U,A)=(1,0,1,1).
\]
For each such \(w\), update simultaneously:
\[
\boxed{(Z,T,U,A)\longleftarrow
(Z(P_w+Q_w),\ TP_w+UR_w,\ UP_w,\ AR_w).}
\]
Return
\[
\boxed{(L_B^{00},L_B^{01},L_B^1)=(Z,T,U+A).}
\]

Here is the exact case analysis. If the parent \(v\) is **omitted**, then at most one vertex of \(B\setminus\{v\}\) may be selected. With none selected, each child vertex is omitted and may have zero or one selected descendant neighbor; this contributes \(Z=\prod_w(P_w+Q_w)\). With exactly one selected child vertex, all other child vertices must be omitted and have **zero** selected descendant neighbors, because the chosen child is already one selected neighbor of each. The state sum for this case is \(T=\sum_w R_w\prod_{u\ne w}P_u\), computed by its two-state accumulator with \(U=\prod_wP_w\). These cases have zero and one selected neighbor of \(v\), respectively.

If the parent \(v\) is **selected**, a clique cannot contain both a selected child vertex and an omitted child vertex: the omitted child would see both \(v\) and that selected child. Hence either all child vertices are omitted, with each such vertex having zero selected descendant neighbors, giving \(U=\prod_wP_w\); or every child vertex is selected, giving \(A=\prod_wR_w\). These are disjoint cases and contribute \(U+A\). This argument also covers bridge blocks \(K_2\), for which there is only one child vertex.

Induction from the leaves proves that all messages enumerate precisely the valid selections in the corresponding branches with their advertised boundary conditions. At the component root, all possibilities are allowed, so its polynomial is
\[
P_r+Q_r+R_r.
\]
Different connected components have no edges between them, and choices therefore multiply. This completes the general theorem, including isolated vertices (which contribute \(1+y_v\)) and the empty graph (which contributes \(1\)).

The vertex–block incidence forest has \(O(|V(G)|)\) incidences: a component with \(n_c\) vertices and \(b_c\) nontrivial blocks has exactly \(n_c+b_c-1\) incidences and \(b_c\le n_c-1\). Every incidence is processed a constant number of times. Standard biconnected-component decomposition costs \(O(|V|+|E|)\). The asserted arithmetic-operation bounds follow; naive multiplication of degree-at-most-\(n\) polynomials gives a conservative \(O(n^3)\) bound for coefficient expansion.

Finally, consider \(W_{t,m}=K_1\vee tK_m\), with center \(z\). If \(z\) is omitted, it may have at most one selected neighbor in the whole graph. Hence the only convex sets omitting it are the empty set and the \(tm\) singletons outside \(z\), yielding \(1+tm\,x\). If \(z\) is selected, every blade must be either entirely selected or entirely omitted: any mixed blade would leave an omitted blade vertex adjacent to both \(z\) and a selected blade vertex. Conversely each such blade choice is valid. The latter contribution is \(x(1+x^m)^t\), proving the formula.

## Verification

The standalone executable `artifacts/verify.py` uses only Python's standard library. It computes biconnected clique blocks and evaluates the three-state polynomial; independently, it enumerates vertex subsets and tests every omitted vertex's number of selected neighbors directly from the graph's adjacency lists.

The script compares all coefficients on every labeled block graph on up to six vertices, as well as 700 reproducibly generated larger clique-glued block graphs. It also compares 562 independent arbitrary-vertex-weight numerical specializations against direct weighted subset sums and checks the generalized-windmill closed form on 60 parameter profiles.

Replay output:

`ALL CHECKS PASSED; small_labeled_block_graphs=8368; random_glued_block_graphs=700; vertex_subsets_checked=3536955; weighted_specializations_checked=562; generalized_windmill_profiles=60; all_labeled_graphs_n<=6`

These computations test only finite instances. The general theorem rests on the exact local clique argument and tree induction, not on extrapolation from enumeration.

## Relationship to prior work

Dourado, Grippo, Lin, and Protti (arXiv:2603.04706v1, first public March 5, 2026) introduced the systematic counting problem for \(P_3\)-convex sets. Their 27-page preprint proves that the problem is number-\(\#P\)-complete even on split graphs and gives linear-time total-count algorithms for trees and threshold graphs, along with exact exponential algorithms for general graphs. The inspected complete text does not state this block-graph polynomial recurrence. Block graphs include arbitrary trees and clique bouquets of unbounded clique size, whereas general threshold graphs and block graphs are incomparable.

Barbosa, Coelho, Dourado, Rautenbach, and Szwarcfiter (2012) investigate the \(P_3\)-Carathéodory number, including for block graphs; Coelho, Dourado, Rautenbach, and Szwarcfiter (2014) extend Carathéodory-number algorithms to chordal graphs. The Carathéodory number concerns bounded witnesses for convex hull membership; it is not the all-convex-set generating polynomial. The 2012 publisher abstract is accessible, but its complete text was not available through the available noninteractive access path.

A broader **prior coverage boundary** is important. Courcelle, Makowsky, and Rotics (2001) establish polynomial-time counting and evaluation for suitable monadic-second-order-definable vertex-set problems on graph classes of bounded clique-width. Golumbic and Rotics (2000) show that distance-hereditary graphs have clique-width at most three; block graphs are distance hereditary. The defining \(P_3\)-convexity predicate is expressible in vertex-set monadic second-order logic. Thus prior meta-theorems already **imply polynomial-time countability**, including size weights, on block graphs. That qualitative complexity consequence is **not** claimed as novel here. The contribution is the explicit, positive **three-state vertex–block polynomial recurrence**, its linear-size multivariate arithmetic circuit with small transparent states, and its direct closed-form specialization on clique bouquets.

## Limitations

This theorem applies to block graphs, not arbitrary chordal or split graphs. The incidence-forest proof uses the special property that distinct clique blocks meet in at most one vertex. A chordal graph with overlapping maximal cliques need not admit the same three-state messages.

The expanded multivariate polynomial may have exponentially many monomials; the circuit is compact, and the exact ordinary cardinality histogram has only \(n+1\) coefficients. Operation counts do not conceal the bit size of large integer counts.

Full-text access to the 2012 block-graph Carathéodory paper was unavailable after public-access searches; the authorized institutional fallback required noninteractive approval and could not be completed. That paper's stated theorem is different, but an unadvertised related recurrence is a residual originality risk. General bounded-clique-width metatheorems already cover the existence of polynomial-time counting; they do not supply the explicit recurrence asserted above.

## References

1. M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, “Counting \(P_3\)-convex sets in graphs,” arXiv:2603.04706v1, March 5, 2026.
2. R. M. Barbosa, E. M. M. Coelho, M. C. Dourado, D. Rautenbach, and J. L. Szwarcfiter, “On the Carathéodory Number for the Convexity of Paths of Order Three,” SIAM Journal on Discrete Mathematics 26 (2012), 929–939; DOI 10.1137/110828678; primary MSC 05C99.
3. E. M. M. Coelho, M. C. Dourado, D. Rautenbach, and J. L. Szwarcfiter, “The Carathéodory number of the \(P_3\) convexity of chordal graphs,” Discrete Applied Mathematics 172 (2014), 104–108; DOI 10.1016/j.dam.2014.03.004.
4. B. Courcelle, J. A. Makowsky, and U. Rotics, “On the fixed parameter complexity of graph enumeration problems definable in monadic second-order logic,” Discrete Applied Mathematics 108 (2001), 23–52; DOI 10.1016/S0166-218X(00)00221-3.
5. M. C. Golumbic and U. Rotics, “On the clique-width of some perfect graph classes,” International Journal of Foundations of Computer Science 11 (2000), 423–443; DOI 10.1142/S0129054100000260.
