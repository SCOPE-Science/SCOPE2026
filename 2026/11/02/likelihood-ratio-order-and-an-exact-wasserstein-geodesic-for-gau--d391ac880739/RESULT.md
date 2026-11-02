# Likelihood-ratio order and an exact Wasserstein geodesic for Gaussian peak heights

## Finding
Let \(H_\eta\), for \(0\leq\eta\leq1\), denote the Gaussian smooth-Palm peak-height family described below. For every \(0\leq a<b<1\), the likelihood ratio \(h_b(x)/h_a(x)\) is **strictly increasing** over the whole real line. At \(b=1\), this ratio is nondecreasing and is strictly increasing for positive arguments. Moreover, for every real \(x\),
\[
F_b(x)<F_a(x)\quad(0\leq a<b\leq1),
\]
and the first-Wasserstein distance is exactly
\[
W_1(H_a,H_b)=\sqrt{\pi/2}\,(b-a).
\]
Thus the family is an isometric, constant-speed path in first-Wasserstein distance, and its first-order stochastic order is strict at every finite threshold.

## Assumptions and scope
Write \(\phi(x)=(2\pi)^{-1/2}\exp(-x^2/2)\) and \(\Phi(x)=\int_{-\infty}^x\phi(u)\,du\). For \(0<\eta<1\), set \(s=\sqrt{1-\eta^2}\) and define the density
\[
h_\eta(x)=s\phi(x/s)+\sqrt{2\pi}\,\eta x\phi(x)\Phi(\eta x/s),\qquad x\in\mathbb R.
\]
Set \(h_0(x)=\phi(x)\) and \(h_1(x)=x\exp(-x^2/2)\mathbf1_{\{x>0\}}\). Let \(F_\eta\) be the corresponding CDF. This is the one-dimensional unit-variance Gaussian peak-height family from Cheng and Ginos (2026, equation (3.9)), where \(\eta\) describes the magnitude of the height–curvature correlation conditioned on zero slope. The theorem is **about these probability distributions**, not arbitrary Gaussian random fields or their finite-mesh peak laws.

Equivalently, if \(R\) is Rayleigh with density \(r\exp(-r^2/2)\mathbf1_{\{r>0\}}\) and \(Z\) is standard Gaussian independent of \(R\), then
\[
H_\eta\ \stackrel d=\ \eta R+\sqrt{1-\eta^2}\,Z.
\]
The convolution identity follows directly by completing the square; it covers both endpoints. All first moments are finite.

