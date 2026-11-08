# A logarithmic tail threshold for sublinear Brownian confinement with Poisson resets

## Finding

For a one-dimensional Brownian particle in a weak confining potential, Poisson resetting creates an exponential far tail, but the confining force leaves a second, sharply classified fingerprint. At the half-power confinement exponent, the stationary tail acquires an explicit **nontrivial power prefactor**; below it the residual prefactor tends to a positive constant, while above it a new stretched-exponential correction survives.

Precisely, let \(\rho_{\alpha,r}(x)\) be the normalized stationary density of the process described below. Put
\[
k=\sqrt{r/D},\qquad
V_\alpha(x)=\lambda\big((1+x^2)^{\alpha/2}-1\big),\qquad
F_\alpha(x)=\log\rho_{\alpha,r}(x)+kx+\frac{V_\alpha(x)}{2D}.
\]
For every fixed \(D,r,\lambda>0\) and \(0<\alpha<1\), as \(x\to+\infty\),

1. If \(0<\alpha<1/2\), \(F_\alpha(x)\) converges to a finite real constant. Equivalently, there exists \(A_\alpha\in(0,\infty)\) such that
\[
\rho_{\alpha,r}(x)\sim A_\alpha\exp\left(-kx-\frac{V_\alpha(x)}{2D}\right).
\]
2. If \(\alpha=1/2\), \(F_{1/2}(x)+\vartheta\log x\) converges to a finite real constant, where
\[
\vartheta=\frac{\lambda^2}{32D^2k}>0.
\]
Thus a constant \(A_{1/2}\in(0,\infty)\) exists with
\[
\rho_{1/2,r}(x)\sim A_{1/2}x^{-\vartheta}
\exp\left(-kx-\frac{V_{1/2}(x)}{2D}\right).
\]
3. If \(1/2<\alpha<1\), then
\[
\lim_{x\to\infty}\frac{F_\alpha(x)}{x^{2\alpha-1}}
=-\frac{\lambda^2\alpha^2}{8D^2k(2\alpha-1)}.
\]

The same statements hold with \(x\) replaced by \(|x|\) on the negative half-line. The assertions include the existence of positive leading prefactor constants at and below the boundary; no such exact constant is asserted for the supercritical, coarser log-asymptotic statement.

## Assumptions and scope

The unreset dynamics on \(\mathbb R\) are the nonexplosive diffusion
\[
dX_t=-V_\alpha'(X_t)\,dt+\sqrt{2D}\,dB_t
\]
with \(0<\alpha<1\), where \(B\) is a standard Brownian motion. Independently, a rate-\(r\) Poisson clock instantaneously sends the position to \(0\). All parameters are fixed while \(|x|\to\infty\). The potential is smooth, even, bounded below, and grows like \(\lambda |x|^\alpha\) at large distance. Units are chosen so the smoothing length is \(1\).

The stationary density exists uniquely. Indeed, if \(p_0(t;0,x)\) is the transition density without resets, then the regenerative resolvent
\[
\rho_{\alpha,r}(x)=r\int_0^\infty e^{-rt}p_0(t;0,x)\,dt
\]
is nonnegative, integrates to \(1\), and is invariant. This representation also gives strict positivity for every \(x\). Reset events regenerate the process, establishing uniqueness.

## Proof

