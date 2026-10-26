# Unique Gaussian-coverage crossover and sharp normal-approximation constants for partial-reset Brownian motion

## Finding

For a stationary driftless Brownian motion with Poissonian proportional resetting, standardized to mean zero and variance one, the probability of a symmetric interval differs from the corresponding standard-normal probability in a remarkably rigid way: **for every reset contraction strictly between zero and one, the difference changes sign exactly once as the interval radius increases.** Small intervals have *greater* coverage than the Gaussian comparator, while sufficiently large intervals have *smaller* coverage. As resetting becomes weak, this sole crossover converges to \(\sqrt3\), corresponding to central Gaussian coverage \(2\Phi(\sqrt3)-1=0.916735483336\ldots\).

The approximation can be quantified sharply in two probability metrics. For \(0<a<1\), put
\[
q=a^2,\qquad s_a=\frac{1-q}{1+q},\qquad
u=\sqrt{3-\sqrt6},\qquad v=\sqrt{3+\sqrt6}.
\]
Let \(f_a\) and \(F_a\) denote the density and distribution function of the standardized stationary position, and let \(\varphi\) and \(\Phi\) be the standard normal density and distribution function. As \(a\uparrow1\),
\[
\left\|f_a-\varphi-\frac{s_a}{8}(x^4-6x^2+3)\varphi\right\|_{L^1(\mathbb R)}=O(s_a^{3/2}),
\]
\[
\sup_{x\in\mathbb R}\left|F_a(x)-\Phi(x)+\frac{s_a}{8}(x^3-3x)\varphi(x)\right|=O(s_a^{3/2}).
\]
Consequently, with total variation defined as half the density \(L^1\) distance,
\[
\begin{aligned}
d_{\mathrm{TV}}(F_a,\Phi)&=\frac{\sqrt6}{4}\bigl(\nu\varphi(\nu)+v\varphi(v)\bigr)s_a+O(s_a^{3/2}),\\
d_{\mathrm K}(F_a,\Phi)&=\frac{\sqrt6}{8}\nu\varphi(\nu)s_a+O(s_a^{3/2}).
\end{aligned}
\]
Their strictly positive sharp leading constants are respectively \(0.1750375188018648\ldots\) and \(0.0688234799376024\ldots\). The crossover radius \(z_a\) satisfies \(z_a=\sqrt3+O(s_a^{1/2})\).

## Assumptions and scope

Fix a diffusion coefficient \(D>0\), a reset rate \(r>0\), and a proportional reset parameter \(0<a<1\). Between the jumps of an independent rate-\(r\) Poisson process, the real-valued state evolves by \(dX_t=\sqrt{2D}\,dW_t\). At each jump the state becomes \(aX_{t-}\). This process has a unique stationary law. Write \(X_a\) for a stationary draw and normalize
\[
Y_a=X_a\sqrt{\frac{r(1-a^2)}{2D}}.
\]
The law of \(Y_a\) is independent of \(D\) and \(r\); \(F_a(x)=\Pr(Y_a\le x)\). Define central-coverage discrepancy
\[
\Delta_a(z)=\Pr(|Y_a|\le z)-\Pr(|Z|\le z),\qquad z\ge0,
\]
where \(Z\sim N(0,1)\). The crossover is the unique \(z_a>0\) solving \(\Delta_a(z_a)=0\). It does not include the trivial equality at \(z=0\). All asymptotic error statements refer to \(a\uparrow1\) with no dependence on \(D\) or \(r\).

## Proof

