# A critical extinction-exponent trichotomy for periodically harvested rank-one competition

## Finding

Consider two competitive populations whose intrinsic growth is canceled exactly over each harvesting cycle. When the competition matrix has proportional rows, their post-harvest states follow an exact nonlinear power-law invariant. Every strictly positive orbit tends to extinction, with a sharp three-regime decay law determined by the row-proportionality exponent \(\kappa\). Write \(I_i=(e^{r_i\tau}-1)/r_i\) and \(h=y_0/x_0^\kappa\). Then:

\[
\begin{array}{ll}
0<\kappa<1:&\displaystyle\lim_{m\to\infty}m^{1/\kappa}x_m=(\kappa b hI_2)^{-1/\kappa},\quad \lim_{m\to\infty}m y_m=(\kappa b I_2)^{-1};\\[6pt]
\kappa=1:&\displaystyle\lim_{m\to\infty}m x_m=(aI_1+b hI_2)^{-1},\quad\lim_{m\to\infty}m y_m=h(aI_1+b hI_2)^{-1};\\[6pt]
\kappa>1:&\displaystyle\lim_{m\to\infty}m x_m=(a I_1)^{-1},\quad\lim_{m\to\infty}m^\kappa y_m=h(aI_1)^{-\kappa}.
\end{array}
\]

At \(\kappa=1\) the reciprocal relation is **exact for every** \(m\ge0\):
\[
\frac1{x_m}=\frac1{x_0}+m(aI_1+b hI_2),\qquad y_m=h x_m.
\]
The result is global in the positive quadrant of post-pulse initial states, not a local expansion near the origin.

## Assumptions and scope

Fix \(a,b,r_1,r_2,\tau,\kappa>0\). Between pulse times \(m\tau\) and \((m+1)\tau\), let
\[
\dot x=x(r_1-a x-b y),\qquad
\dot y=y(r_2-\kappa a x-\kappa b y).
\]
Immediately after time \((m+1)\tau\), impose the multiplicative harvest
\[
 x((m+1)\tau^+)=e^{-r_1\tau}x((m+1)\tau^-),\qquad
 y((m+1)\tau^+)=e^{-r_2\tau}y((m+1)\tau^-).
\]
Write \((x_m,y_m)=(x(m\tau^+),y(m\tau^+))\) and start with any \(x_0,y_0>0\). The minus and plus superscripts indicate one-sided physical-time limits. The state exactly after each pulse is the discrete observation, so \(m\) is the number of complete harvest cycles. The two net growth multipliers at zero equal one; this is a simultaneously critical and not strictly permanent regime. The competition matrix \(\bigl(\begin{smallmatrix}a&b\\\kappa a&\kappa b\end{smallmatrix}\bigr)\) has rank one.

For each \(s\in[0,\tau)\), within-cycle states also have the uniform asymptotic envelopes
\[
 \frac{x(m\tau+s)}{e^{r_1 s}x_m}\longrightarrow1,\qquad
 \frac{y(m\tau+s)}{e^{r_2 s}y_m}\longrightarrow1,
\]
with convergence uniform in \(s\in[0,\tau)\) when the pre-pulse value at \(\tau\) is used for the endpoint. Both continuous populations tend to zero as physical time tends to infinity.

## Proof

**Exact conserved post-pulse ratio.** Within a pulse-free interval,
\[
\frac{d}{dt}(\log y-\kappa\log x)=r_2-\kappa r_1.
\]
The logarithmic harvest changes \(\log y-\kappa\log x\) by \(-r_2\tau+\kappa r_1\tau\), exactly canceling its intervening drift. Hence \(y_m=h x_m^\kappa\) for every integer \(m\ge0\), with \(h=y_0/x_0^\kappa>0\).

**One-dimensional cycle.** On a given cycle set \(u_m(s)=e^{-r_1s}x(m\tau+s)\) and \(v_m(s)=e^{-r_2s}y(m\tau+s)\) for \(0\le s<\tau\). The preceding identity, now with the natural exponential factors stripped, gives \(v_m(s)=h u_m(s)^\kappa\) and
\[
\frac{du_m}{ds}=-a e^{r_1s}u_m^2-b h e^{r_2s}u_m^{\kappa+1},\quad u_m(0)=x_m,\quad x_{m+1}=u_m(\tau^-).
\]
In particular \(0<x_{m+1}<x_m\) for every cycle. If \(x_m\to\ell>0\), continuity of the strictly decreasing scalar period map at \(\ell\) would give \(P(\ell)=\ell\), whereas the scalar flow satisfies \(P(\ell)<\ell\), a contradiction. Therefore \(x_m\to0\), and the conserved power relation yields \(y_m\to0\).

