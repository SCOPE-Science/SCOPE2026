# Discreteness and universal second-adjoint norm attainment in real \(C_0(K)\)

## Finding
Let \(K\) be a **nonempty, first-countable, locally compact Hausdorff space**, and put \(X=C_0(K;\mathbb R)\), with the supremum norm. For a bounded operator \(A:X\to X\), write \(A\in\operatorname{NA}_2(X,X)\) when there is \(z\in S_{X^{**}}\) such that \(\|A^{**}z\|=\|A\|\). Then
\[
\boxed{\operatorname{NA}_2(X,X)=\mathcal L(X,X)\quad\Longleftrightarrow\quad K\text{ is discrete}.}
\]
More generally, **whenever any locally compact Hausdorff space \(K\) contains a nontrivial convergent sequence**, there is a norm-one \(A\in\mathcal L(C_0(K))\) for which \(A^{**}\) does not attain its norm. The first-countability hypothesis is used only to ensure that every non-isolated point yields such a sequence.

## Assumptions and scope
All scalar fields are real. The space \(K\) is Hausdorff and locally compact, and \(C_0(K)\) means the real continuous functions vanishing at infinity. The space \(K\) is assumed nonempty, so that the zero operator attains its norm on the nonempty unit sphere. A nontrivial convergent sequence means distinct points \(t_n\to p\) with \(t_n\ne p\). No assertion is made for non-first-countable spaces which have no such sequence. An operator's second adjoint has domain and codomain \(X^{**}\).

## Proof
**1. The discrete case.** If \(K\) is discrete, the canonical restriction of functions to points identifies \(C_0(K)\) isometrically with \(c_0(K)\). For infinite \(K\), Dantas–Jung–Martín, Remark 3.5, proves that every operator on \(c_0(K)\) has a norm-attaining second adjoint, with no cardinality restriction. If \(K\) is finite and nonempty, this follows instead from compactness of its finite-dimensional unit sphere.

**2. A contractively complemented convergent-sequence space.** Suppose \(K\) contains a nontrivial convergent sequence. By passing to a subsequence, choose points \(t_n\to p\), a relatively compact neighborhood \(V_0\) of \(p\), and decreasing neighborhoods \(V_n\) of \(p\) such that \(\overline{V_n}\subseteq V_{n-1}\), \(t_n\in V_{n-1}\setminus\overline{V_n}\), and each annulus \(V_{n-1}\setminus\overline{V_n}\) contains the point \(t_n\). To perform the induction, after \(V_{n-1}\) is chosen, select a sufficiently late unused point of the convergent sequence inside \(V_{n-1}\), then use regularity to choose \(V_n\) with closure inside \(V_{n-1}\) but avoiding that point. For first-countable \(K\), one may additionally require \(V_n\) to lie in the \(n\)-th neighborhood of a fixed local base, giving convergence directly.

By local compactness, choose \(\psi_n\in C_c(K;[0,1])\) supported in \(V_{n-1}\setminus\overline{V_n}\) with \(\psi_n(t_n)=1\). These supports are pairwise disjoint. Choose \(h\in C_c(K;[0,1])\) which equals \(1\) on \(\overline{V_0}\); such a cutoff exists because \(\overline{V_0}\) is compact. For \(a=(a_n)\in c\), write \(a_\infty=\lim_n a_n\) and define
\[
(Ea)(t)=a_\infty h(t)+\sum_{n\ge1}(a_n-a_\infty)\psi_n(t),
\qquad (Rf)_n=f(t_n).
\]
The series converges uniformly: its tail is bounded in supremum norm by \(\sup_{n\ge N}|a_n-a_\infty|\to0\), owing to disjoint supports. Each summand has compact support in \(\overline{V_0}\), so \(Ea\in C_0(K)\). Moreover \(R:C_0(K)\to c\) is bounded with \(\|R\|\le1\), because \(t_n\to p\). On the support of each \(\psi_n\), \(h=1\); hence \(Ea\) is a convex combination of \(a_n\) and \(a_\infty\), while off the supports it equals \(a_\infty h\). Therefore \(\|Ea\|\le\|a\|\). At \(t_n\) we have \((Ea)(t_n)=a_n\), and at \(p\) the value is \(a_\infty\). Consequently
\[
RE=I_c,\qquad \|E\|=\|R\|=1.
\]
Thus \(c\) is the range of a norm-one projection \(ER\) on \(C_0(K)\). Notice that the construction does not require first countability once a convergent sequence is given.

