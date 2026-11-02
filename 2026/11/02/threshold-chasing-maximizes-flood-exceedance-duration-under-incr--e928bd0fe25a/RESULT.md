# Threshold-chasing maximizes flood-exceedance duration under increasing recession laws

## Finding

Fix a hazard discharge threshold \(h>0\) and \(n\geq2\) prescribed positive effective-discharge pulses \(P_1,\ldots,P_n\), each strictly larger than \(h\). Starting from zero discharge, a scalar hydrograph \(q(t)\) follows \(\dot q=-f(q)\) between pulses, and pulse \(P_i\) raises \(q\) instantly by \(P_i\). Assume \(f:[0,\infty)\to[0,\infty)\) is locally Lipschitz, \(f(0)=0\), positive on \((0,\infty)\), and strictly increasing. Both the pulse order and nonnegative inter-pulse intervals may be chosen; the first pulse is fixed at \(t=0\). Define total flood-exceedance duration by \(L=\operatorname{Leb}\{t\geq0:q(t)>h\}\), and the recession clock by

\[
\Phi_h(z)=\begin{cases}0,&z\leq h,\\[3pt]\displaystyle\int_h^z\frac{du}{f(u)},&z>h.\end{cases}
\]

**The exact global maximum** is

\[
L_{\max}=\Phi_h(P_{\max})+\sum_{i:P_i\text{ not the selected largest pulse}}\Phi_h(h+P_i).
\]

Here one occurrence of a maximal \(P_i\) is selected; the sum includes all other occurrences. Every maximizing calendar fires a largest pulse first, and fires each subsequent pulse **exactly when the recession reaches \(h\)**. The remaining pulse order is arbitrary. Conversely, every such calendar is maximizing, and with a unique largest pulse the first event is uniquely prescribed by its size. The required first gap is \(\Phi_h(P_{\max})\); each later gap, after pulse \(P_i\), is \(\Phi_h(h+P_i)\). The optimizer exists with strictly positive gaps because each \(P_i>h\).

For linear recession \(f(q)=kq\) with \(k>0\), the maximum becomes

\[
L_{\max}=\frac1k\log\left(\frac{P_{\max}}h\prod_{i\ne i_{\max}}\left(1+\frac{P_i}{h}\right)\right).
\]

For example, \(h=k=1\) with prescribed pulses \(2,3,5\) gives \(L_{\max}=\log60\). The optimal order \(5,2,3\) uses gaps \(\log5,\log3\), whereas putting all three pulses simultaneously produces duration only \(\log10\).

## Assumptions and scope

This is a deterministic, scalar, zero-initial-discharge event model with \(n\) indivisible instantaneous additive increments in the discharge state; no rain is added after the final pulse. Each increment individually exceeds the chosen hazard threshold. The recession law is autonomous and strictly increasing, but need not be linear, convex, or a power law. The objective is **total Lebesgue time above a fixed level**, not peak discharge, cumulative flow volume, a stochastic exceedance probability, or an optimal control law subject to a fixed terminal horizon. The pulse sequence is finite and all event times must be finite. Equal pulses and simultaneous events are allowed as candidate calendars, but an optimal calendar has positive gaps under the stated strict inequalities.

## Proof

1. The ordinary differential equation has a unique nonnegative forward solution between events. From any positive state it decreases strictly and tends to zero; it reaches a given level \(h>0\) in the finite time \(\Phi_h(q_{\mathrm{initial}})\) when initially above that level. For \(q>h\), the chain rule gives \(d\Phi_h(q(t))/dt=-1\). For \(q<h\), the derivative of \(\Phi_h(q(t))\) vanishes. The times when the solution equals exactly \(h\) form a finite set and have zero Lebesgue measure.

2. Let \(q_j^-\) denote the state immediately before pulse \(P_{\sigma(j)}\). Integrating the recession clock over all continuous pieces, using its initial value zero before the first pulse and its final limit zero after all pulses, gives the **exact telescoping identity**

\[
L=\sum_{j=1}^{n}\bigl[\Phi_h(q_j^-+P_{\sigma(j)})-\Phi_h(q_j^-)\bigr].
\]

3. For any pulse \(P>h\) and any nonnegative pre-pulse state \(y\), define its clock increment \(G_P(y)=\Phi_h(y+P)-\Phi_h(y)\). If \(y<h\), then \(G_P(y)=\Phi_h(y+P)<\Phi_h(h+P)\), because \(y+P<h+P\); this also covers \(y+P\leq h\). If \(y>h\), then

\[
G_P(y)=\int_y^{y+P}\frac{du}{f(u)}<\int_h^{h+P}\frac{du}{f(u)}=\Phi_h(h+P),
\]

