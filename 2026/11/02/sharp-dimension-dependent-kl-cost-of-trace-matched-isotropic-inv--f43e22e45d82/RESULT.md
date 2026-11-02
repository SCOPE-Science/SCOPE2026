# Sharp dimension-dependent KL cost of trace-matched isotropic inverse covariance

## Finding

Let \(k\ge 2\), \(\kappa>1\), and \(B\) be any real symmetric positive-definite \(k\times k\) matrix with spectral condition number at most \(\kappa\). Define its trace-matched isotropic inverse approximation by
\[
\omega_B=\frac{1}{k}\operatorname{tr}(B^{-1}),\qquad
\widetilde\Sigma_B=\omega_B I_k.
\]
For \(1\le j\le k-1\), put \(p_j=j/k\) and
\[
\mathcal H_\kappa(p)=\frac12\left[
\frac{(\kappa-1)^2}{\kappa}p(1-p)
-\log\left(1-p+\frac p\kappa\right)-p\log\kappa\right].
\]
Then the **exact sharp uniform bound** is
\[
\boxed{\frac1k D_{\mathrm{KL}}\bigl(\mathcal N(0,\widetilde\Sigma_B)\,\|\,\mathcal N(0,B^{-1})\bigr)
\ \le\ \max_{1\le j\le k-1}\mathcal H_\kappa(j/k).}
\]
Equality holds exactly for matrices whose spectrum, up to a common positive scale, consists of \(j\) copies of \(\kappa\) and \(k-j\) copies of \(1\), where \(j\) attains the displayed finite maximum. For \(\kappa=1\), both sides are zero, with all matrices scalar.

More precisely, \(\mathcal H_\kappa(p)\) has a unique maximizer \(p_*\in(0,1)\). It is the unique solution of
\[
\frac{(\kappa-1)^2}{\kappa}(1-2p)
+\frac{1-\kappa^{-1}}{1-p+p/\kappa}-\log\kappa=0.
\]
Consequently the finite maximum needs only the two integers adjacent to \(k p_*\), clipped to the range \(1,\ldots,k-1\), rather than a search over arbitrary spectra.

The sharp bound satisfies the two distinct condition-number asymptotics
\[
\max_j\mathcal H_\kappa(j/k)
=\frac{(\kappa-1)^2}{16}\,\eta_k+O((\kappa-1)^3)
\quad(\kappa\downarrow1),
\]
\[
\max_j\mathcal H_\kappa(j/k)
=\frac{\kappa}{8}\,\eta_k+O(\log\kappa)
\quad(\kappa\to\infty),
\qquad
\eta_k=\begin{cases}1,&k\text{ even},\\1-k^{-2},&k\text{ odd}.
\end{cases}
\]
In contrast, the general spectral estimate \(\frac1k D_{\mathrm{KL}}\le \frac12(\kappa-1)^2\) is not asymptotically sharp in either regime.

## Assumptions and scope

All matrices are finite-dimensional, real, symmetric and strictly positive definite; all logarithms are natural. The comparison is in the **ordered** direction \(D_{\mathrm{KL}}(\mathcal N(0,\omega_B I_k)\|\mathcal N(0,B^{-1}))\), not the reverse KL. The isotropic coefficient is the mean inverse eigenvalue (trace matching), which minimizes Frobenius error of \(B^{-1}\) among scalar matrices; it is *not* chosen to minimize this KL direction. The condition number is the spectral ratio \(\lambda_{\max}(B)/\lambda_{\min}(B)\). No assumptions are made on eigenvectors.

The result is a sharp extremal statement over all such \(B\). It can be applied to the generic positive-definite bulk/complement operators in stochastic-Lanczos inverse approximations, but the extremizers need not be realizable under every additional constraint imposed by a particular fixed Krylov construction.

## Proof

**Step 1 (spectral reduction).** By orthogonal invariance of KL divergence between centered Gaussians, write the eigenvalues of \(B\) as \(t_1,\ldots,t_k>0\). Multiplying all of them by the same positive scalar leaves the divergence unchanged. Set
\[
m=\frac1k\sum_{i=1}^k t_i,\qquad
h=\frac1k\sum_{i=1}^k t_i^{-1},\qquad
\ell=\frac1k\sum_{i=1}^k\log t_i.
\]
The exact centered-Gaussian KL formula gives
\[
F(t_1,\ldots,t_k)
:=\frac2k D_{\mathrm{KL}}\bigl(\mathcal N(0,hI_k)\|\mathcal N(0,B^{-1})\bigr)
=mh-1-\log h-\ell.
\tag{1}
\]
By scale invariance, normalize the smallest eigenvalue to \(1\); then every \(t_i\in[1,\kappa]\).

**Step 2 (a strict coordinate-convexity lemma).** Fix all eigenvalues except one, denoted \(t>0\), and put
\[
S=\sum_{i\ne j}t_i,\qquad R=\sum_{i\ne j}t_i^{-1}.
\]
Both are positive. Differentiating (1) twice in \(t\), while holding the others fixed, yields exactly
\[
\frac{\partial^2 F}{\partial t^2}
=\frac{2S}{k^2t^3}+\frac{R^2}{(Rt+1)^2}-\frac{k-1}{kt^2}.
\tag{2}
\]
Cauchy–Schwarz gives \(SR\ge(k-1)^2\). Let \(a=(k-1)/k\in[1/2,1)\) and \(y=Rt/(1+Rt)\in(0,1)\). Multiplying (2) by \(t^2\) and applying this Cauchy bound gives
\[
t^2F_{tt}\ge\frac{2a^2}{y}+y^2-2a^2-a.
\]
The arithmetic–geometric mean inequality applied to \(y^2,a^2/y,a^2/y\) gives
\[
\frac{2a^2}{y}+y^2\ge3a^{4/3}.
\]
The remaining lower bound factors as
\[
3a^{4/3}-2a^2-a
=a(1-a^{1/3})(2a^{2/3}+2a^{1/3}-1)>0,
\]
because \(1/2\le a<1\). Hence **\(F\) is strictly convex separately in every positive eigenvalue coordinate**, for every \(k\ge2\).

