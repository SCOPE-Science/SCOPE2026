# Sharp trace-ratio conservatism at balanced diagonal second moments

## Finding

Let \(d\ge1\), \(P=\operatorname{diag}(p_1,\ldots,p_d)\succ0\), and \(s_i=c p_i^2\) for a common \(c>0\). Define the moment-weighted admissibility ratio and its inverse-trace surrogate by
\[
q=\frac{\sum_{i=1}^d s_i/p_i}{\sum_{i=1}^d s_i/p_i^2},\qquad
T=\frac{\sum_{i=1}^d 1/p_i}{\sum_{i=1}^d 1/p_i^2},\qquad
\kappa=\frac{\max_i p_i}{\min_i p_i}.
\]
Then \(q=d^{-1}\sum_i p_i\), and the **sharp dimension-free comparison** is
\[
1\le\frac{q}{T}\le\frac{(\kappa-\sqrt{\kappa}+1)^2}{\kappa}.
\tag{1}
\]
For every \(\kappa>1\), the right-hand side is the supremum over finite dimensions and positive diagonal preconditioners having that exact condition number. In a finite dimension equality is possible exactly when \(\sqrt\kappa\) is rational. For positive integer \(\sqrt\kappa=t\), equality holds with one entry \(p_i=1\) and \(t\) entries \(p_i=t^2\). For arbitrary \(\kappa\), two-level spectra whose relative frequency of the smaller eigenvalue tends to \(1/(1+\sqrt\kappa)\) approach equality. The loss can grow linearly with \(\kappa\), although the second moments are perfectly aligned with the diagonal scales.

## Assumptions and scope

All coordinates are real and strictly positive; \(d\) is finite but arbitrary. A moment vector \(s_i=\mathbb E[g_i^2]>0\) is **balanced** with an unregularized diagonal preconditioner when \(s_i=c p_i^2\) for some \(c>0\). This is the exact frozen-moment fixed-point relation of the feedback
\[
p_i^{+}=\frac{p_i+\alpha\gamma s_i/p_i}{1+\alpha}
\]
when \(\alpha>0\) and \(c=1/\gamma\). It is not an assertion that a time-varying stochastic optimization trajectory converges to such a fixed point. It refers to the unsmoothed update, not the implementation with a positive regularizer \(\varepsilon\).

The ratio \(q\) appears in the sufficient one-step learning-rate condition in Yu--Chen--Feng (2026), while \(T\) is their computable trace-ratio lower bound under coordinatewise alignment. The comparison (1) concerns **headroom in that sufficient condition**, not a globally optimal learning rate or a convergence-rate guarantee.

## Proof

**Step 1: exact balance.** Substituting \(s_i=c p_i^2\) gives
\[
q=\frac{c\sum_i p_i}{cd}=\frac1d\sum_i p_i=:A.
\]
The same substitution is equivalent to \(p_i^{+}=p_i\) under the frozen expected preconditioner update when \(\gamma c=1\). Since inverse-square weights emphasize the smaller \(p_i\), the weighted Chebyshev inequality gives \(T\le A\). Explicitly,
\[
 d\sum_i p_i^{-1}\le \Big(\sum_i p_i\Big)\Big(\sum_i p_i^{-2}\Big),
\]
because the difference is \(\sum_{i<j}(p_i-p_j)(p_j^{-2}-p_i^{-2})\ge0\). This proves the left inequality.

**Step 2: reduction to two endpoints.** Scale all entries by their minimum; \(q/T\) is unchanged, and the entries lie in \([1,\kappa]\). For a probability measure \(\mu\) on that interval put
\[
 A_\mu=\int z\,d\mu(z),\quad B_\mu=\int z^{-1}\,d\mu(z),\quad C_\mu=\int z^{-2}\,d\mu(z),\quad F(\mu)=\frac{A_\mu C_\mu}{B_\mu}.
\]
The empirical measure of the entries yields \(F=q/T\). Compactness of the space of probability measures on \([1,\kappa]\) and positivity of all three continuous moments ensure that \(F\) has a maximizer \(\mu_*\). Assume \(\kappa>1\). Some nontrivial mixture of the endpoint masses has \(F>1\), by the strict weighted Chebyshev inequality; hence \(\mu_*\) is not a point mass.

For each \(z\in[1,\kappa]\), the one-sided derivative of \(\log F((1-\epsilon)\mu_*+\epsilon\delta_z)\) at \(\epsilon=0\) is
\[
 h(z)-1,\qquad h(z)=\frac{z}{A_*}+\frac{z^{-2}}{C_*}-\frac{z^{-1}}{B_*},
\]
with \(A_*=A_{\mu_*}\), and similarly for \(B_*\), \(C_*\). Maximality gives \(h(z)\le1\) for every \(z\). Also \(\int h\,d\mu_*=1\), so \(\mu_*\) is concentrated on \(\{z:h(z)=1\}\). But
\[
 h'(z)=\frac{z^3/A_*+z/B_*-2/C_*}{z^3}.
\]
Its numerator is strictly increasing for \(z>0\), so \(h\) is strictly decreasing and then strictly increasing, with at most one turning point. Consequently every interior point of \((1,\kappa)\) has \(h(z)<\max\{h(1),h(\kappa)\}\le1\). Thus \(\mu_*\) is supported entirely at the two endpoints. This argument covers all finite spectra, because their empirical measures are among the allowed probability measures.

