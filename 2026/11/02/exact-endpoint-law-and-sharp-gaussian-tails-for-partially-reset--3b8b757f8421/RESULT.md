# Exact endpoint law and sharp Gaussian tails for partially reset Ornstein–Uhlenbeck diffusion

## Finding
Fix \(\kappa,D,\rho>0\) and \(0<c<1\). The Ornstein–Uhlenbeck process with independent Poisson epochs of rate \(\rho\) at which its position is multiplied by \(c\) has a unique invariant distribution. Let \(v_\star=D/\kappa\) and \(\theta=\rho/(2\kappa)\).

Its invariant position \(X\) is conditionally Gaussian with random variance \(V\), and the variance has an *exact* right-endpoint law:
\[
\Pr(V\ge v_\star-w)=Cw^\theta,\qquad 0<w\le v_\star(1-c^2),
\]
where \(C=\mathbb E[(v_\star-c^2V)^{-\theta}]\) is finite and positive. The endpoint coefficient has an absolutely convergent power series in known rational functions of the model parameters:
\[
C=v_\star^{-\theta}\sum_{k=0}^\infty\frac{(\theta)_k}{k!}c^{2k}\prod_{j=1}^{k}\frac{2\kappa j}{2\kappa j+\rho(1-c^{2j})}.
\]
Empty products have value one and \((\theta)_k\) is the rising factorial. The stationary density and one-sided survival probability have sharp asymptotics, as \(x\to+\infty\):
\[
p(x)\sim\frac{C\Gamma(1+\theta)(2v_\star^2)^\theta}{\sqrt{2\pi v_\star}}x^{-2\theta}e^{-x^2/(2v_\star)},
\]
\[
\Pr(X>x)\sim\frac{C\Gamma(1+\theta)(2v_\star^2)^\theta\sqrt{v_\star}}{\sqrt{2\pi}}x^{-2\theta-1}e^{-x^2/(2v_\star)}.
\]
The negative tail is identical by symmetry. The *critical quadratic-exponential moment* has a reset-rate phase transition:
\[
\mathbb E e^{\eta X^2}
\begin{cases}
<\infty,&0\le\eta<1/(2v_\star),\\
<\infty\ \text{if and only if}\ \rho>\kappa,&\eta=1/(2v_\star),\\
=\infty,&\eta>1/(2v_\star).
\end{cases}
\]
In particular, the sharp Gaussian rate does not depend on \(c\), while the multiplicative polynomial exponent depends on the Poisson rate and the endpoint prefactor depends on the entire resetting law.

## Assumptions and scope
Between jumps the real-valued process solves \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dB_t\), with standard Brownian motion \(B\). Independently, a homogeneous Poisson process of rate \(\rho\) generates the jump map \(X_t=cX_{t-}\). The four parameters are fixed, deterministic, and in the ranges given above. The density means the Lebesgue density of the invariant probability measure. Every asymptotic is for fixed parameters as \(x\to\infty\), not uniform in the weak-reset scale.

## Proof
**1. Conditional normal representation and uniqueness.** Let \(N\) be a two-sided stationary Poisson process and let \(B\) be an independent two-sided Brownian motion. The unique stationary solution is the almost surely convergent stochastic convolution
\[
X=\sqrt{2D}\int_{-\infty}^0 e^{\kappa u}c^{N((u,0])}\,dB_u.
\]
The conditional variance is
\[
V=2D\int_0^\infty e^{-2\kappa t}c^{2N([-t,0])}\,dt\in(0,v_\star).
\]
It is strictly positive and strictly below \(v_\star\) almost surely because Poisson points occur in the infinite past and \(c<1\). Integrability follows from the deterministic bound \(V\le v_\star\). Two solutions driven by the same Brownian and Poisson paths have difference \(e^{-\kappa t}c^{N((0,t])}\) times their starting difference, converging to zero; this proves uniqueness of the invariant law.

**2. Exact endpoint law.** Let \(E\sim\operatorname{Exp}(\rho)\) be the age of the most recent jump. Conditioning on this jump and using the independent past gives the perpetuity
\[
V\stackrel{d}=v_\star(1-e^{-2\kappa E})+c^2e^{-2\kappa E}V',
\]
where \(V'\stackrel d=V\) is independent of \(E\). Put \(W=v_\star-V\) and \(B_\star=v_\star-c^2V'\). Then
\[
W\stackrel d=U B_\star,\qquad U=e^{-2\kappa E},\qquad \Pr(U\le u)=u^\theta\quad(0\le u\le1).
\]
Moreover, \(v_\star(1-c^2)\le B_\star\le v_\star\) almost surely. Consequently, for every \(0<w\le v_\star(1-c^2)\), conditioning on \(B_\star\) gives
\[
\Pr(W\le w)=\mathbb E\big[(w/B_\star)^\theta\big]=Cw^\theta,
\]
with \(0<C<\infty\). This identity is exact, not merely a limiting approximation.

**3. Explicit endpoint coefficient.** The variance process evolves between Poisson events by \(\dot V=2D-2\kappa V\), and jumps to \(c^2V\). Applying its stationary generator to powers of \(V/v_\star\) yields
\[
m_k=\mathbb E[(V/v_\star)^k]=\prod_{j=1}^{k}\frac{2\kappa j}{2\kappa j+\rho(1-c^{2j})},\qquad k\ge1.
\]
The expansion \((1-z)^{-\theta}=\sum_{k\ge0}(\theta)_kz^k/k!\), applied with \(z=c^2V/v_\star\le c^2<1\), proves the asserted convergent series for \(C\).

