# Shot-driven bond rupture survives infinite stiffness while its Gaussian surrogate freezes

## Finding

Consider a harmonically confined dimer whose monomers receive independent Poisson-distributed active kicks. When bond stiffness tends to infinity at **fixed nonzero jump size**, the first time the bond extension exceeds a fixed rupture threshold becomes, on the natural common-noise coupling, **eventually identical pathwise** to the time of the first individually rupture-capable kick. Thus the full first-rupture-time distribution, including every positive integer moment, has a finite explicit exponential limit. Nevertheless, replacing the active shots by Gaussian white noise with exactly the same instantaneous variance makes the predicted mean rupture time grow exponentially in stiffness.

Precisely, let \(\lambda>0\), \(\omega>0\), \(\sigma>0\), \(L>0\), \(D\geq0\), and \(k\geq0\), and define the stochastic dynamics below. Write \(\tau_k\) for first rupture of the relative coordinate, \(a_k=\lambda+2k\), and \(q_L=2\omega\operatorname{erfc}(L/(\sqrt2\sigma))\). Let \(\tau_*\) be the time of the first shot with absolute relative-coordinate mark greater than \(L\). Then

\[
\boxed{\Pr(\exists k_0<\infty:\ \tau_k=\tau_*\ \text{for every}\ k\geq k_0)=1,}
\qquad
\boxed{\tau_*\sim\operatorname{Exp}(q_L).}
\]

Consequently, for every real \(p>0\),

\[
\boxed{\lim_{k\to\infty}\mathbb E\tau_k^p
=\frac{\Gamma(p+1)}{q_L^p}.}
\]

The variance-matched Gaussian surrogate has exact mean exit time \(u_{a_k}(0)\) satisfying

\[
\boxed{u_{a}(0)\sim\frac{\sqrt{\pi\Theta/2}}{a^{3/2}L}
\exp\!\left(\frac{aL^2}{2\Theta}\right)\to\infty,}
\quad \Theta=2D+\omega\sigma^2.
\]

This is a noncommutation of stiff-restoring-force and white-noise-replacement limits, not a claim about the original nonlinear double-well passage time.

## Assumptions and scope

The model consists of two real-valued monomer positions, initially \(X_1(0)=X_2(0)=0\), governed by the Itô equations with jumps

\[
\begin{aligned}
 dX_1&=[-\lambda X_1+k(X_2-X_1)]\,dt+\sqrt{2D}\,dB_1+dJ_1,\\
 dX_2&=[-\lambda X_2+k(X_1-X_2)]\,dt+\sqrt{2D}\,dB_2+dJ_2.
\end{aligned}
\]

Here \(B_1,B_2\) are independent standard Brownian motions, \(J_1,J_2\) are independent compound Poisson processes of equal rate \(\omega\), and each jump of each \(J_i\) has an independent centered Gaussian amplitude of variance \(\sigma^2\). All drivers are mutually independent. A jump is instantaneous in position, with no finite-duration kick regularization. The relative extension is \(R_k(t)=X_2(t)-X_1(t)\), and its rupture time is
\[
\tau_k=\inf\{t\ge0:|R_k(t)|\ge L\}.
\]

All parameters except \(k\) remain fixed as \(k\to\infty\). The common-noise coupling uses the same realizations of \(B_i,J_i\) simultaneously for all \(k\ge0\). The comparison Gaussian model starts from zero and matches the relative coordinate's infinitesimal second-moment rate, not its jump paths or higher cumulants.

## Proof

**1. Relative-mode reduction and shot law.** Subtracting the monomer equations gives exactly
\[
 dR_k=-a_k R_k\,dt+\sqrt{4D}\,dB+dJ,
 \qquad a_k=\lambda+2k,
\]
where \(B=(B_2-B_1)/\sqrt2\) is standard Brownian motion. Since the independent Poisson clocks almost surely never ring simultaneously, the superposition of \(J_2\) and \(-J_1\) is a compound Poisson process of rate \(2\omega\) with independent marks \(Y_n\sim N(0,\sigma^2)\). Denote its jump times \(T_n\). Let
\[
\tau_*=\min\{T_n:|Y_n|>L\}.
\]
Independent Poisson thinning gives \(\Pr(\tau_*>t)=e^{-q_L t}\) for every \(t\ge0\), with \(q_L=2\omega\Pr(|Y_1|>L)=2\omega\operatorname{erfc}(L/(\sqrt2\sigma))>0\).

