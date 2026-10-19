# Hidden fourfold anisotropy in an orthogonally switched harmonic trap

## Finding
A Brownian particle confined by two complementary, randomly interchanged harmonic stiffnesses has an exactly isotropic stationary covariance matrix, yet exhibits strictly negative covariance of its squared Cartesian coordinates and a strictly positive fourth angular harmonic. Both fourth-order signatures weaken strictly as the interchange rate increases.

More precisely, for the stationary process defined below, put \(T=k(k+\sigma)-a^2\) and \(U=2(k^2-a^2)+k\sigma\). For every \(k>a>0\), \(\sigma>0\) and \(D>0\),
\[
\mathbb E[X^2]=\mathbb E[Y^2]=\frac{D(k+\sigma)}{T},\qquad \mathbb E[XY]=0,
\]
\[
\boxed{\operatorname{Cov}(X^2,Y^2)=-\frac{D^2a^2(k+\sigma)}{kT^2}<0},
\]
and
\[
\boxed{H_4:=\mathbb E[X^4-6X^2Y^2+Y^4]=\frac{12D^2a^2(2k+\sigma)}{kUT}>0}.
\]
The latter is the fourth angular harmonic \(\mathbb E[(X^2+Y^2)^2\cos(4\theta)]\) under polar coordinates away from the origin. Moreover, \(\operatorname{Cov}(X^2,Y^2)\) increases strictly toward zero with \(\sigma\), while \(H_4\) decreases strictly toward zero. Their fast-switching scaling is
\[
\lim_{\sigma\to\infty}\sigma\operatorname{Cov}(X^2,Y^2)=-\frac{D^2a^2}{k^3},\qquad
\lim_{\sigma\to\infty}\sigma H_4=\frac{12D^2a^2}{k^3}.
\]

## Assumptions and scope
Let \(S_t\) be an autonomous continuous-time Markov chain on \(\{-1,+1\}\), with each state switching to the other at rate \(\sigma>0\). Let \(W^{(1)},W^{(2)}\) be independent standard Brownian motions, independent of \(S\). Consider on the whole real plane
\[
\begin{aligned}
 dX_t&=-(k+aS_t)X_t\,dt+\sqrt{2D}\,dW_t^{(1)},\\
 dY_t&=-(k-aS_t)Y_t\,dt+\sqrt{2D}\,dW_t^{(2)}.
\end{aligned}
\]
Here \(k>a>0\) ensures uniform confining curvature, and \(D>0\) is translational diffusivity. Both stiffness eigenvalues are positive. Expectations refer exclusively to the unique stationary joint law of \((X,Y,S)\). The axes do not physically rotate continuously: their larger and smaller stiffnesses are interchanged at telegraph switching events. There is no direct coordinate interaction; their dependence arises through the shared switching chain.

## Proof
**Existence, finite moments, and symmetries.** Construct the stationary solution using a bi-infinite stationary switching chain and independent two-sided Brownian motions:
\[
X_t=\sqrt{2D}\int_{-\infty}^{t}\exp\!\left(-\int_u^t(k+aS_v)\,dv\right)dW^{(1)}_u,
\]
with the analogous expression for \(Y_t\) using \(k-aS_v\). Since each damping coefficient is at least \(k-a>0\), these integrals converge and have moments of every finite order. Coupling from any two initial coordinates contracts at least at rate \(k-a\), giving uniqueness. Sign reversals of each Brownian noise independently imply vanishing odd-coordinate means and \(\mathbb E[XY]=0\). The transformation interchanging the two coordinate axes and changing \(S\) to \(-S\) preserves the stationary law, yielding equal even marginal moments.

**Second moments.** Define \(m=\mathbb E[X^2]\) and \(b=\mathbb E[SX^2]\). Stationarity of the diffusion-plus-switching generator gives
\[
0=-2km-2ab+2D,\qquad 0=-2(k+\sigma)b-2am.
\]
(The telegraph generator acts on \(S\) as \(-2\sigma S\).) Thus \(b=-am/(k+\sigma)\) and
\[
m=\frac{D(k+\sigma)}{T},\qquad T=k(k+\sigma)-a^2>0.
\]

