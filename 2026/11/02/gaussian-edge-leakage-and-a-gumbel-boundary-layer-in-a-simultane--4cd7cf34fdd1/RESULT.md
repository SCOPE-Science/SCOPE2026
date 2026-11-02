# Gaussian-edge leakage and a Gumbel boundary layer in a simultaneously reset Brownian gas

## Finding

Consider a gas of \(N\) independent one-dimensional Ornstein–Uhlenbeck particles in a harmonic trap. All particles are instantaneously reset to the origin at the same events of a Poisson clock. Although the leading stationary distribution of the maximum, divided by its natural \(\sqrt{\log N}\) scale, has compact support, the finite-population maximum retains positive probability beyond that limiting edge.

Write \(\mu>0\) for the drift-to-origin rate, \(D>0\) for diffusivity, \(r>0\) for the common reset rate, \(\sigma=\sqrt{D/\mu}\), and \(\beta=r/(2\mu)>0\). Let \(M_N\) be the maximum of the \(N\) stationary positions. Define \(L_N=\log N\), \(u_N=\Phi^{-1}(1-1/N)\) for \(N\ge3\), and the edge-layer coordinate
\[
Y_N=u_N\bigl(M_N/\sigma-u_N\bigr),
\]
where \(\Phi\) is the standard normal distribution function. Let \(G\) have the standard Gumbel distribution \(\Pr(G\le t)=\exp(-e^{-t})\).

**Theorem (finite-population edge and reset-age selection).** For every fixed \(x\in\mathbb R\),
\[
\boxed{\lim_{N\to\infty}(\log N)^\beta\Pr(Y_N>x)
=K_\beta(x):=\beta\int_0^\infty v^{\beta-1}
\bigl[1-\exp(-e^{-x-v})\bigr]dv
=\mathbb E(G-x)_+^\beta.}
\]
The constant is strictly positive and finite for every \(\beta>0\) and finite \(x\). The Gaussian extreme-value centering \(u_N\), including its logarithmic correction, is essential for this window.

Let \(A_N\) be the common time elapsed since the last reset in the stationary snapshot and put \(V_N=(\log N)e^{-2\mu A_N}\). Conditional on the rare event \(Y_N>x\),
\[
\boxed{\mathcal L(V_N\mid Y_N>x)\Longrightarrow
\frac{\beta v^{\beta-1}[1-\exp(-e^{-x-v})]}{K_\beta(x)}\,dv,
\qquad v>0.}
\]
Equivalently, the conditional reset age is localized at the \(\log\log N\) scale:
\[
2\mu A_N-\log\log N\ \Big|\ \{Y_N>x\}
\ \Longrightarrow\ -\log V_x,
\]
where \(V_x\) has the density in the previous display.

There is also a sharp nonzero **probability of crossing the nominal hard edge** of the leading compact-support law:
\[
\boxed{\lim_{N\to\infty}(\log N)^{\beta+1/2}
\Pr\!\left(M_N>\sigma\sqrt{2\log N}\right)
=\frac{\Gamma(\beta+1)}{\sqrt{4\pi}}.}
\]
In particular, the exponent of finite-population leakage is \(\beta+1/2\), not simply \(\beta\). The additional half-power comes from the Gaussian extreme tail at the uncorrected \(\sqrt{2\log N}\) edge.

The crossover function has the matching limits \(K_\beta(x)\sim(-x)^\beta\) as \(x\to-\infty\) and \(K_\beta(x)\sim\Gamma(\beta+1)e^{-x}\) as \(x\to+\infty\). For \(\beta=1\), \(K_1(0)=\gamma_{\mathrm E}+E_1(1)\), with \(\gamma_{\mathrm E}\) Euler's constant and \(E_1\) the exponential integral. These identities facilitate independent numerical checks.

## Assumptions and scope

For each fixed integer \(N\ge3\), the particles have independent Brownian drivers and, between the common reset times, solve
\[
dX_i(t)=-\mu X_i(t)\,dt+\sqrt{2D}\,dB_i(t),
\qquad i=1,\ldots,N.
\]
All coordinates jump simultaneously to zero at rate \(r\), independently of the Brownian paths. Parameters \(\mu,D,r\) are fixed while \(N\to\infty\); no weak-noise, weak-reset, or changing-trap scaling is assumed. The theorem concerns a stationary observation of the entire gas, not independent resetting clocks for individual particles. This finite-dimensional Markov process has a unique stationary distribution: two copies driven by the same Brownian paths and Poisson clock agree from the first common reset onward, giving a total-variation coupling bound \(e^{-rt}\).

The common reset age in stationarity is exponential with rate \(r\). Conditional on this age, positions are independent centered Gaussians with variance
\[
\sigma^2\bigl(1-e^{-2\mu A_N}\bigr).
\]
This conditional-independent representation, and the leading compact-support law for the rescaled maximum, are prior results. The claim here is restricted to the **sharp finite-population near-edge crossover, its conditional age law, and the explicit beyond-edge leakage amplitude**.

## Proof

