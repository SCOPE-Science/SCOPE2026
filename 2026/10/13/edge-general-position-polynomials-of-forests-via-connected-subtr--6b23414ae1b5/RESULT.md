# Edge-general-position polynomials of forests via connected-subtree boundaries

## Finding

For any finite simple tree \(T\), let \(m=|E(T)|\) and define the edge-general-position polynomial
\[
\mathcal E_T(z)=\sum_{S\subseteq E(T),\ S\text{ edge-general-position}}z^{|S|},
\]
where a set of edges is *edge-general-position* when no path in \(T\) contains three of its edges. Define the connected-boundary polynomial
\[
\mathcal C_T(z)=\sum_{\substack{\varnothing\ne K\subseteq V(T)\\ T[K]\text{ connected}}}z^{|\delta_T(K)|},
\]
where \(\delta_T(K)\) is the set of edges with exactly one endpoint in \(K\). Then the **complete counting identity** is
\[
\boxed{\mathcal E_T(z)=\mathcal C_T(z)-m z.}
\]
Thus for every \(k\ge2\), the number of \(k\)-edge-general-position sets equals the number of nonempty connected vertex subsets with edge boundary of cardinality \(k\), and the coefficient of \(z\) is \(m\). The formula also covers the one-vertex tree, when both polynomials equal \(1\).

For a rooted tree with root \(r\), write \(\mathrm{ch}(v)\) for the children of \(v\). Set
\[
B_v(z)=\prod_{u\in\mathrm{ch}(v)}\bigl(z+B_u(z)\bigr),\qquad
\mathcal C_T(z)=B_r(z)+z\sum_{v\ne r} B_v(z),
\]
with an empty product equal to \(1\). These identities constitute a rooted-tree recurrence for every coefficient, evaluable with \(O(n^3)\) integer arithmetic operations for a tree on \(n\) vertices. For a forest \(F\) with components \(T_1,\ldots,T_q\), define the polynomial componentwise and obtain
\[
\boxed{\mathcal E_F(z)=\prod_{j=1}^{q}\mathcal E_{T_j}(z).}
\]
The empty forest has polynomial \(1\).

There is also an exact extremal multiplicity formula. If \(T\) is not a path and has \(\ell\ge3\) leaves, let \(\lambda_1,\ldots,\lambda_\ell\) be the edge lengths of the leaf arms: the paths from the leaves to their first vertices of degree at least three. Then
\[
\deg \mathcal E_T=\ell,\qquad
\boxed{[z^\ell]\mathcal E_T(z)=\prod_{i=1}^{\ell}\lambda_i.}
\]
For a path with \(m\ge2\) edges, \(\mathcal E_T(z)=1+mz+\binom m2 z^2\); for \(m=0\) or \(1\), it is \(1+mz\).

## Assumptions and scope

All graphs are finite, simple, undirected and acyclic. Paths in a tree are unique and therefore geodesics. A connected vertex subset means one whose induced graph is connected; the empty subset is excluded from \(\mathcal C_T\). The formulas count labeled vertex/edge subsets, not isomorphism classes. A forest is handled by the independent choices of valid edge subsets within its connected components. The tree-only boundary identity is not claimed for arbitrary graphs with cycles.

## Proof

**(1) Quotient characterization.** Fix a subset \(S\subseteq E(T)\) of cardinality \(k\). Contract every edge of \(T\setminus S\). Since \(T\) is a tree, the resulting quotient \(Q_S\) is a tree with exactly \(k\) edges. Every vertex of \(Q_S\) represents a connected component of \(T-S\). For any two vertices of \(T\), the number of edges of \(S\) lying on their unique connecting path is exactly the graph distance between their quotient vertices. Conversely every pair of quotient vertices has original representatives. Hence \(S\) is edge-general-position if and only if \(Q_S\) has diameter at most two.

**(2) Connected-boundary bijection.** If \(k\ge2\), a tree on \(k\) edges has diameter at most two if and only if it is a star. Such a star has a unique center (the vertex of degree \(k\), including \(k=2\)). Let \(K\) be the connected vertex set of \(T\) represented by the central vertex of \(Q_S\). All edges of \(S\) have exactly one endpoint in \(K\). Any edge with one endpoint in \(K\) and one outside must be in \(S\), since otherwise its endpoints would lie in the same component of \(T-S\). Thus \(S=\delta_T(K)\). This determines \(K\) uniquely.

Conversely let \(K\ne\varnothing\) induce a connected subtree and suppose \(k=|\delta_T(K)|\ge2\). Removing the boundary edges isolates \(K\). Every component of the complement is incident to exactly one boundary edge, since two such edges would create a cycle in \(T\). Contracting edges outside \(\delta_T(K)\) therefore produces a star with center \(K\) and \(k\) leaves. Its diameter is at most two, so \(\delta_T(K)\) is an edge-general-position set. The maps are inverse for \(k\ge2\).

