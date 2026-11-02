# Optimal reset cadence and the long-lag envelope of viscoelastic excursion memory

## Finding

Consider a probe and an unreset bath coordinate satisfying the dimensionless coupled Langevin equations
\[
 dX_t=(Q_t-X_t)\,dt+\sqrt{2}\,dW_t,\qquad
 dQ_t=g(X_t-Q_t)\,dt+\sqrt{2g}\,dB_t,
\]
where \(g>0\), \(W\) and \(B\) are independent standard Brownian motions, and an independent rate-\(r\) Poisson clock, \(r>0\), instantaneously changes \((X,Q)\mapsto(0,Q)\). Let \(T_j\) denote successive reset epochs of its stationary version, indexed in both directions, and let \(Y_j=X_{T_j-}\) be the probe position just before the \(j\)-th reset. The event-indexed correlation at lag \(m\in\{1,2,\ldots\}\) is exactly
\[
 \boxed{\rho_m(r,g)=\operatorname{Corr}(Y_0,Y_m)
 =\frac{r+2g+2}{2(r+g+1)^2}
 \left(\frac{r+1}{r+g+1}\right)^{m-1}.}
\]
It is strictly positive and decreases geometrically with \(m\) at every fixed \(r,g>0\). However, its dependence on the resetting *rate* undergoes a sharp lag-dependent change:

- For \(m=1\), \(\rho_m\) is strictly decreasing in \(r>0\).
- For \(m\ge2\), if \(g\le 3/[2(m-1)]\), it is strictly decreasing in \(r>0\); if \(g>3/[2(m-1)]\), it first increases, reaches exactly one global maximum, and then strictly decreases. This maximum occurs at
\[
 \boxed{r_m^*(g)=\frac{g(m-4)-4+
 \sqrt{g^2m^2+4(g+1)(2g+1)}}{2}>0.}
\]
In particular, for every fixed finite bath friction \(\gamma=1/g>0\), all sufficiently large integer event lags have such an interior optimal reset rate. Furthermore,
\[
 \boxed{\lim_{m\to\infty}\frac{r_m^*(g)}{m}=g,
 \qquad \lim_{m\to\infty}m\,\rho_m(r_m^*(g),g)=\frac{1}{2eg}.}
\]
Thus an optimally chosen reset rate changes the best attainable long-event-lag correlation from geometric decay at any fixed \(r\) to the sharp algebraic envelope \(\sim 1/(2egm)\). At this optimum, the expected physical separation \(m/r_m^*(g)\) of two reset events approaches the bath relaxation time \(1/g=\gamma\).

## Assumptions and scope

All rates are dimensionless and strictly positive; \(g=\gamma^{-1}\) is the inverse bath friction relative to the probe, and no external trap or feedback is present. The noises are independent, the reset clock is independent of the diffusion, and only the probe coordinate is reset. The process is observed in its unique stationary regime. Correlations refer to the sequence of probe positions **immediately before Poisson resets**, not to correlations at fixed physical-time lag, not to positions just after resetting (which are zero), and not to event-count fluctuations. The integer \(m\) counts *reset events*, and may vary independently of \(r\).

The embedded bath chain at reset epochs is a contractive random affine recursion: for a fresh exponentially distributed interval \(T>0\), its conditional mean multiplier is \((1+g e^{-(1+g)T})/(1+g)\), strictly between zero and one. Brownian increments have finite second moments, giving a unique stationary event-chain law with finite second moment and, consequently, the stationary continuous-time construction used here.

## Proof

**1. Stationary moments.** Set \(U=\mathbb E[X^2]\), \(V=\mathbb E[XQ]\), and \(Z=\mathbb E[Q^2]\). Stationarity under the diffusion generator and the reset map gives exactly
\[
 0=-(2+r)U+2V+2,\quad
 0=gU-(1+g+r)V+Z,\quad
 0=2g(V-Z+1).
\]
The stationary means vanish. Solving these three linear equations produces
\[
 U=\frac{2(g+r+1)}{r(g+r+2)},\qquad
 V=\frac{2g+r+2}{r(g+r+2)},\qquad
 Z=\frac{(r+2)(g+r+1)}{r(g+r+2)}.
\]
These identities follow directly from the stochastic generator, and are included for normalizations and reproducibility. As the reset hazard is a state-independent constant, the compensator identity for its counting process shows that the distribution of \((X_{T_j-},Q_{T_j-})\) at reset epochs has these same stationary moments: the pre-reset event sampling is unbiased.

**2. Propagation between events.** Between resets, the conditional first moments evolve under
\[
 M=\begin{pmatrix}-1&1\\g&-g\end{pmatrix},
 \qquad \operatorname{spec}M=\{0,-(1+g)\}.
\]
Starting immediately after an event at \((0,q)\), a time \(t>0\) without a reset yields
\[
 \mathbb E[X_t\mid q]=\frac{1-e^{-(1+g)t}}{1+g}q,
 \quad
 \mathbb E[Q_t\mid q]=\frac{1+ge^{-(1+g)t}}{1+g}q.
\]
Averaging over the fresh independent \(\operatorname{Exp}(r)\) waiting time gives the conditional event-to-event regressions
\[
 \mathbb E[Y_{j+1}\mid \mathcal F_{T_j}]=bQ_{T_j},\quad
 \mathbb E[Q_{T_{j+1}}\mid\mathcal F_{T_j}]=aQ_{T_j},\quad
 b=\frac1{r+g+1},\quad a=\frac{r+1}{r+g+1}\in(0,1).
\]
Here the sigma-field includes the state immediately after reset \(j\) and all earlier events. Iterating the regressions gives \(\mathbb E[Y_{j+m}\mid\mathcal F_{T_j}]=ba^{m-1}Q_{T_j}\) for each integer \(m\ge1\). Therefore
\[
 \operatorname{Cov}(Y_j,Y_{j+m})=ba^{m-1}V.
\]
Dividing by \(\operatorname{Var}(Y_j)=U>0\) gives the claimed exact correlation formula. The factor \(a\in(0,1)\) proves positivity and fixed-rate geometric lag decay.

