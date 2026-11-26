# Spectral identifiability of near-isotropic random zonogon deficits

## Finding

Let \(K\ge1\) be fixed, and let \(g\) be a real, mean-zero trigonometric polynomial on the unoriented direction circle \([0,\pi)\),
\[
g(\theta)=\sum_{m=1}^K(\eta_m e^{-2im\theta}+\overline{\eta_m}e^{2im\theta}),\qquad \eta_m\in\mathbb C,
\]
where \(\eta_m=0\) for \(m>K\). For \(n\ge2\) sample \(\theta_1,\ldots,\theta_n\) independently with density \((1+\varepsilon_n g)/\pi\), with \(\varepsilon_n\ge0\), \(\varepsilon_n\to0\), and a nonnegative density. Let \(u_j=(\cos\theta_j,\sin\theta_j)\) and \(Z_n=\sum_{j=1}^n[-u_j/2,u_j/2]\) have area \(A_n\) and perimeter \(2n\). Set
\[
D_n=\frac{n^2/\pi-A_n}{n},\qquad c_m=\frac{2}{\pi(4m^2-1)},\qquad Q(g)=\sum_{m=1}^Kc_m|\eta_m|^2.
\]

**Exact finite-row law of the statistic in Fourier coordinates.** For every realization, the following nonnegative series converges absolutely:
\[
D_n=\sum_{m\ge1}c_m\left|n^{-1/2}\sum_{j=1}^ne^{2im\theta_j}\right|^2,
\qquad \mathbb E D_n=\frac1\pi+(n-1)\varepsilon_n^2 Q(g).
\]

**Critical window.** Suppose \(n\varepsilon_n^2\to\lambda\in[0,\infty)\). Then \(D_n\) converges in law, with convergence of its first two moments, to
\[
Y_{\lambda,g}=\sum_{m\ge1}c_m|G_m+\sqrt{\lambda}\,\eta_m|^2,
\]
where the \(G_m\) are independent standard circular complex Gaussians with \(\mathbb E|G_m|^2=1\). Its Laplace transform for \(s\ge0\) is
\[
\mathbb E e^{-sY_{\lambda,g}}
 =F(s)\exp\!\left(-\lambda\sum_{m=1}^K\frac{s c_m|\eta_m|^2}{1+s c_m}\right),\qquad
F(s)=\prod_{m\ge1}(1+s c_m)^{-1}.
\]
For \(0\le s<\pi/2\), \(F(s)=a/\sin(\pi a/2)\) with \(a=\sqrt{1-2s/\pi}\). At \(s=\pi/2\) it equals \(2/\pi\); for \(s>\pi/2\) it equals \(b/\sinh(\pi b/2)\) with \(b=\sqrt{2s/\pi-1}\).

**Inverse theorem and sensitivity.** For each fixed known \(\lambda>0\), two polynomial tilts give the same limit law if and only if all their powers \(|\eta_m|^2\) agree. Phases are not identified. More generally, if \(\lambda\) is unknown, equality of limit laws is exactly equality of the products \(\lambda|\eta_m|^2\) for all \(m\). The mean and variance are
\[
\mathbb E Y_{\lambda,g}=\frac1\pi+\lambda Q(g),\qquad
\operatorname{Var}(Y_{\lambda,g})=\frac14-\frac2{\pi^2}+2\lambda\sum_{m=1}^Kc_m^2|\eta_m|^2.
\]
At fixed \(H=\sum_{m=1}^K|\eta_m|^2>0\) and fixed \(\lambda>0\), the shift \(\lambda Q(g)\) is maximized exactly by placing all power in mode \(1\), and minimized exactly by placing it in mode \(K\), in each case up to the phase of the nonzero coefficient. When \(K=1\) these allocations coincide. At \(\lambda=0\), every spectrum with the given \(H\) gives the same shift zero and the same limit law.

**Above the critical window.** If \(n\varepsilon_n^2\to\infty\), still with \(\varepsilon_n\to0\), then \(D_n/(n\varepsilon_n^2)\to Q(g)\) in \(L^1\).

## Assumptions and scope

