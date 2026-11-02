# Gaussian work fluctuations without finite exponential moments in an intermittent harmonic trap

## Finding

Consider the one-dimensional symmetric, randomly switched harmonic trap defined below. Let \(W_T\) denote the stochastic work injected by switches of the trapping potential over a stationary time interval of length \(T\). For all \(k,D,q>0\), the exact mean and long-time work variance are
\[
\mathbb E W_T=\frac{kD}{2}T,\qquad
\lim_{T\to\infty}\frac{\operatorname{Var}(W_T)}{T}
=\sigma^2=2D^2k+\frac{9D^2k^2}{4q}.
\]
Moreover,
\[
\frac{W_T-kDT/2}{\sqrt{T}}\ \Longrightarrow\ \mathcal N(0,\sigma^2).
\]
In sharp contrast to this central limit theorem, for every finite \(T>0\) and every real \(\theta\ne0\),
\[
\mathbb E\exp(\theta W_T)=+\infty.
\]
Every polynomial absolute moment of \(W_T\) is finite. Thus the typical Gaussian work fluctuations coexist with infinite exponential moments on both sides. As the switching rate decreases, the exact variance rate diverges like \(9D^2k^2/(4q)\), although the mean rate stays independent of \(q\).

## Assumptions and scope

Let \((S_t)_{t\in\mathbb R}\) be a stationary two-state continuous-time Markov chain taking values \(0\) (trap off) and \(1\) (trap on), switching in either direction at rate \(q>0\). Let \(B\) be an independent two-sided Brownian motion. The unique stationary solution of
\[
dX_t=-kS_tX_t\,dt+\sqrt{2D}\,dB_t
\]
exists for all \(D,k>0\). The potential is \(U_t=kS_t X_t^2/2\). Define work with the stochastic-energetics convention of counting changes of the external potential *only*, at the actual switching times:
\[
W_T=\frac{k}{2}\sum_{0<t\le T}(S_t-S_{t-})X_t^2.
\]
The process starts in the joint stationary distribution, and all statements use the physical time variable, not a discrete switch-count clock. The symbol \(k\) denotes the on-state relaxation rate, in units where mobility is incorporated into the harmonic stiffness.

## Proof

**Stationarity and moments.** A stationary stochastic convolution is
\[
X_t=\sqrt{2D}\int_{-\infty}^{t}
\exp\!\left(-k\int_u^t S_v\,dv\right)dB_u.
\]
The occupation fraction of the on state tends almost surely to one half on long intervals, ensuring convergence of the convolution. Brownian nondegeneracy, irreducibility of \(S\), and contraction over recurrent on intervals give uniqueness and ergodicity. The stationary transforms below establish finiteness of every polynomial positional moment.

Write \(\alpha=q/(2k)\) and \(\phi_s(u)=\mathbb E[e^{uX_0}\mathbf1_{\{S_0=s\}}]\). For \(|u|<\sqrt{q/D}\), the stationary generator equations are
\[
0=Du^2\phi_0+q(\phi_1-\phi_0),\quad
0=Du^2\phi_1-ku\phi_1'(u)+q(\phi_0-\phi_1),
\]
with \(\phi_0(0)=\phi_1(0)=1/2\). Their normalized solution is
\[
\phi_s(u)=\frac12\exp\left(\frac{Du^2}{2k}\right)
\left(1-\frac{Du^2}{q}\right)^{-\alpha-1+s}.
\]
Equivalently, conditional on \(S_0=s\),
\[
X_0\ \stackrel{d}{=}\ G+\sqrt{D/q}(A_s-B_s),
\]
where \(G\sim\mathcal N(0,D/k)\) and \(A_s,B_s\) are independent unit-scale gamma variables of common shape \(\alpha+1-s\), independent of \(G\). This also identifies the exact boundary of the *linear* moment-generating function: it is finite precisely for \(|u|<\sqrt{q/D}\).

**Mean work.** The generator of the joint diffusion and switching process is
\[
(\mathcal Lf)_s(x)=D\partial_{xx}f_s(x)-ksx\partial_xf_s(x)
+q[f_{1-s}(x)-f_s(x)].
\]
With \(a=\mathbb E[X_0^2\mathbf1_{\{S_0=0\}}]\) and \(b=\mathbb E[X_0^2\mathbf1_{\{S_0=1\}}]\), the stationarity equations are
\[
D+q(b-a)=0,\qquad D-2kb+q(a-b)=0.
\]
Hence \(a=D/k+D/q\) and \(b=D/k\). The compensator of switch work has density \(g(s,x)=qk(1-2s)x^2/2\). Therefore \(\mathbb E[g(S_0,X_0)]=qk(a-b)/2=kD/2\), giving the exact finite-time mean.

