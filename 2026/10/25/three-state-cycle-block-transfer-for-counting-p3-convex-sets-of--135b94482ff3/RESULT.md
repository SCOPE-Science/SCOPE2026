# Three-state cycle-block transfer for counting \(P_3\)-convex sets of cactus graphs

## Finding
For every finite connected simple cactus graph \(G\), including \(K_1\), define
\[
Q_G(z)=\sum_{S\subseteq V(G)\,\colon\,\forall v\notin S,\ |N_G(v)\cap S|\le1} z^{|S|}.
\]
There is an explicit exact arithmetic circuit for \(Q_G(z)\) with \(O(|V(G)|)\) additions and multiplications in \(\mathbb Z[z]\) using a three-state vertex recurrence and a constant-width transfer around each cycle block. Evaluating at \(z=1\) counts all \(P_3\)-convex sets in linear arithmetic-operation time once the graph's blocks have been identified. Replacing \(z\) at a selected vertex by an independent indeterminate \(z_v\) gives the full multivariate selected-set polynomial using the same circuit.

## Assumptions and scope
Graphs are finite, simple, connected and undirected. A cactus is a graph in which every edge belongs to at most one simple cycle; every block is a bridge edge or a simple cycle. A subset \(S\) is \(P_3\)-convex exactly when every vertex outside \(S\) has at most one neighbor in \(S\). The graph's blocks are supplied by an ordinary biconnected-block decomposition, with vertices around each cycle listed in cyclic order. The vertex–block incidence graph is a tree rooted at an arbitrary original vertex \(r\). A one-vertex graph has no blocks. An arithmetic operation counts one polynomial-ring addition/multiplication, not constant bit time on unbounded integers or polynomials.

## Proof
For each original vertex \(v\) with its descendant block subtrees, define three generating functions. Write \(X_v\) for configurations where \(v\) is selected, \(Y_v^0\) for those where it is unselected and has zero selected neighbors in the descendant subgraph, and \(Y_v^1\) for those where it is unselected and has exactly one selected descendant neighbor. All other unselected vertices must satisfy the convexity condition. The parent block is excluded, so \(v\)'s potential neighbor there is deliberately left for the parent to handle.

For a child block \(B\) attached to \(v\), write \(T_B^X\) for all valid block-side configurations when \(v\) is selected, and \(T_B^0,T_B^1\) for block-side configurations where \(v\) is unselected and sees respectively zero or one selected neighbor *within that block*. The block-side weights omit the factor for \(v\). Distinct descendant blocks meet only at \(v\), so
\[
X_v=z\prod_B T_B^X,\quad Y_v^0=\prod_B T_B^0,\quad
Y_v^1=\sum_B T_B^1\prod_{C\ne B}T_C^0.
\]
Empty products equal one and empty sums zero. Products and the one-selected-block sum are jointly evaluated in linear gate count by the update \((p,q)\leftarrow(pa,qa+pb)\), initialized at \((1,0)\), for each pair \((a,b)\). In the multivariate version the leading factor in \(X_v\) is \(z_v\).

For a bridge block \(B=\{v,u\}\), its child endpoint \(u\) already has messages \((X_u,Y_u^0,Y_u^1)\). Directly inspecting the unique edge gives
\[
T_B^X=X_u+Y_u^0,\qquad T_B^0=Y_u^0+Y_u^1,\qquad T_B^1=X_u.
\]

