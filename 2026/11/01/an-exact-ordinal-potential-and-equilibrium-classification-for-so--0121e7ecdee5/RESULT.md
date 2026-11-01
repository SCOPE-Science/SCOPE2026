# An exact ordinal potential and equilibrium classification for social-distancing network creation on cactus hosts

## Finding

For the bilateral social-distancing network creation game on **any finite connected simple cactus host** \(H\) and **every** \(\alpha>0\), the set of connected spanning states admits an exact ordinal potential. Every sequence of strictly improving admissible single-edge moves terminates; every pairwise-stable state is characterized independently on each cycle, and the number and social welfare of all equilibria admit explicit cycle-product formulas. The same decomposition computes a social optimum and both extreme equilibrium welfare values in polynomial time.

A cactus is a finite connected simple graph whose edges belong to at most one simple cycle. All vertices and edges are labeled. Define \(d_F(x,y)\) as shortest-path distance in a connected graph \(F\). Let \(\mathcal C\) be the family of distinct simple cycles of \(H\). For each cycle edge \(e=\{a,b\}\), define

\[
q_a(e)=\sum_{z\in V(H)}\left[d_{H-e}(a,z)-d_H(a,z)\right],\quad
q_b(e)=\sum_{z\in V(H)}\left[d_{H-e}(b,z)-d_H(b,z)\right],\quad
\tau_e=\max\{q_a(e),q_b(e)\}.
\]

For each cycle \(C\), put \(M_C=\max_{e\in E(C)}\tau_e\). Let \(\bot\) denote retaining that entire cycle, and let symbol \(e\) denote deleting its edge \(e\). Then the exact set of independently allowed equilibrium choices for \(C\) is

\[
\mathcal E_C(\alpha)=
\{\bot: \alpha\ge M_C\}\cup\{e\in E(C):\alpha\le\tau_e\},
\]

with the first set interpreted as empty when its condition fails. Thus

\[
\#\{\text{pairwise-stable connected spanning states}\}
=\prod_{C\in\mathcal C}\left(\mathbf1_{\{\alpha\ge M_C\}}+
\sum_{e\in E(C)}\mathbf1_{\{\alpha\le\tau_e\}}\right).
\]

An empty product is one, covering tree hosts. Every factor is positive.

## Assumptions and scope

Let \(H=(V,E)\) be any finite, connected, undirected, simple cactus with \(|V|\ge2\) and \(\alpha>0\). A state is any connected spanning subgraph \(G=(V,F)\) with \(F\subseteq E\). Each player \(v\) maximizes

\[
u_v(G)=\alpha\deg_G(v)+\sum_{z\in V}d_G(v,z).
\]

An existing edge may be deleted unilaterally by either endpoint if the resulting graph stays connected and the deleting endpoint's utility strictly increases. A missing host edge may be added only when **both** endpoints strictly increase utility. There are no simultaneous multiedge moves, no disconnected states, and no edge additions outside the host. Ties never count as improvements. This is the pairwise-stability convention in the source model.

For a state \(G\), bridges of \(H\) must remain. For every \(C\in\mathcal C\), the state contains either all of \(E(C)\) or precisely \(E(C)\setminus\{e\}\) for one edge \(e\). Denote that cycle's choice by \(s_C(G)\in\{\bot\}\cup E(C)\).

## Proof

**1. Cactus decomposition and its distance identity.** The block-cut incidence structure of a connected cactus is a tree, and every block is either a bridge or one of the edge-disjoint simple cycles. If two edges in the same cycle were deleted, some arc between consecutive articulation/ordinary vertices would disconnect; a deleted bridge also disconnects. Conversely, deleting at most one edge from each cycle and no bridges leaves every block connected, hence the graph connected. This establishes the state representation above.

For any two vertices \(x,y\), there is a unique block-cut-tree itinerary joining them. Its geodesic length equals the sum of shortest distances through the blocks on that itinerary: a path exiting a block and later returning would revisit the same articulation point and cannot shorten a simple path. Replacing a cycle by its single-edge-deleted path changes only that cycle's term. Consequently, if \(R=E(H)\setminus E(G)\), then **for all** \(x,y\in V\),

\[
d_G(x,y)-d_H(x,y)=\sum_{e\in R}\left(d_{H-e}(x,y)-d_H(x,y)\right).
\tag{1}
\]

Each sum on the right has at most one term from each cycle. Equation (1) is an identity, not a first-order approximation, and holds even when distinct cycles share articulation vertices.

**2. Exact potential.** Define

\[
\Phi_\alpha(G)=\sum_{C\in\mathcal C}\phi_C(s_C(G)),\qquad
\phi_C(\bot)=\alpha,\quad\phi_C(e)=\tau_e.
\]

When \(C\) is intact and \(e=\{a,b\}\in E(C)\) is deleted, equation (1) shows that the utility changes at the endpoints are exactly \(q_a(e)-\alpha\) and \(q_b(e)-\alpha\), independent of changes on the other cycles. Such a deletion is strictly profitable for at least one endpoint exactly when \(\tau_e>\alpha\), which is exactly when \(\Phi_\alpha\) increases. When \(e\) is the unique missing cycle edge, adding it raises utilities by exactly \(\alpha-q_a(e)\) and \(\alpha-q_b(e)\). Both are strictly positive exactly when \(\alpha>\tau_e\), again precisely when the potential increases. No other edge move is feasible. Thus the potential strictly increases on **every** improving move. The finite state space implies finite termination, without any assumption of fair scheduling.

