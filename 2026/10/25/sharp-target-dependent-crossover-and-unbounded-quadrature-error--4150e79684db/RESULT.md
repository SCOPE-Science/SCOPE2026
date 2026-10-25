# Sharp target-dependent crossover and unbounded quadrature error gap between pivoted Cholesky and volume sampling

## Finding

**Theorem (two-level discrete kernel, complete target classification).** Let \(m\ge2\), \(2\le k\le m\), and \(L>1\). Equip the finite set \(X=\{0,1,\ldots,m\}\) with counting measure and the positive-definite diagonal kernel
\[
K_L=\operatorname{diag}(L,1,\ldots,1).
\]
Draw \(k\) distinct quadrature nodes by either residual-diagonal randomly pivoted Cholesky (RPChol, denoted \(R\)), or fixed-size determinantal volume sampling with subset probabilities proportional to principal \(k\)-minors (denoted \(D\)). For every real target density \(g=(g_0,\ldots,g_m)\), use the optimal kernel-quadrature weights at the drawn nodes to approximate the functional \(I_g(f)=\sum_{i=0}^{m}g_i f_i\). Write \(\mathcal E_R(g)\) and \(\mathcal E_D(g)\) for the **expectations of the squared worst-case RKHS quadrature errors**, not the squares of expected errors.

Define the spike-omission probabilities
\[
p_R=\prod_{j=0}^{k-1}\frac{m-j}{L+m-j},\qquad
p_D=\frac{m-k+1}{kL+m-k+1}.
\]
Then \(0<p_R<p_D<1\), and, writing \(Q=\sum_{i=1}^m g_i^2\),
\[
\mathcal E_J(g)=L g_0^2p_J+\frac{m-k+1-p_J}{m}Q
\quad (J\in\{R,D\}).
\]
In particular,
\[
\boxed{\mathcal E_D(g)-\mathcal E_R(g)
=(p_D-p_R)\left(Lg_0^2-\frac{Q}{m}\right).}
\]
RPChol is strictly better **exactly when** \(Lg_0^2>Q/m\); fixed-size volume sampling is strictly better **exactly when** \(Lg_0^2<Q/m\); equality holds **exactly when** \(Lg_0^2=Q/m\). Thus neither sampler uniformly dominates the other for all target densities, despite the strictly smaller dominant-coordinate omission probability under RPChol.

For the natural coordinate target \(g=e_0\), the comparison is unbounded: as \(L\to\infty\) with \(m,k\) fixed,
\[
\mathcal E_R(e_0)\sim (m)_kL^{1-k}\to0,\qquad
\mathcal E_D(e_0)\to\frac{m-k+1}{k}>0,
\]
\[
\boxed{\frac{\mathcal E_D(e_0)}{\mathcal E_R(e_0)}
\sim\frac{L^{k-1}}{k(m)_{k-1}}\to\infty,}
\]
where \((m)_r=\prod_{j=0}^{r-1}(m-j)\). These asymptotics concern **expected squared error**, not a high-probability comparison.

## Assumptions and scope

The underlying Hilbert space is the real RKHS on the finite space \(X\) with Gram matrix \(K_L\); it consists of all functions \(f=(f_0,\ldots,f_m)\) with
\[
\|f\|_{\mathcal H}^2=\frac{f_0^2}{L}+\sum_{i=1}^m f_i^2.
\]
RPChol starts from residual \(K_L\), chooses each next pivot with probability proportional to its current residual diagonal, and updates the residual by an exact Schur complement. The determinant sampler assigns to each unordered \(k\)-set \(S\subseteq X\) probability proportional to \(\det K_L[S,S]\). Both rules use **the same kernel, number of nodes, and target functional**; optimal quadrature weights are recomputed after the subset is drawn. All parameters are exact, with no numerical-roundoff assumptions. The theorem is not a pointwise assertion about individual random pivot sets.

## Proof

**1. Exact optimal weights and residual.** Evaluation at \(i\) has representer \(K_L(:,i)\). The representer of \(I_g\) is \(K_Lg\). Because this kernel is diagonal, the kernel sections supported at a sampled node are mutually orthogonal in \(\mathcal H\), and the optimal approximation to \(K_Lg\) is obtained by taking weight \(g_i\) at each \(i\in S\). Consequently the squared worst-case error for a fixed set \(S\) is exactly
\[
E(S;g)^2=\sup_{\|f\|_{\mathcal H}\le1}
\left|I_g(f)-\sum_{i\in S}g_if_i\right|^2
=L g_0^2\mathbf1_{\{0\notin S\}}+
\sum_{i=1}^m g_i^2\mathbf1_{\{i\notin S\}}.
\]
This is the squared norm of the unsampled part of the representer, not a heuristic proxy.

**2. Exact inclusion probabilities.** Every unselected diagonal entry is unchanged by a Cholesky pivot, while the selected diagonal entry becomes zero. Thus, conditional on excluding node \(0\) in the first \(j\) pivots, the next pivot also excludes it with probability \((m-j)/(L+m-j)\), which yields \(p_R\).

Under volume sampling, there are \(\binom m{k-1}\) subsets containing node \(0\), each with determinant \(L\), and \(\binom m k\) subsets excluding it, each with determinant \(1\). Hence
\[
p_D=\frac{\binom m k}{L\binom m{k-1}+\binom m k}
=\frac{m-k+1}{kL+m-k+1}.
\]
At \(L=1\), both omission probabilities equal \((m-k+1)/(m+1)\). For \(L>1\),
\[
\frac{\mathrm d}{\mathrm dL}\log p_R
=-\sum_{j=0}^{k-1}\frac1{L+m-j}
\le-\frac{k}{L+m}
<-\frac{k}{kL+m-k+1}
=\frac{\mathrm d}{\mathrm dL}\log p_D.
\]
The strict inequality uses \(k\ge2\) and \((k-1)(L-1)>0\). Integration from \(1\) to \(L\) yields \(p_R<p_D\); positivity is immediate.

