# Exact weak-compactness gaps and Hilbert-factorable nonregular language Hankel operators

## Finding

Let \(S=\Sigma^*\), where \(\Sigma\) is a nonempty finite alphabet, and let \(L\subseteq S\) be any language. Its **real language Hankel operator** is
\[
(H_Lx)(v)=\sum_{u\in S}x(u)\mathbf1_L(uv),\qquad x\in\ell_1(S;\mathbb R),\ v\in S.
\]
Write \(\mathcal W\) for the weakly compact operators \(\ell_1(S;\mathbb R)\to\ell_\infty(S;\mathbb R)\). Then the following exact dichotomy holds:
\[
\operatorname{dist}(H_L,\mathcal W)=
\begin{cases}0,&H_L\in\mathcal W,\\[2pt]1/2,&H_L\notin\mathcal W.\end{cases}
\]
This statement is a specialization of a general **Boolean-matrix gap lemma**: the same conclusion holds for any real bounded operator \(T:\ell_1(I)\to\ell_\infty(J)\) whose matrix entries are all in \(\{0,1\}\), for nonempty index sets \(I,J\). In the non-weakly-compact case the distance \(1/2\) is attained by the rank-one midpoint operator.

For the binary alphabet \(\{0,1\}\), there are two explicit and structurally different nonregular families. For **every injective** map \(f:\mathbb N_0\to\mathbb N_0\), define
\[
L_f=\{0^n1^{f(n)}:n\ge0\}.
\]
Then \(H_{L_f}\) is **noncompact but factors through a Hilbert space**, and it has a factorization with product of operator norms at most \(\sqrt2\). In particular \(\operatorname{dist}(H_{L_f},\mathcal W)=0\). By contrast, the nonregular order language
\[
L_{\le}=\{0^i1^j:0\le i\le j\}
\]
satisfies \(\operatorname{dist}(H_{L_{\le}},\mathcal W)=1/2\). Both have \(a_n(H)=1/2\) for all \(n\ge2\), by the prior compact-approximation theorem [1]. Thus the entire approximation-number tail does not distinguish these two weak-compactness behaviors.

## Assumptions and scope

All spaces and operators are **real**. A weakly compact operator maps the closed unit ball into a relatively weakly compact subset. The empty word is included in \(S\); \(\mathbb N_0=\{0,1,2,\ldots\}\). The alphabet and index sets are nonempty. No effectiveness or computability assumption on the injection \(f\) is imposed. The factorization statement is qualitative about a concrete Hilbert intermediary; it does **not** claim an optimal factorization constant or classify Hilbert factorability of every weakly compact language Hankel operator.

## Proof

**1. Boolean-matrix gap lemma.** Suppose \(T:\ell_1(I;\mathbb R)\to\ell_\infty(J;\mathbb R)\) has entries \(t_{ji}\in\{0,1\}\). The rank-one midpoint
\[
(Ax)(j)=\tfrac12\sum_{i\in I}x(i)
\]
satisfies \(\|T-A\|=1/2\): each column of \(T-A\) is pointwise in \(\{-1/2,1/2\}\). Thus the distance to weakly compact operators is at most \(1/2\).

