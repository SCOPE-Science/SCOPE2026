# Sharp Gaussian moment threshold for noisy Anderson extrapolation at any memory depth

## Finding

For an unregularized Anderson extrapolation computed from fresh independent Gaussian-noisy evaluations at fixed, affinely independent points in \(\mathbb R^d\), with memory \(1\le m\le d\), the extrapolated point has a finite absolute \(p\)-th moment **if and only if**

\[
\boxed{\mathbb E\|Z\|_2^p<\infty\quad\Longleftrightarrow\quad 0<p<d-m+1.}
\]

The same threshold holds for the least-squares mixing coefficient vector. It does not depend on the noise magnitude, provided that magnitude is positive, nor on the deterministic fixed-point mapping. In particular, unregularized full memory \(m=d\) has no finite first moment; memory \(m=d-1\) has a finite first moment but infinite second moment; and the second moment is finite exactly when \(m\le d-2\). Fixed nonzero outer relaxation does not repair the diverging moments, whereas any fixed positive Tikhonov parameter makes all polynomial moments finite.

An exact conditional identity is

\[
\mathbb E[\|\alpha\|_2^2\mid R]
=\left\|\frac{\mathbf 1}{m+1}-R^+a\right\|_2^2
+\frac{\sigma^2}{m+1}\operatorname{tr}\big((R^{\mathsf T}R)^{-1}\big),
\]

where the residual-mean vector \(a\), the Gaussian difference matrix \(R\), and the Anderson coefficients \(\alpha\) are defined below. At \(m\ge d-1\), the trace term is nonintegrable even for an arbitrarily small nonzero noise variance.

## Assumptions and scope

Fix integers \(d\ge1\) and \(1\le m\le d\); deterministic points \(x_0,\ldots,x_m\in\mathbb R^d\) for which the \(d\times m\) displacement matrix

\[
H=[x_1-x_0,\ldots,x_m-x_0]
\]

has full column rank; and any deterministic mapping \(q:\mathbb R^d\to\mathbb R^d\) with finite values at these points. The mapping may, in particular, be a strict affine contraction. Let \(\sigma>0\) and take independent \(\varepsilon_i\sim N(0,\sigma^2 I_d)\) for \(i=0,\ldots,m\). These are **fresh evaluations of fixed points**, not a claim about adaptively chosen iterates.

Set \(y_i=q(x_i)+\varepsilon_i\) and \(r_i=y_i-x_i\), and let

\[
R=[r_1-r_0,\ldots,r_m-r_0],\qquad
\alpha=\underset{v\in\mathbb R^m}{\operatorname{argmin}}\,\|r_0+Rv\|_2^2.
\]

The full-column-rank Gaussian matrix \(R\) is nonsingular in the least-squares sense almost surely, so \(\alpha=-R^+r_0\), with \(R^+=(R^{\mathsf T}R)^{-1}R^{\mathsf T}\). Define the type-II Anderson output

\[
Z=y_0+\sum_{j=1}^{m}\alpha_j(y_j-y_0)=y_0+(H+R)\alpha.
\]

A fixed relaxed output is \(Z_\theta=(1-\theta)B_0+\theta Z\), for any fixed \(\theta\ne0\) and a baseline \(B_0\) whose moments of all positive orders are finite (e.g. \(x_m\) or \(y_m\)). For \(\lambda>0\), the Tikhonov variant replaces \(\alpha\) by

\[
\alpha_\lambda=-(R^{\mathsf T}R+\lambda I_m)^{-1}R^{\mathsf T}r_0,
\]

and defines \(Z_\lambda=y_0+(H+R)\alpha_\lambda\). The claims concern exact arithmetic and the stated noise law.

## Proof

**1. Independent Gaussian residual average.** Write \(\bar r_i=q(x_i)-x_i\) and \(a=(m+1)^{-1}\sum_{i=0}^m\bar r_i\). The noise average \(\xi=(m+1)^{-1}\sum_{i=0}^m\varepsilon_i\) is independent of every difference \(\varepsilon_j-\varepsilon_0\), by joint Gaussianity and zero cross-covariance, and satisfies \(\xi\sim N(0,\sigma^2 I_d/(m+1))\). Consequently,

\[
r_0=a-\frac{R\mathbf1}{m+1}+\xi,
\qquad
\alpha=\frac{\mathbf1}{m+1}-R^+(a+\xi).
\]

