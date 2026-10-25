# Strict absolute monotonicity of one-point types under graph-cell attachments

## Finding
Fix a labeled set \(V\) with \(n\ge0\) vertices. For any simple graph \(H=(V,E)\), construct the finite **incidence poset** \(P_H\) with one point for each vertex, one separate point for each edge, and only the strict comparisons \(v<e\) when \(v\) is incident to \(e\). Embed and individually name these \(n+|E|\) points in the countable universal homogeneous partial order \(\mathbb P\). Let \(t_n(E)\) be the number of complete **nonalgebraic** one-types over the named points.

Write \(e_H(A)=|E(H[A])|\) for \(A\subseteq V\), and \(Z_H=\sum_{A\subseteq V}2^{e_H(A)}\). The underlying census is
\[
t_n(E)=2Z_H-1+\sum_{v\in V}(2^{\deg_H(v)}-1)+|E|. \tag{1}
\]
The principal result concerns **all-order simultaneous sensitivity**, not just the specialized count (1). If \(F\) is any nonempty set of distinct edges absent from \(H\), let \(V(F)\) denote their endpoints and \(\delta(v)\) the set of potential edges in the complete graph on \(V\) incident with \(v\). Put
\[
\Delta_Ft_n(E)=\sum_{S\subseteq F}(-1)^{|F|-|S|}t_n(E\cup S).
\]
Then for every \(n\), every existing \(E\), and every nonempty missing-edge set \(F\),
\[
\boxed{\Delta_Ft_n(E)=2\sum_{A\supseteq V(F)}2^{e_H(A)}+\sum_{v:\,F\subseteq\delta(v)}2^{\deg_H(v)}+\mathbf1_{\{|F|=1\}}>0.} \tag{2}
\]
The first sum is over \(A\subseteq V\); the second is over \(v\in V\). In particular \(t_n\) is **strictly absolutely monotone on the edge Boolean lattice**: every nonempty mixed discrete derivative is positive, including derivatives of arbitrarily high order. Equivalently, its Boolean Möbius coefficients are all positive, with explicit formula
\[
\boxed{t_n(E)=2^{n+1}-1+\sum_{\varnothing\ne F\subseteq E}\left(2^{n-|V(F)|+1}+s(F)+\mathbf1_{\{|F|=1\}}\right),} \tag{3}
\]
where \(s(F)=|\{v\in V:F\subseteq\delta(v)\}|\). The term \(s(F)\) counts common endpoints of every edge of \(F\). The coefficient in (3) is *strictly* positive for any possible \(F\). The edge-edit operation here **adds one new upper parameter point** to \(P_H\) per newly inserted graph edge; it is not the different operation of inserting a comparability between two existing poset points.

As one natural special case, the incidence poset of the simple cycle \(C_m\), \(m\ge3\), is the \(2m\)-point crown. With the classical Lucas numbers \(L_0=2,L_1=1,L_{j+2}=L_{j+1}+L_j\),
\[
t_m(E(C_m))=2L_{2m}+4m-1,\qquad m\ge3. \tag{4}
\]
Formula (4) is a concrete instance of the more general sensitivity law, **not** an assertion that the known Lucas count of crown order ideals is new.

## Assumptions and scope
The graph is finite, undirected, loop-free, and simple. The vertex set remains fixed in all finite differences; each selected missing edge creates a new, distinct maximal parameter in the incidence poset. Isolated vertices and the empty graph are permitted. Nonalgebraic means the new realization differs from every named parameter; the complete type count including equality types is \(t_n(E)+n+|E|\), which does **not** obey precisely the same formula (2), because the algebraic count changes linearly with \(|E|\). The countably infinite random poset realizes every finite induced one-point extension, and its homogeneity identifies these with complete types.

## Proof
**One-point extension reduction.** For a finite parameter poset \(P\), a nonalgebraic one-point extension \(x\) is determined by a downset \(L=\{p:p<x\}\) and an upset \(U=\{p:x<p\}\) with \(\ell<u\) for all \(\ell\in L,u\in U\). The Fraïssé extension and homogeneity properties realize each admissible pair in one complete one-type. This characterization is classical and is not a claimed new component.

Pairs with \(U=\varnothing\) contribute \(J(P)\), the number of downsets, and pairs with \(L=\varnothing\) contribute the same number of upsets. The double-empty pair is counted twice; hence their union contributes \(2J(P)-1\). In the incidence order \(P_H\), if both sets are nonempty, then \(L\) consists entirely of lower vertices and \(U\) entirely of upper edge-points. If \(|L|=1\), say \(L=\{v\}\), any nonempty subset of the \(\deg_H(v)\) edge-points incident with \(v\) can form \(U\). This gives \(2^{\deg_H(v)}-1\). If \(|L|=2\), both vertices must be endpoints of a common edge, and simplicity makes that edge unique, giving one pair for each \(e\in E\). If \(|L|\ge3\), no edge-point lies above all its members. Thus the number of two-nonempty-side pairs is \(\sum_v(2^{\deg_H(v)}-1)+|E|\).