**2. Uniform collapse of the continuous OU component.** For the standard Brownian path \(B\), let
\[
Z_a(t)=\sqrt{4D}\int_0^t e^{-a(t-s)}\,dB_s.
\]
The Itô integration-by-parts identity for each continuous Brownian path gives
\[
\frac{Z_a(t)}{\sqrt{4D}}=
 e^{-at}B_t+a\int_0^t e^{-a(t-s)}(B_t-B_s)\,ds,
\]
when \(D>0\); for \(D=0\) the component is identically zero. On each finite deterministic time horizon \([0,H]\), Brownian continuity and uniform continuity imply
\[
\sup_{0\le t\le H}|Z_a(t)|\longrightarrow0
\quad\text{almost surely as}\quad a\to\infty.
\]
Indeed, the first term vanishes uniformly because \(B_0=0\), while the integral is bounded by the Brownian modulus of continuity at lag \(\delta\) plus \(2\sup_{s\le H}|B_s|e^{-a\delta}\). First let \(a\to\infty\), then \(\delta\downarrow0\). Countable integer horizons give a single probability-one event for every finite horizon.

**3. Every rupture time eventually equals the first large-shot time.** The shot component is
\[
 S_a(t)=\sum_{T_j\le t}Y_j e^{-a(t-T_j)}.
\]
On every bounded time interval there are finitely many jumps. Their jump times are distinct almost surely. Hence at each such time \(T_j\),
\[
 S_a(T_j-)=\sum_{i<j}Y_i e^{-a(T_j-T_i)}\longrightarrow0,
\]
and between consecutive shots \(|S_a(t)|\) decreases monotonically from its immediately post-shot value. Furthermore, for each fixed integer horizon, no individual mark is exactly of magnitude \(L\) almost surely, because the mark distribution is continuous. Since \(\tau_*<\infty\) almost surely, only finitely many marks precede or occur at \(\tau_*\). Their distances from the rupture threshold have a strictly positive minimum. Combining that gap with uniform decay of \(Z_a\) and the residual contributions from all earlier shots yields, for all sufficiently large \(a\), no rupture before \(\tau_*\), followed by immediate rupture at the shot \(\tau_*\). Therefore \(\tau_k=\tau_*\) for every sufficiently large \(k\) on almost every common-noise sample path. This is stronger than convergence in distribution.

**4. Uniform domination and all positive moments.** Define \(\tau_{2L}=\min\{T_j:|Y_j|>2L\}\). Whenever this jump occurs before an earlier rupture, the left limit satisfies \(|R_k(T_j-)|<L\), so the triangle inequality gives \(|R_k(T_j)|\ge|Y_j|-|R_k(T_j-)|>L\). Thus, simultaneously for every \(k\ge0\),
\[
0\le\tau_k\le\tau_{2L},\qquad
\tau_{2L}\sim\operatorname{Exp}\!\left(2\omega\operatorname{erfc}\!\left(2L/(\sqrt2\sigma)\right)\right).
\]
The right-hand random variable has all positive moments. Dominated convergence applied to \(\tau_k^p\) for each \(p>0\) gives the stated complete moment law.

**5. The variance-matched Gaussian surrogate fails sharply.** The relative-coordinate diffusion plus shot quadratic-variation rate is \(4D+2\omega\sigma^2=2\Theta\) with \(\Theta=2D+\omega\sigma^2\). Replace both sources by a single Gaussian Brownian driver and consider
\[
dR^{\rm G}=-aR^{\rm G}\,dt+\sqrt{2\Theta}\,dW,\quad R^{\rm G}(0)=0.
\]
For the exit time from \((-L,L)\), the bounded mean-exit solution \(u_a(x)\) satisfies \(\Theta u_a''(x)-axu_a'(x)=-1\), \(u_a(\pm L)=0\), and \(u_a'(0)=0\). Integration of the first-order derivative equation yields exactly
\[
 u_a(0)=\frac1\Theta\int_0^L e^{ax^2/(2\Theta)}
 \left[\int_0^x e^{-ay^2/(2\Theta)}\,dy\right]dx.
\]
For fixed \(L,\Theta>0\), the inner integral in the region contributing at the endpoint \(x=L\) is \(\sqrt{\pi\Theta/(2a)}(1+o(1))\); the outer endpoint integral is \((\Theta/(aL))e^{aL^2/(2\Theta)}(1+o(1))\). These standard Gaussian and endpoint-Laplace estimates give the asserted asymptotic with its full leading constant. The shot model instead has \(\mathbb E\tau_k\to 1/q_L<\infty\).