**1. Invariant law and Gaussian variance mixture.** The stationary characteristic function \(\psi(t)\) obeys the generator identity
\[
0=-Dt^2\psi(t)+r\bigl(\psi(at)-\psi(t)\bigr),
\]
so repeated substitution and \(\psi(0)=1\) yield
\[
\psi_{X_a}(t)=\prod_{j=0}^{\infty}\left(1+\frac{D}{r}a^{2j}t^2\right)^{-1}.
\]
This is the established independent-Laplace representation for partial-reset Brownian diffusion; uniqueness of the invariant law also follows by coupling two trajectories with the same Brownian path and resets, whose difference is multiplied by \(a\) at each reset. Let \(E_j\) be iid unit-mean exponential variables and \(Z_j\) iid standard Gaussians, mutually independent. The Laplace identity \(\mathbb E[e^{it\sqrt{E_j}Z_j}]=(1+t^2/2)^{-1}\) gives
\[
Y_a\ \stackrel{d}=\ \sum_{j\ge0}\sqrt{(1-q)q^j E_j}\,Z_j
\ \stackrel{d}=\ \sqrt{V_a}\,Z,
\qquad V_a=(1-q)\sum_{j\ge0}q^j E_j,
\]
with \(Z\sim N(0,1)\) independent of \(V_a\). All sums converge in second mean and almost surely. Moreover,
\[
\mathbb EV_a=1,\quad
\operatorname{Var}(V_a)=\sum_{j\ge0}(1-q)^2q^{2j}=s_a,\quad
\mathbb E(V_a-1)^4=3s_a^2+6\frac{(1-q)^4}{1-q^4}.
\]
For any \(0<a<1\), \(V_a\) is nondegenerate and positive with \(\Pr(V_a>1)>0\).

**2. Exactly one central-coverage crossover.** For \(y\ge0\), divide the mixture density by the unit-normal density at \(x=\sqrt{2y}\):
\[
R_a(y)=\frac{f_a(\sqrt{2y})}{\varphi(\sqrt{2y})}
=\mathbb E\left[V_a^{-1/2}\exp\left(y\left(1-\frac1{V_a}\right)\right)\right].
\]
The expectation is finite, since \(V_a\) dominates a positive multiple of \(E_0\), so \(\mathbb EV_a^{-1/2}<\infty\). It is strictly convex on \((0,\infty)\): the integrand is an exponential affine function of \(y\), with nonzero slope except on the null event \(V_a=1\). Jensen's strict inequality gives \(R_a(0)=\mathbb EV_a^{-1/2}>1\). For some \(\eta>0\), \(\Pr(V_a>1+\eta)>0\), whence \(R_a(y)\to\infty\) as \(y\to\infty\). But \(f_a\) and \(\varphi\) are distinct probability densities with the same total integral; therefore \(R_a(y)<1\) for at least one \(y\). Strict convexity implies that \(R_a-1\) has exactly two zeros: the sign pattern of \(f_a(x)-\varphi(x)\) on the positive half-line is \(+,-,+\). The central-coverage difference \(\Delta_a(z)=2\int_0^z(f_a-\varphi)(x)\,dx\) thus first increases above zero, then decreases, then increases to zero from below. It crosses zero exactly once for \(z>0\), with \(\Delta_a(z)>0\) for \(0<z<z_a\) and \(\Delta_a(z)<0\) for \(z>z_a\).

**3. A uniform, integrable second-order expansion.** For \(v>0\), write \(g(v,x)=v^{-1/2}\varphi(x/\sqrt v)\) and \(U_a=V_a-1\). Scale differentiation gives the identities in \(L^1(\mathbb R)\)
\[
\partial_v g(1,\cdot)=\tfrac12(x^2-1)\varphi(x),\qquad
\partial_v^2g(1,\cdot)=\tfrac14(x^4-6x^2+3)\varphi(x).
\]
Furthermore \(\|\partial_v^3g(v,\cdot)\|_1\le Cv^{-3}\) for a finite universal constant \(C\), by scaling of Gaussian derivatives. On the event \(V_a\ge1/2\), Taylor's formula about \(v=1\) has an \(L^1\) remainder bounded by \(C|U_a|^3\). Its contribution is \(O(s_a^{3/2})\) by Hölder's inequality and the fourth central-moment formula in step 1.

For completeness, the complementary event is negligible at this precision. With \(w_0=1-q\) and \(w_j=w_0q^j\), the inequality \(x-\log(1+x)\le x^2/2\) for \(x\ge0\) and exponential Markov inequality at \(t=(2w_0)^{-1}\) give
\[
\Pr(V_a<1/2)\le\exp\left(-\frac1{4w_0}+\frac{s_a}{8w_0^2}\right)
\le\exp\left(-\frac1{8w_0}\right).
\]
Since \(-1<U_a<-1/2\) on this event, the \(L^1\)-norms of the density and its quadratic Taylor surrogate there are bounded by a constant times that probability. Thus, using \(\mathbb EU_a=0\),
\[
\|\mathbb Eg(V_a,\cdot)-g(1,\cdot)-\tfrac12s_a\partial_v^2g(1,\cdot)\|_1
=O(s_a^{3/2}),
\]
which is the stated density expansion. Integrating from \(-\infty\) to \(x\) gives its uniform distribution-function counterpart because
\[
\int_{-\infty}^x(t^4-6t^2+3)\varphi(t)\,dt=-(x^3-3x)\varphi(x).
\]

