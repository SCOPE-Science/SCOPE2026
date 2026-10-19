# Scientific review: bipartite exclusion jump-count noise

## Correctness — PASS

For all integers \(a,b\ge1\), \(N=a+b\ge4\), and \(1\le k<N\), the stationary configuration law is uniform and the part-occupancy chain has hypergeometric weights and rates \(u_j=(a-j)(k-j)\), \(d_j=j(b-k+j)\). Its centered linear and quadratic modes have the exact relaxation rates \(N\) and \(2(N-1)\). The total successful-hop intensity is a quadratic polynomial in part occupancy, so the tilted-generator second derivative reduces to just these modes. Exact falling-factorial moment calculations give the displayed rational nonnegative decomposition; every denominator is positive on the scope. Equality cases and the \(N^{-1/4}\) scaling follow directly. The packaged program passed 59 independent full-state exact-rational Poisson-equation comparisons and one symbolic all-parameter fourth-moment identity; these are checks of, not replacements for, the analytical proof.

## Originality — PASS within inspected sources; residual risk

Mendonça (arXiv:1207.4106, Sections 2, 4, and 6) already solves the unperturbed complete-bipartite exclusion generator and its spectrum, but the inspected material does not derive the long-time *total successful-hop count* variance, the two positive components, the complete Poisson equality cases, or the joint balance law. Stinchcombe and de Queiroz (arXiv:1202.0774, Introduction and Section II opening) study snapshot activity, explicitly distinguishing it from integrated current, and their graph is a one-dimensional directed exclusion chain. Roche, Derrida and Douçot (arXiv:cond-mat/0312659) furnish a general full-counting-statistics context; only bibliographic/abstract material was inspected, so their work cannot be used to exclude every more general reduction. Targeted prior-database and published-literature searches found no exact matching claim, but non-retrieval is not proof of uniqueness. The possibility that a general Hahn-polynomial, Bernoulli–Laplace, or tilted-spin result already implies the formula is a genuine residual risk.

## Mathematical value — PASS

The total jump count is a physical kinetic observable distinct from the instantaneous number of active edges and from macroscopic particle drift. The formula resolves its long-time noise for *every* bipartition and conserved inventory, describes exceptional cases where the count is exactly Poisson, and exposes a two-channel balance mechanism with an unusual \(N^{-1/4}\) joint scaling and explicit crossover constant. This provides an all-size structural classification, not a recomputation of the generator spectrum or an arbitrary finite-parameter example. No higher cumulants, dynamical large-deviation function, or limit theorem for the whole event process is asserted.

## Closest literature and limits

- Mendonça, arXiv:1207.4106: same graph and process, ordinary spectrum; preexisting ingredient rather than same evaluated counted-activity claim.
- Stinchcombe–de Queiroz, arXiv:1202.0774: same terminology, different *instantaneous* activity variable and different topology/directionality.
- Roche–Derrida–Douçot, arXiv:cond-mat/0312659: broader full-counting-statistics methods, accessible abstract only; equivalence cannot be categorically excluded.

The mathematical conclusion is restricted to homogeneous complete bipartite exclusion at fixed particle number and stationary long-time cumulants. Independent historical verification remains important.

Self-review: passed. Independent audit: not yet performed.
