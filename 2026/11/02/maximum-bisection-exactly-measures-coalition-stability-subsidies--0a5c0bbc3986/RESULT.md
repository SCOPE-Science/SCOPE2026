# Maximum bisection exactly measures coalition-stability subsidies in regular-edge approval elections

## Finding

For every finite nonempty simple undirected \(d\)-regular graph \(H\) on \(2k\) vertices, with \(d\ge1\) and \(k\ge1\), consider a transferable-utility (TU) approval committee game with one candidate for every vertex and one voter for every edge, approving precisely its two endpoints. The committee has \(k\) seats. Write \(n=|E(H)|=kd\) and let the maximum **bisection** size be
\[
B(H)=\max_{T\subseteq V(H),\ |T|=k}|\delta_H(T)|.
\]
For both Chamberlin--Courant (CC) and Proportional Approval Voting (PAV), the exact *cost of stability*, defined as the least nonnegative subsidy to the grand coalition that permits a fully coalition-stable redistribution of total score, is
\[
\operatorname{CoS}_{\mathrm{CC}}(H)=\frac{n-B(H)}2,\qquad
\operatorname{CoS}_{\mathrm{PAV}}(H)=\frac{n-B(H)}4.
\]
A single subsidy-optimal allocation gives **one unit of payoff to each edge-voter**. The original TU core is nonempty for either rule if and only if \(H\) is bipartite. This is a formula for balanced maximum cuts; an unrestricted maximum cut is not interchangeable without a proof that an optimum can be balanced.

## Assumptions and scope

A graph may be disconnected but is simple, loopless, nonempty and regular of common degree \(d\). The vertex count is even. The voter set consists of the distinct edges of the graph. Thus the total number of voters is \(n=kd\); no two graph edges represent the same voter in a simple graph. Each vertex is a candidate, and each edge-voter approves its two endpoints. A winning grand-coalition committee uses exactly \(k\) candidates.

For any voter coalition \(S\subseteq E(H)\), the entitlement is \(q(S)=\lfloor k|S|/n\rfloor=\lfloor|S|/d\rfloor\). A deviating committee \(T\subseteq V(H)\) is admissible when \(|T|\le q(S)\). Its edge-voter's CC score is zero for no approved vertex in \(T\), and one otherwise. Its PAV score is zero, one or \(3/2\) when the number of approved vertices is respectively zero, one or two. Define the coalition's TU worth by
\[
v_R(S)=\max_{|T|\le q(S)}\sum_{e\in S}u_R(e,T),\qquad R\in\{\mathrm{CC},\mathrm{PAV}\}.
\]
An augmented grand-coalition payoff of total \(v_R(E(H))+\Delta\), with nonnegative \(\Delta\), is stable if there are nonnegative real payments \(w_e\) summing to that total and satisfying \(\sum_{e\in S}w_e\ge v_R(S)\) for **every** voter coalition \(S\subseteq E(H)\). Only the grand coalition receives this subsidy; its use does not alter the values of deviating coalitions. This is the standard grand-coalition cost-of-stability convention [2].

## Proof

**1. Exact grand-coalition totals.** Fix a committee \(T\) with \(|T|=k\). Let \(b\) be its cut-edge count, \(i\) its number of internally selected edges, and \(o\) its number of edges entirely outside. Counting the degrees of the selected \(k\) vertices and of the unselected \(k\) vertices gives
\[
kd=2i+b=2o+b=n,\qquad i=o=\frac{n-b}{2}.
\]
Exactly \(b+i\) edge-voters receive CC score one, so the total CC score is \(b+i=(n+b)/2\). Under PAV, a crossing edge scores one, an internally selected edge scores \(3/2\), and an outside edge zero. Thus total PAV score is \(b+(3/2)i=(3n+b)/4\). Both expressions increase with \(b\). Maximizing over balanced selections gives
\[
v_{\mathrm{CC}}(E(H))=\frac{n+B(H)}2,\qquad
v_{\mathrm{PAV}}(E(H))=\frac{3n+B(H)}4.
\]
Here the maximum is over precisely the size-\(k\) committees; all scores are monotone in the selected set, so allowing at most \(k\) produces the same grand optimum.

**2. Every stable augmented payoff totals at least \(n\).** For each candidate \(c\), take its coalition of incident-edge voters \(S_c=\{e\in E(H):c\in e\}\). Regularity gives \(|S_c|=d\), hence \(q(S_c)=1\). That coalition can choose \(\{c\}\), giving CC and PAV score one to each member, and total worth \(d\) (one seat cannot give any voter more than one). Stability forces
\[
\sum_{e\ni c} w_e\ge d
\]
for each of the \(2k\) candidates. Summing the constraints counts each edge-voter twice, yielding
\[
2\sum_{e\in E(H)}w_e\ge2kd=2n,
\qquad\text{so}\qquad \sum_e w_e\ge n.
\]
Therefore \(\Delta\ge n-v_R(E(H))\) for either scoring rule. This conclusion does not assume the payments are symmetric.

