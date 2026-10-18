# Exact bidual-attainment and Baire dichotomy for block-contrast perturbations of \(c_0\to c\)

## Finding
Fix real scalars \(0<\kappa<1\) and \(0<t_n<1\) with \(t_n\to1\). Let \(b_n\in\ell_1(\mathbb N;\mathbb R)\) have pairwise disjoint nonempty **finite** supports, and assume \(\|b_n\|_1=1\) and \(\sum_j b_n(j)=0\). Such a \(b_n\) is a normalized signed block contrast: its positive and negative masses are both \(1/2\). Define the positive probability simplex
\[
\mathcal P=\{u\in\ell_1(\mathbb N;\mathbb R):u_j\ge0,\ \sum_j u_j=1\}
\]
and, for \(u\in\mathcal P\), the bounded operator \(T_u:c_0(\mathbb N;\mathbb R)\to c(\mathbb N;\mathbb R)\) by
\[
(T_ux)_n=\kappa\sum_j u_jx_j+(1-\kappa)t_n\sum_jb_n(j)x_j.
\]
The following statements hold simultaneously for **every** permitted choice of the contrast blocks, every \(u\in\mathcal P\), and every permitted scalar sequence:

1. \(\|T_u\|=1\), but neither \(T_u\) nor its first adjoint \(T_u^*\) attains its norm.
2. With the *negative-support conflict mass*
\[
D_n(u)=\sum_{\substack{j\in\operatorname{supp}b_n\\b_n(j)<0,\ u_j>0}}|b_n(j)|\quad(0\le D_n(u)\le1/2),
\]
one has the exact **if-and-only-if** classification
\[
\boxed{T_u^{**}\text{ attains its operator norm}\iff\liminf_{n\to\infty}D_n(u)=0.}
\]
3. In the norm topology of \(\mathcal P\), the parameter set on which \(T_u^{**}\) attains its norm is dense and meagre; the nonattaining set is comeagre. The norm of \(T_u\) is identically one throughout both strata.

For the canonical disjoint first differences \(b_n=(e_{2n-1}-e_{2n})/2\), the criterion becomes
\[
\boxed{T_u^{**}\text{ norm-attains}\iff u_{2n}=0\text{ for infinitely many }n.}
\]
The general criterion is genuinely *quantitative*, rather than merely requiring a disjoint block with zero conflict mass: for \(b_n=\frac12e_{3n-2}-(\frac12-\frac1{4n})e_{3n-1}-\frac1{4n}e_{3n}\) and \(u_{3n}=2^{-n}\), with all other entries of \(u\) zero, every \(D_n(u)\) is positive but \(D_n(u)=1/(4n)\to0\), so the second adjoint nevertheless attains its norm.

## Assumptions and scope
The scalar field throughout is real. The sequence space \(c\) contains all convergent real sequences with supremum norm, and \(c_0\) its closed vanishing subspace. The canonical bidual identifications are \(c_0^{**}=\ell_\infty(\mathbb N)\) and \(c^{**}=\ell_\infty(\mathbb N\cup\{\infty\})\), where the additional coordinate corresponds to the limit functional on \(c\). Adjoint and second-adjoint norm attainment mean attainment by some vector of the appropriate domain unit sphere. The blocks are fixed independently of \(u\), have pairwise disjoint supports, and need not cover all of \(\mathbb N\); since each is nonempty, the supports escape every fixed finite set. No uniform rate of convergence of \(t_n\) is assumed.

## Proof
**Step 1: well-defined operators and common norm.** For any \(x\in c_0\), the pairwise-disjoint supports of \(b_n\) escape to infinity, so \(|\langle b_n,x\rangle|\le\sup_{j\in\operatorname{supp}b_n}|x_j|\to0\). Therefore \((T_ux)_n\to\kappa\langle u,x\rangle\), and \(T_u\) really maps to \(c\). Write
\[
a_n=\kappa u+(1-\kappa)t_nb_n\in\ell_1.
\]
Each \(\|a_n\|_1\le\kappa+(1-\kappa)t_n<1\). Conversely, putting \(m_n=\sum_{j\in\operatorname{supp}b_n}u_j\), the reverse triangle inequality inside the support gives
\[
\kappa+(1-\kappa)t_n-2\kappa m_n\le\|a_n\|_1\le\kappa+(1-\kappa)t_n.
\]
As the blocks are disjoint and \(u\in\ell_1\), one has \(m_n\to0\). Thus \(\|a_n\|_1\to1\), so \(\|T_u\|=\max\{\kappa,\sup_n\|a_n\|_1\}=1\).