Generator lengths are exactly one. For a degenerate segment zonogon, perimeter means its continuous convex-geometric extension (twice the length of the segment), so the stated identity is pathwise even there. Degeneracy has probability zero under the row densities. The direction circle is unoriented, the polynomial is fixed as \(n\to\infty\), and within-row independence is required. No coupling or independence between rows is required. Since \(g\) is bounded, positivity of the densities holds automatically for all sufficiently large \(n\).

## Proof

**1. Geometry and the Fourier identity.** Perimeter is Minkowski additive in the plane by the Cauchy width formula. Each segment contributes two. The planar zonotope area formula gives \(A_n=\sum_{i<j}|\sin(\theta_i-\theta_j)|\). Insert the absolutely convergent Fourier series
\[
|\sin t|=\frac2\pi-\frac4\pi\sum_{m\ge1}\frac{\cos(2mt)}{4m^2-1}
\]
and use \(2\sum_{i<j}\cos(2m(\theta_i-\theta_j))=|\sum_j e^{2im\theta_j}|^2-n\). The cancellation uses \(\sum_m c_m=1/\pi\), by telescoping. Thus with \(V_{m,n}=n^{-1/2}\sum_j e^{2im\theta_j}\) the deficit is \(\sum_m c_m|V_{m,n}|^2\). Absolute convergence is also a consequence of \(|V_{m,n}|^2\le n\).

**2. Exact mean.** Orthogonality gives \(\mathbb E e^{2im\theta}=\varepsilon_n\eta_m\). By independence \(\mathbb E|V_{m,n}|^2=1+(n-1)\varepsilon_n^2|\eta_m|^2\). Nonnegative summation gives the stated mean.

**3. Joint limit and moments.** For finitely many positive modes, apply the multivariate Lindeberg–Feller theorem to their centered real and imaginary parts. The summands before normalization are bounded uniformly; since the row densities converge uniformly to the uniform density, the covariance matrix converges to that of the uniform row, namely one half times the identity on the real coordinates, by orthogonality. The deterministic shifts \(\sqrt n\varepsilon_n\eta_m\) tend to \(\sqrt\lambda\eta_m\). This gives the stated circular complex normals and independence for each fixed cutoff.

For \(M\ge K\) the expected tail of the statistic is exactly \(\sum_{m>M}c_m=1/[\pi(2M+1)]\). To justify moment convergence, the sixth moments of the centered normalized real and imaginary sums are uniformly bounded in \(m,n\): after expanding the sixth power any surviving index pattern uses at most three distinct indices (a singleton has mean zero), and there are \(O(n^3)\) such terms, all uniformly bounded before division by \(n^3\). The bound holds for the complex absolute sixth moments as well. Adding the bounded shifts in the critical regime gives \(\sup_{m,n}\mathbb E|V_{m,n}|^6<\infty\). It follows, by Minkowski, both that the \(L^2\) tail of \(\sum_m c_m|V_{m,n}|^2\) is uniformly bounded by a constant times \(\sum_{m>M}c_m\) and that its finite cutoffs have uniformly bounded third moments. The latter ensures uniform integrability of their squared values; weak convergence of the cutoffs therefore also yields convergence of their first and second moments. The limit Gaussian series has the same summable \(L^2\) tail bound and finite mean. Letting \(M\to\infty\) proves the full weak and moment convergence, using the uniform tail bounds (for second moments, bound the difference of squared \(L^2\) norms by the \(L^2\) truncation error times the sum of the norms).

**4. Transform and constants.** A direct Gaussian integral for a standard circular complex normal \(G\) gives
\[
\mathbb E e^{-t|G+v|^2}=(1+t)^{-1}\exp[-t|v|^2/(1+t)],\qquad t\ge0.
\]
Taking products and passing to the almost surely finite series gives the formula for the Laplace transform. The central product is the ratio of \(\prod_{m\ge1}(1-1/(4m^2))\) to \(\prod_{m\ge1}(1-(1-2s/\pi)/(4m^2))\). Euler's sine product gives the stated expression and its hyperbolic continuation, with the value at \(s=\pi/2\) obtained by continuity. The elementary moments are \(\mathbb E|G+v|^2=1+|v|^2\) and \(\operatorname{Var}|G+v|^2=1+2|v|^2\). In the variance sum use
\[
\frac{1}{(4m^2-1)^2}=\frac14\left(\frac1{(2m-1)^2}+\frac1{(2m+1)^2}\right)-\frac{1}{2(4m^2-1)}
\]
to get \(\sum_m c_m^2=1/4-2/\pi^2\).