To prove the reverse inequality when \(T\) is not weakly compact, suppose a weakly compact \(R\) satisfies \(\|T-R\|=\delta<1/2\). Choose a continuous real function \(g\) with \(g(t)=0\) for \(t\le\delta\) and \(g(t)=1\) for \(t\ge1-\delta\). Then, at every coordinate,
\[
Te_i=g(Re_i).
\]
We use the following standard weak-compactness observation, with its proof included. If \(K\) is compact Hausdorff, \(F\subset C(K;\mathbb R)\) is relatively weakly compact, and \(g\) is continuous, then \(g(F)=\{g\circ h:h\in F\}\) is relatively weakly compact. Indeed, from any sequence in \(F\), Eberlein--Smulian extracts a weakly convergent subsequence. Weak convergence gives pointwise convergence and uniform boundedness. Dominated convergence against every finite signed regular Borel measure on \(K\) gives weak convergence of the composed subsequence. Eberlein--Smulian applies again. Now identify \(\ell_\infty(J;\mathbb R)\) with \(C(\beta J;\mathbb R)\), where \(\beta J\) is the Stone--Cech compactification of the discrete set \(J\). Since \(\{Re_i:i\in I\}\) is relatively weakly compact, so is \(\{Te_i:i\in I\}\). The weak closure of its closed absolutely convex hull is weakly compact (Krein's weak compactness theorem), while the unit-ball image of \(T\) lies in that hull. Hence \(T\) is weakly compact, a contradiction. Thus every weakly compact \(R\) lies at distance at least \(1/2\). This establishes the dichotomy, without a finite-dimensional approximation argument.

**2. The Hilbert-factorable languages.** Fix any injection \(f:\mathbb N_0\to\mathbb N_0\). The nonzero Boolean left derivatives \(q_u(v)=\mathbf1_{L_f}(uv)\) have exactly two forms:
\[
q_{0^a}=\mathbf1_{D_a},\quad D_a=\{0^r1^{f(a+r)}:r\ge0\},
\]
and
\[
q_{0^a1^b}=\mathbf1_{\{1^{f(a)-b}\}}
\quad(1\le b\le f(a)).
\]
All other left derivatives vanish. The sets \(D_a\), indexed by \(a\ge0\), are pairwise disjoint: equality of \(0^r1^{f(a+r)}\) and \(0^{r'}1^{f(a'+r')}\) forces \(r=r'\), then injectivity forces \(a=a'\). The singleton supports \(\{1^t\}\) are also pairwise disjoint among different \(t\).

Define bounded maps
\[
U:\ell_1(S)\longrightarrow\ell_2(\mathbb N_0)\oplus_2\ell_2(\mathbb N_0),
\qquad Ux=(A,B),
\]
where \(A_a=x(0^a)\) and
\[
B_t=\sum_{\substack{a\ge0,\ 1\le b\le f(a)\\ f(a)-b=t}}x(0^a1^b).
\]
These sums are absolutely convergent, and \(\|A\|_1+\|B\|_1\le\|x\|_1\), hence \(\|U\|\le1\). Set
\[
V(A,B)(v)=\sum_{a\ge0}A_a\mathbf1_{D_a}(v)+\sum_{t\ge0}B_t\mathbf1_{\{1^t\}}(v).
\]
At any \(v\) at most one term occurs in each sum, so
\[
\|V(A,B)\|_\infty\le\|A\|_2+\|B\|_2\le\sqrt2\,(\|A\|_2^2+\|B\|_2^2)^{1/2}.
\]
The derivative formulas show \(H_{L_f}=VU\). The intermediate direct sum is Hilbert, so \(H_{L_f}\) is weakly compact. For distinct \(a,a'\), the disjoint nonempty supports \(D_a,D_{a'}\) imply \(\|q_{0^a}-q_{0^{a'}}\|_\infty=1\). Therefore \(H_{L_f}\) is not compact; the infinitely many distinct left derivatives also show that \(L_f\) is nonregular (Myhill--Nerode).

**3. The non-weakly-compact order language.** Let \(L_{\le}=\{0^i1^j:i\le j\}\). Its coefficient matrix contains the half-graph
\[
\mathbf1_{L_{\le}}(0^i1^j)=\mathbf1_{\{i\le j\}}.
\]
The two iterated limits, taking \(i\to\infty\) and \(j\to\infty\) in opposite orders, are \(0\) and \(1\). This contradicts the necessary double-limit property of relatively weakly compact subsets of \(\ell_\infty(S)\), so \(H_{L_{\le}}\) is not weakly compact. Equivalently, if a subsequence of the columns \(q_{0^i}\) converged weakly, its limit would be zero at every coordinate \(1^j\), while evaluation by any free-ultrafilter limit along those coordinates would give the constant value one, an impossibility. Distinct columns make this language nonregular. Part 1 yields the distance exactly \(1/2\).

**4. Same approximation-number tail.** For completeness, the elementary proof of the prior result [1, Section 8] can be checked here. Every nonregular language has infinitely many distinct characteristic left derivatives by Myhill--Nerode, pairwise at supremum distance exactly one. If a compact operator \(R\) satisfied \(\|H_L-R\|=\delta<1/2\), the infinitely many images \(Re_u\) corresponding to distinct derivatives would remain pairwise separated by at least \(1-2\delta>0\), contradicting relative norm compactness of \(R(B_{\ell_1})\). Hence every finite-rank approximant is at distance at least \(1/2\). The rank-one midpoint attains exactly \(1/2\), proving \(a_n(H_L)=1/2\) for all \(n\ge2\). This fact was established in [1]; its verification here is not a novelty claim.

## Verification

All steps above are analytic and quantify over arbitrary injections and infinitely many words. The Boolean-matrix threshold lemma has an explicit weak-compactness proof using the Stone--Cech representation and dominated convergence. For the positive example, the disjoint-support decomposition and the operator-norm inequalities are explicit; no finite truncation is used to infer weak compactness. The half-graph obstruction follows from the complete formula \(\mathbf1_{\{i\le j\}}\), not from finite matrix observations. The exact approximation-number statement is explicitly attributed to [1]. No machine experiment is needed for the proof.

## Relationship to prior work

Hristov, Ilchev, Nedelcheva, and Zlatanov [1] construct the language Hankel representation and prove compactness if and only if regularity, together with a \(1/2\) distance to compact and finite-rank operators and a flat approximation-number tail for nonregular languages. The present result asks a distinct operator-ideal question: distance to **weakly compact** maps. The midpoint approximation is acknowledged as the same elementary upper-bound mechanism used in [1]; the additional contribution is the sharp lower bound under failure of weak compactness and the explicit Hilbert-factorable/non-weakly-compact separation within the same flat approximation profile. The weak-convergence, compactification and double-limit facts in the proof are classical and are not claimed as new.

## Limitations

The half-distance gap relies on exact Boolean coefficients and real scalars. The explicit Hilbert-factorable construction requires injectivity of \(f\); it makes no statement about general noninjective functions. This theorem does not provide an algorithm to decide weak compactness for arbitrary formal languages. There is a genuine priority risk that the general Boolean-matrix gap can be deduced from previously published folklore about weakly almost periodic functions and idempotents in uniform algebras. The separately identified language-family factorization is the substantive example-level separation; a fully equivalent prior treatment under stability or weak almost periodicity terminology has not been ruled out. No independent audit has been performed.

## References

[1] M. Hristov, A. Ilchev, D. Nedelcheva, and B. Zlatanov, *Banach Spaces Generated by Finite-Valued Functions: Superreflexive Rigidity, Hankel Operators, and Universality*, arXiv:2608.15185v1, first posted 15 August 2026, Section 8. https://arxiv.org/abs/2608.15185

[2] Classical results used explicitly: Eberlein--Smulian weak sequential compactness, weak compactness of closed convex hulls (Krein), the Riesz representation for duals of \(C(K)\), the Stone--Cech representation of \(\ell_\infty\), and the weak-compactness double-limit necessity criterion. These are standard inputs, not novelty claims.
