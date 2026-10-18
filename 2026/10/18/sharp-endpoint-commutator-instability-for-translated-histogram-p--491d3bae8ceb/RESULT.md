# Sharp endpoint commutator instability for translated histogram projections

## Finding

Let \(n\ge2\) be an integer and \(0<t<1\). On the length-\(n\) circle \(\mathbb T_n=\mathbb R/n\mathbb Z\), let \(P\) be conditional expectation onto the partition \(I_j=[j,j+1)\), and \(Q_t\) onto the shifted partition \(J_j=[j+t,j+1+t)\), where all indices are taken modulo \(n\). Define \(K_t=PQ_t-Q_tP\). The **sharp endpoint norm** is

\[
\|K_t\|_{L^1\to L^1}=\|K_t\|_{L^\infty\to L^\infty}=
\begin{cases}
2\max\{t,1-t\}|2t-1|,&n=2,\\
2\max\{t,1-t\}^{2},&n\ge3.
\end{cases}
\]

In particular, for every fixed \(n\ge3\), the endpoint commutator norm tends to \(2\) as the two partitions coalesce, even though the commutator vanishes at coincident partitions. The same endpoint limit is \(2\) for \(n=2\), but at half-translation the two-interval case instead has \(K_{1/2}=0\). The largest norm is witnessed, for \(n\ge3\), by normalized characteristic functions of the **short** cells in the common refinement (there are two choices when \(t=1/2\)).

## Assumptions and scope

The measure is Lebesgue measure, normalized or unnormalized. Operators act on real or complex \(L^p(\mathbb T_n)\). Both conditional expectations are unital positive contractions. No assertion of a dimension-uniform bound smaller than \(2\) is made; all results here are for a fixed finite integer \(n\). The singular-value statement concerns the Hilbert-space realization of the same finite-rank commutator, with zeros omitted and multiplicities retained.

## Proof

**1. Exact common-refinement matrix.** Write \(A_j=[j,j+t)\) and \(B_j=[j+t,j+1)\). Their lengths are \(t\) and \(u=1-t\). The two partitions are \(I_j=A_j\cup B_j\) and \(J_j=B_j\cup A_{j+1}\). Relative to the \(2n\) atom-indicator basis, the two expectation matrices are explicitly

\[
P_{vw}=|C_w|\mathbf 1_{\{I(v)=I(w)\}},\qquad
(Q_t)_{vw}=|C_w|\mathbf 1_{\{J(v)=J(w)\}},
\]

where \(C_w\) is one of the \(A_j,B_j\). Thus \(K_t\) vanishes on inputs with zero integral on every common-refinement cell; its integral kernel is constant on every product of two such cells. Therefore the exact \(L^1\) norm is the largest integral absolute value of a kernel column, equivalently

\[
\|K_t\|_{1\to1}=\max_w\frac1{|C_w|}\sum_v |C_v|\,|(K_t)_{vw}|.
\]

This identity is exact on the ambient \(L^1\), not merely on its finite-dimensional step subspace: the cell-integral map is contractive and surjects onto the full finite-dimensional weighted \(\ell^1\) space.

**2. The two column types.** For the input \(\mathbf1_{A_0}/t\) the identities \(P(\mathbf1_{A_0}/t)=\mathbf1_{I_0}\) and \(Q_t(\mathbf1_{A_0}/t)=\mathbf1_{J_{-1}}\) give

\[
K_t(\mathbf1_{A_0}/t)=u\mathbf1_{I_{-1}}+t\mathbf1_{I_0}-t\mathbf1_{J_{-1}}-u\mathbf1_{J_0}.
\]

For the input \(\mathbf1_{B_0}/u\), similarly,

\[
K_t(\mathbf1_{B_0}/u)=u\mathbf1_{I_0}+t\mathbf1_{I_1}-t\mathbf1_{J_{-1}}-u\mathbf1_{J_0}.
\]

When \(n\ge3\), the nonzero cell contributions in the first identity have total absolute integral \(2u(t+|2t-1|)\); in the second they total \(2t(u+|2t-1|)\). Cyclic translations account for every kernel-column type. Their maximum is \(2u^2\) when \(t\le1/2\) and \(2t^2\) when \(t\ge1/2\), giving the asserted formula and all elementary sharp witnesses.

For \(n=2\), two cell targets that are distinct for \(n\ge3\) coincide modulo two; their coefficients cancel. Directly collecting the two identities yields column norms \(2u|2t-1|\) and \(2t|2t-1|\). This proves the exceptional formula, including the exact vanishing at \(t=1/2\).

