# Sharp minimax risk and optimal meshes for reflected-pair quadrature of convex Lipschitz functions

## Finding
Let \(n\ge 1\), \(L>0\), and fix a deterministic partition \(0=t_0<t_1<\cdots<t_n=1\) with \(h_i=t_i-t_{i-1}>0\). Independently sample \(U_i\sim\operatorname{Unif}[0,1]\), and evaluate the reflected-pair (antithetic) estimator
\[
Q(f)=\sum_{i=1}^{n}\frac{h_i}{2}\bigl(f(t_{i-1}+h_iU_i)+f(t_i-h_iU_i)\bigr),\qquad I(f)=\int_0^1 f(x)\,dx.
\]
Over the class \(\mathcal F_L\) of **all real, convex, \(L\)-Lipschitz functions on \([0,1]\)**, the estimator is unbiased and has **exact minimax mean-squared error**
\[
\boxed{\sup_{f\in\mathcal F_L}\mathbb E(Q(f)-I(f))^2=\frac{L^2}{48}\max_{1\le i\le n}h_i^4.}\tag{1}
\]
The supremum is attained **only** by \(f(x)=L|x-c|+C\), where \(C\in\mathbb R\) and \(c=(t_{j-1}+t_j)/2\) is the midpoint of some cell of maximal width. Every such choice attains equality.

Consequently, the equal-width partition is the **unique minimax \(n\)-cell partition**, with sharp risk \(L^2/(48n^4)\) and root-mean-square error \(L/(\sqrt{48}\,n^2)\). There are precisely two function evaluations per cell; evaluations in distinct cells and within a pair are reflections of a **single uniform point** per cell, not two independent uniform points.

The same analysis gives a robust version. If the \(2n\) evaluations instead have mutually independent, mean-zero, equal-variance additive noises with variance \(\nu^2\ge0\), independent of the \(U_i\), then
\[
\boxed{\sup_{f\in\mathcal F_L}\mathbb E(\widetilde Q(f)-I(f))^2
=\frac{L^2}{48}\max_i h_i^4+\frac{\nu^2}{2}\sum_i h_i^2.}\tag{2}
\]
The unique minimax partition remains equal-width, giving \(L^2/(48n^4)+\nu^2/(2n)\). No claim is made that this estimator is minimax among **all possible quadrature rules**.

## Assumptions and scope
The partition is deterministic with positive cell widths summing to one. The samples \(U_1,\ldots,U_n\) are independent uniforms. The integrand is continuous, convex and globally \(L\)-Lipschitz; its distributional second derivative may be singular or atomic, and differentiability is **not** assumed. In the noisy extension, each call produces fresh independent additive noise with mean zero and variance \(\nu^2\); its distribution otherwise is unrestricted. All expected squared errors include integration randomness and, where stated, measurement randomness. The optimization concerns the supremum over this class **for a fixed partition**, followed by deterministic partition choice at fixed \(n\).

## Proof
**1. Representation and affine cancellation.** Since \(f\) is convex and Lipschitz, its right derivative on the interior is nondecreasing and takes values in \([-L,L]\). Its distributional second derivative is a finite nonnegative Borel measure \(\mu\) on \((0,1)\), of mass \(M\le 2L\). For some real \(a,b\),
\[
f(x)=a+bx+\int_{(0,1)}(x-s)_+\,\mu(ds).
\]
This representation holds on the closed interval by continuity; the possible endpoint derivative conventions are absorbed in \(a,b\). Each reflected pair integrates affine functions exactly for **every sample** because its two abscissas have sum equal to the cell endpoints, and the pair's mean is the cell midpoint. Hence
\[
Q(f)-I(f)=\int_{(0,1)}E_s\,\mu(ds),
\]
where \(E_s=Q((\cdot-s)_+)-I((\cdot-s)_+)\). If \(s\) falls outside the interior of a given cell, the hinge is affine on that cell and its local error is identically zero. In particular \(E_s\) depends only on the random sample from its own cell.

**2. Exact local hinge law and covariance.** In a cell \([a,a+h]\) containing \(s\), set \(\theta=(s-a)/h\in(0,1)\), \(\rho=\min\{\theta,1-\theta\}\in(0,1/2]\), and \(Z=\min\{U,1-U\}\sim\operatorname{Unif}[0,1/2]\). A direct evaluation of the two hinges, subtracting their exact cell integral, yields
\[
E_s=\frac{h^2}{2}\bigl[(\rho-Z)_+-\rho^2\bigr].\tag{3}
\]
The elementary moments \(\mathbb E(\rho-Z)_+=\rho^2\) and \(\mathbb E(\rho-Z)_+^2=2\rho^3/3\) give
\[
\operatorname{Var}(E_s)=\frac{h^4}{4}\left(\frac{2\rho^3}{3}-\rho^4\right)\le\frac{h^4}{192}.\tag{4}
\]
The quantity in parentheses increases strictly on \((0,1/2)\), since its derivative is \(2\rho^2(1-2\rho)>0\); equality in (4) occurs precisely when \(s\) is the cell midpoint. A more detailed exact covariance identity, useful for arbitrary curvature measures, is: if \(s,t\) lie in the same cell, write \(u=\min\{\rho_s,\rho_t\}\) and \(v=\max\{\rho_s,\rho_t\}\). Then
\[
\operatorname{Cov}(E_s,E_t)=\frac{h^4}{4}\left(u^2v(1-v)-\frac{u^3}{3}\right).\tag{5}
\]
Indeed \(\mathbb E[(u-Z)_+(v-Z)_+]=u^2v-u^3/3\), and subtracting the product of means gives (5). Hinges in different cells have zero covariance. Thus (5) integrates against \(\mu\otimes\mu\) to produce the **exact** error variance of any \(f\) in the class, not merely a bound.