**Step 2: the first two nonattainment assertions.** For fixed \(x\in B_{c_0}\), every finite coordinate satisfies \(|(T_ux)_n|\le\|a_n\|_1<1\), and the coordinate limit has modulus at most \(\kappa<1\); because the coordinates actually converge, their supremum is strictly less than one. Hence \(T_u\) does not norm-attain. Identifying \(c^*\) isometrically with \(\ell_1(\mathbb N\cup\{\infty\})\), the first adjoint sends the functional concentrated at \(n\) to \(a_n\), and the limit functional to \(\kappa u\). If \(g\in B_{c^*}\) is nonzero, its image norm is at most \(\sum_n|g_n|\|a_n\|_1+\kappa|g_\infty|\), which is strictly below \(\sum_n|g_n|+|g_\infty|\le1\): a nonzero absolutely summable positive combination of strictly positive deficits remains positive. So \(T_u^*\) also does not norm-attain.

**Step 3: exact second-adjoint attainment.** For any \(z\in B_{\ell_\infty}\), the standard bidual identification yields
\[
\|T_u^{**}z\|=\max\left\{\kappa|\langle u,z\rangle|,\ \sup_n|\kappa\langle u,z\rangle+(1-\kappa)t_n\langle b_n,z\rangle|\right\}.
\]
The value one cannot occur at a fixed coordinate, since its functional norm is below one, or at the limit coordinate, whose norm is \(\kappa\). Consequently, if \(\|T_u^{**}z\|=1\), there is a sequence \(n_k\to\infty\) along which the finite coordinates have modulus tending to one. The triangle inequality, \(|\langle u,z\rangle|\le1\), and \(|\langle b_{n_k},z\rangle|\le1\), show that \(|\langle u,z\rangle|=1\). Positivity and total mass one of \(u\) then force a common sign \(\sigma\in\{-1,1\}\) with \(z_j=\sigma\) whenever \(u_j>0\). The equality limit for the convex combination further forces \(\sigma\langle b_{n_k},z\rangle\to1\). Because \(\|b_n\|_1=1\), all positive coordinates contribute at most their modulus, and every negative coefficient at a coordinate with \(u_j>0\) instead contributes the negative of its modulus. Thus the **sharp pointwise bound**
\[
\sigma\langle b_n,z\rangle\le1-2D_n(u)
\]
holds. Necessarily \(D_{n_k}(u)\to0\), proving the forward implication.

Conversely, if \(\liminf_nD_n(u)=0\), choose distinct \(n_k\to\infty\) with \(D_{n_k}(u)\to0\). Define one single \(z\in B_{\ell_\infty}\) by \(z_j=1\) whenever \(u_j>0\), and otherwise put \(z_j=\operatorname{sgn}b_n(j)\) if \(j\in\operatorname{supp}b_n\); assign remaining coordinates arbitrarily in \([-1,1]\). Pairwise disjointness makes this definition consistent. It gives \(\langle u,z\rangle=1\) and the exact identity \(\langle b_n,z\rangle=1-2D_n(u)\) for every \(n\). Hence
\[
(T_u^{**}z)_n=\kappa+(1-\kappa)t_n(1-2D_n(u))\to1
\]
along \(n_k\), proving \(\|T_u^{**}z\|=1\). This proves sufficiency without assuming that any one conflict mass is zero.

**Step 4: norm-topological prevalence.** The positive unit-mass simplex \(\mathcal P\) is a closed complete metric subspace of \(\ell_1\). Its finite-support members are dense (truncate and redistribute the discarded positive mass), and for each such member \(D_n(u)=0\) for all sufficiently large \(n\). Thus the norm-attaining stratum is dense. For each fixed \(j\), \(\{u\in\mathcal P:u_j>0\}\) is relatively open and dense; its countable intersection \(\mathcal P_{++}=\{u\in\mathcal P:u_j>0\ \forall j\}\) is a dense \(G_\delta\). For every \(u\in\mathcal P_{++}\), the negative half-mass of each contrast is entirely in \(\operatorname{supp}u\), so \(D_n(u)=1/2\) for all \(n\), and the second adjoint fails norm attainment. Consequently the attaining stratum lies in the complement of the dense \(G_\delta\), a meagre set. The complement is comeagre, while the attaining stratum is dense, as asserted.

