# A universal one-to-root-three reflection crossing for standardized Gamma densities
## Finding
Let \(X_{\alpha,\beta}\sim\operatorname{Gamma}(\alpha,\beta)\), with shape \(\alpha>0\) and scale \(\beta>0\). Define
\[
Z_\alpha=\frac{X_{\alpha,\beta}-\alpha\beta}{\beta\sqrt{\alpha}},
\]
and let \(g_\alpha\) denote the density of \(Z_\alpha\). The density is independent of \(\beta\).

On the common support of the reflected pair, \(0<z<\sqrt{\alpha}\), the following classification holds.

If \(0<\alpha\le1\), then
\[
g_\alpha(z)<g_\alpha(-z)
\]
for every \(0<z<\sqrt{\alpha}\); there is no interior reflected-density crossing.

If \(\alpha>1\), there is a unique \(\kappa_\alpha\) with
\[
1<\kappa_\alpha<\sqrt{3}
\]
such that
\[
g_\alpha(z)<g_\alpha(-z)\quad(0<z<\kappa_\alpha),
\]
\[
g_\alpha(\kappa_\alpha)=g_\alpha(-\kappa_\alpha),
\]
and
\[
g_\alpha(z)>g_\alpha(-z)\quad(\kappa_\alpha<z<\sqrt{\alpha}).
\]
Writing \(r_\alpha=\kappa_\alpha/\sqrt{\alpha}\), the crossing is determined exactly by
\[
\frac{\operatorname{artanh}(r_\alpha)}{r_\alpha}
=\frac{\alpha}{\alpha-1}.
\]
The endpoint behavior is
\[
\kappa_\alpha\longrightarrow1\quad(\alpha\downarrow1)
\]
and
\[
\kappa_\alpha
=\sqrt{3}\left(1-\frac{2}{5\alpha}+O(\alpha^{-2})\right)
\quad(\alpha\to\infty).
\]

## Assumptions and scope
The Gamma parameterization is shape \(\alpha\), scale \(\beta\), so
\[
\mathbb E X_{\alpha,\beta}=\alpha\beta,
\qquad
\operatorname{Var}(X_{\alpha,\beta})=\alpha\beta^2.
\]
The comparison is pointwise between the standardized density at equal distances to the right and left of the mean. The interval \(0<z<\sqrt{\alpha}\) is exactly where both reflected arguments lie in the support. No assertion is made that the magnitude of the density difference stays bounded away from zero as \(\alpha\to\infty\); in fact the standardized Gamma density converges to the standard normal density.

## Proof
The standardized density is
\[
g_\alpha(z)
=
\frac{\sqrt{\alpha}}{\Gamma(\alpha)}
\bigl(\alpha+\sqrt{\alpha}z\bigr)^{\alpha-1}
e^{-\alpha-\sqrt{\alpha}z},
\qquad z>-\sqrt{\alpha}.
\]
For \(0<z<\sqrt{\alpha}\), put \(r=z/\sqrt{\alpha}\in(0,1)\). Direct cancellation gives
\[
\log\frac{g_\alpha(z)}{g_\alpha(-z)}
=
2\bigl((\alpha-1)\operatorname{artanh}r-\alpha r\bigr).
\]
Hence the sign is the sign of
\[
(\alpha-1)F(r)-\alpha,
\qquad
F(r)=\frac{\operatorname{artanh}r}{r}.
\]

For \(0<\alpha\le1\), both terms in
\[
(\alpha-1)\operatorname{artanh}r-\alpha r
\]
are nonpositive and the second is strictly negative, proving the first case.

Now assume \(\alpha>1\). The function \(F\) is strictly increasing on \((0,1)\). Indeed,
\[
F'(r)=
\frac{r/(1-r^2)-\operatorname{artanh}r}{r^2},
\]
and the numerator has derivative
\[
\frac{2r^2}{(1-r^2)^2}>0
\]
and vanishes at \(r=0\). Also \(F(r)\to1\) as \(r\downarrow0\) and \(F(r)\to\infty\) as \(r\uparrow1\). Therefore there is a unique \(r_\alpha\in(0,1)\) satisfying
\[
F(r_\alpha)=\frac{\alpha}{\alpha-1},
\]
and the density-ratio sign changes exactly once there.

It remains to locate the crossing. Since
\[
F(r)-1=\sum_{m=1}^\infty\frac{r^{2m}}{2m+1},
\qquad 0<r<1,
\]
at \(r=1/\sqrt{\alpha}\) one has
\[
F(r)-1
=
\sum_{m=1}^\infty\frac{\alpha^{-m}}{2m+1}
<
\sum_{m=1}^\infty\alpha^{-m}
=
\frac{1}{\alpha-1}.
\]
Thus \(r_\alpha>1/\sqrt{\alpha}\), or \(\kappa_\alpha>1\).

