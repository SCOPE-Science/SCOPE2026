# Continuous reducibility dichotomy for diagonal Hilbert cosets

## Finding
Let \(a=(a_n)_{n\ge0}\) be any real sequence with \(a_n\ge1\). Define the subgroup
\[
H_a=\left\{x\in\ell_2:\sum_{n=0}^\infty a_n x_n^2<\infty\right\}
\]
of real Hilbert space \(\ell_2\), and the coset equivalence relation \(E_a\) on \(\ell_2\) by \(x\,E_a\,y\) exactly when \(x-y\in H_a\). Define \(E_2\) on product space \(\mathbb R^{\mathbb N}\) by \(u\,E_2\,v\) if and only if \(\sum_n(u_n-v_n)^2<\infty\). The topology on \(\mathbb R^{\mathbb N}\) is the product topology; the topology on \(\ell_2\) is its norm topology.

There are exactly two continuous-reducibility degrees among these \(E_a\): bounded \(a\) gives the one-class relation; every unbounded \(a\) gives a relation continuously bireducible with \(E_2\). Indeed, for any two unbounded positive sequences \(a,b\), there are **injective contractive linear reductions** from \(E_a\) to \(E_b\) and conversely. Every \(E_a\) is \(F_\sigma\). For unbounded \(a\), any continuous reduction \(E_2\to E_a\) must be nonlinear in the strong sense that no continuous additive group homomorphism can serve as such a reduction.

## Assumptions and scope
All sequences are indexed by the nonnegative integers. All vector spaces and maps are real. We assume only \(a_n\ge1\), without monotonicity, convergence, or rate conditions. A reduction \(f\) from an equivalence relation \(E\) to \(F\) means \(xEy\iff f(x)Ff(y)\) for *all* domain pairs. A bounded linear reduction \(L:\ell_2\to\ell_2\) is additionally a bounded linear map with that equivalence-preserving property. No assertion is made about arbitrary, nondiagonal \(F_\sigma\) Hilbert subgroups.

## Proof
**1. Trivial and nontrivial cases.** If \(\sup_n a_n<\infty\), then \(H_a=\ell_2\), so \(E_a\) has one equivalence class. Conversely, when \(a\) is unbounded choose distinct indices \(n_j\) such that \(a_{n_j}\ge j^4\) for every positive integer \(j\); the vector supported at these indices with entries \(1/j\) is in \(\ell_2\) but not in \(H_a\). Thus \(E_a\) has at least two classes. The subgroup is always \(F_\sigma\): write it as the union, over positive integers \(K\), of the intersection, over finite cutoffs \(N\), of the closed inequalities \(\sum_{n<N} a_nx_n^2\le K\). The relation \(E_a\) is the inverse image of this subgroup under continuous subtraction.

**2. All unbounded cases linearly reduce to each other.** Given unbounded \(a,b\), recursively choose pairwise distinct indices \(\sigma(n)\) such that \(b_{\sigma(n)}\ge a_n\). This is possible because unboundedness of \(b\) implies that for every finite threshold the set of indices above that threshold is infinite. Put
\[
(Lx)_{\sigma(n)}=\sqrt{a_n/b_{\sigma(n)}}\,x_n,
\qquad (Lx)_m=0\quad\text{if }m\notin\sigma[\mathbb N].
\]
The operator is linear and injective, and \(\|Lx\|_2\le\|x\|_2\). It satisfies the exact identity
\[
\sum_m b_m(Lx)_m^2=\sum_n a_nx_n^2
\]
with extended nonnegative sums, so \(x-y\in H_a\iff Lx-Ly\in H_b\). Interchanging the sequences gives a bounded injective linear reduction in the opposite direction.

**3. Reduction to the standard benchmark.** For any \(a\), the coordinate map \(T_a:\ell_2\to\mathbb R^{\mathbb N}\) defined by \((T_ax)_n=\sqrt{a_n}\,x_n\) is product-continuous and obeys \(xE_ay\iff T_ax\,E_2\,T_ay\).