**1. Exact reduction to a beta-weighted normal extreme.** Introduce independent standard normal variables \(Z_1,\ldots,Z_N\) and \(Z_{(N)}=\max_i Z_i\), independent of the exponential age \(A_N\). The Gaussian Ornstein–Uhlenbeck propagator gives
\[
M_N\stackrel d=\sigma\sqrt{1-e^{-2\mu A_N}}\,Z_{(N)}.
\]
With \(S_N=e^{-2\mu A_N}\), direct change of variables shows
\[
\Pr(S_N\le s)=s^\beta,\qquad 0<s<1,
\]
so \(S_N\) has density \(\beta s^{\beta-1}\). Therefore \(V_N=L_NS_N\) has the **exact** density
\[
f_{V_N}(v)=\beta L_N^{-\beta}v^{\beta-1}\mathbf1_{\{0<v<L_N\}}.
\]
The event \(Y_N>x\), given \(V_N=v\), has probability
\[
q_N(v,x)=1-\Phi\!\left(
\frac{u_N+x/u_N}{\sqrt{1-v/L_N}}
\right)^N.
\]
Consequently
\[
L_N^\beta\Pr(Y_N>x)
=\beta\int_0^{L_N}v^{\beta-1}q_N(v,x)\,dv.
\]
These are exact finite-\(N\) identities.

**2. Gaussian–Gumbel scaling.** The normal Mills ratio implies \(u_N^2/(2L_N)\to1\) and, for each fixed \(y\in\mathbb R\),
\[
\Phi(u_N+y/u_N)^N\longrightarrow\exp(-e^{-y}).
\]
For each fixed \(v\ge0\),
\[
u_N\left[\frac{u_N+x/u_N}{\sqrt{1-v/L_N}}-u_N\right]
=x+\frac{u_N^2}{2L_N}v+o(1)\longrightarrow x+v.
\]
Thus \(q_N(v,x)\to Q(x+v)\), where \(Q(t)=1-\exp(-e^{-t})\).

To justify passage under the noncompact integral, note that for \(t\ge u>0\),
\[
\frac{1-\Phi(t)}{1-\Phi(u)}
\le\exp\!\left[-\frac{t^2-u^2}{2}\right].
\]
Indeed, factor the normal tail as \(\phi(t)\int_0^\infty e^{-tz-z^2/2}dz\) and observe that the integral decreases with \(t\). For each fixed \(x\), when \(N\) is sufficiently large and \(v\ge 4(|x|+1)\), the threshold in \(q_N\) is at least \(u_N\), and its squared difference from \(u_N^2\) is at least \(v/2\). Using \(N[1-\Phi(u_N)]=1\) and the union bound gives
\[
q_N(v,x)\le e^{-v/4}
\qquad\text{for }4(|x|+1)\le v<L_N.
\]
On the remaining bounded interval, \(0\le q_N\le1\). Therefore \(\beta v^{\beta-1}q_N(v,x)\), extended by zero above \(L_N\), has an integrable envelope independent of large \(N\). Dominated convergence yields the first boxed limit. Finally, Tonelli's theorem gives
\[
\beta\int_0^\infty v^{\beta-1}\Pr(G>x+v)dv
=\mathbb E(G-x)_+^\beta,
\]
proving the alternative representation and strict positivity.

**3. Conditional reset-age selection.** For every bounded continuous function \(h\) on \((0,\infty)\), the same integrable domination gives
\[
\lim_{N\to\infty} L_N^\beta
\mathbb E\bigl[h(V_N)\mathbf1_{\{Y_N>x\}}\bigr]
=\beta\int_0^\infty h(v)v^{\beta-1}Q(x+v)dv.
\]
Divide by the first boxed limit to obtain weak convergence of the conditional law of \(V_N\). Because the limiting density is supported strictly on \((0,\infty)\), the continuous mapping theorem applied to \(-\log v\) yields the age-offset assertion, using \(2\mu A_N-\log L_N=-\log V_N\).

**4. Sharp leakage above the limiting hard edge.** Set \(a_N=\sqrt{2L_N}\) and
\[
\widetilde q_N(v)=1-\Phi\!\left(
\frac{a_N}{\sqrt{1-v/L_N}}
\right)^N.
\]
By the same exact beta-mixture identity,
\[
L_N^{\beta+1/2}\Pr(M_N>\sigma a_N)
=\beta\int_0^{L_N}v^{\beta-1}\sqrt{L_N}\,\widetilde q_N(v)dv.
\]
For fixed \(v\), the squared Gaussian threshold is \(2L_N+2v+o(1)\). The Mills ratio now implies
\[
N\overline\Phi\!\left(\frac{a_N}{\sqrt{1-v/L_N}}\right)
\sim\frac{e^{-v}}{\sqrt{4\pi L_N}}.
\]
Since the right side vanishes, the probability of at least one exceedance, \(\widetilde q_N(v)\), is asymptotic to the same expression. Moreover, for all \(0<v<L_N\), the normal-tail ratio inequality gives
\[
0\le\sqrt{L_N}\,\widetilde q_N(v)
\le\sqrt{L_N}\,N\overline\Phi(a_N)e^{-v}
\le C e^{-v}
\]
for a finite absolute constant \(C\) and all sufficiently large \(N\). Thus dominated convergence proves
\[
\lim L_N^{\beta+1/2}\Pr(M_N>\sigma a_N)
=\frac{\beta}{\sqrt{4\pi}}\int_0^\infty v^{\beta-1}e^{-v}dv
=\frac{\Gamma(\beta+1)}{\sqrt{4\pi}}.
\]
No unproved interchange of limits remains.

