# Resolving domination of zero-divisor graphs for mixed products of finite fields

## Finding

Let
\[
R=F_1\times\cdots\times F_n,
\qquad n\ge 3,
\]
where every \(F_i\) is a finite field of order \(q_i\). Let
\[
t=\bigl|\{i:q_i=2\}\bigr|
\]
and let \(\Gamma(R)\) be the Anderson--Livingston zero-divisor graph on the nonzero zero-divisors of \(R\). Then
\[
|V(\Gamma(R))|
=\prod_{i=1}^n q_i-\prod_{i=1}^n(q_i-1)-1=:N,
\]
and its resolving-domination number is
\[
\boxed{\gamma_r(\Gamma(R))=N-(2^n-2)+t.}
\]

Thus each binary field factor contributes exactly one additional vertex beyond the universal twin-class lower bound. In particular, the formula specializes to \(\gamma_r(\Gamma(R))=n\) for \(R\cong(\mathbb F_2)^n\), and to \(\gamma_r(\Gamma(R))=N-(2^n-2)\) when every \(q_i\ge3\).

## Assumptions and scope

The graph has the nonzero zero-divisors of \(R\) as vertices, with distinct vertices adjacent exactly when their product is zero. A resolving dominating set is simultaneously a resolving set and a dominating set, and \(\gamma_r\) denotes its minimum cardinality.

The theorem is stated for \(n\ge3\). The two-factor boundary has additional small complete-bipartite and star behavior and is not part of the claim.

## Proof

For a nonempty proper subset \(S\subset[n]\), let \(C_S\) be the set of vertices whose nonzero coordinates occur exactly in \(S\). Then
\[
|C_S|=a_S:=\prod_{i\in S}(q_i-1),
\]
and the classes \(C_S\) partition \(V(\Gamma(R))\). Two vertices from classes \(C_S\) and \(C_T\) are adjacent exactly when
\[
S\cap T=\varnothing.
\]
Hence two distinct vertices in the same class \(C_S\) have identical open neighborhoods. Because \(S\) is proper, they have distance \(2\) from one another through any vertex supported in \([n]\setminus S\). Therefore every resolving set contains at least \(a_S-1\) vertices from each \(C_S\). Summing over the \(2^n-2\) nonempty proper supports gives the lower bound
\[
|W|\ge \sum_S(a_S-1)=N-(2^n-2).
\]

Now let
\[
B=\{i:q_i=2\},
\qquad |B|=t.
\]
For each \(i\in B\), the class \(C_{\{i\}}\) is a singleton; denote its unique vertex by \(u_i\). Also put
\[
D_i=C_{[n]\setminus\{i\}}.
\]
Every vertex of \(D_i\) has exactly one neighbor, namely \(u_i\), because the only nonempty support disjoint from \([n]\setminus\{i\}\) is \(\{i\}\).

Let \(W\) be a resolving dominating set. The twin-class bound says that \(W\) contains at least \(|D_i|-1\) vertices of \(D_i\). If equality holds there, one vertex of \(D_i\) is omitted and must be dominated by its unique neighbor \(u_i\), so \(u_i\in W\). Otherwise all of \(D_i\) lies in \(W\), which is already one vertex above the twin-class lower bound for \(D_i\). Thus, for each \(i\in B\), the pair of support classes
\[
C_{\{i\}},\qquad C_{[n]\setminus\{i\}}
\]
forces at least one extra chosen vertex beyond the twin-class lower bound. Since \(n\ge3\), these pairs are disjoint for distinct \(i\). Consequently
\[
|W|\ge N-(2^n-2)+t.
\]

For the matching upper bound, choose all but one vertex from every support class \(C_S\), and then add the singleton vertex \(u_i\) for every \(i\in B\). Call the resulting set \(W_0\). Its size is exactly
\[
|W_0|=N-(2^n-2)+t.
\]
For every coordinate \(i\), the set \(W_0\) contains a vertex \(w_i\) whose support is exactly \(\{i\}\): if \(q_i=2\), this is the added vertex \(u_i\); if \(q_i\ge3\), then \(|C_{\{i\}}|=q_i-1\ge2\), so at least one vertex of that class remains among the all-but-one selection.