since \(1/f\) is strictly decreasing. Equality is attained **if and only if** \(y=h\). The initial state is zero, so its first increment is \(\Phi_h(P_{\sigma(1)})\). Therefore, for any fixed order,

\[
L\leq\Phi_h(P_{\sigma(1)})+\sum_{j=2}^n\Phi_h(h+P_{\sigma(j)}).
\]

4. The bound for a given order is attained: fire the first pulse at zero, wait until discharge decreases exactly to \(h\), fire the second, and repeat at each later threshold return. The successive gaps are finite and strictly positive, and the exact identity of step 2 then attains equality. Equality in step 3 proves this schedule is also the only maximizer for that fixed order.

5. Rewrite the fixed-order optimum as

\[
\sum_{i=1}^n\Phi_h(h+P_i)+H(P_{\sigma(1)}),\qquad H(P)=\Phi_h(P)-\Phi_h(h+P)=-\int_P^{P+h}\frac{du}{f(u)}.
\]

For \(P>h\), the function \(H\) is strictly increasing: if \(P_2>P_1\), strict decrease of \(1/f\) makes its integral over the length-\(h\) interval with left endpoint \(P_2\) strictly smaller. Hence precisely a largest pulse must be used first. Subsequent order does not appear in the optimal value. This proves both the sharp formula and the full equality classification.

6. When \(f(q)=kq\), \(\Phi_h(z)=k^{-1}\log(z/h)\) for \(z>h\). Substitution gives the logarithmic formula and the exact example. No approximation or finite enumeration is used in the general proof.

## Verification

The accompanying self-contained Python 3 script `checker.py` uses exact rational arithmetic to test the sharp upper bound and attainable calendars for \(f(q)=q\) and \(f(q)=q^2\) over 9,000 seeded pulse-parameter sets (six values of \(n\), 1,500 each), making 36,000 primary assertions, plus six permutation checks for an exact three-pulse example. For the linear case the exponentiated duration is a rational product, so no floating-point logarithms are needed. For quadratic recession all segment durations are rational. Run with `python3 checker.py`. The proof, rather than finite tests, establishes the result for all specified increasing recession laws.

## Relationship to prior work

Harman, Sivapalan and Kumar (2009) derive hydrological recession behavior from ensembles of linear reservoirs and examine the response to impulse and periodically varying recharge; they do not establish an optimal finite ordering of arbitrary discharge pulses for maximum threshold-exceedance duration. Gnecco, Palla and La Barbera (2018) investigate how rainfall-event structure affects **maximum runoff peak** under a gamma instantaneous-unit-hydrograph model, a different objective and response class. Lawson et al. (2025) model statistical distributions of **observed duration-over-threshold events**, not the deterministic extremal timing of specified impulses. These comparisons concern the authors' stated models, equations and conclusions, not a claim of exhaustive historical novelty. Generic optimal-impulse/rearrangement results might contain a more general statement from which this result follows; independent historical-priority evaluation remains necessary.

A related finite-capacity repeated-storm model studies saturation-excess *runoff volume*. That model has a different state constraint, periodic input assumption, and objective; its equal-storm spacing ordering does not imply this theorem about continuous scalar recession, nonidentical event magnitudes and exceedance duration.

## Limitations

This exact result does not model rainfall pulse duration, rainfall-to-discharge conversion, spatial routing, storage bounds, antecedent inflows, correlations, stochastic rainfall or a prescribed finite evaluation horizon. Additive jumps in discharge are an idealization and are not automatically equivalent to additive **rainfall-depth** inputs in a nonlinear storage-release model. The requirement \(P_i>h\) is substantive: smaller pulses may have to combine to initiate an exceedance, and the stated equality classification is not asserted for that regime. Likewise, strict increase of \(f\) is used in both the unique threshold-trigger characterization and the first-largest rule. The mathematics identifies an extremal hazard scenario, not a prediction that natural storms follow the optimizing schedule.

## References

1. Harman, C. J., Sivapalan, M. and Kumar, P. (2009). *Power law catchment-scale recessions arising from heterogeneous linear small-scale dynamics*. Water Resources Research 45, DOI: https://doi.org/10.1029/2008WR007392 (first online September 9, 2009).
2. Gnecco, I., Palla, A. and La Barbera, P. (2018). *A dimensionless approach for the runoff peak assessment: effects of the rainfall event structure*. Hydrology and Earth System Sciences 22, 943–956. https://doi.org/10.5194/hess-22-943-2018.
3. Lawson, K. S., Underwood, K. L., Diehl, R. M. and Rizzo, D. M. (2025). *A Duration-Over-Threshold Model for Flood Frequency and Flow Regime Characterization*. Water Resources Research 61. https://doi.org/10.1029/2023WR037022.