The difference matrix \(R\) has a strictly positive Gaussian density on all of \(\mathbb R^{d\times m}\): its column-noise covariance is \(\sigma^2(I_m+\mathbf1\mathbf1^{\mathsf T})\), which is positive definite. In particular, \(R\) has full column rank almost surely. Conditioning on \(R\) gives the displayed exact squared-norm identity, since

\[
\operatorname{Cov}(R^+\xi\mid R)=\frac{\sigma^2}{m+1}(R^{\mathsf T}R)^{-1}.
\]

**2. Sharp inverse moment of an orthogonal column remainder.** Fix \(j\in\{1,\ldots,m\}\), and project the \(j\)-th column \(R_j\) orthogonally off the span of all the other columns. Denote the nonzero remainder by \(u_j\). It belongs to a subspace of dimension \(t=d-m+1\) almost surely. Least-squares orthogonality yields, for any \(v\in\mathbb R^d\),

\[
(R^+v)_j=\frac{\langle u_j,v\rangle}{\|u_j\|_2^2},\qquad
\alpha_j=\frac1{m+1}-\frac{\langle u_j,a+\xi\rangle}{\|u_j\|_2^2}.
\]

To determine the distribution of \(u_j\), condition on the other \(m-1\) columns. With \(\delta_j=\bar r_j-\bar r_0\), Gaussian regression for the differences gives

\[
\operatorname{Cov}(R_j\mid R_{-j})
=\sigma^2\frac{m+1}{m}I_d,
\]

and conditional mean \(\delta_j+m^{-1}\sum_{k\ne j}(R_k-\delta_k)\). After projecting perpendicular to the span of \(R_{-j}\), the random sum of other columns vanishes. Thus \(u_j\), conditional on \(R_{-j}\), is a nondegenerate isotropic Gaussian vector in a \(t\)-dimensional subspace with variance \(\sigma^2(m+1)/m\) and mean equal to the projection of the fixed vector \(\delta_j-m^{-1}\sum_{k\ne j}\delta_k\). The latter has a uniformly bounded norm. For \(m=1\), interpret the empty sum and projection in the obvious way.

Every such Gaussian density is strictly positive at the origin, and its density is uniformly bounded above there. Polar integration in its \(t\)-dimensional subspace therefore establishes

\[
\mathbb E\|u_j\|_2^{-p}<\infty\quad\Longleftrightarrow\quad 0<p<t.
\]

For the finite direction, use the density upper bound inside the unit ball and the bound \(\|u_j\|^{-p}\le1\) outside it. For divergence, fix almost any \(R_{-j}\), use its strictly positive Gaussian density on a small ball, and integrate \(r^{t-1-p}\) down to zero. These are full-domain integrals, not finite enumerations.

**3. Coefficient and output moments.** Conditional on \(R\), each \(\alpha_j\) is normal with variance \(\sigma^2/((m+1)\|u_j\|_2^2)\). For every \(p>0\), a shifted centered normal has absolute \(p\)-th moment at least the unshifted normal's (by symmetry and unimodality). Hence, with a strictly positive constant depending only on \(p\),

\[
\mathbb E[|\alpha_j|^p\mid R]
\ge c_p\,\frac{\sigma^p}{(m+1)^{p/2}\|u_j\|_2^p}.
\]

This proves divergence for every \(p\ge t\). Conversely, \(\xi\) is independent of \(R\), and

\[
|\alpha_j|\le\frac1{m+1}+
\frac{\|a\|_2+\|\xi\|_2}{\|u_j\|_2}.
\]

All moments of \(\xi\) are finite, so the inverse-moment criterion in step 2 establishes finite \(p\)-th moments for every coordinate when \(p<t\), and hence for the finite-dimensional vector \(\alpha\).

Since \(R\alpha=-\operatorname{Proj}_{\operatorname{col}(R)}r_0\), write

\[
Z=H\alpha+B,
\quad B=y_0-\operatorname{Proj}_{\operatorname{col}(R)}r_0.
\]

The bound \(\|B\|_2\le\|y_0\|_2+\|r_0\|_2\) gives all finite moments of \(B\). Since \(H\) has positive smallest singular value, both \(\|H\alpha\|_2\) and \(\|\alpha\|_2\) bound each other up to deterministic positive constants. Triangle inequalities for \(p\ge1\), and subadditivity for \(0<p<1\), therefore transfer the moment threshold unchanged to \(Z\). The same argument applies to nonzero fixed relaxation against any all-moment baseline.

