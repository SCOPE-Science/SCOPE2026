# A square-root search barrier and a finite-speed optimum for telegraph-modulated resetting

## Finding

Let a Brownian particle with diffusivity \(D>0\) begin at zero and be absorbed on its first arrival at a point \(a>0\). Its instantaneous resetting intensity is modulated by an independent, stationary, symmetric two-state continuous-time Markov chain with transition rate \(\nu>0\): in phase \(0\), the intensity is zero; in phase \(1\), it is \(\rho>0\). A reset returns the particle to zero **without resetting the phase**. Write \(T_\nu\) for the absorption time when the initial phase has its stationary probabilities \((1/2,1/2)\), and \(M(\nu)=\mathbb E T_\nu\).

Define the positive-definite matrix and its matrix functions
\[
B_\nu=\begin{pmatrix}\nu&-\nu\\-\nu&\nu+\rho\end{pmatrix},\qquad
E_\nu=\exp\!\left[-a\sqrt{B_\nu/D}\right],\qquad
H_\nu=(I-E_\nu)B_\nu^{-1}.
\]
With \(\mathbf 1=(1,1)^\top\), put \(e=E_\nu\mathbf1\), \(h=H_\nu\mathbf1\), and index their components by phases \(0,1\). The *exact* phase-resolved mean first-passage times, each starting at position zero, are
\[
\boxed{m_1(0)=\frac{h_1}{e_1},\qquad
m_0(0)=h_0+(1-e_0)\frac{h_1}{e_1},\qquad
M(\nu)=\tfrac12[m_0(0)+m_1(0)].}
\]
The denominator \(e_1\) is strictly positive for all positive parameters.

