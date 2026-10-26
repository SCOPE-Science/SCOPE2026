# Sharp norm transition for intrinsic Laplace covariance on products of circles

## Finding

For each integer \(d\ge2\), fixed \(a>0\), and finite \(1\le p<\infty\), the intrinsic-distance Laplace kernel on the product of \(d\) circles,
\[
K_{a,p}(x,y)=\exp[-aD_p(x,y)],\qquad
D_p(x,y)=\left(\sum_{j=1}^{d}\delta(x_j-y_j)^p\right)^{1/p},
\]
where \(\delta(t)=\min_{k\in\mathbb Z}|t-2\pi k|\), is positive semidefinite on **every** finite set if and only if \(p=1\). At \(p=1\) it is strictly positive definite on pairwise distinct sites. For each finite \(p>1\), every \(a>0\), and sufficiently large integer \(m\), the Fourier coefficient of its restriction to any coordinate two-torus at frequency \((2m,0)\) is strictly negative. Thus every such kernel fails positive semidefiniteness on some finite configuration.

The stronger boundary-sign principle is as follows. Let \(1<p<\infty\) and let \(\phi\in C^2([0,2^{1/p}\pi])\) satisfy \(\phi'(r)<0\) for all \(\pi\le r\le2^{1/p}\pi\). Put \(f_p(x,y)=\phi((\delta(x)^p+\delta(y)^p)^{1/p})\) on \(\mathbb T^2\). Its normalized Fourier coefficients, \(\widehat f_p(n,0)=(2\pi)^{-2}\int_{[-\pi,\pi]^2}f_p(x,y)e^{-inx}\,dx\,dy\), obey
\[
\lim_{n\to\infty}n^2\widehat f_p(n,0)
\quad\text{along even }n
=\frac{1}{\pi^2}\int_0^\pi\phi'\bigl((\pi^p+s^p)^{1/p}\bigr)
\frac{\pi^{p-1}}{(\pi^p+s^p)^{(p-1)/p}}\,ds<0.
\]
Along odd positive integers the limit is the negative of this constant. For \(\phi(r)=e^{-ar}\), the even limit becomes
\[
-\frac{a\pi^{p-1}}{\pi^2}\int_0^\pi
\frac{e^{-a(\pi^p+s^p)^{1/p}}}{(\pi^p+s^p)^{(p-1)/p}}\,ds<0.
\]
The parameter boundary \(p=1\) is sharp despite the uniform convergence of the norms as \(p\downarrow1\).

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). The product metric \(D_p\) is the quotient length distance of the coordinate \(\ell_p\) norm for finite \(p\ge1\). Positive semidefinite means every complex Hermitian Gram form is nonnegative. Strict positive definiteness refers to pairwise distinct sites and nonzero coefficients. The boundary-sign principle requires only the stated smoothness and strict decrease of \(\phi\) at radii reached by the antipodal face; no monotonicity is assumed elsewhere. All Fourier coefficients use normalized Haar measure.

## Proof

**Sufficiency and strictness at the additive endpoint.** For \(p=1\), the kernel factorizes:
\[
K_{a,1}(x,y)=\prod_{j=1}^{d} e^{-a\delta(x_j-y_j)}.
\]
A direct integral yields, for every \(n\in\mathbb Z\),
\[
\widehat{e^{-a\delta}}(n)=\frac{a\bigl(1-(-1)^ne^{-a\pi}\bigr)}{\pi(a^2+n^2)}>0.
\]
Consequently every Fourier coefficient on \(\mathbb T^d\) is strictly positive. If a finite Gram form vanishes, then the Fourier transform of its finitely supported signed atomic measure vanishes at every integer lattice frequency. Uniqueness of Fourier coefficients of finite measures forces that measure and all its weights to vanish. This proves strict positivity for pairwise distinct sites.

