# Scientific assessment: directional first-detour and successful-duration laws

## Correctness — PASS

Every allowed hop/reset event has an exponential waiting time of rate \(r+2d\); a prescribed successful first-hit route of length \(n\) has probability \((r+2d)^{-n}\). The first-detour enumeration is exact: a route of length \(L+2\) has one redundant opposite pair in a unique coordinate, and precisely two length-two loops per shortest path must be removed because they hit the target at step \(L\). Positivity, parity and an absolutely convergent path-counting tail yield the fixed-dimensional laws. The Gamma mixture and its sharp total-variation coefficient follow from exact conditional waiting times and the unique density crossing. The large-dimensional result is supported by a dominated Bessel-series resolvent expansion at fixed positive \(r/d\). The included self-contained checker passed 360 exact finite calculations/comparisons; these do not substitute for the infinite-parameter proof.

## Originality — PASS, with residual risk

Hartmann and Majumdar (arXiv:2505.19903v1, especially Section V.3 and Figure 5) already establish the lattice search model, exact unmarked mean-first-passage/Green functions, and an observed tendency of final successful trajectories to be shortest. That aggregate information is prior. Linn and Lawley (arXiv:2302.05409v1) already prove universal large-reset distribution laws for the **total** first-passage time on discrete networks and identify geodesic effects. The stated contribution is distinct: it derives the coordinate-labeled first nonminimal route law, the associated *successful-segment* Gamma total-variation correction, and analytic leading coefficients for the high-dimensional Figure 5 observation. The unmarked correction is algebraically extractable from Hartmann–Majumdar's exact Green functions; possible interpretation of the new result as a natural refinement of known renewal/path enumeration remains a genuine originality risk. Other nearby papers on extreme network first passages or reset costs have distinct observables; not every primary full text was accessible or inspected.

## Mathematical value — PASS

The motivating lattice study measures the number of hops after the last reset and notes shortest-path domination in two asymptotic regimes without a quantitative rate. The finding makes that specific observable precise, distinguishes longitudinal versus transverse first detours, and determines a sharp error coefficient for treating the entire final search duration as a Gamma law. It also gives concrete \(1/d\) coefficients at the empirically relevant scaling \(r=2d\). These are motivated finite-cutoff/path-geometry and measurement-accuracy facts, not arbitrary parameter substitutions. No claim is made to a new first-passage renewal principle or a result for general weighted graphs.

## Closest sources and scientific limitations

- Hartmann and Majumdar, *Diffusion with stochastic resetting on a lattice*, arXiv:2505.19903v1 (2025), complete relevant paper text and algorithm/Section V.3 inspected; full Green structure implies some unmarked corrections, while marked detour and sharp Gamma-distance laws are not stated.
- Linn and Lawley, *First-passage times under frequent stochastic resetting*, arXiv:2302.05409v1 (2023), complete relevant sections 2, 3.3 and Appendix 5.3.3 inspected; total arrival-time theorems and shortest-network-route dominance are acknowledged.
- Lawley, *Extreme first-passage times for random walks on networks*, arXiv:2008.04496v1 (2020), abstract inspected; extreme-many-searcher limit is a different regime.
- Sunil et al., *The cost of resetting discrete-time random walks*, arXiv:2503.03697v1 (2025), abstract inspected; total cost and continuous jump spaces, not the specified marked lattice successful trial.

The fixed-dimensional asymptotic is not uniform in growing dimension; the separately proved high-dimensional statement is restricted to a distance-two axial starting point and \(r/d\) fixed positive. Results are not finite-parameter error bounds for arbitrary parameters. Independent review remains necessary, especially for implicit prior coverage.

Self-review: passed. Independent audit: not yet performed.