Now let \(B\) be a cyclic block \(v=u_0,u_1,\ldots,u_{\ell-1},u_0\) with \(\ell\ge3\). Give the vertices binary selection bits \(c_0,\ldots,c_{\ell-1}\) (one means selected). For each child vertex \(u_i\), \(i\ge1\), define the local factor \(R_i(a,b,c)\), where \(a,c\) are its two cyclic neighbor bits and \(b\) its own bit:
\[
R_i(a,1,c)=X_{u_i},\qquad
R_i(a,0,c)=\begin{cases}
Y_{u_i}^0+Y_{u_i}^1,&a+c=0,\\
Y_{u_i}^0,&a+c=1,\\
0,&a+c=2.
\end{cases}
\]
For fixed \(c_0=1\), sum \(\prod_{i=1}^{\ell-1}R_i(c_{i-1},c_i,c_{i+1})\) over all choices of the remaining bits, with the boundary convention \(c_\ell=c_0\). This is \(T_B^X\). For \(c_0=0\), take the same sum restricted by \(c_1+c_{\ell-1}=k\), for \(k=0,1\), to obtain \(T_B^k\); discard the possibility \(c_1+c_{\ell-1}=2\). These sums are computable with a constant-size transfer: fix \(c_0,c_1\), propagate the two most recent bits, and apply the local factor for the middle vertex whenever its right-hand neighbor bit is chosen. At the closing edge evaluate the last child factor and the prescribed boundary count. The state count is bounded independently of \(\ell\), so the number of ring operations is \(O(\ell)\).

The local factors enforce exactly the condition that every unselected child vertex sees at most one selected neighbor across its own descendant blocks and its two neighbors in the cycle. The boundary restriction enforces the same at unselected \(v\). Thus each legal vertex assignment is counted once, and no illegal one is counted. Induction upward through the incidence tree proves that all messages have their specified meanings. At the root there is no parent block, so
\[
Q_G(z)=X_r+Y_r^0+Y_r^1.
\]
This proves the formula for every connected cactus, including \(K_1\).

A cactus incidence graph is a tree, so \(\sum_B(|B|-1)=|V(G)|-1\). Therefore \(\sum_B|B|=O(|V(G)|)\); every bridge requires constant work, every cycle linear work in its length, and every vertex linear work in its child-block count. Hence the claimed linear-size arithmetic circuit. A usual block decomposition takes \(O(|V|+|E|)\) time. Coefficient extraction by ordinary polynomial arithmetic is polynomial in \(|V|\), while evaluating at one is linear in arithmetic-operation count.

## Verification
The embedded `verify_cactus_standalone.py` constructs cacti by successively attaching either one edge or a chordless cycle at one existing vertex, independently enumerates every subset to test the \(P_3\)-convexity predicate, and compares all coefficients with the three-state formula. The recorded deterministic run checked 1,211 cases with up to 13 vertices, including simple cycles and mixed block shapes, and returned `VERIFY_OK`. This is corroboration, not the proof for unbounded graph order. Execute `python3 verify_cactus_standalone.py` from the unpacked accompanying files.

## Relationship to prior work
Dourado, Grippo, Lin and Protti (2026) introduced systematic complexity study of counting \(P_3\)-convex sets. Their full paper gives exact linear-time recurrences for trees and threshold graphs and proves general hardness already for split graphs; it does not provide a cactus cycle-block transfer. An earlier restricted result gives an arithmetic circuit on clique-block graphs; cycles of length at least four are not clique blocks and require the cyclic boundary argument above. General bounded-treewidth counting principles already imply abstract tractability of cacti, so *tractability alone is not claimed to be new*. The contribution asserted here is the explicit small-state recurrence/circuit that computes every size coefficient and works with arbitrary interlinked cycles. Work on Cartesian-product \(P_3\)-convexity and hull numbers does not supply such a cactus-block formula.

## Limitations
This is a constructive algebraic-operation bound; it is not a linear bit-complexity bound for exact integer or polynomial outputs. It is not a breakthrough on general #P-completeness, does not cover graphs with noncycle 2-connected blocks, and does not assert priority over all unpublished implementations or equivalent transfer formulations. Formal independent assessment has not been performed.

## References
Dourado, M. C., Grippo, L. N., Lin, M. C., and Protti, F., *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first publicly posted 2026-03-05), especially Theorems 3, 12, and 14 and Section 4.

Brešar, B., and Valencia-Pabon, M., *On the \(P_3\)-hull number of Hamming graphs*, manuscript dated 2019, especially Section 3 (Cartesian products), included for distinction of objects and prior \(P_3\)-convexity structure.
