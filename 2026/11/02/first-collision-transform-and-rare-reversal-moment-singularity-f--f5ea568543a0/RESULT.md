# First-collision transform and rare-reversal moment singularity for a run-and-tumble pair on a ring

## Finding

Let \(T_\alpha\) be the first physical contact time of two independently reversing one-dimensional run-and-tumble particles on a ring, initially approaching one another. For \(\alpha>0\), every \(s\ge0\) has the transform

\[
\mathbb E[e^{-sT_\alpha}]
=\frac{\cosh(\kappa(H-x))+\delta\sinh(\kappa(H-x))}
{\cosh(\kappa H)+\delta\sinh(\kappa H)},\qquad
\kappa=\frac{\sqrt{s(s+4\alpha)}}{2v},\quad
\delta=\frac{\sqrt{s(s+4\alpha)}}{s+2\alpha}.
\]

At \(s=0\), the quotient means its continuous value \(1\). In particular,

\[
\mathbb E[T_\alpha]=\frac{x}{v}+\frac{\alpha x(2H-x)}{2v^2}.
\]

When the independent reversal rate tends to zero, \(T_\alpha\to x/(2v)\) in probability, but

\[
\lim_{\alpha\downarrow0}\mathbb E[T_\alpha]=\frac{x}{v}
\ne\frac{x}{2v}=\mathbb E[T_0],
\qquad
\lim_{\alpha\downarrow0}\alpha^{m-1}\mathbb E[T_\alpha^m]
=\frac{m!x}{2^m v}\quad(m=2,3,\ldots).
\]

Thus \(\operatorname{Var}(T_\alpha)\sim x/(2v\alpha)\). Write \(E_\alpha\) for the event that at least one reversal occurs before the would-be ballistic collision. Its probability is exactly \(1-e^{-\alpha x/v}\). Conditional on \(E_\alpha\), the scaled contact time \(\alpha T_\alpha\) converges in law to \(\operatorname{Exp}(2)\), where \(2\) denotes the rate rather than the mean. This conditional law explains the unusual moment limits.

## Assumptions and scope

The ring has circumference \(2H\), where \(H>0\). Each particle has piecewise constant velocity \(+v\) or \(-v\), with \(v>0\), and reverses its sign at independent Poisson rate \(\alpha>0\). The particles cannot pass through one another; the process is stopped at their **first** contact, so the law of post-contact jamming and release is irrelevant. There is no thermal diffusion, extrinsic drift, or finite-duration tumble. Initially the shorter interparticle distance is \(x\in(0,H]\) and is decreasing at speed \(2v\). The case \(x=H\) uses the initial decreasing branch; no other initial orientation claim is made.

The folded gap lies in \([0,H]\). Before contact, its velocity state is closing \(C\) with slope \(-2v\), opening \(O\) with slope \(+2v\), or stalled \(S\) with slope zero. Since individual velocity flips occur independently, \(C\to S\) and \(O\to S\) have rates \(2\alpha\) and \(S\to C\), \(S\to O\) each have rate \(\alpha\). Reaching the antipodal distance \(H\) while opening changes the folded-gap branch to closing without delay; it is not a physical collision or wall reflection.

## Proof

**Backward boundary-value problem.** Let \(F_C(y;s)\), \(F_O(y;s)\), and \(F_S(y;s)\) denote \(\mathbb E[e^{-sT_\alpha}]\) from folded gap \(y\) with the indicated velocity state. For \(s>0\) and \(0<y<H\), the generator gives

\[
\begin{aligned}
-2v\partial_yF_C&=(s+2\alpha)F_C-2\alpha F_S,\\
 2v\partial_yF_O&=(s+2\alpha)F_O-2\alpha F_S,\\
 (s+2\alpha)F_S&=\alpha(F_C+F_O).
\end{aligned}
\]

The incoming absorbing and antipodal-folding conditions are \(F_C(0;s)=1\) and \(F_O(H;s)=F_C(H;s)\). No independent boundary value for the outgoing state at zero is imposed. The compact state space and a uniform positive probability of following a contact-producing path over a bounded time imply an exponential tail for fixed \(\alpha>0\); hence all moments exist and this bounded boundary-value problem has the probabilistic solution.

Put \(U=F_C+F_O\) and \(W=F_O-F_C\). Elimination of \(F_S\) yields

\[
U' =\frac{s+2\alpha}{2v}W,\qquad
W'=\frac{s(s+4\alpha)}{2v(s+2\alpha)}U,
\qquad U''=\kappa^2U.
\]

The antipodal condition says \(W(H)=0\) or equivalently \(U'(H)=0\). Hence \(U(y)\) is proportional to \(\cosh(\kappa(H-y))\). Because \(W=2vU'/(s+2\alpha)\), it follows that \(F_C=(U-W)/2\) has the claimed hyperbolic quotient, after normalizing by \(F_C(0;s)=1\). This also checks the generator identities and both endpoint conditions directly.

**Exact mean.** Expand at \(s=0\) for fixed positive \(\alpha\): \(\kappa^2=\alpha s/v^2+O(s^2)\) and \(\delta\kappa=s/v+O(s^2)\). Expanding the numerator and denominator gives

\[
F_C(x;s)=1-s\left[\frac{x}{v}+\frac{\alpha x(2H-x)}{2v^2}\right]+O(s^2),
\]

proving the stated mean formula.