**3. Dual endpoint norm.** The two conditional expectations are self-adjoint on \(L^2\), so \(K_t^*=-K_t\). The common-refinement integral kernel is real and skew-symmetric after the standard kernel normalization; hence \(\|K_t\|_{\infty\to\infty}=\|K_t^*\|_{1\to1}=\|K_t\|_{1\to1}\).

**4. Hilbert singular spectrum.** The normalized indicators of \(I_j\) and \(J_j\) are orthonormal bases of the two \(n\)-dimensional projection ranges. Their cross-Gram matrix is the circulant \(G=uI+tS\), where \(S\) is the cyclic shift. Discrete Fourier diagonalization gives its singular values

\[
\gamma_k=|u+t\exp(2\pi\mathrm i k/n)|
=\sqrt{1-4t(1-t)\sin^2(\pi k/n)},\qquad 0\le k<n.
\]

For a principal-angle pair with cosine \(\gamma\in(0,1)\), the restrictions of the two projections to the canonical two-dimensional block have commutator singular values \(\gamma\sqrt{1-\gamma^2}\), twice. At \(\gamma=0\) or \(\gamma=1\) that block contributes only zeros. Orthogonality of the principal-angle blocks proves the full nonzero singular-value multiset and in particular

\[
\|K_t\|_{2\to2}
=\max_{1\le k<n}2\sqrt{t(1-t)}|\sin(\pi k/n)|
\sqrt{1-4t(1-t)\sin^2(\pi k/n)}
\le2\sqrt{t(1-t)}.
\]

Because \(\|K_t\|_{1\to1},\|K_t\|_{\infty\to\infty}\le2\), interpolation between \(L^1,L^2\) or \(L^2,L^\infty\) proves \(\|K_t\|_{p\to p}\to0\) for every fixed \(1<p<\infty\) at both translation boundaries. Directly \(Q_0=P\) and \(Q_1=P\), so \(K_0=K_1=0\), while the endpoint interior limits are \(2\). This establishes the claimed endpoint-only operator-norm discontinuity.

## Verification

The accompanying `check.py` independently constructs the two exact-rational averaging matrices on the common refinement for \(2\le n\le12\), compares all weighted column sums with both formulas at many rational translations, and verifies weighted skew-adjointness. It separately checks the Fourier principal-angle identity numerically. Run `python3 check.py` using the Python standard library. The analytic proof above supplies the all-\(n\), all-\(t\) conclusion; the finite tests alone would not.

## Relationship to prior work

Cohen's study of iterates of products of conditional expectations establishes pointwise convergence and maximal inequalities; its object is the iterated product, not the one-step commutator on translated periodic histogram partitions. Badea–Seifert study alternating-projection convergence and geometric rates in Hilbert spaces. Bauschke and collaborators study Douglas–Rachford convergence in terms of the Friedrichs angle. These lines explain why the Hilbert principal angles here are natural, but the **exact sharp \(L^1/L^\infty\) commutator profiles, exceptional two-bin cancellation, and endpoint-only translation instability** are not conclusions of those inspected results. No global priority claim beyond these checked comparisons is asserted.

## Limitations

The theorem is restricted to uniform periodic partitions, a common translation with \(0<t<1\), and finite \(n\ge2\). It does not classify arbitrary nonuniform meshes or general sigma-algebras. Unindexed equivalent calculations could exist in earlier work on histograms, alternating expectations, and finite Markov kernels. The Hilbert-space principal-angle calculation by itself is elementary; the claimed added content is the sharp endpoint behavior and its exceptional small-dimension boundary.

## References

1. Guy Cohen, *Iterates of a product of conditional expectation operators*, Journal of Functional Analysis 242 (2007), 658–668, DOI:10.1016/j.jfa.2006.09.008. Relevant preprint text at https://www.researchgate.net/publication/222830976_Iterates_of_a_product_of_conditional_expectation_operators.
2. H. H. Bauschke, J. Y. Bello Cruz, T. A. Nghia, H. M. Phan, X. Wang, *The rate of linear convergence of the Douglas–Rachford algorithm for subspaces is the cosine of the Friedrichs angle*, arXiv:1309.4709v1, 2013-09-18. https://arxiv.org/html/1309.4709v2.
3. C. Badea and D. Seifert, *Ritt operators and convergence in the method of alternating projections*, arXiv:1510.04560v1, 2015-10-15. https://arxiv.org/html/1510.04560v2.