Let
\[
\mathcal T(s)=\frac{e^{a\sqrt{s/D}}-1}{s},\qquad
z=a\sqrt{\frac{\rho}{2D}}.
\]
As the environmental switching rate tends to either endpoint, the exact two-phase result has the asymptotics
\[
\boxed{M(\nu)=\frac{a}{2\sqrt{D\nu}}+O(1)\quad(\nu\downarrow0),}
\]
\[
\boxed{M(\nu)=\mathcal T(\rho/2)-\frac{\rho^2}{8\nu}\mathcal T'(\rho/2)+O(\nu^{-2})\quad(\nu\to\infty).}
\]
All \(O\)-constants depend on the fixed parameters \(a,D,\rho\). In particular, the slow-switching divergence is a square-root singularity, although \(M(\nu)<\infty\) at every \(\nu>0\).

The derivative has the exact sign formula
\[
\mathcal T'(s)=\frac{1+e^u(u/2-1)}{s^2},\qquad u=a\sqrt{s/D}.
\]
Let \(z_*\) be the unique strictly positive solution of \(z_*=2(1-e^{-z_*})\) (numerically \(z_*\approx1.593624260\)). If \(z>z_*\), then \(M(\nu)<\mathcal T(\rho/2)\) for every sufficiently large finite \(\nu\). Together with the slow-switching divergence and continuity, this **proves existence of at least one globally minimizing finite switching rate** \(0<\nu_*<\infty\). If \(0<z<z_*\), the large-\(\nu\) approach instead lies strictly above \(\mathcal T(\rho/2)\); no global absence of a finite optimum is asserted in that regime. No uniqueness assertion for \(\nu_*\) is made.

## Assumptions and scope

The initial position is exactly \(X_0=0\), while the independent phase chain starts in its invariant distribution. Between events, \(dX_t=\sqrt{2D}\,dW_t\) on \(( -\infty,a)\) with absorption at \(a\). Phase changes occur at rate \(\nu\) in both directions and do not affect position. Conditional on the phase trajectory, resetting is Poisson with predictable intensity \(\rho\mathbf1_{\{J_t=1\}}\); resets set \(X_t=0\) and **leave \(J_t\) unchanged**. The target is always active. All parameters \(D,a,\rho,\nu\) are strictly positive. There is no immobile refractory interval. Means are unconditional over both Brownian and phase/reset randomness.

The matrix square root is the principal positive-definite square root. For clarity, the full formula applies phase by phase, not solely after averaging; the square-root slow-switching prefactor \(a/(2\sqrt D)\) specifically uses the stationary initial phase probabilities.

## Proof

**1. Finite expectation and backward equation.** For fixed \(\nu>0\), the phase chain enters the active phase in finite mean time. There is uniformly positive probability on a bounded time interval that it remains active long enough for a reset to occur and, after that reset, the Brownian particle hits the target before either the next reset or phase change. By repeating fixed-length blocks and the strong Markov property, the absorption time has a uniformly bounded mean over all initial positions below the target and both phases. Its backward equations therefore admit the bounded probabilistic solution \(m_j(x)=\mathbb E_{x,j}T_\nu\), uniquely among bounded solutions, with \(m_j(a)=0\):
\[
D m_0''+\nu(m_1-m_0)=-1,
\qquad
D m_1''+\nu(m_0-m_1)+\rho[m_1(0)-m_1(x)]=-1.
\]
The nonrenewal condition appears in the latter term: the resetting phase does **not** redraw when position resets.

**2. Exact matrix formula.** Put \(m=(m_0,m_1)^\top\) and \(e^{(1)}=(0,1)^\top\). The system is
\[
D m''-B_\nu m=-\mathbf1-\rho e^{(1)}m_1(0).
\]
Both eigenvalues of \(B_\nu\) are strictly positive since its trace and determinant are \(2\nu+\rho>0\) and \(\nu\rho>0\). The unique bounded solution with the absorbing boundary is
\[
m(x)=\left(I-e^{-(a-x)\sqrt{B_\nu/D}}\right)
B_\nu^{-1}(\mathbf1+\rho e^{(1)}m_1(0)).
\]
The identity \(B_\nu^{-1}\rho e^{(1)}=\mathbf1\) converts its value at zero to \(m(0)=h+(\mathbf1-e)m_1(0)\), proving the displayed exact formula. The matrix exponential is positivity preserving on \(\mathbf1\) here: it is the Laplace transform at the absorbing boundary for a finite-state switching Brownian motion killed at phase-dependent rates; hence \(e_1>0\).

**3. Slow switching.** Write the eigenvalues as
\[
b_\pm=\nu+\rho/2\pm\sqrt{\nu^2+\rho^2/4},
\qquad P_\pm=\frac{B_\nu-b_\mp I}{b_\pm-b_\mp}.
\]
The small eigenvalue satisfies \(b_-=\nu+O(\nu^2)\), and its projector tends to the projection onto phase \(0\); the other eigenvalue tends to \(\rho\). In the spectral expansions
\[
E_\nu=\sum_{\sigma\in\{-,+\}}e^{-a\sqrt{b_\sigma/D}}P_\sigma,
\quad
H_\nu=\sum_{\sigma\in\{-,+\}}
\frac{1-e^{-a\sqrt{b_\sigma/D}}}{b_\sigma}P_\sigma,
\]
the low-eigenvalue factor is \(a/\sqrt{D\nu}+O(1)\). Thus \(h_0=a/\sqrt{D\nu}+O(1)\), \(h_1=O(1)\), \(e_1\to e^{-a\sqrt{\rho/D}}>0\), and \(e_0=1+O(\sqrt\nu)\). Substitution gives \(m_0(0)=a/\sqrt{D\nu}+O(1)\), \(m_1(0)=O(1)\) and the asserted average.

**4. Fast switching.** The small eigenvalue now satisfies
\[
b_-=\rho/2-\rho^2/(8\nu)+O(\nu^{-3}),
\qquad b_+=2\nu+O(1).
\]
The rows of \(P_-\mathbf1\) equal \(1+O(\nu^{-1})\), while those of \(P_+\mathbf1\) are \(O(\nu^{-1})\). Therefore the fast-mode contribution to \(H_\nu\mathbf1\) is \(O(\nu^{-2})\) and to \(E_\nu\mathbf1\) is exponentially small in \(\sqrt\nu\). Writing \(q=e^{-a\sqrt{b_-/D}}\) and \(h_*=(1-q)/b_-\), the exact formula yields, in **each** phase,
\[
m_j(0)=h_*/q+O(\nu^{-2})=\mathcal T(b_-)+O(\nu^{-2}).
\]
Taylor expansion around \(\rho/2\) proves the stated coefficient.

**5. Strict sign crossover and optimizer.** The sign of \(\mathcal T'(\rho/2)\) is the sign of \(g(z)=1+e^z(z/2-1)\). Here \(g(0)=0\) and \(g'(z)=e^z(z-1)/2\): it decreases on \((0,1)\), then increases to infinity, giving exactly one further zero \(z_*>1\). When \(z>z_*\), the fast-switching correction is strictly negative. Thus \(M\) takes a value strictly below its limit at infinity. Continuity of the matrix formula for \(\nu>0\), combined with divergence as \(\nu\downarrow0\), ensures that the global infimum is attained inside a compact positive switching-rate interval.

## Verification

Run `python verify.py` using Python's standard library. This reproduces both phase means by independent scalar spectral calculations, checks the reset-coupled boundary consistency for positive parameters, checks both singular asymptotic regimes and the optimizer-existence witness, and compares analytic means with independent continuous-time particle paths. In the latter test, each Brownian segment uses its exact first-hitting-time distribution and, upon survival to a competing reset/switch event, a rejection sampler from the **killed Brownian heat kernel** (rather than an Euler time grid). The embedded verifier passed 739 deterministic and statistical checks on the stated run, including 48,000 exact-segment sample trajectories. Monte Carlo is supplementary, not a proof of asymptotics or of existence.

For an illustrative non-boundary choice \(D=\rho=1\) and \(a=5\), \(M(0.3)\) is strictly below the fast-switching limit \(\mathcal T(1/2)\). The proof above, rather than that numerical witness, establishes existence whenever \(z>z_*\).

## Relationship to prior work

Arutkin and Reuveni (2025), *Diffusion with doubly stochastic resetting*, study a resetting intensity that refreshes independently of the particle, derive a spatial stationary law and explicitly identify fluctuating-intensity first passage as a further direction. Their arXiv HTML was examined through the exact renewal-rate model and conclusions, including their stationary transform. The present result is a target-hitting theorem for a particular two-valued independent refresh law, not a new derivation of their spatial stationary distribution.

Santra, Das and Nath (2021), *Brownian motion under intermittent harmonic potentials*, analyze switching between free diffusion and **continuous harmonic confinement** and report a switching-rate optimum for their distinct mechanism; the target-hitting discussion and refractory limit were examined. Their model has a confining drift (or an immobile refractory period in its singular limit), whereas here Brownian motion remains free in both phases and resets occur at a separate phase-dependent Cox intensity, without resetting the phase. Their qualitative optimum is not claimed as new; the new statement concerns the exact finite-speed criterion and square-root scaling for this different intensity mechanism.

Bressloff (2020), *Switching diffusions and stochastic resetting*, treats switching diffusivities with an externally imposed homogeneous resetting clock that also redraws the discrete state. Its accessible abstract and model description were compared: neither the phase-preserving, phase-dependent resetting intensity nor the derived fast-switching correction is a specialization of that setting. The full primary text was not accessible in this examination, a residual comparison limitation. General constant-rate Brownian restarting and the optimal-root value \(z_*\) are preexisting results and are used, not claimed as discoveries.

## Limitations

No claim is made about the uniqueness of a finite optimal modulation rate. The sign of the fast-switching correction below \(z_*\) is **not** a theorem ruling out finite-rate global minimizers there. At the equality \(z=z_*\), the leading correction vanishes and no sign is claimed. The model assumes two symmetric environmental phases, zero resetting in one phase, an independent Brownian driver, and an unbounded half-line geometry. The square-root coefficient applies to a stationary *initial environmental phase*, not to the active-phase-only initial condition. For other phase weights, nonzero rates in both phases, moving traps, reflecting geometries, or time-dependent targets, no extension is proved. Scientific priority is a best-knowledge statement, not an independent audit.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first public 2025-09-29), https://arxiv.org/html/2509.25365.
2. I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, J. Phys. A 54, 334001 (2021), arXiv:2104.00609, https://arxiv.org/html/2104.00609v2.
3. P. C. Bressloff, *Switching diffusions and stochastic resetting*, J. Phys. A 53, 275003 (2020), DOI:10.1088/1751-8121/ab97e0.
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106, 160601 (2011).
5. A. Pal, A. Kundu and M. R. Evans, *Diffusion under time-dependent resetting*, J. Phys. A 49, 225001 (2016), arXiv:1512.08211. (This resets based on age since the preceding reset, rather than an independently evolving intensity.)
