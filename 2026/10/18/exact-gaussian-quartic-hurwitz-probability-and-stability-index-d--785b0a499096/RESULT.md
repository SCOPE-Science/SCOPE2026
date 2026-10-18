# Exact Gaussian quartic Hurwitz probability and stability-index distribution

## Finding

For independent standard normal variables \(A_0,\ldots,A_4\), let \(N_-\) be the number, counted with algebraic multiplicity, of zeros in the open left half-plane of the polynomial
\[
P(z)=A_4z^4+A_3z^3+A_2z^2+A_1z+A_0.
\]
With \(I\) defined by the proper one-dimensional quadrature
\[
I=\int_0^{\pi/2}\arctan\!\left(\frac{\sin^2\theta}{\cos\theta}\right)\,d\theta,
\]
where the endpoint value is the continuous limit, set \(h=1/16-I/(2\pi^2)\). Then
\[
\bigl(\Pr(N_-=0),\ldots,\Pr(N_-=4)\bigr)
=\left(h,\frac14,\frac12-2h,\frac14,h\right).
\]
Numerically, \(h=0.0092838447242981189571499241965554\ldots\). The claim is the exact **elementary one-dimensional integral**, not an assertion of an elementary closed form for its value.

## Assumptions and scope

All five coefficients are independent real \(N(0,1)\) variables. The polynomial has degree four with probability one; its imaginary-axis root event has probability zero. Hence \(N_-\) is almost surely well defined, and the companion-matrix stable-manifold dimension equals \(N_-\). Common positive variance scaling does not change the index distribution. Other coefficient laws or stochastic time-dependent differential equations are not covered.

## Proof

**Hurwitz event.** By the degree-four Routh–Hurwitz criterion, after normalizing the leading coefficient positive, all four roots have negative real part exactly when all five coefficients have one common strict sign and
\[
A_3A_2A_1>A_4A_1^2+A_3^2A_0.
\]
Indeed, the nontrivial Hurwitz determinants for positive coefficients are \(A_3A_2-A_4A_1\) and \(A_3A_2A_1-A_4A_1^2-A_3^2A_0\); positivity of the latter implies the former. Reversing all five signs leaves the roots unchanged, so the probability of stability is \(1/16\) times the probability of the displayed inequality conditional on all magnitudes positive.

**Folded-Cauchy reduction.** Write the positive magnitudes \(B_j=|A_j|\). The ratio \(U=B_1/B_3\) is independent of \(B_0,B_2,B_4\). Since it is the absolute value of the ratio of two independent standard Gaussians, its density is
\[
f_U(u)=\frac{2}{\pi(1+u^2)},\qquad u>0.
\]
The Hurwitz inequality becomes \(B_2>uB_4+u^{-1}B_0\). Given \(U=u\), this is a three-dimensional Gaussian orthant condition.

**Exact orthant angle.** Take independent unconditioned standard Gaussians \(G_4,G_0,G_2\) and put \(V=G_2-uG_4-u^{-1}G_0\). Write \(s=\sqrt{1+u^2+u^{-2}}\). The correlations of \((G_4,G_0,V)\) are \(0,-u/s,-u^{-1}/s\). For a centered nondegenerate Gaussian triple \((X,Y,Z)\) with pairwise correlations \(\rho_{ij}\),
\[
\Pr(X,Y,Z>0)=\frac18+\frac{1}{4\pi}\sum_{i<j}\arcsin\rho_{ij}.
\]
For completeness, expand \(\mathbf 1_{+++}=\prod_{i=1}^3(1+\operatorname{sgn}X_i)/8\). Central symmetry kills odd-sign expectations. For any Gaussian pair, planar rotational symmetry makes the positive-positive sector subtend angle \(\pi/2+\arcsin\rho\); hence \(\mathbb E[\operatorname{sgn}X_i\operatorname{sgn}X_j]=2\arcsin\rho_{ij}/\pi\), proving the displayed formula without an unverified orthant assumption.