**5. Crossover matching.** The representation \(K_\beta(x)=\mathbb E(G-x)_+^\beta\) gives \(K_\beta(x)\sim(-x)^\beta\) as \(x\to-\infty\), using the finite positive moments of the Gumbel law. Its upper tail \(\Pr(G>t)\sim e^{-t}\) gives \(K_\beta(x)\sim\Gamma(\beta+1)e^{-x}\) as \(x\to+\infty\), by dominated convergence after factoring out \(e^{-x}\). At \(\beta=1,x=0\), substituting \(w=e^{-v}\) in the defining integral yields \(\int_0^1(1-e^{-w})\,dw/w=\gamma_{\mathrm E}+E_1(1)\).

## Verification

The companion `verify.py` evaluates the exact finite-\(N\) beta-mixture integrals by stable Gaussian-tail formulas and compares them with both limiting constants for \(\beta\in\{1/2,1,2\}\), several edge coordinates, and nominal sizes extending to \(10^{80}\). It also checks the two matching asymptotics and the exponential-integral identity. The program passed 94 numerical and exact-identity diagnostics on execution. It is self-contained apart from NumPy/SciPy and uses no simulation of an astronomical number of particles: the exact one-dimensional integral is evaluated numerically. Finite numerical checks support the algebra but are not substitutes for the dominated-convergence proofs above.

Reproduce with `python verify.py` after installing `numpy` and `scipy` (for example, from the versions already installed in a standard numerical Python environment). All sources and parameter normalizations needed for the analytical proof are printed above; the code is not a necessary hypothesis.

## Relationship to prior work

The conditional-independent stationary reset-age representation is established in the resetting-gas literature; it is not claimed here. De Mauro, Majumdar and Schehr (2026), *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634, derive the harmonic-trap leading maximum density \(S_H(z)=\nu_H^2 z(1-z^2)^{\nu_H^2/2-1}\) for \(0<z<1\), where \(\nu_H^2=r/\mu\). Their Sec. VI.1.1, especially Eqs. (126) and (129)–(136), identifies a slowly shrinking finite-\(N\) edge layer of width \(O(1/\log N)\) and an approximate cutoff, but does not display the beta-weighted Gumbel crossover constant, the conditional age-selection law, or the amplitude and extra half-power for leakage beyond \(\sigma\sqrt{2\log N}\).

Biroli, Kulkarni, Majumdar and Schehr (2024), arXiv:2312.02570, derive compact-support large-population extremes in a stochastically switching harmonic trap. Its mathematical setting is more general in trap switching but its stated asymptotics resolve the leading law, not these finer finite-size exceedance probabilities. De Mauro, Biroli, Majumdar and Schehr (2025), arXiv:2509.06658, establish arbitrary-renewal conditional independence and extreme laws for *free* Brownian gases; harmonic confinement and the upper compact-support edge layer are absent from that model. Standard Gaussian maxima and Mills ratios remain prior mathematical tools.

The present results are a **refinement of a known exact stationary mixture**, not an independent model solution. The concrete additional information is the leading coefficient of the rare finite-size boundary layer, the marked reset-age distribution of edge exceedances, and the distinct sharp exponent for crossing the nominal compact edge. Priority beyond the specifically inspected literature remains subject to independent checking.

## Limitations

The conclusions require identical harmonic confinement, complete simultaneous Poisson resetting to zero, independent Brownian drivers, and fixed positive parameters as population size increases. They are not a theorem for independent reset clocks, interacting particles, varying stiffness, non-Poisson clocks, or arbitrary Gaussian-mixture models. The probability limits concern fixed \(x\) in the corrected Gumbel window and a separate threshold at \(\sigma\sqrt{2\log N}\); they do not assert uniformity over \(x\) depending on \(N\). No finite-population relative-error bound or experimental feasibility claim is established. The claim describes stationary maxima and rare reset ages, not temporal hitting-time extremes. The displayed finite diagnostic counts do not certify the infinite-dimensional asymptotics or literature priority.

## References

1. G. de Mauro, S. N. Majumdar, G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first posted 2026-06-30), https://arxiv.org/abs/2606.31634 . See especially Sec. VI.1.1 and Eqs. (115)–(136).
2. M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first posted 2023-12-05), https://arxiv.org/abs/2312.02570 . See the main-text extreme-value section and supporting derivations.
3. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first posted 2025-09-08), https://arxiv.org/abs/2509.06658 . See conditional-independent renewal and free-gas extreme-statistics sections.
4. Standard Gaussian maximum domain-of-attraction and Mills-ratio facts, as recalled in the references and appendices of the preceding articles; no special unpublished lemma is assumed.