**3. Complete risk comparison.** Permuting the \(m\) unit-eigenvalue coordinates preserves both subset laws. Their common per-coordinate probability of omission, say \(q_J\), satisfies the counting identity \(p_J+m q_J=m+1-k\), because exactly \(m+1-k\) coordinates are omitted. Hence \(q_J=(m-k+1-p_J)/m\). Taking expectations in the residual formula of step 1 gives the two displayed risk formulas. Subtracting proves the exact sign classification, including its equality boundary. In matrix form, the expected residual quadratic forms differ by
\[
\mathcal E_D(g)-\mathcal E_R(g)
=(p_D-p_R)\,g^{\mathsf T}\operatorname{diag}(L,-1/m,\ldots,-1/m)g.
\]
The difference has one positive and \(m\) negative eigenvalues, proving the failure of target-uniform quadratic-form dominance in both directions.

**4. Sharp large-contrast separation.** Directly from step 2,
\[
p_R=(m)_k L^{-k}(1+O(L^{-1})),\qquad
p_D=\frac{m-k+1}{k}L^{-1}(1+O(L^{-1})).
\]
For \(g=e_0\), step 3 reduces both risks to \(Lp_J\). Multiplying these expansions proves the two error limits and the stated ratio, using \((m)_k=(m-k+1)(m)_{k-1}\). All asymptotics are for fixed integers \(m,k\). For instance, at \(m=3,k=2\), the omission probabilities simplify exactly to
\[
p_R=\frac6{(L+3)(L+2)},\qquad p_D=\frac1{L+1},
\]
so \(\mathcal E_R(e_0)=6L/((L+3)(L+2))\to0\) whereas \(\mathcal E_D(e_0)=L/(L+1)\to1\).

## Verification

The accompanying `verify.py` uses only the Python standard library, and sums **all ordered distinct RPChol pivot paths** and **all fixed-size determinantal subsets** with exact rational arithmetic for \(2\le m\le5\), \(2\le k\le m\), and \(L\in\{1,3/2,2,5,20\}\). For three different rational target vectors at each parameter choice, it checks the exact subset probabilities, optimal-weight RKHS error, risk identities, and risk difference. It separately checks the two-pivot witness and high-contrast coefficient numerically in rational arithmetic. Invocation: `python3 verify.py`. Its successful check string is `VERIFY_OK`. This finite enumeration only corroborates the all-parameter symbolic proof above.

## Relationship to prior work

Epperly and Moreno (2023) introduced RPChol kernel quadrature and explicitly identified separating its performance from continuous volume sampling as an interesting research direction. The present theorem is a deliberately discrete, finite-rank comparison and is not an improvement of their generic spectral-error bound.

Belhadji, Bardenet, and Chainais (2020) established expected kernel interpolation/quadrature bounds for continuous volume sampling and a diagonal spectral decomposition of expected squared errors. Fixed-size determinant sampling and optimal RKHS weights are not new here. Chen, Epperly, Tropp, and Webber (2022 preprint; later journal publication), including their Appendix C, developed RPChol matrix approximation and fixed-size DPP comparisons; those results concern matrix-approximation guarantees and do not state this all-target quadrature-risk crossover. Yu (2010) proved general inclusion-probability comparisons between successive and rejective sampling: in this diagonal model, these are the sampling mechanisms underlying RPChol and volume sampling, respectively. Hence the qualitative dominant-coordinate inclusion ordering is **not** claimed as original; the contribution is the exact target-dependent quadrature comparison, its indefinite risk difference, and its sharp unbounded-error separation on a concrete kernel family.

The reduction to unequal-probability sampling, and the existence of closely related results outside kernel-quadrature terminology, remain significant prior-art risks. A numerical finite-space counterexample alone does not establish uniform claims for continuous domains.

## Limitations

This is a finite, diagonal, highly symmetric **one-spike** kernel and a fixed node budget with \(2\le k\le m\). It proves neither performance dominance for arbitrary kernels nor consequences for smooth continuous spaces, noisy evaluations, nonoptimal weights, specific real-world data, high-probability errors, or ratios of expected unsquared errors. The large-contrast limit fixes \(m,k\) before sending \(L\to\infty\); interchanging limits is not covered. The strict inclusion inequality and the selected-omission probabilities were already motivated by classical unequal-probability sampling, so the theorem's interpretation should not be inflated to a new general stochastic ordering.

## References

1. Ethan N. Epperly and Elvira Moreno, *Kernel quadrature with randomly pivoted Cholesky*, arXiv:2306.03955, first posted June 6, 2023. https://arxiv.org/abs/2306.03955
2. Ayoub Belhadji, Rémi Bardenet, and Pierre Chainais, *Kernel interpolation with continuous volume sampling*, arXiv:2002.09677, 2020. https://arxiv.org/abs/2002.09677
3. Tyler Chen, Ethan N. Epperly, Joel A. Tropp, and Robert J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503, 2022; in particular Appendix C on determinantal sampling. https://arxiv.org/abs/2207.06503
4. Yaming Yu, *On the inclusion probabilities in some unequal probability sampling plans without replacement*, arXiv:1005.4107, 2010. https://arxiv.org/abs/1005.4107