**Sharp drift and power law.** The scalar equation implies \(0<u_m(s)\le x_m\) and
\[
0\le\log\frac{x_m}{u_m(s)}
\le a I_1 x_m+b h I_2 x_m^\kappa
\quad(0\le s\le\tau).
\]
Consequently \(u_m(s)/x_m\to1\) uniformly on the closed pre-pulse cycle. Integrating the scalar equation gives
\[
 x_m-x_{m+1}=a I_1 x_m^2(1+o(1))+b h I_2 x_m^{\kappa+1}(1+o(1)).
\]
Set \(\alpha=\min\{1,\kappa\}\). Thus for the positive coefficient
\[
 C=\begin{cases}bhI_2,&0<\kappa<1,\\ aI_1+bhI_2,&\kappa=1,\\ aI_1,&\kappa>1,\end{cases}
\]
we have \(x_{m+1}=x_m-C x_m^{1+\alpha}(1+o(1))\). The mean-value theorem applied to \(z\mapsto z^{-\alpha}\) yields
\[
 x_{m+1}^{-\alpha}-x_m^{-\alpha}=\alpha C+o(1).
\]
Summing and dividing by \(m\) proves \(m x_m^\alpha\to(\alpha C)^{-1}\). Substitution into \(y_m=h x_m^\kappa\) gives all three pairs of limits displayed above. When \(\kappa=1\), the scalar equation is \(u_m'=-[a e^{r_1s}+b h e^{r_2s}]u_m^2\), which integrates exactly to \(x_{m+1}^{-1}-x_m^{-1}=aI_1+b h I_2\), proving the asserted finite-cycle formula.

**Physical-time envelope.** The bound on \(\log(x_m/u_m(s))\) gives \(x(m\tau+s)=e^{r_1 s}x_m[1+o(1)]\) uniformly in \(s\). Since \(v_m(s)=h u_m(s)^\kappa\), the same holds for the second population. The multipliers are uniformly bounded on each finite cycle, so both species tend to zero at all physical times, including pulse instants.

## Verification

The supplied `verify.py` numerically integrates the exact scalar cycle for \(\kappa\in\{1/2,1,2\}\) at positive, unequal intrinsic growth rates. It compares the normalized post-pulse states after 4000 cycles with all six analytical limiting constants, and it checks the exact interspecies power invariant in the original two-dimensional system within numerical integration tolerance. The exact value of the coefficient \(C\), the monotonicity argument, and the infinite-time conclusions are proved above; numerical sampling is not used as their proof. Run `python verify.py` after installing the package listed in `requirements.txt`.

## Relationship to prior work

Courcelle, MacDonald and Patel (2026, arXiv:2609.09343v1) develop a general permanence framework for periodic multiplicative pulses; their Theorem 4.3 applies under **strictly positive** pulse-adjusted intrinsic growth rates and strict invasion inequalities. The present result lies at **simultaneously zero** adjusted intrinsic rates and determines rates of extinction rather than permanence. Schreiber (2025, arXiv:2507.02157) studies invasion-growth-rate criteria for flow-kick persistence and extinction, but the relevant strict-sign criteria do not determine this double-critical rank-one asymptotic law. Jin, Han and Li (2005) study persistence and extinction for impulsive competition; accessible bibliographic material does not settle whether their full text contains this particular degeneration. The exact power invariant, exponent trichotomy, limiting constants and uniform within-cycle envelopes are not implied by the accessible statements of those results. No claim of definitive historical priority is made.

## Limitations

The critical pulse factors must exactly cancel each species' intrinsic linear growth over each cycle, and the competition rows must be exactly proportional. No universality is asserted for perturbations of these equalities, nonperiodic pulses, stochastic dynamics, or higher-rank competition matrices. Only strictly positive initial populations are covered. Numerical checks cover finite examples and do not independently certify the analytic theorem; a separate independent review has not been performed.

## References

1. E. Courcelle, J. S. MacDonald, S. Patel, *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses*, arXiv:2609.09343v1 (first posted September 8, 2026), https://arxiv.org/abs/2609.09343.
2. S. J. Schreiber, *Coexistence and Extinction in Flow-Kick Systems: An Invasion Growth Rate Approach*, arXiv:2507.02157v1 (July 2, 2025), https://arxiv.org/abs/2507.02157.
3. Z. Jin, M. Han, G. Li, *The persistence in a Lotka–Volterra competition systems with impulsive*, Chaos, Solitons & Fractals 24 (2005), 1105–1117; DOI: 10.1016/j.chaos.2004.09.065. Full text not inspected.