**Mixed and fourth moments.** Put \(V=\mathbb E[X^2Y^2]\), \(M=\mathbb E[X^4]\), and \(c=\mathbb E[SX^4]\). The drift of \(X^2Y^2\) is \(-4kX^2Y^2\) regardless of the switching state: the opposite anisotropies cancel. Its diffusion terms contribute \(2D(X^2+Y^2)\). Consequently,
\[
0=-4kV+4Dm,\qquad V=\frac{Dm}{k}.
\]
Similarly, the \(X^4\) and \(SX^4\) stationary equations are
\[
0=-4kM-4ac+12Dm,
\]
\[
0=-(4k+2\sigma)c-4aM+12Db.
\]
Eliminating \(c\) and inserting \(b=-am/(k+\sigma)\) yields, with \(U=2(k^2-a^2)+k\sigma>0\),
\[
M=\frac{3D^2(2a^2+2k^2+3k\sigma+\sigma^2)}{UT}.
\]
The squared-coordinate covariance is \(V-m^2\); inserting the formulas and simplifying gives
\[
V-m^2=\frac{D^2(k+\sigma)}{kT}-\frac{D^2(k+\sigma)^2}{T^2}=-\frac{D^2a^2(k+\sigma)}{kT^2}.
\]
Axis-exchange symmetry gives \(\mathbb E[Y^4]=M\). Consequently \(H_4=2M-6V\), and algebra reduces it to the stated strictly positive expression. All moment equations are justified by the already established finite moments and stationarity. The identity \(X^4-6X^2Y^2+Y^4=(X^2+Y^2)^2\cos(4\theta)\) proves the angular interpretation, without assuming a density formula.

**Strict switching-rate monotonicity and boundaries.** Direct differentiation gives
\[
\frac{\partial}{\partial\sigma}\operatorname{Cov}(X^2,Y^2)=\frac{D^2a^2(a^2+k^2+k\sigma)}{kT^3}>0.
\]
For the positive angular harmonic,
\[
\frac{\partial}{\partial\sigma}\log H_4
=\frac{1}{2k+\sigma}-\frac{k}{U}-\frac{k}{T}<0,
\]
because \(U=2(k^2-a^2)+k\sigma<k(2k+\sigma)\), so its first two terms already have a strictly negative sum. Taking the rational limits proves the fast-switching laws. Also, as \(\sigma\downarrow0\), the two signatures tend respectively to \(-D^2a^2/(k^2-a^2)^2\) and \(12D^2a^2/(k^2-a^2)^2\). The latter are one-sided limits; at exactly zero switching, stationary uniqueness does not hold for the switching state.

## Verification
The accompanying `check.py` uses Python's standard-library exact rational arithmetic. It verifies the closed-form stationary generator identities, the covariance and harmonic identities, positivity, finite-grid strict monotonicity, and an exact test case. It reports 4,055 passed exact-rational assertions. At \((k,a,\sigma,D)=(2,1,1,1)\), the exact outputs are \(m=3/5\), \(V=3/10\), \(M=51/40\), \(\operatorname{Cov}(X^2,Y^2)=-3/50\), and \(H_4=3/4\). Universal quantification follows from the displayed analytic arguments, not the finite check grid. Reproduce with `python3 check.py` after extracting this package.

## Relationship to prior work
Biroli, Kulkarni, Majumdar, and Schehr (arXiv:2312.02570, first public 2023-12-05) derive the stationary state of noninteracting Brownian particles driven by a **common scalar** fluctuating harmonic stiffness. Their conditional coordinate variances are identical, which yields nonnegative squared-coordinate dependence. The present model instead alternates **complementary directional stiffnesses**: it has a negative squared-coordinate covariance and a nonzero fourth angular harmonic despite an isotropic covariance matrix. Thus it is not the scalar-stiffness case treated in that source, nor a corollary of its common-variance mixture formulas. The broader discussion in Majumdar and Schehr (arXiv:2603.03162) again addresses shared stochastic environments and does not in its inspected text state this complementary-axes moment theorem. The proof uses standard Markov-modulated Ornstein–Uhlenbeck generator methods rather than asserting a new general moment method.

## Limitations
The result applies to a two-dimensional diagonal trap whose orthogonal stiffnesses interchange at a symmetric Poisson rate, and to independent isotropic Gaussian thermal noises. No claim is made for arbitrary rotations, asymmetric switching, nonlinear potentials, colored noise, or multiple particles. Isotropic **second** moments do not imply a radially symmetric distribution. No finite-sample detector performance or entropy-production formula is established. Wider general theorems on Markov-modulated linear diffusions may yield the identities as special cases; an independent literature-priority examination, including uninspected supplements of closely related publications, is still warranted.

## References
- M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first posted 2023-12-05). https://arxiv.org/html/2312.02570v1
- S. N. Majumdar, G. Schehr, *Dynamically Emergent Correlations*, arXiv:2603.03162 (2026). https://arxiv.org/html/2603.03162v1
- I. Santra, S. Das, S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (2021). https://arxiv.org/abs/2104.00609
