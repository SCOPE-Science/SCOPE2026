# Independent mathematical audit

## correctness

PASS

The conditional inclusion probabilities are p_i=2x_i−x_i² and EΔT=2−Q, so the exact quotient update gives mean increment x_i(Q−x_i)/T+O(T⁻²), uniformly. For V=Q, the one-step Lyapunov decrease is governed by G=Σx_i³−Q²=Σx_i(x_i−Q)². The almost-supermartingale estimate proves ΣG(X_n)/T_n<∞. In the time scale with mesh 1/T_n, G has uniformly bounded slope after linear interpolation, and its integral is finite (the interpolation error is bounded by a summable multiple of T_n⁻²). Nonnegative Lipschitz spikes of fixed height would have fixed positive area, so G→0. The zero set is finite and the one-step changes vanish; disjoint neighborhoods of its points cannot be exchanged without leaving their union, so the limit is one such point. Each U_i diverges by conditional Borel–Cantelli using p_i≥U_i(0)/(T_0+2n). For log X_i the two log-increments give drift (Q−x_i)/T with error O(1/(U_i T)+T⁻²); this uses p_i≤2U_i/T. The centered increments have variance O(1/T). Dividing them by log(n+2) gives a square-integrably convergent martingale since Σ1/((T_0+n)log²(n+2))<∞; Kronecker's lemma then gives an unweighted martingale sum o(log n). An omitted colour at a putative size-s limit would instead have eventual positive conditional log drift asymptotic to 1/(sT), whose cumulative sum dominates a positive multiple of log n. This contradicts log X_i≤0. The proof holds for every stated positive initial composition.

## originality

PASS

The update is a special case of an established replacement-function model, and its Lyapunov and martingale tools are classical. The distinct content is an all-positive initial-state almost-sure limit for this non-balanced multicolour rule. Inspected general urn theorems either require fixed balance or supply an ODE limit-set/conditional convergence result without boundary exclusion. The two-colour analogue is already covered by the non-balanced two-colour theorem; it is not part of the claimed novelty.

## value

PASS

Suppressing repeated additions is a simple, symmetric update with a genuinely random total increment and quadratic mean reinforcement. The exact uniform limit is not a finite-time symmetry identity: symmetry admits several face equilibria, and the proof identifies why an initially present but rare colour cannot be lost in proportion. It supplies an interpretable multicolour example outside the balanced theorem, not a claimed solution for all non-balanced urns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