**Step 3 (extremal spectrum).** On the compact box \([1,\kappa]^k\), strict coordinate convexity implies any maximizer has every eigenvalue at an endpoint: any strictly interior coordinate could be moved to one endpoint with a strictly larger objective. Thus a maximizer has \(j\) eigenvalues equal to \(\kappa\) and \(k-j\) equal to \(1\), for some integer \(0\le j\le k\). Set \(p=j/k\). Substitution in (1) gives
\[
m=1+p(\kappa-1),\qquad h=1-p+p/\kappa,\qquad \ell=p\log\kappa,
\]
and
\[
F=p(1-p)\frac{(\kappa-1)^2}{\kappa}
-\log(1-p+p/\kappa)-p\log\kappa.
\tag{3}
\]
The two constant spectra \(p=0,1\) have zero divergence. Every mixed endpoint spectrum with \(\kappa>1\) has positive divergence, because two nonsingular centered Gaussian distributions have zero KL divergence only when their covariance matrices agree. Therefore the maximizing integer lies in \(1,\ldots,k-1\). Equation (3), combined with \(F=2D_{\mathrm{KL}}/k\), proves the sharp bound and all equality cases.

**Step 4 (location and asymptotics).** Put \(c=1-\kappa^{-1}\) and \(A=(\kappa-1)^2/\kappa\). The derivative of the bracket in (3) is
\[
G'(p)=A(1-2p)+\frac{c}{1-cp}-\log\kappa,
\quad
G'''(p)=\frac{2c^3}{(1-cp)^3}>0.
\]
Here \(G'\) is strictly convex, \(G'(0)=\kappa-1-\log\kappa>0\), and \(G'(1)=1-\kappa^{-1}-\log\kappa<0\). A strictly convex function with these endpoint signs has a single zero, so \(G\) increases and then decreases, with unique maximizer \(p_*\). The integer maximizer is therefore one of the adjacent feasible lattice points.

For each fixed \(p\in(0,1)\), expansion of (3) gives \(G(p)=\frac12p(1-p)(\kappa-1)^2+O((\kappa-1)^3)\) as \(\kappa\downarrow1\). As \(\kappa\to\infty\), it gives \(G(p)=p(1-p)\kappa+O(\log\kappa)\). The maximum of \(p(1-p)\) over \(p=j/k\), \(1\le j\le k-1\), is \(\eta_k/4\), proving both claimed asymptotics.

## Verification

The included `verify.py` is standalone Python 3 code with no external dependencies. It checks the exact rational positivity of the coordinate curvature \(t^2F_{tt}\) on 2,600 parameter sets, the sharp KL bound and equality-attaining endpoint spectra on 4,180 random spectral configurations, and unimodality/integer localization on 207 dimension–condition-number configurations; all 6,987 tests passed. The analytic inequalities above, not the finite tests, establish the quantified theorem.

For a concrete benchmark, at \(k=4\), \(\kappa=10\), the exact worst case has two eigenvalues at each spectral endpoint and
\[
\frac1k D_{\mathrm{KL}}=0.735772227129\ldots,
\]
compared with the existing sufficient upper bound \(40.5\). At \(k=10\), \(\kappa=3\), the maximizing upper-endpoint multiplicity is \(4\), not \(5\), illustrating a genuinely dimension-dependent spectral optimizer.

## Relationship to prior work

Fifen, Karambal and Hennig (2026), Section 4.4, Theorem 13, use the same trace-matched isotropic inverse covariance and prove an upper KL bound of \(\frac12(\kappa_B-1)^2\) per dimension, for any positive-definite complement operator \(B\). Their theorem and proof do not identify the exact extremal spectrum, the discrete dependence on the complement dimension, or the linear-in-condition-number sharp high-contrast behavior. The present statement sharpens that specific quantitative bound, not the construction of stochastic Lanczos quadrature or its convergence theorem.

The Gaussian KL formula, classical arithmetic–harmonic mean relations and spectral endpoint optimization are established tools. Zhang et al. (2021) study extremal relations between forward and reverse Gaussian KL divergences under KL constraints, rather than the fixed-condition-number, trace-matched isotropic family here. Alyani et al. (2017) analyze KL diagonality measures using a diagonal covariance surrogate, not this scalar trace match. No claim is made to priority for those underlying tools.

## Limitations

This is an exact-arithmetic finite-dimensional extremal theorem, not a bound on stochastic sampling error, quadrature bias, or the complete covariance of any specific Lanczos implementation. It concerns only the trace-matched coefficient and one orientation of Gaussian KL. In a particular structured Krylov complement the realizable spectral family may be smaller, so sharpness over all SPD operators does not assert sharpness under additional constraints. Historical-priority uncertainty remains for general mean-inequality formulations.

## References

1. H. Fifen, I. Karambal, and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1, first posted 2026-09-09. In particular, Section 4.4, Theorem 13. https://arxiv.org/html/2609.10080
2. Y. Zhang, W. Liu, Z. Chen, J. Wang, and K. Li, *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, arXiv:2102.05485, first posted 2021-02-10. https://arxiv.org/abs/2102.05485
3. F. Alyani, M. Congedo, and M. Moakher, *Diagonality measures of Hermitian positive-definite matrices with application to the approximate joint diagonalization problem*, Linear Algebra and its Applications (2017), Section 3.3. https://doi.org/10.1016/j.laa.2016.08.031
