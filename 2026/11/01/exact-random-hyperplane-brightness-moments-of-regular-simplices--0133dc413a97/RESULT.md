# Exact random hyperplane brightness moments of regular simplices and the finite-size Gaussian correction

## Finding
Let \(m\ge3\), \(n=m-1\), and let \(\Delta_n=\operatorname{conv}\{e_1,\ldots,e_m\}\) be the regular simplex of edge length \(\sqrt2\) in the affine hyperplane \(\mathcal H=\{x\in\mathbb R^m:\sum_i x_i=1\}\). Take \(U\) uniformly from the Euclidean unit sphere of \(\mathcal H_0=\{u\in\mathbb R^m:\sum_i u_i=0\}\). Let \(P_m\) be the \((n-1)\)-dimensional Euclidean volume of the orthogonal projection of \(\Delta_n\) along \(U\), and normalize
\[
S_m=\frac{2(n-1)!}{\sqrt m}P_m=\sum_{i=1}^m|U_i|.
\]
The normalization uses the published projection identity, not a new derivation of that identity.

The complete first-two-moment profile is
\[
\mathbb E S_m=\frac{\sqrt{m(m-1)}\,\Gamma((m-1)/2)}{\sqrt\pi\,\Gamma(m/2)},
\]
\[
\mathbb E S_m^2
=1+\frac{2(m-1)}{\pi}\left(
\sqrt{1-\frac{1}{(m-1)^2}}+\frac{\arcsin(1/(m-1))}{m-1}\right).
\]
Consequently \(\operatorname{Var}(S_m)=\mathbb E S_m^2-(\mathbb E S_m)^2\) is an explicit finite-dimensional invariant. As \(m\to\infty\),
\[
\operatorname{Var}(S_m)=1-\frac3\pi-\frac{1}{4\pi m}+O(m^{-2}),
\qquad
S_m-\sqrt{\frac{2m}{\pi}}\ \Longrightarrow\ N\!\left(0,1-\frac3\pi\right).
\]
In particular the dispersion remains nonzero on the unscaled \(\ell_1\)-normalization, and its first finite-size correction is negative with exact coefficient \(1/(4\pi)\).

## Assumptions and scope
These statements hold for every integer \(m\ge3\) under Haar-uniform orientation in \(\mathcal H_0\). The sample-volume normalization corresponds specifically to the simplex with vertices the standard basis vectors; changing the edge length scales \(P_m\) but leaves \(S_m\) unchanged. Gamma is Euler's gamma function. The asymptotic normal law concerns growing ambient dimension; it is not a finite-dimensional Gaussian distribution.

## Proof
**Projection reduction.** Pandis' exact hyperplane-projection identity states \(P_m=\sqrt m\sum|U_i|/[2(n-1)!]\). It is used as a starting point. Let \(G_i\) be independent standard normal random variables, let \(\overline G=m^{-1}\sum_iG_i\), and write \(Y_i=G_i-\overline G\). By rotational invariance in \(\mathcal H_0\),
\[
(U_1,\ldots,U_m)\ \overset d=\ (Y_1,\ldots,Y_m)/(\sum_iY_i^2)^{1/2}.
\]
The denominator is independent of the uniform spherical direction, and \(\mathbb E\sum_iY_i^2=m-1\). For \(i\ne j\),
\[
\mathbb E Y_i^2=(m-1)/m,\qquad
\operatorname{Corr}(Y_i,Y_j)=-1/(m-1).
\]

**First moment.** An individual coordinate of \(U\) has the law of \(\sqrt{(m-1)/m}\) times the first coordinate of a uniform point on the sphere in \(\mathbb R^{m-1}\). The sphere-beta integral gives \(\mathbb E|W_1|=\Gamma((m-1)/2)/(\sqrt\pi\Gamma(m/2))\), yielding the claimed mean upon multiplying by \(m\).

**Second moment.** For a standard centered bivariate Gaussian with unit marginals and correlation \(r\), direct Gaussian covariance differentiation shows
\[
\frac{d}{dr}\mathbb E(|Z_1||Z_2|)=\mathbb E[\operatorname{sgn}(Z_1)\operatorname{sgn}(Z_2)]
=\frac2\pi\arcsin r.
\]
At \(r=0\), the expectation is \(2/\pi\); integration gives the identity
\[
\mathbb E(|Z_1||Z_2|)=\frac2\pi\big(\sqrt{1-r^2}+r\arcsin r\big).
\]
Using spherical radial independence and \(\mathbb E\sum Y_i^2=m-1\) thus yields
\[
\mathbb E|U_iU_j|=\frac{2}{\pi m}
\left(\sqrt{1-\frac1{(m-1)^2}}+\frac{\arcsin(1/(m-1))}{m-1}\right).
\]
Expanding \(S_m^2=\sum_iU_i^2+2\sum_{i<j}|U_iU_j|\), with \(\sum_iU_i^2=1\), proves the displayed second-moment formula for all \(m\ge3\).