Conditioning \(G_4,G_0,G_2\) individually to be positive multiplies this orthant probability by eight. Thus
\[
q(u)=\Pr(B_2>uB_4+u^{-1}B_0)
=1-\frac2\pi\left(\arcsin\frac u s+\arcsin\frac{u^{-1}}s\right).
\]
Under \(u\mapsto u^{-1}\), both the folded-Cauchy probability element \(2\,du/[\pi(1+u^2)]\) and the two arcsines exchange. The first arcsine simplifies to
\[
\arcsin\frac{u}{s}=\arctan\!\left(\frac{u^2}{\sqrt{1+u^2}}\right).
\]
Consequently, the stable probability is exactly
\[
\begin{aligned}
h&=\frac1{16}\int_0^\infty\frac{2q(u)}{\pi(1+u^2)}\,du\\
&=\frac1{16}-\frac1{2\pi^2}\int_0^\infty\frac{\arctan(u^2/\sqrt{1+u^2})}{1+u^2}\,du\\
&=\frac1{16}-\frac1{2\pi^2}\int_0^{\pi/2}\arctan\!\left(\frac{\sin^2\theta}{\cos\theta}\right)\,d\theta,
\end{aligned}
\]
using \(u=\tan\theta\) in the final step.

**The other four indices.** The coefficient law is invariant under alternating coefficient signs, corresponding to \(P(z)\mapsto P(-z)\). Hence \(\Pr(N_-=0)=\Pr(N_-=4)=h\) and \(\Pr(N_-=1)=\Pr(N_-=3)\). Corollary 5.2 and Table 5.1 in Cima–Gasull–Mañosa [1] establish the exact independent linear relation \(\Pr(N_-=1)=1/4\) for this Gaussian fourth-order differential-equation ensemble. Normalization yields \(\Pr(N_-=2)=1/2-2h\). This final distributional relation uses the precisely identified earlier theorem, rather than treating its earlier numerical estimate of \(h\) as exact.

## Verification

Direct 65-digit adaptive quadrature gives \(I=1.05044480063624395127922021885686910772725093849666192467429116\ldots\) and \(h=0.00928384472429811895714992419655543453132463760732168417153218\ldots\). The included standalone Python checker uses the standard library, integrates a second parametrization via composite Simpson quadrature, and checks the normalization and mirror symmetry. The exact formula follows analytically from the preceding proof and not from finite quadrature. Gaussian Monte Carlo with \(1{,}600{,}000\) draws yielded about \(0.009345\), consistent at sampling precision but not an exact proof.

## Relationship to prior work

Cima, Gasull and Mañosa [1] introduced this random stability-index distribution, established the exact relations among index probabilities, and reported the degree-four endpoint probability as approximately \(0.00925\) via Monte Carlo and least squares (their Table 5.1, p. 18). Their discussion of degree-four Routh–Hurwitz inequalities on p. 16 is the exact starting event here. The present additional result replaces the unknown endpoint probability by a one-dimensional elementary quadrature and therefore makes the entire five-point index distribution exact. Gasull [2] discusses the numerical value and related higher-order questions. The present calculation does not resolve the higher-order sequence or its asymptotics.

## Limitations

The one-dimensional integral is not evaluated in elementary constants. High-precision digits are numerical, not independently interval-certified. No assertion is made about non-Gaussian coefficients, dependence, discrete-time stability, or any order beyond four. An older orthant-probability or random-polynomial formulation may contain an equivalent identity under a different name; the cited primary study and targeted comparisons did not reveal it. Independent mathematical scrutiny remains appropriate.

## References

[1] A. Cima, A. Gasull and V. Mañosa, *Stability index of linear random dynamical systems*, Electronic Journal of Qualitative Theory of Differential Equations 2021, no. 15, pp. 1–27, DOI 10.14232/ejqtde.2021.1.15; public preprint arXiv:1904.05725 (first submitted 11 April 2019).

[2] A. Gasull, *Some open problems in low dimensional dynamical systems*, arXiv:2012.02524 (4 December 2020).