**5. Identifiability and extremizers.** For \(s>0\), divide out the same nonzero \(F(s)\) and take logarithms. Equality of limit laws implies equality of the rational sums \(\sum_m s c_m\lambda|\eta_m|^2/(1+s c_m)\) on the positive axis, hence identically. The pole positions \(-1/c_m\) are pairwise distinct and at each the residue is \(-\lambda|\eta_m|^2/c_m\), with zero residue allowed. This identifies precisely the products, and conversely equal products give equal Laplace transforms and laws. For known positive \(\lambda\), divide by it to recover the powers. The strict decrease of the weights gives the asserted extremizers by a weighted average at fixed total power, provided \(\lambda>0\); at \(\lambda=0\) the shift vanishes identically.

**6. Above the critical window.** Write \(V_{m,n}=\sqrt n\varepsilon_n\eta_m+\xi_{m,n}\), with \(\mathbb E\xi_{m,n}=0\) and \(\mathbb E|\xi_{m,n}|^2\le1\). The total cross term in the deficit is bounded in \(L^1\) by \(2\sqrt n\varepsilon_n\sum_{m=1}^K c_m|\eta_m|\), by Cauchy–Schwarz. The noise sum has mean at most \(\sum_m c_m=1/\pi\). Dividing these bounds by \(n\varepsilon_n^2\to\infty\) proves the \(L^1\) result.

## Verification

The included Python `verify.py` checks finite angle patterns, the Fourier truncation bound, the Euler product and a finite-row expectation example. These diagnostics do not prove the distributional limits, the strict sensitivity statements or the inverse theorem. The exact estimates and residue calculation above supply those results.

## Relationship to prior work and limitations

The deficit is, up to normalization, an existing circular uniformity statistic: for \(X_j=e^{2i\theta_j}\) on the unit circle, Bakshaev's chordal \(N\)-distance statistic (equation (3), with the norm itself as kernel) equals \(4D_n\), since the mean uniform chord is \(4/\pi\) and \(\sum_{i,j}|X_i-X_j|=4A_n\). It also equals the circular Sobolev statistic of Jammalamadaka–Meintanis–Verdebout (equation (4)) for weights \(c_m/2\), in the normalization \(D_n\). The isotropic baseline and the mechanism of weighted Gaussian-square local limits are not claimed as new. The model with one unusually long segment also gives a noncentral limit, by a different mechanism. Schneider gives general random-segment valuation expectations and a central limit theorem with a nondegenerate first projection; at isotropy here that projection is constant. Buffière–Marchal study a different lattice model. The result here classifies equality in law for the scalar deficit under arbitrary fixed finite-band angular tilts in the critical window. It does not identify phases or separate the intensity from the powers when both are unknown. No growing-bandwidth, correlated-directions, variable-length, or higher-dimensional theorem is asserted; no exhaustive historical priority claim is made.

## References

1. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774, especially the projection-variance assumption in §4.
2. T. Buffière and P. Marchal, *Fluctuations of lattice zonotopes and polygons*, arXiv:2303.18045.
3. H.-K. Hwang and S. Kuriki, arXiv:2404.06040, Theorems 3.2–3.3 on generalized Watson statistics.
4. E. García-Portugués, D. Paindaveine and T. Verdebout, arXiv:2108.09874, Proposition 5 and Theorems 2 and 4 on Sobolev tests under local alternatives.
5. A. Bakshaev, *N-distance tests of uniformity on the hypersphere*, Nonlinear Analysis: Modelling and Control 15 (2010), 15–28, equation (3), Proposition 1 and §3.2.1.
6. S. R. Jammalamadaka, S. Meintanis and T. Verdebout, *On Sobolev tests of uniformity on the circle with an extension to the sphere*, Bernoulli 26 (2020), 2226–2252, equation (4).