For \(1<\alpha\le3\), the support condition itself gives
\[
\kappa_\alpha<\sqrt{\alpha}\le\sqrt{3}.
\]
For \(\alpha>3\), put \(r_0=\sqrt{3/\alpha}\). Then
\[
F(r_0)-1
=
\sum_{m=1}^\infty
\frac{3^m}{2m+1}\alpha^{-m}.
\]
The coefficient for \(m=1\) equals one, while
\[
3^m>2m+1
\]
for every \(m\ge2\). Hence
\[
F(r_0)-1>
\sum_{m=1}^\infty\alpha^{-m}
=
\frac{1}{\alpha-1},
\]
so \(r_\alpha<r_0\), equivalently \(\kappa_\alpha<\sqrt{3}\).

As \(\alpha\downarrow1\), the right side \(\alpha/(\alpha-1)\) diverges, forcing \(r_\alpha\uparrow1\); together with \(\sqrt{\alpha}\to1\), this gives \(\kappa_\alpha\to1\).

For the large-shape expansion, write \(s_\alpha=\kappa_\alpha^2=\alpha r_\alpha^2\). With \(e=1/\alpha\),
\[
F(r_\alpha)
=
1+\frac{s_\alpha e}{3}
+\frac{s_\alpha^2 e^2}{5}
+O(e^3),
\]
whereas
\[
\frac{\alpha}{\alpha-1}
=
1+e+e^2+O(e^3).
\]
Setting \(s_\alpha=3+c e+O(e^2)\) and comparing the \(e^2\) coefficient gives
\[
\frac{c}{3}+\frac{9}{5}=1,
\qquad
c=-\frac{12}{5}.
\]
Therefore
\[
\kappa_\alpha^2
=
3-\frac{12}{5\alpha}+O(\alpha^{-2}),
\]
and taking the positive square root yields
\[
\kappa_\alpha
=
\sqrt{3}
\left(1-\frac{2}{5\alpha}+O(\alpha^{-2})\right).
\]

## Verification
The proof is exact and analytic. A companion script, `verify.py`, recomputes the reflected-density log-ratio identity symbolically, checks the first two coefficients of the crossing expansion, and numerically solves the defining equation at representative shapes. Those calculations are regression checks only; uniqueness, the interval \((1,\sqrt{3})\), and the asymptotic expansion are established above without finite enumeration.

## Relationship to prior work
Sun, Hu, and Sun study Gamma probability inequalities centered at the mean. Their earliest public version, arXiv:2303.17487 (30 March 2023), proves that the probability within one standard deviation of the mean exceeds its standard-normal counterpart and notes that analogous comparisons for other radii can change sign. The full public preprint was inspected. It does not state a pointwise reflected-density crossing, the exact \(\operatorname{artanh}\) equation, the universal interval \((1,\sqrt{3})\), or the large-shape crossing-radius expansion.

A separate 2023 paper by the same authors, arXiv:2304.11459, studies one-standard-deviation variation comparison for several infinitely divisible families. Its stated scope is again probability mass in a central interval, not equality of Gamma density values at points symmetric about the mean.

Targeted database and web searches for reflected Gamma-density crossings, symmetric-point density ratios, and the `artanh` characterization did not locate a covering statement. The closest published-finding corpus records concern different Gamma approximation, quantile-curvature, and special-function monotonicity problems.

## Limitations
The finding concerns pointwise reflection of the density around the mean, not a complete classification of central probabilities for every radius. For \(z\ge\sqrt{\alpha}\), the reflected point lies outside the Gamma support, so the common-support comparison ends. The literature search cannot rule out an older equivalent observation under different skewness terminology; that residual risk is recorded in the accompanying review data.

## References
1. P. Sun, Z.-C. Hu, W. Sun, *The extreme values of two probability functions for the Gamma distribution*, arXiv:2303.17487, first public version 30 March 2023. https://arxiv.org/abs/2303.17487
2. P. Sun, Z.-C. Hu, W. Sun, *The infimum values of two probability functions for the Gamma distribution*, Journal of Inequalities and Applications 2024, Article 5. https://doi.org/10.1186/s13660-024-03081-w
3. P. Sun, Z.-C. Hu, W. Sun, *Variation comparison between infinitely divisible distributions and the normal distribution*, arXiv:2304.11459, first public version 22 April 2023. https://arxiv.org/abs/2304.11459
