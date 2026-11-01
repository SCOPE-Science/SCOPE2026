# Mathematical assessment

## Correctness
PASS. The reduction to a triple \((k,h,\ell)\) is exact for all labelled initial configurations because every nonhub clique vertex sees the same clique except itself and the hub has the unique leaf neighbor. The one-step equations treat ties correctly. Explicit even- and odd-parity threshold ranges cover every triple with \(h=0\); bit complementation covers the other half. The periodic-entry and binomial basin calculations follow from the disjoint cases; two standalone programs corroborate both the reduced case split and direct labelled-vertex updates. No finite-size extrapolation is needed for the theorem.

## Originality
PASS, qualified. The classical period-at-most-two theorem and the standard clique's majority behavior are not new. The exact one-leaf perturbation, sharp parity-dependent three-versus-two update cutoff, absence of transient attraction into two-cycles and fully labelled basin census are not supplied by the inspected 2014 random/unimodular majority study or by the 2015 general voting-time bounds and clique-module argument. Searches also considered lollipop and threshold-graph variants, and related exact classifications on complete split, clique corona, clique windmill and bridged-clique graphs. These have different adjacency rules and their recorded conclusions do not imply the present theorem. Residual risk: an unindexed or inaccessible specialized treatment may have the same formula.

## Value
PASS. A single pendant leaf is a minimal, natural perturbation of complete-graph voting. The theorem reveals that clique parity sends the same central-binomial-sized exceptional collection to distinct phases: maximal-delay consensus trajectories versus primitive period-two orbits. It provides complete first-entry data, exact basins and their asymptotic proportions for every clique size; this is not an arbitrary finite-table recomputation.

## Scientific limits
No claims concern several leaves, longer tails, other majority conventions, arbitrary threshold graphs, or stochastic/asynchronous rules. Finite test logs are corroboration rather than an infinite proof. The status records a self-review only.

Self-review: passed. Independent audit: not yet performed.