**Variance and central limit theorem.** Define
\[
h_0(x)=\frac{kx^2}{2},\qquad h_1(x)=-\frac{kD}{2q},\qquad c=\frac{kD}{2}.
\]
Direct substitution yields the Poisson identity \(\mathcal Lh=c-g\) in each switching state. Consequently,
\[
M_T=W_T-cT+h(X_T,S_T)-h(X_0,S_0)
\]
is a centered square-integrable martingale. Its switch jumps are the bounded constants \(-kD/(2q)\) when the trap turns on and \(+kD/(2q)\) when it turns off; its continuous martingale coefficient is \(\sqrt{2D}\,kX_t\mathbf1_{\{S_t=0\}}\). Thus its predictable quadratic variation is exactly
\[
\langle M\rangle_T
=2Dk^2\int_0^T X_t^2\mathbf1_{\{S_t=0\}}\,dt
+\frac{k^2D^2}{4q}T.
\]
By ergodicity, \(\langle M\rangle_T/T\) converges almost surely and in mean to
\[
2Dk^2a+\frac{k^2D^2}{4q}
=2D^2k+\frac{9D^2k^2}{4q}=\sigma^2.
\]
The jumps satisfy the martingale Lindeberg condition automatically because their sizes are fixed. The martingale central limit theorem gives \(M_T/\sqrt T\Rightarrow\mathcal N(0,\sigma^2)\). The stationary boundary correction \(h(X_T,S_T)-h(X_0,S_0)\) is uniformly bounded in \(L^2\) (the fourth positional moment is finite), so it disappears after dividing by \(\sqrt T\). Finally, \(\mathbb E[M_T^2]=\mathbb E\langle M\rangle_T=\sigma^2T\); Cauchy–Schwarz bounds covariance with the boundary correction by \(O(\sqrt T)\). The exact variance-rate limit follows.

**Divergence of every nontrivial exponential work moment.** Both stationary conditional laws of \(X_0\) have finite polynomial moments, but their linear moment generating functions diverge for sufficiently large \(|u|\), by the gamma-difference representation. If \(\mathbb E[e^{cX_0^2}\mid S_0=s]\) were finite for some \(c>0\), the bound \(ux\le cx^2+u^2/(4c)\) would force the entire linear moment-generating function to be finite, a contradiction. Hence
\[
\mathbb E[e^{cX_0^2}\mid S_0=s]=\infty
\quad\text{for both }s\in\{0,1\},\ c>0.
\]
For \(\theta>0\), restrict to paths initially off with exactly one switch at some time \(t\in(0,T)\). The switch is an off-to-on jump and \(W_T=kX_t^2/2\); before the jump, \(X_t=X_0+\sqrt{2D}B_t\). Jensen's inequality conditional on \(X_0\) bounds the exponential expectation below by \(e^{\theta kX_0^2/2}\), whose stationary expectation is infinite. The one-switch event has strictly positive probability density \(q e^{-qT}dt\), so this lower bound proves divergence.

For \(\theta<0\), use paths initially on with exactly one on-to-off switch. Now \(W_T=-kX_t^2/2\) and \(X_t=e^{-kt}X_0+G_t\) with centered Gaussian \(G_t\). Jensen yields the nonintegrable bound \(e^{|\theta|ke^{-2kt}X_0^2/2}\) for any \(t<T\). This proves divergence for negative \(\theta\) as well. All polynomial work moments remain finite, since the finite-time number of switches is Poisson, the stationary initial position has moments of every order, and the linear diffusion has bounded coefficients on finite time intervals.

## Verification

The accompanying `verify.py` is a standalone numerical and algebraic checker, requiring Python 3 with NumPy. Execute `python verify.py` after extracting it. It verifies four exact rational stationary-moment and variance identities, eighteen Fourier-transform generator identities, and three independently simulated stationary switching-diffusion cases with exact between-switch propagators. The simulations corroborate the variance rate but are not used as a proof. All limiting statements above are established analytically; the infinite exponential-moment statement uses a positive-probability one-switch event, not extrapolation from finite sampling.

## Relationship to prior work

Frydel's 2024 paper derives the model, stationary spatial distribution, and rate-independent energetic observables. Santra, Das and Nath (2021) study the same alternating confinement and its transport/first-passage properties. Alston, Cocconi and Bertrand (2022) investigate mean nonequilibrium thermodynamic observables of fluctuating potentials. Frydel's 2026 semi-Markovian extension treats arbitrary residence-time laws and derives mean injected power through the second moments of switching-state birth distributions. These sources provide the background stationary model and mean work; their inspected statements do not give the explicit integrated-work variance coefficient above, the joint central-limit and moment-generating-function distinction, or the two-sided finite-time exponential-moment obstruction. Classical Gaussian quadratic-functional and martingale theories are relevant general methods, but a general central limit theorem alone does not supply this variance coefficient or the nonexistence of exponential work moments. No claim of comprehensive publication-priority certification is made.

## Limitations

This theorem assumes symmetric Poisson switching, a single overdamped particle, harmonic stiffness alternating strictly between zero and \(k>0\), stationary initialization, and the switching-work convention above. The result does not cover asymmetric switching, nonlinear confinement, finite inertia, non-Poisson residence times, pathwise large-deviation principles, or a finite moment-generating function after truncation. The absence of a finite exponential work moment forbids a standard bilateral Cramér-generating-function treatment but does not by itself prove any particular large-deviation scaling. An independent audit and comprehensive publication-priority verification have not been performed.

## References

- D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (first posted 2024-07-16), https://arxiv.org/html/2407.12213v1.
- I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (2021), https://arxiv.org/abs/2104.00609.
- H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (2022), https://arxiv.org/abs/2202.02630.
- D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (2026), https://arxiv.org/abs/2607.05173.
- A. Pal and S. Sabhapandit, *Work fluctuations for a Brownian particle in a harmonic trap with fluctuating locations*, Phys. Rev. E 87, 022138 (2013), https://doi.org/10.1103/PhysRevE.87.022138 (different trap-center modulation model).
