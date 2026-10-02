# Sign-imbalance phase interpolation for flat Gaussian-chaos maxima

## Statement

Let \(p\to\infty\), put \(L=\log p\), and let \(R=R_p\to\infty\). Choose
\(s_{1,R},\ldots,s_{R,R}\in\{-1,+1\}\) and write
\[
\delta_R=\frac1R\sum_{i=1}^R s_{i,R}.
\]
For \(j=1,\ldots,p\), let
\[
Q_{j,R}=\frac1{\sqrt{2R}}\sum_{i=1}^R s_{i,R}(G_{ji}^2-1),
\]
with all \(G_{ji}\) independent standard Gaussians, and let
\[
M_{p,R}=\max_{j\le p}Q_{j,R}.
\]
All such spectra have fourth effective rank \(R\) and fourth cumulant \(12/R\), while
\[
\kappa_3(Q_{j,R})=\frac{2\sqrt2\,\delta_R}{\sqrt R}.
\]

Assume
\[
\frac{R}{L^{5/3}}\longrightarrow\infty.
\]
Define
\[
\Theta_p=
\frac43\,\delta_R\frac{L^{3/2}}{\sqrt R}
+
(2-4\delta_R^2)\frac{L^2}{R}.
\]
Let \(b_p=\Phi^{-1}(1-p^{-1})\) and \(c_p=b_p^{-1}\).

If \(\Theta_p\to\theta\in\mathbb R\), then for every fixed \(x\),
\[
\Pr\!\left(\frac{M_{p,R}-b_p}{c_p}\le x\right)
\longrightarrow
\exp\{-e^{-(x-\theta)}\}.
\]
Hence the Kolmogorov distance from the maximum of \(p\) independent standard Gaussians
converges to the distance between two Gumbel laws separated by \(\theta\); writing
\(c=|\theta|\),
\[
D(c)=
\begin{cases}
0,&c=0,\\[2mm]
(1-e^{-c})\exp\!\left[-\frac{c}{e^c-1}\right],&c>0.
\end{cases}
\]

The transition between cubic and quartic behavior is controlled by sign imbalance.
In particular, the two corrections are comparable when
\[
|\delta_R|\asymp\sqrt{\frac{L}{R}}.
\]
Thus the signed third spectral moment is a second phase coordinate that is invisible to
fourth effective rank.

A fully indefinite separation follows. Let \(R_p\sim L^{5/2}\), rounded to a multiple of
four. Compare a spectrum with \(3R_p/4\) positive and \(R_p/4\) negative eigenvalues
against a perfectly balanced spectrum. Both have the same fourth effective rank and the same
fourth cumulant, and both are indefinite, but the first has a diverging cubic correction while
the second has a vanishing quartic correction. Therefore their maximum-Gaussianization
behavior is asymptotically opposite.

## Proof

For one coordinate, put
\[
Y_i=\frac{s_{i,R}(G_i^2-1)}{\sqrt2},
\qquad
Q_R=R^{-1/2}\sum_{i=1}^R Y_i.
\]
The averaged cumulant generating function is
\[
K_\delta(t)
=
-\frac{\delta t}{\sqrt2}
-\frac{1+\delta}{4}\log(1-\sqrt2\,t)
-\frac{1-\delta}{4}\log(1+\sqrt2\,t),
\]
so
\[
K_\delta(t)
=
\frac{t^2}{2}
+\frac{\sqrt2\,\delta}{3}t^3
+\frac12t^4
+O(t^5).
\]
Series inversion of \(K_\delta'(t)=a\) gives
\[
I_\delta(a)
=
\frac{a^2}{2}
-\frac{\sqrt2\,\delta}{3}a^3
+\left(\delta^2-\frac12\right)a^4
+O(a^5).
\]

Exponential tilting at \(x\asymp\sqrt L\), together with the analytic moment bounds of this
finite-parameter family, gives the uniform relative-tail expansion
\[
\log\frac{\Pr(Q_R>x)}{\overline\Phi(x)}
=
\frac{\sqrt2\,\delta_R}{3}\frac{x^3}{\sqrt R}
+
\left(\frac12-\delta_R^2\right)\frac{x^4}{R}
+
O\!\left(
\frac{x^5}{R^{3/2}}+\frac{x}{\sqrt R}+x^{-2}
\right).
\]
The displayed remainder is \(o(1)\) at the Gaussian extreme scale under
\(R/L^{5/3}\to\infty\). Since \(b_p\sim\sqrt{2L}\), substitution of
\(x=b_p+c_py\) yields
\[
\log\frac{\Pr(Q_R>x)}{\overline\Phi(x)}
=
\Theta_p+o(1).
\]
Because \(p\overline\Phi(b_p+c_py)\to e^{-y}\), independence of the \(p\) coordinates
gives the shifted-Gumbel limit. Maximizing the difference between two translated Gumbel
distribution functions gives the stated \(D(c)\).

For the two indefinite spectra at \(R\sim L^{5/2}\), the \(3/4\)-positive spectrum has
\(\delta_R=1/2\), so its cubic term grows like \(L^{1/4}\), whereas the balanced spectrum
has \(\delta_R=0\) and its quartic term is \(2L^{-1/2}\to0\). This proves the separation.

## Prior boundary

An earlier 18 September 2026 result already proves the sharp all-positive
\((\log p)^3\) endpoint, the perfectly balanced \((\log p)^2\) endpoint, their exact critical
Gumbel shifts and Kolmogorov profiles, and the resulting conclusion that fourth effective rank
alone is not a sharp universal phase coordinate. Those endpoint theorems are prior input here.

The contribution retained here is the interpolation across partially imbalanced signed spectra:
the explicit two-term phase coordinate \(\Theta_p\), the cubic/quartic crossover scale, and the
same-effective-rank separation using two genuinely indefinite spectra.

## Limitations

The theorem treats independent coordinates and flat spectra with a common absolute eigenvalue.
The two-term expansion assumes \(R/(\log p)^{5/3}\to\infty\); lower ranks can require further
Cramér terms. It concerns the Gaussian-chaos target and not the separate finite-sample
approximation from a canonical \(U\)-statistic. Older general triangular-array Cramér theory may
contain analytic ingredients, but no earlier sign-imbalance effective-rank phase theorem was
identified.

## References

1. L. Cai and Q. Hu, *Approximation Theorems for High-Dimensional Canonical U-Statistics:
   Gaussian Chaos and Phase Transition*, arXiv:2609.20529.
2. Published result, *Sharp sign-sensitive Gaussianization thresholds for equal-spectrum
   second-chaos maxima*, 18 September 2026.
3. A. Bose, A. Dasgupta and K. Maulik, *Maxima of Dirichlet and triangular arrays of gamma
   variables*, arXiv:0803.3518.
4. C. W. Anderson, S. G. Coles and J. Hüsler, *Maxima of Poisson-like variables and related
   triangular arrays*, Annals of Applied Probability 7 (1997), 953–971.