**3. Complete equilibrium classification.** An intact cycle permits no improving edge deletion precisely if \(\alpha\ge\tau_e\) for every edge \(e\) on it, equivalently \(\alpha\ge M_C\). A broken cycle with missing edge \(e\) permits no improving addition precisely if \(\alpha\le\tau_e\). These comparisons involve no other cycle, so the equilibrium set is the Cartesian product \(\prod_{C\in\mathcal C}\mathcal E_C(\alpha)\). If \(\alpha\ge M_C\), the intact choice is valid; if \(\alpha<M_C\), an edge attaining \(M_C\) is a valid broken choice. Hence every factor is nonempty, including threshold equality.

**4. Exact welfare optimization and efficiency.** Define the ordered-pair distance increment and the net welfare increment

\[
Q_e=\sum_{x,y\in V}\left[d_{H-e}(x,y)-d_H(x,y)\right],
\qquad \omega_e(\alpha)=Q_e-2\alpha.
\]

Let \(W(G)=\sum_v u_v(G)\). Degree sums contribute \(2\alpha|E(G)|\), while equation (1) splits the entire ordered-pair distance sum. Therefore

\[
W(G)=W(H)+\sum_{C:s_C(G)\ne\bot}\omega_{s_C(G)}(\alpha).
\tag{2}
\]

The optimal welfare equals

\[
W_{\mathrm{opt}}=W(H)+\sum_{C\in\mathcal C}\max\left(0,\max_{e\in E(C)}\omega_e(\alpha)\right).
\tag{3}
\]

For exact stable-welfare extrema, define \(A_C(\alpha)=\{0:\alpha\ge M_C\}\cup\{\omega_e(\alpha):e\in E(C),\alpha\le\tau_e\}\), retaining values as a multiset if counts are desired. Then

\[
W_{\mathrm{best\,stable}}=W(H)+\sum_C\max A_C(\alpha),\qquad
W_{\mathrm{worst\,stable}}=W(H)+\sum_C\min A_C(\alpha).
\]

All welfares are positive (connected graph, positive \(\alpha\)), so the exact price of stability and price of anarchy are respectively \(W_{\mathrm{opt}}/W_{\mathrm{best\,stable}}\) and \(W_{\mathrm{opt}}/W_{\mathrm{worst\,stable}}\). The cycles, all \(\tau_e\) and \(Q_e\), and these formulas can be evaluated by repeated breadth-first search in \(O(|V|^3)\) time on a cactus, since it has \(O(|V|)\) edges.

**5. A structural inefficiency family.** Take a triangle on \(a,b,c\), attach \(k-1\) leaves to each of \(a\) and \(b\), with integer \(k\ge2\). All three cycle edges satisfy \(\tau_e=k\). Directly from equation (1), the welfare gains from deleting \(\{a,b\}\), \(\{a,c\}\), or \(\{b,c\}\) are, respectively,

\[
2(k^2-\alpha),\qquad2(k-\alpha),\qquad2(k-\alpha).
\]

For \(k<\alpha<k^2\) the intact host is the **unique** stable network, yet deleting the edge between the two high-attachment vertices is the unique social optimum. In particular,

\[
W(H)=2\alpha(2k+1)+10k^2-4k,
\qquad
\operatorname{PoS}=
1+\frac{2(k^2-\alpha)}{2\alpha(2k+1)+10k^2-4k}>1.
\]

For the concrete case \(k=5\), \(\alpha=10\), stable welfare is \(450\) and optimal welfare is \(480\). With \(\alpha=k+\tfrac12\), the price of stability tends to \(8/7\) as \(k\to\infty\).

## Verification

Execute `python3 verification/cactus_check.py` from the extracted package root (Python 3.10 or later; standard library only). It deterministically checks 1,093 cactus/parameter instances and 26,710 connected states, comparing every permissible edge move with its potential threshold, the stable-state product formula, all welfare values, and the independently computed optimum. For 1,526 small states it separately enumerates every edge subset and tests the connected-state representation. Its exact-rational arithmetic checks all ties and inequalities without floating-point error. The eleven-vertex example is also checked directly. These tests support the formulas but do not replace the all-size block-decomposition proof above.

## Relationship to prior work

Friedrich, Gawendowicz, Lenzner and Melnichenko introduced this game; its preprint was first public on 2022-04-21. Their complete and general-host analyses give parameter-range existence/efficiency theorems, and they exhibit improving-response cycles in the unrestricted class (their Theorem 4). They also explicitly discuss a cycle host with a unique stable yet inefficient outcome. Those results are **not** claimed as novel here. The new conclusion is the full cactus-host, all-parameter cycle-factorization, its exact ordinal potential, and the resulting complete enumeration/optimization formulas. The cited general-host sufficient bounds and cycle examples do not state or directly furnish that characterization. A novel result is not certified solely by the absence of search matches.

## Limitations

The cactus assumption is essential to the stated proof; networks with an edge in multiple cycles may have coupled distance changes and improvement cycles. The model requires connected states and exactly the source's asymmetric deletion/bilateral-addition rule. The result does not characterize disconnected states, multi-edge coalition moves, edge weights, or external nonhost edges. The literature comparison is a best-knowledge search, not an independent novelty certification.

## References

1. Tobias Friedrich, Hans Gawendowicz, Pascal Lenzner and Anna Melnichenko, *Social Distancing Network Creation*, arXiv:2204.10423v1, first public 2022-04-21, https://arxiv.org/abs/2204.10423.
2. Same authors, *Social Distancing Network Creation*, ICALP 2022, LIPIcs 229, article 62, https://doi.org/10.4230/LIPIcs.ICALP.2022.62.
3. Same authors, *Social Distancing Network Creation*, *Algorithmica* 85 (2023), 2087–2130, https://doi.org/10.1007/s00453-022-01089-6; accessible full text https://link.springer.com/article/10.1007/s00453-022-01089-6.