**4. Tikhonov repair.** Singular-value calculus gives

\[
\|(R^{\mathsf T}R+\lambda I_m)^{-1}R^{\mathsf T}\|_2
\le\max_{s\ge0}\frac{s}{s^2+\lambda}
=\frac1{2\sqrt\lambda}.
\]

Thus \(\|\alpha_\lambda\|_2\le\|r_0\|_2/(2\sqrt\lambda)\). Both \(r_0\) and \(H+R\) have Gaussian polynomial moments of every order, so Hölder's inequality gives all positive moments of \(Z_\lambda\). This completes the proof.

## Verification

The included standalone `verify.py` (run with `python verify.py`) checks the exact Gaussian covariance inverses for memory sizes one through eight, the independent-average coefficient decomposition, every projected-column formula, the output decomposition, and the Tikhonov singular-value bound on 2,250 reproducible Gaussian instances covering nine dimension-memory pairs. It also checks positive inverse chi-radius expressions below their critical dimension. It returned **PASS: 12310 deterministic exact and matrix identities**. These checks corroborate the algebra; the Gaussian conditional-density proof above, not sampling, proves the infinite-moment statements.

## Relationship to prior work

The basic Anderson coefficient and residual least-squares formulas are standard; see De Sterck and He, arXiv:2109.14176, equations (1.4)–(1.10). Lupo Pasini and coauthors, arXiv:2110.14813, explicitly motivate smoothing by stochastic oscillations in Anderson-accelerated iterative optimization and define least-squares mixing, relaxation, and an additive-noise model. Shi and coauthors, arXiv:1909.03245, analyze regularization for perturbed Anderson mixing. Pollock and Rebholz, arXiv:2211.12953, develop deterministic condition-number filtering. Classical Gaussian smallest-singular-value and inverse-Wishart results describe the matrix-level small-ball mechanism.

The present statement is narrower in oracle model but sharper in a different direction: it proves the exact **output moment-existence boundary** for correlated residual-difference columns with a shared evaluation noise, relates that boundary to the affine span of the inputs, and distinguishes ordinary fixed outer relaxation from positive Tikhonov regularization. It does not claim novelty for Anderson's update formula, Gaussian density integration, Wishart moment facts, or the general idea of regularization.

## Limitations

This is a one-shot, exact-arithmetic result for fresh independent isotropic Gaussian oracle evaluations at deterministic, affinely independent points. It does not directly describe adaptively generated Anderson trajectories, correlated sampling, discrete or bounded oracle noise, non-Gaussian densities, rank-deficient input displacements, floating-point safeguards, or infinite-horizon convergence. The result's critical behavior is driven by very rare near-rank-deficiencies, which may be invisible in ordinary Monte Carlo runs. Near-square residual windows, rather than typical high-dimensional small-memory settings, are the principal relevant regime. A corresponding formulation may exist within broader Gaussian regression or random-matrix literature; publication priority requires independent verification.

## References

1. Massimiliano Lupo Pasini, Junqi Yin, Viktor Reshniak, Miroslav Stoyanov, *Stable Anderson Acceleration for Deep Learning*, first arXiv version 2021-10-26, arXiv:2110.14813. https://arxiv.org/abs/2110.14813
2. Hans De Sterck and Yunhui He, *Linear Asymptotic Convergence of Anderson Acceleration: Fixed-Point Analysis*, arXiv first version 2021-09-29, arXiv:2109.14176. https://arxiv.org/abs/2109.14176
3. Wenjie Shi, Shiji Song, Hui Wu, Ya-Chu Hsu, Cheng Wu, Gao Huang, *Regularized Anderson Acceleration for Off-Policy Deep Reinforcement Learning*, arXiv 2019-09-07, arXiv:1909.03245. https://arxiv.org/abs/1909.03245
4. Sara Pollock and Leo G. Rebholz, *Filtering for Anderson Acceleration*, arXiv 2022-11-23, arXiv:2211.12953. https://arxiv.org/abs/2211.12953
5. Damien Scieur, Alexandre d'Aspremont, Francis Bach, *Regularized Nonlinear Acceleration*, arXiv 2016-06-13, arXiv:1606.04133. https://arxiv.org/abs/1606.04133
6. Mark Rudelson and Roman Vershynin, *The Smallest Singular Value of a Random Rectangular Matrix*, arXiv 2008-02-27, arXiv:0802.3956. https://arxiv.org/abs/0802.3956
