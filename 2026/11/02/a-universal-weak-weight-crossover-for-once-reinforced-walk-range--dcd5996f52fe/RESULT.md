# A universal weak-weight crossover for once-reinforced walk ranges

## Finding

Let \(R_n\) denote the length of the interval visited through time \(n\) by either of the two one-dimensional once-reinforced random walks defined below. In a triangular family, every previously traversed edge has weight \(c_n>0\), every untraversed edge has weight one, and the parameter \(c_n\) is fixed throughout that entire walk of length \(n\).

**Critical regime.** For every deterministic sequence \(c_n>0\) with \(c_n\sqrt n\to\gamma\in[0,\infty)\),
\[
\frac{R_n}{n}\ \Longrightarrow\ Z_\gamma.
\]
If \(\gamma=0\), then \(Z_0=1\) almost surely. If \(0<\gamma<\infty\), then the limit is continuous, supported on \((0,1)\), and has distribution function and density
\[
\Pr(Z_\gamma\le r)=2\Phi\!\left(\frac{\gamma r}{\sqrt{1-r}}\right)-1,\quad
f_\gamma(r)=\frac{\gamma(2-r)}{(1-r)^{3/2}}\,\varphi\!\left(\frac{\gamma r}{\sqrt{1-r}}\right),\qquad 0<r<1,
\]
where \(\Phi\) and \(\varphi\) are the standard normal distribution and density. The distribution function is zero at nonpositive arguments and one at arguments at least one.

**Weak-weight diffusive-side regime.** If \(c_n\to0\) and \(c_n\sqrt n\to\infty\), then
\[
\frac{c_nR_n}{\sqrt n}\ \Longrightarrow\ |N|,\qquad N\sim N(0,1).
\]
The two different geometries have the *same* laws in both regimes. Thus the sharp crossover between a deterministic ballistic range fraction and the weak-weight half-normal range scale occurs when \(c_n\) is of order \(n^{-1/2}\).

## Assumptions and scope

The **full-line model** is a nearest-neighbor walk on \(\mathbb Z\), started at zero. Each edge starts with weight one and, upon its first crossing, permanently receives weight \(c_n\); each next step selects its incident edge proportionally to its current weight. Define \(R_n=\max_{j\le n}X_j-\min_{j\le n}X_j\).

The **reflected half-line model** is the same walk on \(\mathbb Z_{\ge0}\), started at zero, with a deterministic step to one whenever the walk is at zero. Define \(R_n=\max_{j\le n}X_j\). In both cases the number of visited sites is \(R_n+1\). The condition \(c_n>0\) permits the self-repelling range \(0<c_n<1\); it is essential that \(c_n\) can vary *between* experiments indexed by \(n\), not during the individual path.

The conclusions concern distributional limits, not pathwise limits or fixed-positive-weight limits. In the full-line case, the initial step may be positive or negative with probability one half each.

## Proof

**1. Inverse-range decomposition.** Let \(S_m=\inf\{j\ge0:R_j=m\}\) and \(T_i=S_{i+1}-S_i\), so that \(S_1=1\) and \(S_m=1+\sum_{i=1}^{m-1}T_i\). At the moment the range becomes \(i\), the walk is at an extreme point. An outward step succeeds with probability \(1/(1+c_n)\); on a failure it makes an inward step and follows an ordinary simple random walk until the next extreme point is reached. In the half-line case the interior path reflects at zero. Reflection symmetry on the full line and the strong Markov property imply independent waiting times \(T_i\), each equal in law to
\[
1+\sum_{j=1}^{Y_i}(1+\tau_i^{(j)}),\qquad
\Pr(Y_i=k)=\frac1{1+c_n}\left(\frac{c_n}{1+c_n}\right)^k,\quad k\ge0.
\]
Here \(\tau_i^{(j)}\) are independent return times of the ordinary walk after an inward step. They are the hitting times of \(\{0,i\}\) from \(i-1\) on the full line, and of \(i\) from \(i-1\) with reflection at zero on the half-line.

