# Isometric \(c_0\) structure and strictly singular, weakly compact Hankel maps for matched-block languages

## Finding

Let \(S\) be any infinite subset of the positive integers and let \(L_S=\{0^n1^n:n\in S\}\) be a language over \(\Sigma=\{0,1\}\). For each word \(u\), write \(q_u(v)=\mathbf1_{L_S}(uv)\). Over the real scalars, let
\[
 X_{L_S}=\overline{\operatorname{span}}\{q_u:u\in\Sigma^*\}^{\|\cdot\|_\infty},\qquad
 (H_S\xi)(v)=\sum_{u\in\Sigma^*}\xi(u)q_u(v),
\]
where \(H_S:\ell_1(\Sigma^*)\longrightarrow\ell_\infty(\Sigma^*)\).

Then \(X_{L_S}\) is linearly **isometric** to \(c_0\), and \(H_S\) is simultaneously **weakly compact and strictly singular but noncompact**. An explicit factorization through the canonical injection \(J:\ell_1(\mathbb N_0\sqcup\mathbb N_0)\to c_0(\mathbb N_0\sqcup\mathbb N_0)\) realizes both positive operator-ideal properties. The exact compact and finite-rank approximation distance is
\[
 \operatorname{dist}(H_S,\mathcal K)=\operatorname{dist}(H_S,\mathcal F)=\tfrac12,
 \quad a_n(H_S)=\tfrac12\quad(n\ge2).
\]
The compact-distance and approximation-number formulas are previously known for **all nonregular languages** [1]; they are included only to quantify the contrast, not asserted as new. If \(S\) is finite, then \(H_S\) is finite rank and \(X_{L_S}\) is finite dimensional.

## Assumptions and scope

Here \(\mathbb N_0=\{0,1,\ldots\}\), \(\Sigma^*\) contains the empty word \(\varepsilon\), \(0^0=1^0=\varepsilon\), and all spaces are real. For an arbitrary infinite \(S\) no density, computability, regularity, or gap condition is assumed. The operator \(H_S\) is the Boolean formal-language Hankel map on \(\ell_1(\Sigma^*)\); it is **not** the classical Hardy-space Hankel operator. In the displayed approximation formula \(a_n\) denotes distance to operators of rank less than \(n\).

## Proof

**1. Disjoint-support normal form.** For \(j\ge0\) let \(\delta_j(v)=\mathbf1_{\{1^j\}}(v)\); in particular \(\delta_0\) is supported on the empty word. For \(a\ge0\) put
\[
 h_a=q_{0^a}-\mathbf1_S(a)\delta_a
 =\mathbf1_{E_a},\qquad
 E_a=\{0^k1^{a+k}:k\ge1,\ a+k\in S\}.
\]
Because \(S\) is unbounded, every \(E_a\) is nonempty. The sets \(E_a\) are pairwise disjoint: the difference between the run of ones and the positive run of zeros is exactly \(a\). They are disjoint from every singleton \(\{1^j\}\), and those singletons are pairwise disjoint.