**3. An optimal allocation exists for every coalition.** Set \(w_e=1\) for each edge-voter, so the total is exactly \(n\). Fix an arbitrary voter coalition \(S\) and an admissible proposal \(T\) with \(|T|\le q(S)\). For an edge \(e\), both the CC score and PAV score are bounded above by the number of its endpoints in \(T\). Hence, denoting by \(\deg_S(c)\) the number of voters in \(S\) who approve \(c\),
\[
\sum_{e\in S}u_R(e,T)
\le\sum_{c\in T}\deg_S(c)
\le d|T|
\le d\left\lfloor\frac{|S|}{d}\right\rfloor
\le |S|=\sum_{e\in S}w_e.
\]
Maximizing over allowed proposals proves every coalition constraint, including the empty and grand coalitions. Therefore the uniform payment vector is stable after subsidy \(\Delta=n-v_R(E(H))\). Together with Step 2, this is optimal; inserting Step 1 yields the two stated formulae.

**4. Exact zero-subsidy criterion.** Since \(B(H)\le n\), both costs vanish exactly when a size-\(k\) vertex set cuts **every** edge, which makes \(H\) bipartite. Conversely, if \(H\) is bipartite and \(d\ge1\), the two sides of each connected bipartite component have equal cardinalities by regular degree-counting. Joining one side from every component therefore gives exactly \(k\) vertices and cuts all \(n\) edges, so \(B(H)=n\). This proves the equivalence even for disconnected graphs.

## Verification

The standard-library Python file `verify.py` reproduces finite arithmetic checks independently of the algebraic argument. Run `python3 verify.py` alongside this document. The checker enumerates every labeled simple graph on two, four and six vertices, selects exactly those that are nonempty and regular, evaluates each balanced committee, and compares direct CC/PAV scores to the formula. There are respectively \(1\), \(7\) and \(171\) qualifying graphs at those orders, covering every regular degree. It also independently checks the bipartiteness criterion by graph coloring. On seven named test graphs (a single edge, two even cycles, a complete four-vertex graph, two disjoint triangles, a triangular prism and a complete six-vertex graph) the checker additionally examines **every** voter coalition and every committee within that coalition's seat entitlement, verifying the uniform-payment domination and singleton-committee demands. It prints `VERIFICATION_OK` on success. These finite tests check the implementation and examples; the unlimited-size theorem follows from the analytical proof, not finite enumeration.

For the four-vertex complete graph, \(n=6\) and \(B(H)=4\), so the exact subsidies are \(1\) for CC and \(1/2\) for PAV, consistent with the six-voter pre-existing nonexistence example in [1]. The disconnected union of two triangles has the same subsidies but demonstrates that connectedness is unnecessary. Every bipartite regular graph has zero cost by Step 4.

## Relationship to prior work

Chen and Hatschka [1] define TU multiwinner voting games with exactly the proportional seat-cap convention above, and Proposition 2 gives the complete-four-vertex example where the unaugmented TU core is empty for CC and PAV. That six-voter example and its four one-seat supporter constraints are **prior results**. Our graph family generalizes its edge-incidence construction, but the new assertion is the sharp, all-regular-graphs *quantitative* cost-of-stability identity in terms of maximum bisection, the uniform optimal payoff, and the exact bipartite/nonbipartite division. The inspected paper's Proposition 2 and main existence/complexity results do not give those formulas.

Bachrach and coauthors [2] define the external-payment cost of stability for cooperative games and provide general results, particularly for weighted voting games. Their generic model permits this new specialized calculation, but their results do not imply the balanced-max-cut evaluation and the all-coalitions constructive payment for edge-generated CC/PAV games. Becker, Greger and Peters [3] establish existence of an approval-based committee in the *ordinary nontransferable-utility* core, not existence or subsidy cost for the transferred-score cores studied here. This distinction matters: the no-subsidy TU cores in this theorem can be empty despite existence of an NTU-stable committee.

## Limitations

The formula assumes exactly one edge-voter for each edge of a **regular** simple graph, a committee of half its vertices, and the stated CC or PAV cardinal-score rules. It does not cover irregular graphs, arbitrary approval ballots, unequal edge weights, other seat entitlements or unrelated transfer models. It does not imply that a best bisection can be found efficiently. The original four-vertex obstruction and the general concept of subsidy are credited to the earlier literature. Claims of priority beyond the inspected sources are subject to unindexed or inaccessible earlier specializations. Self-review was performed; independent scientific validation has not been performed.

## References

[1] J. Chen and C. Hatschka, *Multi-Winner Voting Games in TU and NTU: When is the Core Always Non-Empty?*, arXiv:2605.22528v1, first posted 2026-05-21, especially Section 2 and Proposition 2. https://arxiv.org/pdf/2605.22528

[2] Y. Bachrach, E. Elkind, R. Meir, D. Pasechnik, M. Zuckerman, J. Rothe and J. S. Rosenschein, *The Cost of Stability in Coalitional Games*, arXiv:0907.4385v1, 2009, especially Section 3. https://arxiv.org/pdf/0907.4385

[3] P. Becker, M. Greger and D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912v1, first posted 2026-09-10, especially Theorem 1 and the Introduction. https://arxiv.org/pdf/2609.11912