**2. Exact inverse-range transform.** For \(\theta>0\) put \(q=\operatorname{sech}\theta\). Solving \(g_j=q(g_{j-1}+g_{j+1})/2\) with the appropriate absorbing or reflecting boundary yields
\[
\mathbb E[q^{1+\tau_i}]=1-\tanh\theta\,\tanh(\kappa i\theta),\qquad
\kappa=\begin{cases}\tfrac12&\text{full line},\\1&\text{reflected half-line}.\end{cases}
\]
For the full line the boundary values are \(g_0=g_i=1\), giving \(g_j=\cosh((j-i/2)\theta)/\cosh(i\theta/2)\). For the reflected half-line, \(g_i=1\), \(g_0=qg_1\), giving \(g_j=\cosh(j\theta)/\cosh(i\theta)\). The geometric sum therefore gives, exactly for each positive integer \(m\),
\[
\mathbb E[q^{S_m}]
=q^m\prod_{i=1}^{m-1}\left(1+c_n\tanh\theta\,\tanh(\kappa i\theta)\right)^{-1}.\tag{1}
\]

**3. A uniform summation estimate.** For either fixed \(\kappa\in\{1/2,1\}\),
\[
0\le m-1-\sum_{i=1}^{m-1}\tanh(\kappa i\theta)
\le\sum_{i\ge1}2e^{-2\kappa i\theta}=O(1/\theta),\quad\theta\downarrow0.\tag{2}
\]
Moreover, for \(0\le u\le1\), the error in replacing \(\log(1+u v)\) by \(uv\) is bounded by \(u^2/2\), uniformly in \(0\le v\le1\). Consequently, if \(u_n=c_n\tanh\theta_n\), the logarithm of the product in (1) is
\[
-u_n(m-1)+O\!\left(u_n/\theta_n+m u_n^2\right),\tag{3}
\]
whenever \(\theta_n\downarrow0\). The error is uniform in the choice of the two geometries.

**4. Critical inverse limit.** Fix \(r,s>0\), put \(m_n=\lfloor rn\rfloor+1\) and choose \(\theta_n=\operatorname{arcosh}(e^{s/n})\), so \(q_n=e^{-s/n}\) and \(\theta_n\sim\sqrt{2s/n}\). If \(c_n\sqrt n\to\gamma<\infty\), then
\[
\frac{m_n}{n}\to r,\qquad m_nu_n\to\gamma r\sqrt{2s},\qquad
\frac{u_n}{\theta_n}=c_n\to0,\qquad m_nu_n^2\to0.
\]
Equations (1)--(3) show that
\[
\mathbb E\exp(-sS_{m_n}/n)\to\exp\{-rs-\gamma r\sqrt{2s}\}.\tag{4}
\]
Let \(H_a\) be the first passage time of standard Brownian motion to level \(a\ge0\), with \(H_0=0\). Its Laplace transform is \(\mathbb E e^{-sH_a}=e^{-a\sqrt{2s}}\). Laplace uniqueness in (4) establishes \(S_{m_n}/n\Rightarrow r+H_{\gamma r}\).

**5. Inversion and explicit distribution.** Since the range is integer-valued, nondecreasing and advances by steps of one,
\[
\Pr(R_n\le k)=\Pr(S_{k+1}>n).\tag{5}
\]
For \(0<r<1\) and \(\gamma>0\), the law of \(r+H_{\gamma r}\) is continuous at one. Using (4)--(5) and the reflection principle gives
\[
\lim_{n\to\infty}\Pr(R_n/n\le r)
=\Pr(H_{\gamma r}>1-r)
=2\Phi\!\left(\frac{\gamma r}{\sqrt{1-r}}\right)-1.
\]
The limits at either boundary are zero and one. When \(\gamma=0\), (4) instead gives \(S_{m_n}/n\to r\) in probability; applying (5) for every \(r<1\), together with \(R_n\le n\), proves \(R_n/n\to1\) in probability. Differentiating the distribution function gives the stated density.