**3. A sharp rate bifurcation.** Logarithmic differentiation gives
\[
 \frac{\partial_r\rho_m}{\rho_m}
 =\frac1{r+2g+2}+\frac{m-1}{r+1}-\frac{m+1}{r+g+1}
 =\frac{F_m(r,g)}{(r+2g+2)(r+1)(r+g+1)},
\]
where
\[
 F_m(r,g)=-r^2+[g(m-4)-4]r
 +(g+1)[2g(m-1)-3].
\]
For \(m=1\), \(F_1(r,g)=-(r+1)(r+3g+3)<0\). For \(m\ge2\), the constant term is positive precisely when \(g>3/[2(m-1)]\). In that case the concave quadratic has exactly one positive root; it is the displayed \(r_m^*(g)\), obtained from the discriminant \(g^2m^2+4(g+1)(2g+1)\), and the derivative changes from positive to negative there. If the constant term is nonpositive, then \(g(m-4)-4<0\): this is immediate for \(m\le4\), while for \(m>4\) it follows from \(g\le3/[2(m-1)]\). Hence \(F_m(r,g)<0\) throughout \(r>0\). These cases cover every parameter and prove strictness and uniqueness.

**4. The optimal long-lag envelope.** At fixed \(g>0\), the threshold \(3/[2(m-1)]\) vanishes as \(m\to\infty\), so the interior maximizer exists for all sufficiently large \(m\). Expanding its exact root gives
\[
 r_m^*(g)=gm-2(g+1)+\frac{(g+1)(2g+1)}{gm}+O_g(m^{-2}).
\]
Consequently \(r_m^*(g)/m\to g\). In the closed correlation formula, the prefactor is \(1/[2gm](1+o(1))\) while the factor raised to the \((m-1)\)-st power tends to \(e^{-1}\), proving the second limit. For comparison, at each fixed \(r\), the ratio \((r+1)/(r+g+1)\) is strictly below one, so there is no competing algebraic long-lag tail without optimization.

## Verification

The included `verify.py` is standalone Python (standard library only). It checks the stationary moment balance by exact rational arithmetic; verifies the event-regression/covariance formula and the logarithmic-derivative identity across a finite parameter grid; tests the critical-rate formula and asymptotic predictions; and independently generates sample paths with the **exact between-reset Gaussian transition**, rather than using time-discretized Euler updates. It reports 2,808 successful bounded checks on replay. Reproduce with `python3 verify.py`.

For the exact transition simulator, write \(\ell=1+g\), \(u=(gX+Q)/\ell\), and \(v=X-Q\). Then between resets \(u\) is Brownian with variance rate \(2g/\ell\) and \(v\) is an independent Ornstein–Uhlenbeck process with decay \(\ell\) and equilibrium variance one. This produces the conditional Gaussian updates used by the checker. The exact rational identities and the analytical sign argument above, not the bounded simulation, justify the all-parameter conclusions.

## Relationship to prior work

Santra and Das, *Resetting in a viscoelastic bath: the bath remembers* (arXiv:2603.17027, first posted 2026-03-17), introduce exactly this probe-only reset and unreset bath model. Their stationary moment equations and spatial fluctuation analysis are prior results. Their discussion of retained bath memory motivates the present **event-indexed** observable; the new contribution is a complete expression for serial pre-reset correlations, an exact rate-bifurcation boundary for every event lag, and the optimal \(1/m\) envelope with its time-scale matching law.

Biswas, Dubbeldam, Sandev and Pal, *A resetting particle embedded in a viscoelastic bath* (arXiv:2412.09260), derive correlations under a generalized-Langevin *complete-renewal* resetting convention. Correlation across excursions is destroyed by that renewal convention, unlike the unreset bath model here. Olsen and Löwen (arXiv:2401.12685) analyze partial resetting of the hidden variable in an inertial transport model. Maes and Thiery (arXiv:1705.07670) study a probe influenced by a **resetting bath**, rather than a reset probe with an unreset bath. These models are not silently identified.

A separate exact physical-time covariance result for the same probe–bath process does not itself assert the correlations across successive *reset events*, nor the critical reset-rate classification. Published event- or time-sampling inequalities on other stochastic models similarly do not imply the explicit all-lag rate threshold here. Generic Markov-renewal regression methods explain the technique and are not claimed as newly invented.

## Limitations

This is a theorem only for the specified two-coordinate, linear Gaussian, independent-Poisson, probe-only instantaneous-reset model. It neither asserts a universal correlation law for nonlinear viscoelastic baths nor treats finite-speed returns, non-Poisson resets, resetting the bath itself, or noisy observables sampled at arbitrary physical times. The optimal rate depends on the chosen event lag; as \(m\) changes the measuring protocol changes. The finding establishes correlation structure and an event-lag optimum, not optimal search time, energetic efficiency or independent experimental validation. Stationary moment formulas and generic conditional-regression principles are prior knowledge; only the stated full classification and consequences are assessed here.

## References

1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, 2026-03-17, https://arxiv.org/abs/2603.17027.
2. A. Biswas, J. L. A. Dubbeldam, T. Sandev and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260v1, 2024-12-12, https://arxiv.org/abs/2412.09260.
3. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685, https://arxiv.org/abs/2401.12685.
4. C. Maes and T. Thiery, *The induced motion of a probe coupled to a bath with random resettings*, arXiv:1705.07670, https://arxiv.org/abs/1705.07670.