For a downset of \(P_H\), first choose its lower vertices \(A\subseteq V\). An upper edge-point can be included independently exactly when **both** endpoints lie in \(A\). There are \(2^{e_H(A)}\) possibilities. Hence \(J(P_H)=Z_H\), proving (1).

**All mixed differences.** Fix a nonempty missing-edge set \(F\). For every \(A\subseteq V\) and \(S\subseteq F\),
\[
2^{e_{H\cup S}(A)}=2^{e_H(A)}\prod_{f\in S}2^{\mathbf1_{\{f\subseteq A\}}},
\]
where \(f\subseteq A\) means both endpoints belong to \(A\). Taking the alternating sum over \(S\subseteq F\) yields
\[
\sum_{S\subseteq F}(-1)^{|F|-|S|}2^{e_{H\cup S}(A)}=2^{e_H(A)}\prod_{f\in F}\left(2^{\mathbf1_{\{f\subseteq A\}}}-1\right)=2^{e_H(A)}\mathbf1_{\{V(F)\subseteq A\}}.
\]
Summing over \(A\) and multiplying by \(2\) gives the first term of (2). Similarly, for a given vertex \(v\), the alternating difference of \(2^{\deg(v)}\) equals \(2^{\deg_H(v)}\) precisely when \(v\) belongs to **every** edge in \(F\), and vanishes otherwise. Constants contribute zero. The term \(|E|\) contributes one when \(|F|=1\) and zero for higher orders. These are exactly the remaining terms of (2).

The first sum contains \(A=V\) and is therefore positive, proving **strict** positivity even for widely separated missing edges and arbitrarily large \(|F|\). At \(E=\varnothing\), its value is \(2^{n-|V(F)|+1}\), and the degree term equals \(s(F)\). Möbius inversion on the edge Boolean lattice now gives (3), with the empty-edge constant \(t_n(\varnothing)=2^{n+1}-1\).

**Crown case.** If \(H=C_m\), the incidence comparability graph of \(P_H\) is an alternating cycle on \(2m\) vertices. Downsets correspond to antichains, hence to independent sets of that cycle, counted by \(L_{2m}\). Every original graph vertex has degree two, so the correction to \(2J(P_H)-1\) is \(m(2^2-1)+m=4m\); this proves (4). The Lucas enumeration itself is classical.

## Verification
Run the standalone standard-library program `verify_incidence_types.py` using `python verify_incidence_types.py`. A saved output record is `verify_output.txt`. The independent direct method enumerates all \(3^{n+|E|}\) ternary insertion relations for every graph on up to four labeled vertices, filters them by actual transitivity, and compares against (1). It separately checks 1,284 mixed-difference identities of orders one through three and compares the crown formula for ten cycle lengths. The logged execution ends in `ALL_TESTS_PASS`.

These finite checks verify implementation consistency. All-size positivity, exact census and Möbius expansion are established by the proof, not finite enumeration.

## Relationship to prior work
The correspondence between one-point extensions of finite posets and compatible downset/upset pairs is prior mathematics; Dolinka–Mašulović (2010/2012) use it in their work on endomorphism monoids, and Hubička (2010) develops an explicit generic poset. An earlier exact finite-height-two type-count formula (published research record cited below) applies to incidence posets **pointwise** and so gives a different, broader route to individual values of \(t_n(E)\). Formula (1) is presented as a derivation for the specialized graph parameter family, not itself as the novelty claim. The contribution of (2)–(3) is a *simultaneous*, all-orders, strictly positive relation among counts for different edge sets, with explicit mixed coefficients, which is not stated by the published individual-census formula.

A separate previous result studies the effect of adding an order-comparability between already-named elements of a fixed bipartite parameter poset; that operation can have negative sensitivity. Here a graph edge instead becomes a **new named upper cell**, changing the parameter set. Confusing those operations would yield a false implication comparison. The existing crown order-polytope literature already gives the Lucas number of crown ideals; (4) is consequently a check and concrete application, not a standalone novelty claim. A title-level search for graph-induced partition functions alone cannot prove that this positivity law was unpublished.

## Limitations
The theorem does not say that the graph-incidence poset one-type count is computationally easy for arbitrary graphs, nor does it claim any complexity classification or approximation scheme. The proof uses graph simplicity in its two-element-lower-set case. It does not address multiplicities for loops or hyperedges, and it does not concern adding an order relation without adding a new parameter. Despite targeted database and literature comparison, an equivalent, unindexed statement of the all-order difference law cannot be excluded. The result has not undergone independent scientific auditing.

## References
1. Jan Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566, initial posting 2010-09-03, §3 on the generic partial order, https://arxiv.org/html/1009.0566v1.
2. Igor Dolinka and Dragan Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892 (initial posting 2010-09-15), §3.1, subsequently *Proc. Edinburgh Math. Soc.* 55 (2012), 635–656, https://arxiv.org/abs/1009.2892.
3. Teemu Lundström and Leonardo Saud Maia Leite, *Order polytopes of crown posets*, arXiv:2504.05123 (first posting 2025-04-07), §3 and Corollary 3.9, https://arxiv.org/html/2504.05123v2.
4. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly indexed mathematical record, section on the ideal/filter characterization and full finite-parameter type-count theorem, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1/RESULT.md.