**Step 5: canonical pairs and strictly positive conflict masses.** For \(b_n=(e_{2n-1}-e_{2n})/2\), the negative mass on \(\operatorname{supp}u\) equals \(1/2\) when \(u_{2n}>0\), and zero otherwise; the limit-infimum condition is exactly infinitely many even zero coefficients. For the displayed triple-block example with \(u_{3n}=2^{-n}\), every block has nonzero conflict mass \(1/(4n)\), but the conflict decays to zero. Both are encompassed by the same sharp criterion.

## Verification
The result is an infinite-dimensional analytic proof. The normalization and nonattainment use exact dual row norms and convergence in \(c\); the essential lemma is the explicit sharp signed-block inequality \(\sigma\langle b_n,z\rangle\le1-2D_n(u)\), with equality realized simultaneously on disjoint blocks. No finite experiment is promoted to a proof. The canonical pair and triple-block examples can be checked by direct coefficient sums; the Baire statement uses relatively open dense coordinate-positivity sets in the complete \(\ell_1\) simplex.

## Relationship to prior work
Dantas, Jung and Martín (arXiv:2609.00794v1, September 1, 2026), particularly Theorem 3.3 and Lemma 3.14 with Theorem 3.15, give universal second-adjoint norm attainment for endomorphisms of \(c_0\) and exhibit a specific nonattaining second adjoint into \(c\), using a fixed strictly positive \(\ell_1\) core and paired differences. Those facts are **prior**. The present theorem treats a variable positive core, arbitrary normalized disjoint signed zero-sum finite contrasts, an exact limiting conflict-mass criterion for either behavior, and a dense-meagre classification of its full fixed-norm parameter family.

The published published-finding corpus finding “Three dense attainment strata for rank-one perturbations of \(c_0\hookrightarrow\ell_\infty\)” studies a distinct diagonal perturbation into \(\ell_\infty\) and separates ordinary, quasi-, and weak-star quasi-norm attainment according to vanishing coordinates; its full RESULT.md was inspected. That theorem supplies a closely related genericity paradigm and a special support-zero mechanism, but does not state the above exact weighted block-conflict criterion for second-adjoint attainment into \(c^{**}\), notably its positive-but-vanishing conflict examples. Choi, Jung, Kim and Martín (arXiv:2209.07763v1) provide the broader weak-star quasi-norm-attainment framework; this theorem concerns ordinary norm attainment of \(T_u^{**}\). These are close comparisons and a remaining conceptual novelty risk, not claims of absolute priority.

## Limitations
The theorem is about real \(c_0\to c\) maps of the stated normalized rank-one-plus-disjoint-contrast form, not all operators between these spaces. It assumes a positive core, finite disjoint zero-mean contrast supports, and strictly subunit contrast amplitudes converging to one. It does not assert anything for complex coefficients, overlapping contrasts or general perturbations. The Baire category statement concerns the positive coefficient simplex with its \(\ell_1\)-norm topology. Full novelty against unindexed or differently formulated literature cannot be guaranteed; the nearby rank-one weak-star-attainment literature poses a substantive priority/implication-comparison risk. No independent audit has taken place.

## References
1. Sheldon Dantas, Mingu Jung and Miguel Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794v1, initially submitted 2026-09-01, Theorem 3.3, Lemma 3.14 and Theorem 3.15. https://arxiv.org/abs/2609.00794
2. *Three dense attainment strata for rank-one perturbations of* \(c_0\hookrightarrow\ell_\infty\), published-finding corpus public scientific record 2026/10/11/SCOPE-three-dense-attainment-strata-for-rank-one-perturbations-of-c-0--033e6cd625fd, full RESULT.md consulted. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-dense-attainment-strata-for-rank-one-perturbations-of-c-0--033e6cd625fd
3. Geunsu Choi, Mingu Jung, Sun Kwang Kim and Miguel Martín, *Weak-star quasi norm attaining operators*, arXiv:2209.07763v1, initially submitted 2022-09-16. https://arxiv.org/abs/2209.07763