**4. Continuous reduction from the benchmark.** Suppose \(a\) is unbounded. Choose mutually distinct indices \(n(j,m)\), one for each ordered pair of nonnegative integers, with \(a_{n(j,m)}\ge2^{j+1}\). Such an assignment exists because the weight sequence crosses each finite threshold infinitely often. Fix a real orthonormal basis \((h_m)_{m\ge0}\) of \(L^2(\mathbb R)\), and let
\[
\psi_t(s)=e^{-(s-t)^2/2},\qquad
c_m(t)=\langle\psi_t,h_m\rangle_{L^2}.
\]
Gaussian integration and Parseval give, for every real \(t,u\),
\[
\sum_m c_m(t)^2=\sqrt\pi,
\qquad
\sum_m(c_m(t)-c_m(u))^2
=2\sqrt\pi\bigl(1-e^{-(t-u)^2/4}\bigr).
\]
Define \(\Phi:\mathbb R^{\mathbb N}\to\ell_2\) by
\[
\Phi(v)_{n(j,m)}=a_{n(j,m)}^{-1/2}c_m(v_j),
\]
with all unused coordinates zero. This is well defined because
\[
\|\Phi(v)\|_2^2\le \sqrt\pi\sum_{j\ge0}2^{-j-1}<\infty.
\]
It is continuous from the product topology to the Hilbert norm: the norm-squared contribution of the coordinates with \(j\ge J\) is bounded by \(\sqrt\pi\sum_{j\ge J}2^{-j-1}\), uniformly in \(v\); each of the finitely many preceding blocks is norm-continuous because \(t\mapsto\psi_t\) is norm-continuous in \(L^2\). The weighted difference has exact value
\[
\sum_n a_n(\Phi(v)_n-\Phi(w)_n)^2
=2\sqrt\pi\sum_{j\ge0}\bigl(1-e^{-(v_j-w_j)^2/4}\bigr).
\]
Since \(1-e^{-t^2/4}\) is bounded above and below by positive constant multiples of \(\min(t^2,1)\), the displayed series converges precisely when \(\sum_j(v_j-w_j)^2<\infty\). Therefore \(vE_2w\iff\Phi(v)E_a\Phi(w)\).

**5. Continuous homomorphism obstruction.** Every continuous additive homomorphism \(S:\mathbb R^{\mathbb N}\to\ell_2\) depends on only finitely many source coordinates. Indeed, continuity at zero supplies a basic product neighborhood \(U\), restricting only a finite coordinate set \(F\), with \(\|S(u)\|_2<1\) for \(u\in U\). If \(u\) vanishes on \(F\), then every real multiple \(tu\) lies in \(U\); additivity plus continuity gives real linearity, and therefore \(\|tS(u)\|_2<1\) for every \(t\), forcing \(S(u)=0\). Thus \(S\) factors through the projection to \(F\). Choose \(v=0\) and \(w\) equal to \(1\) on infinitely many indices outside \(F\), zero elsewhere. Then \(v\not E_2w\), while \(S(v)=S(w)\), a contradiction to reduction. The two-degree statement now follows: the one-class relation reduces to every equivalence relation by a constant map, while a relation with at least two classes cannot reduce to the one-class relation.

## Verification
The proof supplies explicit maps and checks both directions of each biconditional, including the nonhomomorphism assertion. Its only analytical identities are Gaussian integration, Parseval, and the elementary equivalence of \(1-e^{-t^2/4}\) with \(\min(t^2,1)\). No finite experiment is used as a substitute for the all-sequence proof. The decisive continuity bound is uniform in every source point.

## Relationship to prior work
Wang's 2026 work constructs \(F_\sigma\) coset equivalence relations of unbounded complexity and rules out an \(F_\sigma\) universal relation. The present restricted diagonal family behaves differently: all its nontrivial members lie in the single standard \(E_2\) degree, even for continuous reductions. Ding's 2015/2017 work establishes Borel bireducibility with \(\mathbb R^{\mathbb N}/\ell_2\) for Schauder relations generated by Hilbert bases; this is relevant prior theory, but its stated domain is \(\mathbb R^{\mathbb N}\) and does not by itself state the restriction to diagonal subgroups on normed \(\ell_2\), the pairwise contractive linear embeddings, or the continuous-homomorphism obstruction. Dougherty and Hjorth's classical work establishes benchmark reducibility theory for the \(\ell_p\) sequence equivalence relations.

## Limitations
The conclusion applies only to weights bounded below by \(1\) and only to coordinate-diagonal Hilbert cosets. It does not classify general \(F_\sigma\) subgroup cosets, nor prove that the topological refinements are absent from all previous literature. Ding's complete preprint text could not be inspected through the available access route, leaving a concrete historical-priority risk for the continuous classification. The result contains no claim of independent mathematical certification.

## References
1. Ruijun Wang, *There is no universal Fσ equivalence relation*, arXiv:2610.31052, first public 2026-10-22.
2. Longyun Ding, *On equivalence relations generated by Schauder bases*, arXiv:1504.00299 (2015); *Journal of Symbolic Logic* 82 (2017), 1459–1481, DOI 10.1017/jsl.2017.67.
3. R. Dougherty and G. Hjorth, *Reducibility and nonreducibility between ℓp equivalence relations*, *Transactions of the American Mathematical Society* 351 (1999), 1835–1844.
