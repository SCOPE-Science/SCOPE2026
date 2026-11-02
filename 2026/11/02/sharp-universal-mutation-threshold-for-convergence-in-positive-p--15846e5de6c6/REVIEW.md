# Review

## Correctness — PASS

The equation, payoff normalization and mutation convention match the stated multiplayer game. A complete proof establishes invariant interval, unique strictly transverse fitness-odds intersection for \(q\ge(d-1)/(2d)\), attraction from both simplex endpoints, the \(q=1/2\) case and an explicitly positive family with at least three equilibria for every \(0<q<(d-1)/(2d)\). Exact algebra and Sturm counts were rerun using the accompanying source file. Finite tests do not certify the infinite statement; the analytical inequalities do.

## Originality — PASS

Duong–Han (arXiv:1904.09805) give the identical \(d\)-player replicator–mutator model and a payoff-conditional polynomial root-count procedure; this does not state or imply the degree-only bound without the new Bernstein log-slope comparison. Chen–Deng–Duong–Han (arXiv:2303.16558) and Duong–Han (arXiv:2107.06025) study distributions of equilibrium counts in pairwise games with payoff restrictions that differ. Search checks against related published mathematical summaries and source papers disclosed no precise or stronger coverage. An analogous threshold may exist in obscure or unindexed mutation–selection literature; non-discovery is not a priority guarantee.

## Mathematical value — PASS

The threshold precisely characterizes how much symmetric mutation eliminates all payoff-dependent multistability in two-strategy multiplayer games with positive payoffs. The sharpness example quantifies necessity rather than merely giving a sufficient condition. The dependence on group size distinguishes multiplayer from pairwise dynamics.

## Scope and limits

No statement is made for mutation-free, more than two strategies, asymmetric mutation, additive mutation, negative/zero fitness, or noisy sampled populations. Only local exponential rates—not a uniform payoff-independent rate—follow. The result has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