**Asymptotic variance.** Standard Stirling expansions of the gamma ratio and Taylor series at zero of the square-root/arcsine terms give, respectively,
\[
(\mathbb ES_m)^2=\frac{2m}{\pi}+\frac1\pi+\frac{5}{4\pi m}+O(m^{-2}),
\]
\[
\mathbb ES_m^2=\frac{2m}{\pi}+1-\frac2\pi+\frac{1}{\pi m}+O(m^{-2}).
\]
Subtracting proves the finite-size correction.

**Gaussian limit.** Define \(T_m=\sum_i|G_i|/(\sum_iG_i^2)^{1/2}\). Since \(\overline G=O_{\mathbb P}(m^{-1/2})\), the deterministic inequality
\[
\big||x-t|-|x|+t\operatorname{sgn}(x)\big|\le 2|t|\mathbf1_{\{|x|\le|t|\}}
\]
combined with \(\sum_i\operatorname{sgn}(G_i)=O_{\mathbb P}(\sqrt m)\) and the Gaussian density bound yields \(\sum_i|G_i-\overline G|-\sum_i|G_i|=O_{\mathbb P}(1)\). Indeed, on \(|\overline G|\le C/\sqrt m\), the number of \(i\) with \(|G_i|\le|\overline G|\) is dominated by the number with \(|G_i|\le C/\sqrt m\), which is \(O_{\mathbb P}(\sqrt m)\). Also \(\sum_i(G_i-\overline G)^2=\sum_iG_i^2-m\overline G^2\), so the denominators differ by \(O_{\mathbb P}(m^{-1/2})\) and are both of order \(\sqrt m\). It follows that \(S_m-T_m=O_{\mathbb P}(m^{-1/2})\). The established central limit theorem of Kabluchko–Litvak–Zaporozhets for random line-width of the unit cube is precisely \(T_m-\sqrt{2m/\pi}\Longrightarrow N(0,1-3/\pi)\). Slutsky's theorem concludes the limit. The cube limit is credited as a prior theorem; the centering transfer is the new reduction here.

## Verification
A standalone, standard-library-only Python program accompanies this result. It checks the finite formulas against Cauchy's projection means for a triangle and tetrahedron, against direct angular integration in the two-dimensional zero-sum plane, and against reproducible Gaussian simulations for two further dimensions. It additionally checks the exact algebraic low-dimensional identity and the leading variance correction numerically. All 210 programmed checks passed on the supplied package. Numerical checks are diagnostics; the preceding analytic derivations establish the all-dimensional and asymptotic claims.

## Relationship to prior work
Pandis (2026) gives the all-direction projection identity and extremizers, and Jakimiuk–Pandis (2026) obtains stability bounds for those extremizers; neither supplies the exact Haar first/second moment profile. Kabluchko–Litvak–Zaporozhets (2016 version) derives moments and limiting laws for **one-dimensional** random widths of regular polytopes, including the cube limit used above. That cube limit implies the present *limiting normal distribution* after the explicitly proved centering transfer, but does not give the displayed finite-dimensional moments or their \(m^{-1}\) variance correction. Affentranger–Schneider (1992) concerns expected face numbers of random simplex projections, not the geometric volume moments proved here. Thus the strongest new component is the exact finite-dimensional brightness-variance law with its correction, rather than the already-established cube CLT.

## Limitations
No claim is made about higher moments, nonuniform orientation distributions, or a central limit theorem for arbitrary convex bodies. The formula and rate are specific to regular simplices under Haar orientation and the normalization displayed above. Older unindexed literature, including results on spherical \(\ell_1\) norms in the zero-sum hyperplane, remains a priority risk. The published projection identity and cube-width limit are treated as known inputs.

## References
1. C. Pandis, *On Extremal Volume Projections of the Simplex and the Cube*, arXiv:2601.18436 (first posted 26 January 2026), Theorem 1.2. https://arxiv.org/abs/2601.18436
2. J. Jakimiuk and C. Pandis, *Stability of Hyperplane Projections of the Regular Simplex and \(L_p\)-Projection Bodies of balls in \(\ell_q^n(\mathbb R)\)*, arXiv:2610.23489 (first posted 16 October 2026), equation (1.2) and Theorem 1.1. https://arxiv.org/abs/2610.23489
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, version 3 (6 April 2016), Theorem 3.6, Section 6. https://arxiv.org/html/1511.08479v3
4. F. Affentranger and R. Schneider, *Random Projections of Regular Simplices*, Discrete & Computational Geometry 7 (1992), 219–226, doi:10.1007/BF02187839 (abstract and bibliographic description consulted).