**Rare reversals and the conditional law.** Without a reversal the particles collide at \(t_0=x/(2v)\). The combined initial flip clock has rate \(2\alpha\), so \(\Pr(E_\alpha)=1-e^{-2\alpha t_0}=1-e^{-\alpha x/v}\) and \(T_\alpha=t_0\) on its complement. This proves convergence in probability to \(t_0\). If a reversal occurs first, the relative gap immediately stalls for an independent \(\operatorname{Exp}(2\alpha)\) waiting time \(B_\alpha\). After leaving the stalled state, a flip-free trajectory reaches physical contact within \(H/v\), no matter which of the two mobile directions is chosen. The probability of a further flip before that deterministic contact is at most \(2\alpha H/v\). Consequently, under conditioning on \(E_\alpha\),

\[
\alpha T_\alpha-\alpha B_\alpha\longrightarrow0
\quad\text{in probability},
\]

and \(\alpha B_\alpha\) has the \(\operatorname{Exp}(2)\) law for every \(\alpha>0\). The conditional limiting law follows.

**All-moment singularity.** For \(s=\alpha z\), the hyperbolic quotient is holomorphic in a fixed complex disk \(|z|<1\) for all sufficiently small positive \(\alpha\). The apparent square roots cancel because \(\kappa^2\) and \(\delta\kappa\) are rational and analytic in \(z\) there. Expanding uniformly on any compact subdisk gives

\[
\mathbb E[e^{-\alpha zT_\alpha}]
=1-\frac{\alpha x}{2v}\frac{z(z+4)}{z+2}+O(\alpha^2).
\]

For every integer \(m\ge2\), the coefficient of \(z^m\) in the first-order term equals \((-1)^m x/(2^m v)\). Holomorphic uniformity permits coefficient extraction by Cauchy's integral formula, so

\[
\alpha^m\mathbb E[T_\alpha^m]
=\alpha\frac{m!x}{2^m v}+O(\alpha^2)
\]

for each fixed \(m\ge2\), completing the proof. For \(\alpha=0\) exactly, there is no reversal and \(T_0=x/(2v)\) deterministically.

## Verification

The accompanying `verification.py` independently reconstructs the backward equations, both endpoint conditions, and the coefficient of the exact mean by symbolic algebra. It checks the rare-rate Taylor coefficients for moment orders \(2\) through \(10\), compares the transform and mean against 114,000 independently simulated event-driven sample paths across three parameter choices, and evaluates the scaled-Laplace expansion at six high-precision parameter pairs. All 30 implemented checks passed. These finite diagnostics are reproducibility tests, not substitutes for the proof of all-order moments or all positive parameters. Run `python verification.py` with `sympy` and `mpmath` installed.

## Relationship to prior work

Hahn, Guillin and Michel (arXiv:2306.00831, first public 2023-06-01) establish the general continuous two-particle ring-jamming model, its folded-distance dynamics, and stationary measures. Their Section II supplies the folding and collision geometry used here; their steady-state classifications do not by themselves determine the first-contact law. Le Doussal, Majumdar and Schehr (arXiv:1902.06176) derive exact first-encounter probabilities for two active particles on an **unbounded line**, a genuinely different geometry with algebraic survival and no finite positive-rate mean first collision. Guillin, Hahn and Michel (arXiv:2411.13964), Section 4.2, solve backward equations for **the mean time to a specified oriented jammed state** as part of mixing bounds; the process continues after jamming at the other oriented boundary. Their stopping condition is not the present first contact at either meeting location, and their result does not state this Laplace transform or the rare-reversal hierarchy. Grange and Yuan (arXiv:2509.11308), Sections 3–5 and 7, study a related three-velocity particle with **nonzero imposed drift** and two absorbing interval endpoints, calculating exit probabilities and conditional means; their paper explicitly leaves higher first-passage moments as a further extension. These techniques are relevant antecedents, not claims of priority over them.

## Limitations

The statement is for **initially closing**, independent, symmetric, instantaneous-flip walkers with strictly positive speeds and finite ring circumference. All-order singularity concerns each fixed integer moment order as the flip rate decreases, not a bound uniform in order. The conditional weak limit does not by itself prove the moment asymptotics; those require the transform's analytic expansion. The limit is singular and must not be evaluated by substituting zero flip rate into positive-rate mean formulas. This result is not a mixing-time theorem, an arbitrary-velocity classification, a thermodynamic limit, or a statement about continued jammed residence times. No independent publication-priority audit is claimed.

## References

1. L. Hahn, A. Guillin and M. Michel, *Jamming pair of general run-and-tumble particles: Exact results and universality classes*, arXiv:2306.00831, first publicly submitted 2023-06-01. https://arxiv.org/abs/2306.00831
2. P. Le Doussal, S. N. Majumdar and G. Schehr, *Non-crossing run-and-tumble particles on a line*, arXiv:1902.06176 (2019). https://arxiv.org/abs/1902.06176
3. A. Guillin, L. Hahn and M. Michel, *Long-time analysis of a pair of on-lattice and continuous run-and-tumble particles with jamming interactions*, arXiv:2411.13964 (2024). https://arxiv.org/abs/2411.13964
4. P. Grange and L. Yuan, *First passage of a run-and-tumble particle with exponentially-distributed tumble duration in the presence of a drift*, arXiv:2509.11308 (2025; revised 2026). https://arxiv.org/abs/2509.11308
5. A. B. Slowman, M. R. Evans and R. A. Blythe, *Exact solution of two interacting run-and-tumble random walkers with finite tumble duration*, arXiv:1705.04812 (2017). https://arxiv.org/abs/1705.04812
