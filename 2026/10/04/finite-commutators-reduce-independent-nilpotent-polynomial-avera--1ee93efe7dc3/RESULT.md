# Finite commutators reduce independent nilpotent polynomial averages to the commuting case
## Finding
Let \((X,\mathcal X,\mu,T_1,\ldots,T_\ell)\) be a probability-preserving system, and let \(H=\langle T_1,\ldots,T_\ell\rangle\) be 2-step nilpotent with finite commutator subgroup \([H,H]\). Suppose every \(T_i\) is totally ergodic. If \(p_1,\ldots,p_\ell\in\mathbb Z[n]\) are independent, meaning that no nonzero linear combination of them is constant, then for every \(f_1,\ldots,f_\ell\in L^\infty(\mu)\),
\[
\frac1N\sum_{n=1}^N\prod_{i=1}^\ell T_i^{p_i(n)}f_i
\longrightarrow
\prod_{i=1}^\ell\int f_i\,d\mu
\]
in \(L^2(\mu)\).

Consequently, the independent-polynomial joint-ergodicity conjecture posed by Koutsogiannis, Kuca and Sun is true throughout the finite-commutator part of the 2-step nilpotent setting. In particular, any genuinely new obstruction to their same-degree model problem must use an infinite commutator subgroup.

## Assumptions and scope
All transformations are invertible and measure preserving. The group \(H\) is assumed nilpotent of class at most two, so \([H,H]\) is central. Its finiteness is essential to the reduction below. Total ergodicity means that \(T_i^m\) is ergodic for every integer \(m\ge1\). The polynomial-independence hypothesis is the one used in the commuting joint-ergodicity literature: the images of the \(p_i\) modulo constants are linearly independent.

The statement concerns the product-limit conclusion under total ergodicity. It does not assert the more general seminorm estimate requested in the non-totally-ergodic setting.

## Proof
Let \(q\) be the exponent of the finite group \([H,H]\). Because \(H\) has nilpotency class at most two, commutators are central and
\[
[x^q,y]=[x,y]^q
\]
for all \(x,y\in H\). Hence \([T_i^q,T_j]=e\) for every \(i,j\). Put \(U_i=T_i^q\). Then the transformations \(U_1,\ldots,U_\ell\) commute. Moreover each \(U_i\) is totally ergodic, since every positive power \(U_i^m=T_i^{qm}\) is ergodic.

Fix a residue \(r\in\{0,1,\ldots,q-1\}\). For each \(i\), define
\[
P_{i,r}(m)=\frac{p_i(qm+r)-p_i(r)}q.
\]
Because \(p_i\in\mathbb Z[n]\), the difference \(p_i(qm+r)-p_i(r)\) is coefficientwise divisible by \(q\), so \(P_{i,r}\in\mathbb Z[m]\). Independence is preserved: if a nonzero linear combination of the \(P_{i,r}\) were constant, then the corresponding linear combination of the \(p_i(qm+r)\), and therefore of the \(p_i\), would be constant.

Writing \(g_{i,r}=T_i^{p_i(r)}f_i\), for \(n=qm+r\) we have
\[
T_i^{p_i(n)}f_i
=
U_i^{P_{i,r}(m)}g_{i,r}.
\]
The independent-polynomial joint-ergodicity theorem for commuting totally ergodic transformations therefore gives
\[
\frac1M\sum_{m=1}^M
\prod_{i=1}^\ell
U_i^{P_{i,r}(m)}g_{i,r}
\longrightarrow
\prod_{i=1}^\ell\int g_{i,r}\,d\mu
=
\prod_{i=1}^\ell\int f_i\,d\mu
\]
in \(L^2(\mu)\).

Splitting the original average into its \(q\) residue classes gives an asymptotic convex combination of these \(q\) limits. The discrepancy from the incomplete final block contains at most \(q\) summands and has \(L^2\)-norm \(O(q/N)\prod_i\|f_i\|_\infty\). Hence the original average has the asserted product limit.

## Verification
The reduction uses only three algebraic facts that can be checked directly: in a class-two group \([x^q,y]=[x,y]^q\); the exponent \(q\) annihilates every element of the finite commutator subgroup; and \(p(qm+r)-p(r)\) is divisible by \(q\) for every \(p\in\mathbb Z[n]\). Total ergodicity passes from \(T_i\) to \(T_i^q\), and measure preservation gives \(\int T_i^{p_i(r)}f_i\,d\mu=\int f_i\,d\mu\).

The only imported analytic input is the published commuting-transformation theorem for independent polynomial iterates. Koutsogiannis--Kuca--Sun explicitly cite this commuting result when contrasting it with their open 2-step nilpotent problem.

## Relationship to prior work
Koutsogiannis, Kuca and Sun prove the product-limit theorem for 2-step nilpotent actions when the polynomial degrees are distinct, and they explicitly ask for an extension to all independent polynomials. Their model unresolved average has equal-degree independent iterates. In the commuting case they point to the theorem of Frantzikinakis and Kuca, which supplies exactly the product limit used above.

The present observation joins those two regimes: finite central noncommutativity can be killed by one common power and a finite residue-class decomposition, after which the commuting theorem applies separately on every progression. The inspected source does not state this finite-commutator subcase. Frantzikinakis and Host treat certain noncommuting polynomial averages under entropy hypotheses, but their results do not imply the finite-commutator independent-polynomial statement above.

## Limitations
The argument does not address 2-step nilpotent actions with infinite commutator subgroup, including the genuinely Heisenberg-type situation that motivates the difficult open problem. It also does not provide the source paper's desired Host--Kra seminorm estimate without total ergodicity. The reduction is elementary once the finite-commutator hypothesis is recognized, so a residual originality risk is that the statement may exist implicitly as folklore about virtually abelian actions even though targeted searches and the inspected source did not locate it.

## References
1. Andreas Koutsogiannis, Borys Kuca and Wenbo Sun, *Structure of 2-step nilpotent ergodic averages for distinct-degree polynomials*, arXiv:2607.29368v1, 31 July 2026. Primary MSC 37A30.
2. Nikos Frantzikinakis and Borys Kuca, *Joint ergodicity for commuting transformations and applications to polynomial sequences*, Inventiones Mathematicae 239 (2025), 621--706. DOI: 10.1007/s00222-024-01313-w.
3. Nikos Frantzikinakis and Bernard Host, *Multiple recurrence and convergence without commutativity*, Journal of the London Mathematical Society 107 (2023), 1635--1659. DOI: 10.1112/jlms.12721.