## Proof
**Likelihood-ratio order.** For \(\eta<1\), put \(t=\eta/\sqrt{1-\eta^2}\) and \(g(z)=\phi(z)+z\Phi(z)=\mathbb E(Z+z)_+\). Completing the square in the Rayleigh–Gaussian convolution yields
\[
h_\eta(x)=\sqrt{2\pi}\,\sqrt{1-\eta^2}\,\phi(x)g(tx).
\]
Here \(g(z)>0\) on the entire real line and \(g'(z)=\Phi(z)\). The logarithmic derivative in \(x\) is \(-x+t\Phi(tx)/g(tx)\). For \(z=tx\), straightforward differentiation gives
\[
\frac{\partial}{\partial t}\left[\frac{t\Phi(tx)}{g(tx)}\right]
=\frac{\phi(z)\big((1+z^2)\Phi(z)+z\phi(z)\big)}{g(z)^2}>0.
\]
Indeed the bracket is \(\mathbb E[(Z+z)^2\mathbf1_{\{Z+z>0\}}]>0\). Since \(t\) increases strictly with \(\eta\), subtracting the logarithmic derivatives for \(a<b<1\) shows \(\partial_x\log(h_b/h_a)>0\). If \(b=1\), the ratio is zero on \(( -\infty,0]\); for \(x>0\) its logarithmic derivative is
\[
\frac1x-\frac{t_a\Phi(t_ax)}{g(t_ax)}=\frac{\phi(t_ax)}{xg(t_ax)}>0.
\]
Therefore the endpoint ratio is nondecreasing globally and strictly increasing on the positive half-line. No differentiability of a likelihood ratio at the support boundary is presumed.

**Pointwise strict stochastic order.** From the independent Rayleigh–Gaussian representation, for \(\eta<1\)
\[
F_\eta(x)=\int_0^\infty r e^{-r^2/2}\,\Phi\left(\frac{x-\eta r}{\sqrt{1-\eta^2}}\right)dr.
\]
Differentiation under the integral on compact parameter subsets of \([0,1)\) is justified by Gaussian domination. With \(s=\sqrt{1-\eta^2}\), completing the square and integrating by parts yield
\[
\begin{aligned}
\partial_\eta F_\eta(x)
&=\frac{\phi(x)}{s^3}\int_0^\infty r(\eta x-r)e^{-(r-\eta x)^2/(2s^2)}dr\\
&=-\frac{\phi(x)}s\int_0^\infty e^{-(r-\eta x)^2/(2s^2)}dr\\
&=-\sqrt{2\pi}\,\phi(x)\Phi\left(\frac{\eta x}s\right)<0.
\end{aligned}
\]
This is strictly negative for every finite \(x\) and every \(0\leq\eta<1\). Continuity of \(F_\eta(x)\) at \(\eta=1\) by dominated convergence proves \(F_b(x)<F_a(x)\) also when \(b=1\); one can integrate the strictly negative derivative over any compact subinterval inside \([a,1)\) to obtain a strict gap before taking the endpoint limit.

**Exact metric.** The representation gives \(\mathbb E H_\eta=\eta\mathbb ER=\eta\sqrt{\pi/2}\). Because the distributions are stochastically ordered, the one-dimensional quantile coupling is monotone; hence its absolute-difference cost equals the difference of means. The universal Kantorovich–Rubinstein lower bound furnished by the \(1\)-Lipschitz test function \(x\mapsto x\) is the same difference. Therefore
\[
W_1(H_a,H_b)=\mathbb E H_b-\mathbb E H_a=\sqrt{\pi/2}(b-a).
\]
Every endpoint and parameter range in the claim is covered.

## Verification
The standalone \(\texttt{verify.py}\) requires only Python 3 standard-library modules. Run \(\texttt{python3 verify.py}\). It compares the density with an independently integrated Rayleigh–Gaussian convolution, compares two CDF representations, checks the sign of sample likelihood-ratio increments and stochastic dominance, compares numerical parameter derivatives against the analytic identity, and checks the first-moment formula. The recorded execution passed 347 deterministic checks. These tests corroborate computations but do not prove the continuous-infinite assertion; the analytic positivity and integral derivations above do.

## Relationship to prior work
Cheng and Ginos (arXiv:2610.27687v1, Section 3, equation (3.9) and Remark 4.2) derive the height density and identify Gaussian and Rayleigh endpoints under Gaussian-process regularity, together with total-variation infill convergence. Their formula, used as the starting premise here, is **not new**. The present result establishes a global likelihood-ratio comparison, an explicit strictly signed CDF derivative, and the exact pairwise first-Wasserstein metric; these are stronger distributional comparisons rather than a rederivation of the density. Cheng and Schwartzman (arXiv:1307.5863v3) give earlier general Palm peak-height formulas, and Zhao, Cheng, Davenport, and Schwartzman (arXiv:2502.12452v1) give a general one-dimensional nonstationary Gaussian height law. Neither inspected result was found to state this complete ordered-family and metric identity. General likelihood-ratio and stochastic-order theory supplies implications after verifying the kernel comparison, not its specific sign calculation.

## Limitations
An exhaustive historical-priority determination is not claimed; a broader prior total-positivity theorem could subsume part of the order proof. The parameter \(\eta\) varies across Gaussian covariance models; stochastic order does not assert that changing covariance in an arbitrary way increases \(\eta\). The result concerns the limiting Palm family, not finite-grid distributions, peak counts, multidimensional fields, or joint peak-height dependence. The exact \(W_1\) formula is a statement about one-dimensional marginal laws and does not imply joint sample-path couplings of different Gaussian processes.

## References
1. D. Cheng and J. Ginos, *Local Maxima of Discrete Gaussian Processes: Exact Distributions and Infill Limits*, arXiv:2610.27687v1, 20 October 2026. https://arxiv.org/html/2610.27687v1
2. D. Cheng and A. Schwartzman, *Distribution of the Height of Local Maxima of Gaussian Random Fields*, arXiv:1307.5863v3. https://arxiv.org/html/1307.5863v3
3. Y. Zhao, D. Cheng, S. Davenport, and A. Schwartzman, *On the peak height distribution of non-stationary Gaussian random fields: 1D general covariance and scale space*, arXiv:2502.12452v1, 18 February 2025. https://arxiv.org/html/2502.12452v1