**6. The weak-weight diffusive-side limit.** Suppose \(c_n\to0\) and \(c_n\sqrt n\to\infty\). For fixed \(r,s>0\) take \(m_n=\lfloor r\sqrt n/c_n\rfloor+1\), with the same \(\theta_n\). Then
\[
\frac{m_n}{n}\to0,\qquad m_nu_n\to r\sqrt{2s},\qquad
u_n/\theta_n=c_n\to0,\qquad m_nu_n^2\to0.
\]
Equations (1)--(3) imply \(\mathbb E e^{-s S_{m_n}/n}\to e^{-r\sqrt{2s}}\), so \(S_{m_n}/n\Rightarrow H_r\). Applying (5) yields, for every \(r>0\),
\[
\lim_{n\to\infty}\Pr(c_nR_n/\sqrt n\le r)
=\Pr(H_r>1)=2\Phi(r)-1.
\]
This is the distribution function of \(|N|\), completing both regimes and their geometry-independent limits.

## Verification

The standalone `checker.py` runs using only the Python standard library. It independently enumerates the finite-time walk states and the waiting-time renewal process for both geometries, using exact rational probabilities; it also compares finite-state discounted hitting equations with the gambler's ruin transform. The full run reproduced **608 assertions**. Deterministic numerical convergence checks of the product in (1) supplement these exact checks, for both scaling regimes and both boundary conditions. Execute `python checker.py` and compare with `checks.txt`. These tests are not substitutes for the analytic limit proof above.

## Relationship to prior work

Hu, Ma, Song and Wang (2026) obtain all fixed-positive-weight range moment asymptotics on the reflected half-line. Pfaffelhuber and Stiefel (2019/2020) develop the corresponding full-line inverse-range decomposition and fixed-weight range moments. Hu, Song and Wang (2026) establish iterated-logarithm results for the full-line range at fixed positive weight. Serlet (2013, 2018) develops exact hitting-time and record laws and fixed-parameter invariance principles for perturbed walks, a closely related literature whose full texts were not available for complete comparison. The waiting-time representation is inherited from these works; the result proved here instead analyzes **triangular families with weight tending to zero**, identifies the sharp \(n^{-1/2}\) boundary, proves the distributional crossover, and establishes a common limit for the two geometries despite their different fixed-weight constants. Generic inverse-stable-subordinator theory identifies the *limiting law* after its Laplace transform is established, but does not supply the triangular-array transform or its connection to these two reinforced walks.

## Limitations

No convergence rate, almost-sure limit, position-process scaling limit, or extension to general graphs is established. The weak-weight half-normal conclusion requires both \(c_n\to0\) and \(c_n\sqrt n\to\infty\); it is not claimed for a fixed positive weight. The full-line and half-line limit laws coincide in the two stated regimes, not in the general fixed-positive-weight regime. Earlier work on weakly repulsive walks, particularly Serlet's perturbed-walk results, could potentially use equivalent language; those two full texts were inaccessible and historical priority has not been independently confirmed.

## References

1. Z. Hu, T. Ma, R. Song and L. Wang, *The range of once-reinforced random walk on the half-line*, arXiv:2602.10721v1, first posted 11 February 2026. https://arxiv.org/abs/2602.10721
2. P. Pfaffelhuber and J. Stiefel, *The range of once-reinforced random walk in one dimension*, arXiv:1903.05234, first posted 12 March 2019; Random Structures & Algorithms 58 (2021), 164–175. https://arxiv.org/abs/1903.05234 ; https://doi.org/10.1002/rsa.20948
3. Z.-C. Hu, R. Song and L. Wang, *Laws of the iterated logarithm for the range of once-reinforced random walk on \(\mathbb Z\)*, arXiv:2610.36790v1, 27 October 2026. https://arxiv.org/abs/2610.36790
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. I, 3rd ed., Wiley, 1968 (gambler's ruin and Brownian first passage).
5. L. Serlet, *Hitting times for the perturbed reflecting random walk*, Stochastic Processes and their Applications 123 (2013), 110–130. https://doi.org/10.1016/j.spa.2012.09.003
6. L. Serlet, *Explicit Laws for the Records of the Perturbed Random Walk on \(\mathbb Z\)*, Séminaire de Probabilités XLIX, Lecture Notes in Mathematics 2215 (2018), 495–519. https://doi.org/10.1007/978-3-319-92420-5_14