**A regularized axial marginal.** Fix finite \(p>1\) and \(\phi\) as in the finding, and write
\[
R(t,s)=(t^p+s^p)^{1/p},\qquad
F(t)=\frac1\pi\int_0^\pi\phi(R(t,s))\,ds,
\quad 0\le t\le\pi.
\]
For positive \(t,s\), differentiation gives
\[
0\le R_t=t^{p-1}R^{1-p}\le1,
\qquad R_{tt}=(p-1)t^{p-2}s^pR^{1-2p}\ge0.
\]
For almost every \(s\in(0,\pi]\), \(R_t(0,s)=0\) and \(\int_0^\pi R_{tt}(t,s)\,dt=R_t(\pi,s)\le1\). By dominated convergence, \(F\) is continuously differentiable on its closed interval and \(F'(0)=0\). Its second derivative exists almost everywhere and is integrable: differentiation under the integral away from the origin, Tonelli's theorem, and the preceding inequalities show
\[
\int_0^\pi|F''(t)|\,dt\le
\pi\|\phi''\|_\infty+\|\phi'\|_\infty.
\]
Equivalently \(F'\) is absolutely continuous, which justifies both integrations by parts below. Its antipodal derivative is
\[
F'(\pi)=\frac{1}{\pi}\int_0^\pi\phi'(R(\pi,s))
\frac{\pi^{p-1}}{R(\pi,s)^{p-1}}\,ds<0.
\]
The strict inequality follows from the assumed derivative signs, including the full positive-measure range of antipodal radii.

**Fourier asymptotics and impossibility.** Evenness and the definition of \(F\) give
\[
\widehat f_p(n,0)=\frac1\pi\int_0^\pi F(t)\cos(nt)\,dt.
\]
Twice integrating by parts for any positive integer \(n\) gives the exact identity
\[
n^2\widehat f_p(n,0)=\frac{(-1)^nF'(\pi)-F'(0)}{\pi}
-\frac1\pi\int_0^\pi F''(t)\cos(nt)\,dt.
\]
The final integral tends to zero by the Riemann–Lebesgue lemma because \(F''\in L^1\). Together with \(F'(0)=0\) and \(F'(\pi)<0\), this gives the stated negative even-frequency and positive odd-frequency limits. Applying \(\phi(r)=e^{-ar}\) proves a negative Fourier coefficient for each fixed \(a>0\), finite \(p>1\), on the two-torus. A continuous translation-invariant positive-semidefinite kernel on a compact abelian group has nonnegative Fourier coefficients; conversely its Fourier energy on a character is that coefficient. A negative coefficient therefore contradicts positive semidefiniteness. If only finite matrices are considered, approximate the signed character-weighted Haar measure by atomic grid measures; continuity preserves a negative quadratic form for a sufficiently fine grid. Restricting any higher-dimensional product to two varying coordinate circles proves the conclusion for every \(d\ge2\).

## Verification

The accompanying Python checker numerically evaluates Fourier coefficients using normalized two-dimensional FFTs, independently integrates the analytic antipodal constant, compares the separable \(p=1\) Fourier coefficients with their exact formula, and constructs a finite-grid negative spectral witness for \(p=2\). Run `python verify_torus.py` with NumPy and SciPy installed. The checker is a consistency test; the theorem for all dimensions, all damping parameters, and every finite exponent uses the preceding analytic argument, not finite computation. For \(a=1\), \(p=2\), the even-axial asymptotic constant is approximately \(-0.00849361549034\). The normalized \((24,0)\) coefficient on a \(128\)-by-\(128\) grid is approximately \(-4.35569586777\times10^{-6}\).

## Relationship to prior work

Feragen–Lauze–Hauberg establish the relationship between conditional negative definiteness of a distance and positive definiteness of its Laplace kernel at **all** damping scales, but do not give an all-exponent classification on Finsler product circles. Guella–Menegatto–Peron provide the general Schoenberg/Fourier characterization on products of circles and a strictly positive-definite support criterion; their results apply directly to the additive endpoint but do not determine the sign for nonadditive \(\ell_p\) metrics. Zhou proves high-frequency cut-locus obstructions for radial functions of the **Euclidean** quotient metric on flat tori; the \(p=2\) obstruction here is consequently not claimed as new. The extension to every finite non-Euclidean exponent \(p>1\), its exact normalized even-axial coefficient, and the sharp separability transition are the distinct statements compared. No claim is made that the underlying Fourier or cut-locus techniques are newly invented.

## Limitations

The result concerns products with at least two circle factors and finite \(p\); it does not classify arbitrary nonproduct torus norms, variable damping, or frequency-independent finite-grid cutoffs. For \(p\) near one, the first negative even mode can be very large, and fixed-resolution sampling is not conclusive. The literature comparison is bounded rather than an exhaustive novelty certificate. Independent mathematical validation has not been performed.

## References

1. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296v1 (first public 2014-11-02), https://arxiv.org/abs/1411.0296.
2. J. C. Guella, V. A. Menegatto, and A. P. Peron, *An extension of a theorem of Schoenberg to products of spheres*, arXiv:1503.08174v1 (2015-03-27), https://arxiv.org/abs/1503.08174.
3. J. C. Guella, V. A. Menegatto, and A. P. Peron, *Strictly positive definite kernels on a product of circles*, arXiv:1505.01169v1 (2015-05-05), https://arxiv.org/abs/1505.01169.
4. Y. Zhou, *Distance Energies and Negative Type of Flat Tori*, arXiv:2609.05622v1 (2026-09-04), https://arxiv.org/abs/2609.05622.