**1. Exact stationary boundary-value equation.** On either open half-line, the stationary Fokker--Planck equation has no delta source:
\[
D\rho''+(V_\alpha'\rho)'-r\rho=0.
\]
The source at the origin imposes the derivative jump but does not modify the far-field equation. Symmetry makes the normalized density even.

**2. Exact ground-state transformation.** Put
\[
\psi(x)=e^{V_\alpha(x)/(2D)}\rho_{\alpha,r}(x).
\]
Direct differentiation, without approximation, yields
\[
\psi''(x)=Q(x)\psi(x),\qquad
Q(x)=k^2+\frac{V_\alpha'(x)^2}{4D^2}
-\frac{V_\alpha''(x)}{2D}.
\]
Here
\[
V_\alpha'(x)=\lambda\alpha x(1+x^2)^{\alpha/2-1},\quad
V_\alpha''(x)=\lambda\alpha(1+x^2)^{\alpha/2-2}
\big(1+(\alpha-1)x^2\big).
\]
In particular, as \(x\to\infty\),
\[
Q(x)=k^2+\frac{\lambda^2\alpha^2}{4D^2}x^{2\alpha-2}
+O(x^{\alpha-2})+O(x^{2\alpha-4}).
\]
Moreover \(Q(x)>k^2/2\) eventually, \(Q'(x)=O(x^{2\alpha-3})\), and \(Q''(x)=O(x^{2\alpha-4})\).

**3. Control of the decaying solution.** Fix a sufficiently large \(x_0>0\) and define
\[
w(x)=Q(x)^{-1/4}\exp\left(-\int_{x_0}^x\sqrt{Q(s)}\,ds\right).
\]
Its exact differential defect is
\[
\frac{w''-Qw}{w}
=\frac{5Q'(x)^2}{16Q(x)^2}-\frac{Q''(x)}{4Q(x)}.
\]
The defect is absolutely integrable on \([x_0,\infty)\); indeed, it is \(O(x^{2\alpha-4})\), and \(2\alpha-4<-2\). The standard Volterra comparison for the two separated exponential modes of \(y''=Qy\) (equivalently, the elementary Liouville--Green asymptotic theorem with integrable defect) therefore supplies a decaying solution \(\psi_-(x)=w(x)(1+o(1))\), with a positive scalar normalization.

The stationary \(\psi\) must be proportional to this decaying mode: the other independent solution grows at least as an exponential \(e^{cx}\), while \(e^{-V_\alpha/(2D)}\) removes only a sublinear exponential \(e^{-O(x^\alpha)}\); its presence would make \(\rho\) nonintegrable. Strict positivity of the resolvent and uniqueness of the decaying one-dimensional solution force a *strictly positive*, not zero, proportionality constant. Thus
\[
\log\rho_{\alpha,r}(x)
=-\frac{V_\alpha(x)}{2D}
-\int_{x_0}^x\sqrt{Q(s)}\,ds
-\frac14\log Q(x)+C+o(1)
\]
for a finite real \(C\). This is a multiplicative asymptotic, not merely a logarithmic upper bound.

**4. The critical integrability calculation.** Taylor expansion at \(k^2>0\) gives
\[
\sqrt{Q(x)}-k=
\frac{\lambda^2\alpha^2}{8D^2k}x^{2\alpha-2}
+O(x^{\alpha-2})+O(x^{4\alpha-4})+O(x^{2\alpha-4}).
\]
The terms \(x^{\alpha-2}\) and \(x^{2\alpha-4}\) are integrable for \(0<\alpha<1\); the \(x^{4\alpha-4}\) remainder is integrable whenever \(\alpha\le1/2\), and for \(\alpha>1/2\) its integral is \(o(x^{2\alpha-1})\). Also, \(\log Q(x)\) tends to \(\log(k^2)\).

The principal correction \(x^{2\alpha-2}\) is integrable precisely for \(\alpha<1/2\). At \(\alpha=1/2\) its integral is \(\log x\), with coefficient \(\lambda^2/(32D^2k)\). For \(1/2<\alpha<1\), its integral has leading order \(x^{2\alpha-1}/(2\alpha-1)\). Substitution into the asymptotic expression for \(\log\rho\) gives all three claims.

## Verification

The accompanying standalone `check.py` independently evaluates the *exact* derivatives of the potential, the transformed coefficient \(Q\), the local eikonal \(\sqrt Q\), and the logarithmic derivative \(y=-\psi'/\psi\) computed by numerically integrating its Riccati equation backwards from a distant boundary. It tests \(\alpha=1/3,1/2,2/3,0.82\) over multiple distances, including convergence of \(y-k\) to the first-order eikonal correction, and the exact half-power coefficient. It reports 106 passing finite diagnostic assertions.

The numerical checker does **not** establish the infinite-distance theorem. The proof's essential infinite step is the integrable-defect Volterra/Liouville--Green argument and the explicit integral classification.

Run using `python check.py`; the code requires Python 3 and SciPy.

## Relationship to prior work

Defaveri, Barkai and Kessler analyze the **unreset** weak-confined process and its long-time stretched-exponential relaxation; their stationary reference law is the equilibrium Boltzmann distribution and their spatial scaling concerns a different limit. Their supplementary Schrödinger/WKB treatment of excited states supplies an important methodological antecedent, which is credited rather than claimed new. The present theorem instead concerns the non-equilibrium *Poisson-reset stationary* resolvent and its far-spatial tail, including a correction invisible at leading exponential order.

Capała and Dybiec study resetting and a power-law confining force in a **first-passage escape** problem with an absorbing boundary; they do not establish the stationary full-line tail classification. Singh, Metzler and Sandev solve an exactly V-shaped, asymptotically linear trapping case, beyond the strict sublinear exponent range here.

Pal studies a general-potential stationary-reset framework and related classes; that general resolvent framework is credited and is not claimed new. De Mauro, Majumdar and Schehr (2026) study a commonly resetting Brownian gas under confinement, including \(\alpha\le1\) extreme-value scaling; their full text addresses the leading unconfined universality class rather than this stationary single-particle three-way, subleading spatial-tail law.

## Limitations

No statement is made about \(\alpha\ge1\), reset-rate limits \(r\to0\) taken jointly with \(x\to\infty\), spatially dependent reset rates, non-Poisson reset clocks, or higher dimensions. For \(1/2<\alpha<1\), the error term is relative to the *subleading* exponent \(x^{2\alpha-1}\); a positive multiplicative prefactor is not asserted.

The result uses a standard asymptotic ODE method in a specific stochastic-resetting physics problem; no new general Liouville--Green theorem is claimed. Its publication priority remains subject to comparison with further general-potential resolvent literature.

## References

- L. Defaveri, E. Barkai and D. A. Kessler, *Stretched-exponential relaxation in weakly-confined Brownian systems through large deviation theory*, arXiv:2309.13126 (first posted 2023-09-22), https://arxiv.org/abs/2309.13126.
- K. Capała and B. Dybiec, *Optimization of escape kinetics by reflecting and resetting*, arXiv:2305.14832 (2023), https://arxiv.org/abs/2305.14832.
- A. Pal, *Diffusion in a potential landscape with stochastic resetting*, Physical Review E 91, 012113 (2015), https://arxiv.org/abs/1408.1230.
- R. K. Singh, R. Metzler and T. Sandev, *Resetting dynamics in a confining potential*, Journal of Physics A 53, 505003 (2020), https://doi.org/10.1088/1751-8121/abc83a.
- G. de Mauro, S. N. Majumdar and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (2026), https://arxiv.org/abs/2606.31634.