**Step 3: exact endpoint optimization.** Write \(\kappa=t^2\), \(t>1\), and let a proportion \(u\in[0,1]\) lie at \(1\) and the rest at \(t^2\). Then
\[
 F(u)=\frac{\big(u+(1-u)t^2\big)\big(u+(1-u)t^{-4}\big)}{u+(1-u)t^{-2}}.
\]
Direct differentiation gives
\[
 F'(u)=-\frac{(t-1)^2(t+1)^2(t^2+1)\big(1+(t-1)u\big)\big((t+1)u-1\big)}{t^2\big(1+(t^2-1)u\big)^2}.
\]
Every factor except the final parenthesis has fixed positive sign. The unique maximum therefore occurs at \(u=1/(t+1)\), with
\[
F_{\max}=\frac{(t^2-t+1)^2}{t^2}=\frac{(\kappa-\sqrt\kappa+1)^2}{\kappa}.
\]
For \(\kappa=1\), every entry is equal and \(q/T=1\), also the value of the right side of (1). This proves the bound for every \(d\) and every spectrum.

**Step 4: sharpness and stochastic realization.** For integer \(t\ge2\), choose \(d=t+1\), \(p_1=1\), and \(p_2=\cdots=p_{t+1}=t^2\). Then \(u=1/(t+1)\) exactly and the upper bound is attained. More generally, the unique optimal endpoint fraction \(u=1/(1+t)\) is realizable by a finite multiset exactly when \(t\) is rational. For irrational \(t>1\), take rational proportions converging to that fraction; their endpoint multiplicities yield finite spectra with exact condition number \(t^2\) and ratios approaching the bound. The prescribed moments can be realized by independent symmetric signs \(g_i=\pm p_i/\sqrt\gamma\); in that case \(\mathbb E[g_i^2]=p_i^2/\gamma\) and the unregularized preconditioner is stationary even for each realized squared-gradient vector. The asymptotic gap is \(F_{\max}=\kappa-2\sqrt\kappa+3-2/\sqrt\kappa+1/\kappa\).

## Verification

Run the included Python 3 standard-library script with `python verify.py`. It uses exact rational arithmetic and reports `VERIFY_OK` after 32,059 finite-spectrum tests, eight perfect-square condition-number equality instances, and three exact stationary-feedback checks. Finite tests are corroboration, not an exhaustive proof for continuous spectra or arbitrary real \(\kappa\); the variational and derivative arguments above cover those domains.

## Relationship to prior work

Yu, Chen and Feng (arXiv:2605.12878v1, §2 and Appendix C) establish \(q\ge T\) under coordinatewise alignment and use \(T\) as a computable lower bound in a sufficient learning-rate condition. The present result addresses a distinct quantitative question: how large the loss \(q/T\) can be when moments obey the stronger, exact stationary balance \(s_i=c p_i^2\). Their proof establishes ordering, but not the sharp worst-case factor or its optimizing spectral proportions. Yu, Chen and Xu (arXiv:2604.08742v1) analyze the deterministic preconditioned acceleration mechanism; the stochastic trace surrogate is not its subject. Classical Lehmer-mean monotonicity also establishes \(T\le A\); it does not state the sharp spectral-spread-controlled ratio in (1). Classical Kantorovich bounds involve different inverse-moment products, and do not by themselves determine this three-moment extremum.

## Limitations

This is a finite-dimensional algebraic bound for an idealized frozen second-moment balance. It does not prove the balance emerges dynamically, guarantee that larger steps are safe beyond the sufficient condition, handle an implementation regularizer \(\varepsilon>0\) without modification, or establish a better convergence rate. Optimality is across arbitrary finite dimensions; for a prescribed dimension and a non-integral optimal endpoint mass, the exact best constant can be smaller. Historical inequalities for generalized means could contain equivalent special cases not located in the checked literature.

## References

1. Y. Yu, L. Chen, and M. Feng, *Adam-SHANG: A Convergent Adam-Type Method for Stochastic Smooth Convex Optimization*, arXiv:2605.12878v1 (first public 2026-05-13), §2 and Appendix C. https://arxiv.org/html/2605.12878v1
2. Y. Yu, L. Chen, and Z. Xu, *Adam-HNAG: A Convergent Reformulation of Adam with Accelerated Rate*, arXiv:2604.08742v1 (2026), §§3.2--3.6. https://arxiv.org/html/2604.08742
3. D. H. Lehmer, *On the compounding of certain means*, Journal of Mathematical Analysis and Applications 36 (1971), 183--200. Cited for the classical mean family; no claim of its complete text having been inspected.
4. L. V. Kantorovich, classical bounded-spectrum mean inequality; comparison to the familiar product of first and inverse first moments rather than the three-moment quotient proved here. https://en.wikipedia.org/wiki/Kantorovich_inequality