**3. Sharp global bound.** Minkowski's integral inequality in \(L^2(\Omega)\), followed by (4), gives
\[
\|Q(f)-I(f)\|_{L^2}
\le \int\|E_s\|_{L^2}\,\mu(ds)
\le\frac{\max_i h_i^2}{\sqrt{192}}\,M
\le\frac{2L\max_i h_i^2}{\sqrt{192}}.
\]
Squaring yields (1). Each cell pair is individually unbiased by symmetry, so the squared norm is its mean-squared error.

**4. Sharpness and all equality cases.** Pick a longest cell with midpoint \(c\), and set \(f(x)=L|x-c|+C\). Its distributional curvature is \(\mu=2L\delta_c\), so the preceding inequalities are equalities; (4) gives \(\operatorname{Var}(Q(f))=L^2h_j^4/48\). Conversely, if equality holds, the curvature mass must be \(2L\), and (4) forces \(\mu\) to be supported on midpoints of longest cells. If at least two distinct cells carry positive mass, their nondegenerate independent centered errors prevent equality in Minkowski (their \(L^2\) inner product is zero, not positive maximal). Hence \(\mu=2L\delta_c\) at one longest-cell midpoint. Requiring all slopes in \([-L,L]\) and their jump to be \(2L\) fixes the left and right slopes to \(-L\) and \(L\), proving \(f(x)=L|x-c|+C\).

**5. Optimal partition and additive noise.** Because \(\sum_i h_i=1\), \(\max_i h_i\ge1/n\), with equality if and only if every \(h_i=1/n\). Formula (1) therefore gives the unique optimal partition. If independent additive errors \(\epsilon_{i,+},\epsilon_{i,-}\) have common variance \(\nu^2\), the added estimator error is \(\sum_i h_i(\epsilon_{i,+}+\epsilon_{i,-})/2\), independent of the integration error. Its variance is \(\nu^2\sum_i h_i^2/2\), yielding (2). The noise-independent extremizers from step 4 still attain the supremum. The uniform mesh simultaneously and uniquely minimizes both \(\max_i h_i^4\) and \(\sum_i h_i^2\) for positive widths, completing the proof.

## Verification
The embedded `verify.py` needs only standard Python. Run `python verify.py`; the recorded output is `VERIFY_OK 3562 exact rational assertions`. Its exact `Fraction` tests compare a direct piecewise-affine integration of arbitrary finite hinge sums to (5), check local maximizers, verify the global inequality for generated nonuniform rational meshes, test equality for all uniform meshes up to twenty cells, and check the independent-noise term. These finite computations corroborate (3)–(5); the proof of the all-functions, all-partitions claim is analytic and does not depend on exhaustive enumeration. No simulation, computer-assisted infinite certification, or independent expert audit is claimed.

## Relationship to prior work
Wu's 2020 preprint *A randomised trapezoidal quadrature* [1] introduces exactly the reflected within-cell design and analyzes unbiasedness and fractional-Sobolev error bounds. In particular its Theorem 3.2 gives a norm bound with an unspecified constant for its Sobolev class; it does **not** state (1), the complete convex-Lipschitz equality classification, arbitrary partition minimaxity, or the exact independent-query-noise extension. Thus reflected sampling and its general unbiasedness are acknowledged prior art, not asserted new contributions. Owen's 2008 study [2] treats local antithetic sampling within randomized quasi-Monte Carlo nets and derives smooth-function rates, but its estimator and extremal class differ. Goldstein, Rinott and Scarsini [3] study stratified-sampling convex order, not the within-stratum reflected-pair convex-Lipschitz sharp variance. Goda, Kazashi and Suzuki [4] study Gaussian-weight randomized trapezoid error rates, distinct in distribution and function space. The contribution is **the exact sharp minimax law (1), its equality family, and partition/noise consequences for the fixed reflected-pair estimator**, not the basic method of antithetic quadrature or general variance reduction.

## Limitations
The result applies to one-dimensional integration of convex Lipschitz functions, with a fixed number of independent reflected pairs. Nonconvex Lipschitz functions can have signed curvature of unbounded total variation and are not covered. Uniform partitions are optimal **within this design**; adaptivity, alternative unbiased algorithms, independent-within-pair sampling, multivariate domains, unequal query costs, dependent or heteroscedastic errors, and varying evaluation counts are outside the theorem. The exact independence assumptions cannot be weakened by this proof. Searches of indexed prior findings and specified literature are not a proof that all historical publications have been exhausted; specialized earlier exact minimax formulas remain a residual priority risk.

## References
[1] Yue Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086v1, publicly posted 2020-11-30, https://arxiv.org/abs/2011.15086 .

[2] Art B. Owen, *Local antithetic sampling with scrambled nets*, arXiv:0811.0528v1, 2008, https://arxiv.org/abs/0811.0528 .

[3] Larry Goldstein, Yosef Rinott and Marco Scarsini, *Stochastic comparisons of stratified sampling techniques for some Monte Carlo estimators*, arXiv:1005.5414v2, 2011, https://arxiv.org/abs/1005.5414 .

[4] Takashi Goda, Yoshihito Kazashi and Yuya Suzuki, *Randomizing the trapezoidal rule gives the optimal RMSE rate in Gaussian Sobolev spaces*, arXiv:2212.11476v1, 2022, https://arxiv.org/abs/2212.11476 .