**4. Density and survival tails.** The exact endpoint law makes \(W\) absolutely continuous on \((0,w_0)\), with density \(C\theta w^{\theta-1}\), where \(w_0=v_\star(1-c^2)\). Fix an arbitrary \(0<\delta<w_0\) and split the normal-variance mixture according to \(W\le\delta\) or \(W>\delta\). Since \(V\le v_\star-\delta\) on the second event, its density contribution is exponentially negligible relative to \(e^{-x^2/(2v_\star)}\) times any inverse power of \(x\); this follows directly from the monotonicity of \(v^{-1/2}e^{-x^2/(2v)}\) in \(v\) whenever \(x^2>v_\star\). For the first event,
\[
p(x;W\le\delta)=\frac{C\theta}{\sqrt{2\pi}}\int_0^\delta\frac{w^{\theta-1}}{\sqrt{v_\star-w}}\exp\!\left[-\frac{x^2}{2(v_\star-w)}\right]dw.
\]
With \(t=x^2/(2v_\star^2)\), the identity
\[
\frac{x^2}{2(v_\star-w)}=\frac{x^2}{2v_\star}+tw+\frac{x^2w^2}{2v_\star^2(v_\star-w)}
\]
permits the substitution \(z=tw\) and dominated convergence. The limit integral is \(\Gamma(\theta)\), so the leading factor is \(C\Gamma(1+\theta)t^{-\theta}/\sqrt{2\pi v_\star}\). This proves the displayed density asymptotic. Integration of this asymptotic (or normal Mills' ratio uniformly for \(V\) near \(v_\star\)) gives the stated right-tail constant, with the extra factor \(v_\star/x\).

**5. Exact critical moment boundary.** For a centered normal with variance \(V\),
\[
\mathbb E[e^{\eta X^2}\mid V]=(1-2\eta V)^{-1/2}
\]
whenever \(2\eta V<1\), and the expectation is infinite otherwise. If \(\eta<1/(2v_\star)\), the conditional expectation is uniformly bounded. If \(\eta>1/(2v_\star)\), the variance lies above \(1/(2\eta)\) with positive probability, by the endpoint law. At \(\eta=1/(2v_\star)\), the expectation equals \(\mathbb E[(W/v_\star)^{-1/2}]\). Its integrability near zero is exactly that of \(\int_0^{w_0}w^{\theta-3/2}dw\), finite precisely for \(\theta>1/2\), equivalently \(\rho>\kappa\).

**6. Consequence for the weak-reset approximation.** Take \(c=1-s\), \(\rho=\lambda/s\) with \(0<s<1\) and \(\lambda>0\). Expanding the jump generator to second order gives the Itô approximation
\[
dY_t=-(\kappa+\lambda)Y_t\,dt+\sqrt{2D}\,dB_t+\sqrt{\lambda s}\,Y_t\,dW_t,
\]
with independent Brownian noises. The stationary zero-flux equation yields
\[
q_s(x)\propto(2D+\lambda sx^2)^{-1-(\kappa+\lambda)/(\lambda s)}.
\]
For every fixed positive \(s\), this approximate density has algebraic tails and lacks every strictly positive quadratic-exponential moment, whereas the original process has the sharp Gaussian-rate tail above. There is no contradiction: the small-jump expansion is not uniform in the simultaneous large-position limit.

## Verification
The independent exact-fraction checker `CHECK.py` verifies, in five parameter configurations and through moment order eight, equality of the stationary-generator moment recursion and an independently derived beta-perpetuity recursion. It also checks conditional-Gaussian moments and certified elementary bounds on the endpoint coefficient. The recorded `CHECK.out` contains 130 completed assertions. The full infinite-tail and critical-moment claims are proved analytically in Steps 2–5; numerical checks are not used in their place. Run the checker using `python3 CHECK.py` with the standard library.

## Relationship to prior work
Galla (2026, arXiv:2602.21635v1, Eq. (3)–(5)) derives and tests the weak-partial-reset diffusion approximation and provides the algebraic stationary density for linear drift. It does not give this exact fixed-reset stationary tail, its endpoint coefficient, or the quadratic-exponential boundary. Kolb and Wübker (2026) establish stationary and positivity-conditioned properties for **driftless** Brownian partial resetting, with a brief discussion of the Ornstein–Uhlenbeck analogue in their closing remarks; they do not present the stationary OU endpoint-variance theorem. Biroli et al. (2024) and Tal-Friedman et al. (2022) treat driftless diffusion under proportional resetting, whose invariant position distributions have exponential—not Gaussian—far tails. This finding uses their natural model family but its precise statement and consequences are for mean-reverting dynamics. Standard beta-product and Gaussian-mixture Laplace calculations are acknowledged as ingredients, not claimed independently as new methods.

## Limitations
The Gaussian tail and endpoint coefficient are pointwise for fixed \(\kappa,D,\rho,c\); no error estimates uniform as \(s\downarrow0\) are supplied. The process has scalar linear mean reversion, additive Brownian forcing, deterministic contractive reset factor and independent Poisson event times. General nonlinear drifts, correlated resets and random reset multipliers are not covered. The exact series and tail formula do not amount to a full elementary closed form for the invariant density. Independent scientific validation and a comprehensive historical-priority assessment are not yet performed; generalized Gaussian-mixture endpoint theorems could imply some parts of the claim.

## References
1. T. Galla, *A diffusion approximation for systems with frequent weak resetting* (2026), arXiv:2602.21635v1, https://arxiv.org/abs/2602.21635 . First public submission: 2026-02-25.
2. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, Bulletin of the London Mathematical Society 58 (2026), e70314, https://doi.org/10.1112/blms.70314 .
3. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one dimension*, Physical Review E 110 (2024), 044142, arXiv:2406.08387, https://arxiv.org/abs/2406.08387 .
4. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, Physical Review E 106 (2022), 054116, arXiv:2205.03363, https://arxiv.org/abs/2205.03363 .