For \(k=0\), the only edge subset is \(\varnothing\), and the only connected nonempty vertex set with no edge boundary is \(V(T)\). For \(k=1\), each individual edge is valid, while deleting that edge produces two (and exactly two) connected vertex sides having that edge as boundary. Consequently \([z]\mathcal C_T=2m\), \([z]\mathcal E_T=m\), and the displayed identity follows for all coefficients.

**(3) Rooted recurrence.** Fix a root \(r\). For a vertex \(v\), let \(B_v(z)\) count connected vertex subsets inside the descendant subtree at \(v\), containing \(v\), weighted by the number of edges from that selected subset to descendant vertices not selected. For each child \(u\), either no vertex in its descendant subtree is selected (giving one boundary edge and factor \(z\)) or a connected selected set containing \(u\) is chosen (factor \(B_u\)). These mutually exclusive and independent choices prove the product formula, by induction from leaves. Every nonempty connected selected subset has a unique highest vertex \(v\); its boundary weight is \(B_r\) when \(v=r\), and \(zB_v\) when \(v\ne r\), because then the edge to its parent is additional boundary. Summing proves the recurrence for \(\mathcal C_T\), and the identity gives \(\mathcal E_T\). Standard degree-bounded polynomial multiplication over all child products takes at most \(O(n^3)\) arithmetic operations.

**(4) Forest factorization.** A path stays within one component. An edge subset of a forest is valid exactly when each componentwise restriction is valid; weights add and choices multiply. The polynomial factorization follows.

**(5) Number of maximum sets.** Suppose \(T\) has at least one branching vertex and \(\ell\ge3\) leaves. For a nonempty connected \(K\), each connected component of \(T-K\) is joined to \(K\) by exactly one boundary edge and contains at least one original leaf. Since these outside components are disjoint, \(|\delta_T(K)|\le\ell\). Equality holds exactly when each outside component contains one original leaf; it forces every branching vertex into \(K\), since excluding a branching vertex would place at least two leaves in its outside component. A connected \(K\) containing every branching vertex contains every path between them. Therefore its boundary cuts precisely once along each of the \(\ell\) terminal leaf arms. Conversely any independent choice of one of the \(\lambda_i\) edges on each such arm determines a connected central \(K\) with boundary \(\ell\). The bijection in (2) proves the product formula for maximum edge-general-position sets. For paths, every edge subset of cardinality at most two is valid and no larger one is (unless the path has fewer than two edges), establishing all path cases.

## Verification

The accompanying Python-standard-library executable `verify.py` independently enumerates all edge subsets and all tree vertex-pair geodesics, then compares coefficients with the connected-boundary recurrence. Its output is in `verification_output.txt`. It covers all labeled trees of orders one through seven via Prüfer sequences, plus reproducibly sampled labeled trees up to order eleven, checking 1,429,023 candidate edge subsets across 19,254 trees. Additional direct connected-boundary calculations cover 3,039 trees, and the independent leaf-arm product test covers 16,251 nonpath trees. The program also checks disconnected forests, isolated vertices, star examples and path examples. These finite checks test the implementation; the infinite-family conclusion rests on the proof above.

## Relationship to prior work

Manuel, Prabha and Klavžar introduced the edge-general-position concept in 2021 and proved that its maximum cardinality on trees equals the number of leaves. That scalar maximum is not new here. Tian, Klavžar and Tan studied extremal edge-general-position sets on several graph families, including block graphs. The 2022 generalization treats edge \(k\)-general-position extrema and geodesic covers. Iršič, Klavžar, Rus and Tuite introduced cardinality polynomials for **vertex** general-position sets; these are not the edge-general-position enumerators considered here. The theorem here connects all edge-general-position sets of a tree to connected edge boundaries, gives their complete polynomial and counts the maximum sets. General connected-subtree boundary enumerations are an existing combinatorial theme; the claim does not assert that such auxiliary polynomials or elementary product recurrences were previously unknown.

## Limitations

The boundary bijection depends on unique paths and need not extend to cyclic graphs. The method counts every edge-general-position set but does not classify all coefficient shapes, real roots or unimodality. The leading coefficient expression applies as stated to nonpath trees; the path cases are separate. The literature comparison found no equivalent edge-general-position forest polynomial in the inspected works, but does not establish absolute priority over unindexed or inaccessible literature. No independent external validation has occurred.

## References

1. Paul Manuel, R. Prabha, Sandi Klavžar, “Edge General Position Problem,” arXiv:2105.04292, first public 10 May 2021, https://arxiv.org/abs/2105.04292.
2. Paul Manuel, R. Prabha, Sandi Klavžar, “Generalization of Edge General Position Problem,” arXiv:2207.07357, 15 July 2022, https://arxiv.org/abs/2207.07357.
3. Jing Tian, Sandi Klavžar, Elif Tan, “Extremal Edge General Position Sets in Some Graphs,” arXiv:2302.01587, 3 February 2023, https://arxiv.org/abs/2302.01587.
4. Vesna Iršič, Sandi Klavžar, Gregor Rus, James Tuite, “General Position Polynomials,” arXiv:2401.05696, 2024, https://arxiv.org/abs/2401.05696.