**3. An explicit norm-one obstruction on \(c\).** Let \((e_j)_{j\ge1}\) be the standard unit vectors of \(\ell_1\), and set
\[
u=\sum_{j\ge1}2^{-j}e_j,\qquad b_n=\tfrac12(e_{n+1}-e_{n+2}).\]
The canonical isometric identification \(\Phi:\ell_1\to c^*\) is
\[
\Phi(v)(a)=v_1 a_\infty+\sum_{j\ge1}v_{j+1}a_j.
\]
Define \(T:c\to c\) by
\[
(Ta)_n=\tfrac12\Phi(u)(a)+\tfrac12\Phi(b_n)(a)
=\tfrac12\Phi(u)(a)+\tfrac14(a_n-a_{n+1}).
\]
Since the differences tend to zero, \(Ta\) is convergent, with limit \(\Phi(u)(a)/2\). Set \(S=\Phi^{-1}T^*\Phi:\ell_1\to\ell_1\). The defining equations imply
\[
Se_1=\tfrac12u,\qquad Se_{n+1}=\tfrac12u+\tfrac12b_n.
\]
A direct sum over positive and negative coordinates gives
\[
\|Se_1\|_1=\tfrac12,\qquad
\|Se_{n+1}\|_1=1-2^{-(n+2)}\quad(n\ge1).
\]
Since \(\|S\|=\sup_j\|Se_j\|_1\), it follows that \(\|S\|=\|T\|=1\). For any \(\zeta\in B_{\ell_\infty}\),
\[
\|S^*\zeta\|_\infty
=\max\left\{\tfrac12|\zeta(u)|,\ \sup_{n\ge1}\left|\tfrac12\zeta(u)+\tfrac12\zeta(b_n)\right|\right\}
\le\tfrac12|\zeta(u)|+\tfrac12.
\]
If equality \(\|S^*\zeta\|_\infty=1\) held, then \(|\zeta(u)|=1\). Because every coefficient \(2^{-j}\) of \(u\) is strictly positive and the coefficients sum to one, this forces all coordinates of \(\zeta\) to have the same sign, either \(+1\) or \(-1\). But then \(\zeta(b_n)=0\) for all \(n\), giving \(\|S^*\zeta\|_\infty=1/2\), a contradiction. Hence \(S^*\) does not attain its norm. The identity
\[
S^*=\Phi^*T^{**}(\Phi^{-1})^*
\]
is an isometric conjugacy, so \(T^{**}\) does not attain its norm either.

**4. Transfer to \(C_0(K)\).** Define \(A=ETR\) on \(C_0(K)\). Since \(RE=I_c\) and \(E,R\) are norm one, \(\|A\|=\|T\|=1\). If \(A^{**}\) attained its norm at \(z\in S_{C_0(K)^{**}}\), then
\[
1=\|E^{**}T^{**}R^{**}z\|\le\|T^{**}R^{**}z\|\le\|R^{**}z\|\le1.
\]
Thus \(R^{**}z\) would be a unit vector on which \(T^{**}\) attains norm one, contradicting step 3. This proves failure whenever \(K\) contains a nontrivial convergent sequence.

**5. Topological dichotomy.** If \(K\) is first countable and not discrete, choose a non-isolated point \(p\). A countable local base supplies a sequence of distinct points converging to \(p\), so steps 2–4 apply. The discrete case is step 1. Both implications, including all finite and infinite cases under the nonempty hypothesis, follow.

## Verification
The proof uses only compact-support Urysohn cutoffs, uniform convergence of a disjoint-support series, a direct \(\ell_1\)-column norm calculation, isometric dual identification, and the norm-one-retraction inequality. An exact-rational finite-column checker in `verify_columns.py` independently verifies the identity \(\|Se_{n+1}\|_1=1-2^{-(n+2)}\) for 60 distinct values of \(n\). The infinite-dimensional nonattainment argument does not rely on finite testing. The source's \(c_0(\Gamma)\) theorem and \(c\)-counterexample were also checked against the original full text.

## Relationship to prior work
Dantas, Jung, and Martín, *On operators whose adjoints or second adjoints attain their norms* (first public version September 1, 2026), prove universal second-adjoint norm attainment for \(c_0(\Gamma)\) (Remark 3.5), prove its failure for \(c\) (Theorem 3.15), and study the hyperplane family \(W_\alpha\). They do not give a topological characterization across all first-countable locally compact \(C_0(K)\) spaces. The present theorem identifies precisely when those two opposite phenomena occur within this natural continuous-function class, using a norm-one retract arising from a non-isolated point.

A published result *Third-adjoint norm attainment for all isometric \(\ell_1\)-predual pairs* concerns universal **third** adjoints of arbitrary isometric \(\ell_1\)-predual pairs. Its proof and precise claim were inspected. A third-adjoint conclusion is weaker than the present universal second-adjoint question, and in fact \(c\) separates them. Previously known \(c_0\) complementability results concern different operator invariants and do not identify the present dichotomy.

## Limitations
The classification is for **real**, **nonempty**, **first-countable** locally compact Hausdorff spaces with the ordinary supremum norm. The failure implication holds for any locally compact Hausdorff \(K\) containing a nontrivial convergent sequence, but nothing here decides arbitrary compact Hausdorff spaces with no nontrivial convergent sequences. No assertion is made about norm attainment of first adjoints or of the operators themselves. The elementary structure of the transfer leaves the possibility that this classification was previously recorded as an unindexed corollary; this is a remaining originality risk.

## References
1. S. Dantas, M. Jung, M. Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794v1, first public September 1, 2026, in particular Theorem 3.3, Remark 3.5, Lemmas 3.13–3.14 and Theorem 3.15. Public full text: https://arxiv.org/html/2609.00794v1.
2. *Third-adjoint norm attainment for all isometric \(\ell_1\)-predual pairs*, published mathematical research record, October 4, 2026; full `RESULT.md` examined at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-third-adjoint-norm-attainment-for-all-isometric-ell-1-predual-pa--219f642b555a.