To see that \(W_0\) resolves the graph, only pairs of omitted vertices need consideration. There is at most one omitted vertex in each support class. If omitted vertices \(x\in C_S\) and \(y\in C_T\) have \(S\ne T\), choose \(i\in S\triangle T\), say \(i\in S\setminus T\). Then \(w_i\) is adjacent to \(y\), so
\[
d(y,w_i)=1.
\]
Since \(i\in S\), the supports of \(x\) and \(w_i\) intersect. They are not adjacent, and because \(S\) is proper they have a common neighbor supported in \([n]\setminus S\); hence
\[
d(x,w_i)=2.
\]
Thus \(x\) and \(y\) are distinguished.

Finally, \(W_0\) dominates. If \(x\in C_S\) is omitted, then \(S\ne[n]\), so choose \(i\notin S\). The singleton-support vertex \(w_i\in W_0\) is disjoint from \(S\), hence adjacent to \(x\). Therefore \(W_0\) is resolving and dominating, proving
\[
\gamma_r(\Gamma(R))=N-(2^n-2)+t.
\]

## Verification

The included checker constructs the support-class blow-up graph directly from field orders. It verifies the displayed construction for every field-order pattern with \(3\le n\le5\) and \(q_i\in\{2,3,4\}\), checks the lower-bound accounting class by class, and exhaustively computes the minimum resolving-domination number for all tested instances with at most twelve graph vertices. Every tested instance agrees with the formula and the replay returns `VERIFY_OK`.

## Relationship to prior work

Gaded and Narayana studied precisely the resolving-domination number of zero-divisor graphs of direct products of finite fields. Their 2023 paper proves two endpoint regimes: when all factors have order \(2\), they obtain \(\gamma_r=n\) for \(n\ge3\); when all factors have order at least \(3\), they obtain \(\gamma_r=|V|-(2^n-2)\). Their full paper does not state the mixed-order case in which some, but not all, factors have order \(2\). The theorem above fills that gap and shows that the interpolation is exactly one extra vertex per binary factor.

Ali, Siddiqui, Riaz, Qureshi and Akgül studied the same resolving-plus-domination invariant under the name dominant metric dimension for several zero-divisor graphs, especially \(\mathbb Z_n\), Gaussian residue rings, and quotient polynomial rings. Their 2024 paper does not give a general formula for mixed direct products of three or more finite fields.

A 2026 structural paper on semisimple rings determines the determining number and ordinary metric dimension of zero-divisor graphs of non-Boolean semisimple rings, but it does not treat resolving domination. Thus its generalized-join formulas do not subsume the present invariant.

## Limitations

The theorem is restricted to direct products of at least three finite fields. It does not address arbitrary finite reduced rings with nonfield factors, nor does it classify all minimum resolving dominating sets.

The main residual originality risk is terminological: resolving domination is also called dominant metric dimension in some papers, and an unindexed source could state the same mixed-field formula under that name.

## References

1. S. M. Gaded and N. S. Narayana, “On metric dimension and resolving-domination number of zero-divisor graphs of direct product of finite fields,” *JP Journal of Algebra, Number Theory and Applications* 61(2) (2023), 171–182, DOI 10.17654/0972555523016.
2. N. Ali, H. M. A. Siddiqui, M. B. Riaz, M. I. Qureshi and A. Akgül, “A graph-theoretic approach to ring analysis: Dominant metric dimensions in zero-divisor graphs,” *Heliyon* 10(10) (2024), e30989, DOI 10.1016/j.heliyon.2024.e30989.
3. “On determining number and metric dimension of zero-divisor graph of semisimple rings,” *Ars Combinatoria* 168 (2026), 29–48, DOI 10.61091/ars168-03.
