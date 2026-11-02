# Sharp Gaussian noise calibration of a depth-one Anderson projection

## Finding

For the depth-one, Tikhonov-regularized Anderson **projection** constructed from two independent noisy scalar affine residual evaluations at points symmetrically placed about the true root, the unique finite-noise mean-square-optimal squared-residual penalty is
\[
\boxed{\lambda_\star=2\sigma^2.}
\]
This parameter is independent of the nonzero affine residual slope and the distance between the two probe points. In contrast, the unregularized projection has a Pareto-index-one absolute-error tail and a finite absolute-error moment of order \(q>0\) **if and only if** \(q<1\). The exact tail coefficient is calculated below. The conclusion concerns the projection step alone, not the subsequent Anderson mixing step or an arbitrary sequence of iterations.

## Assumptions and scope

Fix \(a>0\), \(\sigma>0\), \(c\in\mathbb R\setminus\{0\}\), and a root \(\theta\in\mathbb R\). Define an affine scalar residual \(r(x)=c(x-\theta)\). Consider two deterministic inputs \(x_-=\theta-a\) and \(x_+=\theta+a\). Observe
\[
R_-=r(x_-)+\varepsilon_-,\qquad R_+=r(x_+)+\varepsilon_+,
\]
with independent \(\varepsilon_-,\varepsilon_+\sim N(0,\sigma^2)\). The root-centering assumption defines a deliberately balanced local benchmark; it is **not** a proposed procedure for selecting these points without knowing the root.

Set \(D=R_+-R_-\) and, for \(\lambda\ge0\), define the depth-one regularized residual projection by
\[
\gamma_\lambda\in\operatorname*{argmin}_{\gamma\in\mathbb R}
\bigl(R_+-D\gamma\bigr)^2+\lambda\gamma^2,
\qquad Z_\lambda=x_+-2a\gamma_\lambda.
\]
For \(\lambda>0\), the minimizer is uniquely \(\gamma_\lambda=DR_+/(D^2+\lambda)\). At \(\lambda=0\), define it as \(R_+/D\) when \(D\ne0\), which holds almost surely. This is the projection update in the standard two-iterate, depth-one Anderson formulation (the full algorithm may additionally apply a residual-mixing update). All expectations are over both Gaussian measurements.

## Proof

**1. Orthogonalize the two noises.** Put \(M=(R_++R_-)/2\). Direct calculation gives
\[
D\sim N(2ca,2\sigma^2),\qquad M\sim N(0,\sigma^2/2),\qquad\operatorname{Cov}(D,M)=0.
\]
Joint Gaussianity implies that \(D\) and \(M\) are independent. Since \(R_+=M+D/2\), the projection error is exactly
\[
Z_\lambda-\theta
=a\frac{\lambda}{D^2+\lambda}-2a\frac{MD}{D^2+\lambda}.
\tag{1}
\]
No approximation is used.

**2. Exact risk and universal optimizer.** For \(\lambda>0\), the independence and centering of \(M\) give
\[
\mathcal R(\lambda)=\mathbb E(Z_\lambda-\theta)^2
=a^2\mathbb E\frac{\lambda^2+2\sigma^2D^2}{(D^2+\lambda)^2}.
\tag{2}
\]
Differentiation under the integral is justified on every compact subinterval of \((0,\infty)\), because the integrands and their derivatives have integrable Gaussian majorants. Algebra then yields
\[
\mathcal R'(\lambda)
=2a^2(\lambda-2\sigma^2)
\mathbb E\frac{D^2}{(D^2+\lambda)^3}.
\tag{3}
\]
The expectation is strictly positive, as \(D\) is a nondegenerate normal variable. Hence \(\mathcal R\) strictly decreases for \(0<\lambda<2\sigma^2\) and strictly increases for \(\lambda>2\sigma^2\). This proves uniqueness of the global minimizer over positive penalties. At the minimizer,
\[
\mathcal R(2\sigma^2)=2a^2\sigma^2\,\mathbb E\frac1{D^2+2\sigma^2}<a^2.
\tag{4}
\]
The inequality is strict because \(D\ne0\) almost surely. For every fixed positive penalty, all positive-order moments of \(Z_\lambda-\theta\) are finite, by (1) and the bounds \(0\le\lambda/(D^2+\lambda)\le1\) and \(|D|/(D^2+\lambda)\le1/(2\sqrt\lambda)\).