**4. Sharp metric constants and the interval threshold.** The zeros of \(H_4(x)=x^4-6x^2+3\) on the positive half-line are \(\nu\) and \(v\). Direct Gaussian integration gives
\[
\int_{\mathbb R}|H_4(x)|\varphi(x)\,dx
=4\sqrt6\bigl(\nu\varphi(\nu)+v\varphi(v)\bigr).
\]
Taking half the \(L^1\) norm in step 3 proves the total variation expression, including its sharp constant. The absolute maximum of \(H_3(x)\varphi(x)=(x^3-3x)\varphi(x)\) occurs at \(|x|=\nu\), because its other stationary radii are \(v\) and \(\nu\varphi(\nu)>v\varphi(v)\). Taking the supremum in the CDF expansion yields the Kolmogorov constant. For each fixed \(z>0\), the central-coverage expansion reads
\[
\Delta_a(z)=-\frac{s_a}{4}(z^3-3z)\varphi(z)+O(s_a^{3/2}).
\]
It is positive at every fixed \(z<\sqrt3\) and negative at every fixed \(z>\sqrt3\) for sufficiently weak resetting. By step 2, the unique crossover tends to \(\sqrt3\). Since the limiting coefficient has a simple root there, the uniform remainder gives \(z_a=\sqrt3+O(s_a^{1/2})\).

## Verification

The accompanying executable `VERIFY.py` checks the exact geometric cumulant sums, Hermite integrations, the numerical leading constants, and a sign-changing crossover calculated by independent characteristic-function inversion for \(a\in\{0,0.5,0.9,0.97\}\). The recorded output reports 62 successful checks. These are finite numerical checks; the all-parameter crossing and asymptotic error estimate are proved in the preceding analytical argument. Run with Python, NumPy and SciPy using `python VERIFY.py`.

## Relationship to prior work

Pierce (2022) solves proportional resetting by a pantograph equation, obtains the stationary law, and identifies weak-reset Gaussian behavior. Tal-Friedman, Roichman and Reuveni (2022) derive the exact independent-Laplace stationary sum and limiting Gaussian characteristic function. Both are credited foundations of step 1; neither source, including the explicit weak-reset analysis, states the unique **central-coverage crossover** or sharp total-variation and Kolmogorov coefficients. Assefa, Keller-Ressel and Palmowski (2026) derive general moment and cross-moment formulas for affine-reset polynomial processes, including the present family in principle; these formulas do not directly give distributional metric expansions or the sign classification. Tong, Trafimow and Chen (2026) give general probability-integral methods for symmetric normal scale mixtures; the inspected article does not state the current sharp constants or partial-reset threshold. General variance-mixture and Gaussian-derivative identities are standard, not claimed as new.

## Limitations

The model is driftless, one-dimensional, has a deterministic contraction and independent Poisson reset epochs. No claim is made for drift, random contraction factors, non-Poisson resets, nonstationary laws, or monotonicity of the crossover in \(a\). The sharp constants concern \(a\uparrow1\) only; the exact one-crossover property holds for every \(0<a<1\). Literature comparisons do not establish absolute priority against every uncatalogued work. Independent mathematical validation has not been performed.

## References

1. J. K. Pierce, *An advection-diffusion process with proportional resetting* (2022), arXiv:2204.07215v1, https://arxiv.org/abs/2204.07215.
2. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting* (2022), arXiv:2205.03363, https://arxiv.org/abs/2205.03363.
3. J. Assefa, M. Keller-Ressel, and Z. Palmowski, *Moments of polynomial processes under affine resetting* (2026), arXiv:2610.01363v1, https://arxiv.org/html/2610.01363v1.
4. T. Tong, D. Trafimow, and X. Chen, *Beyond Normality: Gain-Probability Analysis for Symmetric Scale Mixture of Normal Distributions* (2026), https://doi.org/10.1111/anzs.70042.