All nonzero derivatives are exhausted by the following formulas (with \(a\ge0\), \(b\ge1\)):
\[
 q_{0^a}=h_a+\mathbf1_S(a)\delta_a,
 \qquad q_{0^a1^b}=\begin{cases}
 \delta_{a-b},&a\in S,\ 1\le b\le a,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Every word not of these forms has zero derivative. Conversely, \(h_a\in X_{L_S}\) since \(q_{0^a}\in X_{L_S}\), and \(\delta_j\in X_{L_S}\): choose any \(a\in S\) with \(a>j\) and use \(q_{0^a1^{a-j}}=\delta_j\). Thus the displayed \(h_a\)'s and \(\delta_j\)'s span a dense subspace of \(X_{L_S}\). For all finitely supported real coefficient sequences,
\[
 \Big\|\sum_a\alpha_a h_a+\sum_j\beta_j\delta_j\Big\|_\infty
 =\max\{\sup_a|\alpha_a|,\sup_j|\beta_j|\}.
\]
Completion identifies \(X_{L_S}\) with \(c_0(\mathbb N_0\sqcup\mathbb N_0)\), hence with \(c_0\), by a surjective linear isometry \(U\).

**2. Factorization.** For \(\xi\in\ell_1(\Sigma^*)\), define \(Q\xi=(A,B)\) by
\[
 A_a=\xi(0^a),\qquad
 B_j=\mathbf1_S(j)\xi(0^j)+
 \sum_{\substack{a\in S\\ a>j}}\xi(0^a1^{a-j}).
\]
Absolute convergence is immediate, and the double sum enumerates distinct nonzero input coordinates, so \(\|A\|_1\le\|\xi\|_1\), \(\|B\|_1\le\|\xi\|_1\), and \(\|Q\|\le2\). Each coefficient of \(H_S\xi\) in the disjoint-support basis is exactly \(A_a\) or \(B_j\). With the canonical inclusion \(J:\ell_1(\mathbb N_0\sqcup\mathbb N_0)\to c_0(\mathbb N_0\sqcup\mathbb N_0)\), we therefore have
\[
 H_S=U J Q.
\]

**3. Weak compactness.** The canonical inclusion \(J:\ell_1\to c_0\) is weakly compact. Indeed, given any sequence in its image of the unit ball, diagonal extraction gives coordinatewise convergence to some sequence \(y\). Fatou's lemma yields \(\|y\|_1\le1\), so \(y\in c_0\). For every continuous functional \(\varphi\in c_0^*=\ell_1\), the coordinatewise convergence together with the uniform supremum bound implies \(\varphi(y_n)\to\varphi(y)\), by an elementary finite-head/tail estimate. Eberlein–Šmulian therefore gives relative weak compactness. Bounded composition in \(H_S=UJQ\) preserves weak compactness.

**4. Strict singularity.** The injection \(J\) is strictly singular. Suppose it were bounded below on an infinite-dimensional closed subspace \(E\subseteq\ell_1\). Its image would be a closed infinite-dimensional subspace of \(c_0\). For each \(n\), choose a unit vector \(y_n\) in this image whose first \(n\) coordinates vanish; this is possible since these coordinates impose only finite-dimensional restrictions. The sequence \((y_n)\) is weakly null in \(c_0\), since every functional is in \(\ell_1\). Bounded invertibility of \(J|_E\) implies that \((J|_E)^{-1}y_n\) is weakly null in \(E\) and hence in \(\ell_1\), yet its \(\ell_1\) norms are at least one. This contradicts the Schur property of \(\ell_1\). Thus \(J\), and therefore \(H_S=UJQ\), is strictly singular.

**5. Noncompactness and quantitative separation.** For distinct \(a,b\ge0\), pick \(v\in E_a\). Then \(q_{0^a}(v)=1\) and \(q_{0^b}(v)=0\), so \(\|H_Se_{0^a}-H_Se_{0^b}\|_\infty=1\). Therefore \(H_S\) is noncompact. If \(K\) is compact and \(\|H_S-K\|<\tfrac12\), then the bounded sequence \((Ke_{0^a})\) has pairwise distances at least \(1-2\|H_S-K\|>0\), a contradiction. For the opposite bound, the rank-one operator
\[
 (R\xi)(v)=\tfrac12\sum_{u\in\Sigma^*}\xi(u)
\]
satisfies \(\|H_S-R\|\le\tfrac12\) because each Hankel matrix entry belongs to \(\{0,1\}\). Hence both compact and finite-rank distances equal \(\tfrac12\), and the same argument shows \(a_n(H_S)=\tfrac12\) for all \(n\ge2\). These last formulas reproduce the more general theorem of [1], rather than establishing a novel approximation-number result.

If \(S\) is finite, the language itself is finite, so there are only finitely many nonzero prefixes of its words; therefore \(H_S\) has finite rank and its closed derivative span is finite dimensional.

## Verification

The disjoint-support decomposition is an exact combinatorial identity; its coordinate bounds prove the operator factorization and the functional-analytic conclusions for every infinite \(S\). The accompanying standalone Python diagnostic `check_language.py` checks 68,825 exact finite prefix–suffix/normal-form and support assertions for four finite test sets. Finite tests do not establish the universal claim or the compact/weakly compact operator assertions. The weak compactness and strict singularity arguments use the classical Eberlein–Šmulian and Schur theorems as stated.

## Relationship to prior work

Hristov–Ilchev–Nedelcheva–Zlatanov [1], Sections 6–8, define exactly these language derivative spaces and Boolean Hankel operators and prove that nonregularity is equivalent to noncompactness and gives the compact-distance and approximation-number value \(\tfrac12\). Those generic conclusions, the notion of the operator, and the formal-language setup are prior work. The new claim identifies an explicit, entire infinitely parametrized matched-block family for which the derivative space is isometrically \(c_0\) and the noncompact Hankel map is both weakly compact and strictly singular. The explicit \(\ell_1\to\ell_1\to c_0\) factorization is what establishes the weak compactness not supplied by noncompactness alone. Classical results about \(\ell_1\), \(c_0\), and weak compactness are used rather than claimed as new.

## Limitations

This result concerns real-valued language derivative spaces for balanced two-block words with an arbitrary infinite index set. It makes no classification of general nonregular languages and no claim that all their Hankel maps are weakly compact or strictly singular. The exact compact-distance result is not new. Historical priority of equivalent descriptions in older algebraic-automata or weakly almost periodic language theory has not been independently certified. The finite checker is diagnostic only.

## References

[1] M. Hristov, A. Ilchev, D. Nedelcheva, B. Zlatanov, *Banach Spaces Generated by Finite-Valued Functions: Superreflexive Rigidity, Hankel Operators, and Universality*, arXiv:2608.15185, first posted 2026-08-15; especially Sections 6 and 8. https://arxiv.org/abs/2608.15185

[2] W. F. Eberlein, *Weak compactness in Banach spaces I*, Proceedings of the National Academy of Sciences USA 33 (1947), 51–53; classical Eberlein–Šmulian theorem.

[3] O. Schur, *Über lineare Transformationen in der Theorie der unendlichen Reihen*, Journal für die reine und angewandte Mathematik 151 (1921), 79–111; the Schur property of \(\ell_1\).