**3. Sharp unregularized moment and tail law.** At \(\lambda=0\), (1) becomes \(Z_0-\theta=-2aM/D\) almost surely. Since the normal density of \(D\) is strictly positive at zero, \(\mathbb E|D|^{-q}<\infty\) exactly for \(0<q<1\). Independence from the nondegenerate Gaussian \(M\) gives the claimed necessary-and-sufficient moment condition. Let \(f_D\) denote the density of \(D\). Conditioning on \(M\), the continuity of \(f_D\), and dominated convergence (using its boundedness and \(\mathbb E|M|<\infty\)) yield
\[
\lim_{t\to\infty}t\,\mathbb P(|Z_0-\theta|>t)
=4a f_D(0)\,\mathbb E|M|
=\boxed{\frac{2a}{\pi}\exp\!\left(-\frac{c^2a^2}{\sigma^2}\right)}.
\tag{5}
\]
In particular, the unregularized projection has infinite expected absolute error and infinite mean-square error for every \(\sigma>0\), however small.

## Verification

The companion `verify.py` reproduces (1)–(5) using exact rational checks of the pointwise risk and derivative identities and deterministic Gaussian quadrature at multiple nonzero slopes, lengths, and noise levels. Run `python verify.py` with Python 3.10 or later. The general theorem is proved by the preceding algebra and integrability arguments; no finite grid or numerical quadrature is offered as an infinite-dimensional or probabilistic proof.

## Relationship to prior work

Wei, Bao and Liu (2021) formulate the Anderson projection and mixing steps separately and explicitly introduce regularization of the least-squares coefficient; their equations (4a), (5), (10)–(13) supply the method being specialized here. Their general convergence and adaptive-regularization guarantees do not state the exact Gaussian finite-noise optimizer in (3), nor the sharp tail coefficient (5). Pollock and Rebholz (2022) address condition control by filtering residual differences; Lupo Pasini and Laiu (2022) study approximate calculations with error controls. These are related stabilization ideas rather than an asserted absence of all earlier special-case calculations. An exact statistical equivalent under alternative ratio-of-normal or noisy-secant terminology may exist; priority is not independently verified. The pole in a ratio of normal variables is a classical probability mechanism and is not presented as a new general distributional phenomenon.

## Limitations

This is a **single** depth-one projection, not the complete Anderson/SAM iterate with an additional mixing term. The exact optimal parameter requires independent, equally noisy Gaussian measurements and deterministic probe points at equal distance from the root; neither correlated oracle errors nor generic off-center probes are covered. The fact that the ideal midpoint equals the root in this benchmark makes it a calibration test of the numerical projection, **not** evidence that the projection is optimal over all estimators or that the centered probes can be selected without prior information. The result is about error moments of an algorithmic map, not convergence of an iterated stochastic process. Equations (1)–(5) are exact in real arithmetic. No claims are made for non-Gaussian noise, floating point, larger memory, or multi-step convergence.

## References

1. F. Wei, C. Bao and Y. Liu, *Stochastic Anderson Mixing for Nonconvex Stochastic Optimization*, arXiv:2110.01543v1, first posted 2021-10-04, especially Section 2.1–2.2 and equations (4a), (5), (10)–(13). https://arxiv.org/abs/2110.01543
2. S. Pollock and L. G. Rebholz, *Filtering for Anderson Acceleration*, arXiv:2211.12953, first posted 2022-11-23. https://arxiv.org/abs/2211.12953
3. M. Lupo Pasini and M. P. Laiu, *Anderson acceleration with approximate calculations: applications to scientific computing*, arXiv:2206.03915, first posted 2022-06-08; subsequently *Numerical Linear Algebra with Applications* 31 (2024), e2562. https://arxiv.org/abs/2206.03915