The exact stationary relative-coordinate variance is \(\Theta/a\), yet its stationary fourth cumulant (from the compound Poisson Lévy exponent) is \(3\omega\sigma^4/(2a)\), so standardized excess kurtosis is \(3\omega\sigma^4a/(2\Theta^2)\). Its growth is consistent with the failure of a variance-only Gaussian replacement for this rare-event observable; the cumulant formula itself is background, not a separate novelty claim.

## Verification

The standalone file `verify.py` uses SymPy to verify the relative drift eigenvector, effective second-moment rate, stationary fourth cumulant, and the Gaussian mean-exit differential identity. A 50-digit mpmath quadrature independently evaluates the Gaussian mean-exit integral and its leading constant. A seeded event-driven simulation with zero thermal diffusion compares exact finite-stiffness rupture with the first oversized shot, and tests pathwise domination. Run with `python3 verify.py` in an environment containing `sympy` and `mpmath`.

These finite tests are computational checks only. The almost-sure eventual equality for the full model including \(D>0\), all-real-stiffness quantifier, and convergence of moments follow from the analytical coupling, uniform Brownian approximation, and exponential domination—not from simulation.

## Relationship to prior work

Goel and Marathe (2026) introduce and study a thermally and Poisson-shot-driven dimer with elastic intermonomer coupling and nonlinear double-well escape. Their sections II–III and appendices analyze center-of-mass or well-to-well first passage, deriving analytical MFPT results under the **small-shot-variance Gaussian approximation** and studying the general case numerically. Here the observable is instead a fixed **relative-bond rupture threshold** in the harmonically localized dimer, with jump amplitudes held fixed as stiffness grows. The source's small-kick diffusion approximation does not imply the exact shot-preserving stiff limit.

Masoliver (1987) develops a broad trajectory analysis of first passage under shot noise and treats linearly bound motions. The inspected sections III, V and VI give explicit classes based on one-sided positive exponential or fixed-size jumps; they are important general precursors and are not claimed as new here. Borovkov and Novikov (2007) prove martingale identities for Lévy-driven OU exit and an exponential limit in a **large-boundary** regime with exponential positive jumps. Neither inspected theorem states this fixed-boundary, high-restoring-rate, two-sided Gaussian-amplitude, all-moments bond-rupture result or its full Gaussian approximation contrast. Imkeller, Pavlyukevich and Wetzel (2007) investigate a distinct small-amplitude exponentially light Lévy-noise regime; such general metastability theory may suggest related single-large-jump principles but does not directly identify the stated joint scaling with fixed physical jumps.

## Limitations

- The harmonic model is a local, linear relative-coordinate idealization. No result is established for nonlinear Morse bonds, finite-duration impulses, a joint stochastic model of chemically irreversible rupture, or the original double-well center-of-mass escape problem.
- Exact eventual equality is a coupling statement for **fixed amplitudes and rates** as stiffness increases; it is not a statement about every cross-parameter coupling, nor about taking small-shot variance simultaneously with stiffness.
- A Gaussian amplitude has an unbounded tail, so the event rate \(q_L\) remains strictly positive. Bounded shot-amplitude distributions with bound below \(L\) require a different asymptotic analysis.
- General shot-noise first-passage methods predating the motivating paper may be adaptable to this limit. Although the checked statements differ, an exhaustive literature priority guarantee is not asserted.

## References

1. G. Goel and R. Marathe, *Poisson-shot-noise induced escape dynamics of a passive particle and a dimer*, arXiv:2610.26316v1 (first public 2026-10-19), full-text v2 (2026-10-21), https://arxiv.org/html/2610.26316v2 .
2. J. Masoliver, *First-passage times for non-Markovian processes: Shot noise*, Physical Review A **35** (1987), 3918–3928, doi:10.1103/PhysRevA.35.3918; open text https://hdl.handle.net/2445/9436 .
3. K. Borovkov and A. Novikov, *On exit times of Lévy-driven Ornstein–Uhlenbeck processes*, arXiv:0709.1746 (2007), https://arxiv.org/pdf/0709.1746 .
4. P. Imkeller, I. Pavlyukevich and T. Wetzel, *First exit times for Lévy-driven diffusions with exponentially light jumps*, arXiv:0711.0982 (2007), https://arxiv.org/abs/0711.0982 .
