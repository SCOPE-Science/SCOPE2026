# Self-review

## Correctness — PASS

The generator is reversible and has the unique uniform stationary distribution. The Feynman–Kac semigroup decays because the only undamped Markov vector cannot be an eigenvector of the nonconstant phase generator. A direct \(3\times3\) resolvent calculation establishes the exact positive spectrum. The derivative in squared frequency reduces to a cubic with strictly positive discriminant, and the signs of its coefficients, roots and pairwise sums give a complete count at all positive rates and both quartic-flat boundaries. The standalone code reconstructs these identities and checks 120 unrelated complex-resolvent evaluations to within floating-point precision. Finite tests are not substituted for the analytic all-parameter proof.

## Originality — PASS, provisional

The full inspected Březina et al. (2022) article explicitly covers the **general three-state spectral formula**, so no originality is attributed to that formula or to Kubo–Anderson methods. The inspected source's coalescence analysis, including the listed supplementary topics, addresses two-state transitions and three-state fast-exchange reductions, not the two exact critical ratios and complete three/two/one peak topology here. Komijani and Coleman (2016) give the older stochastic-modulation setting. A 2012 Kovrigin primary article studies numerical regimes of three-state exchange, but its full text was inaccessible; prior graphical coverage remains possible. Accessible previous research records and published semantic results supplied no equivalent statement. An absence of search results is not a proof of historical priority.

## Mathematical value — PASS

The theorem supplies exact diagnostic boundaries for a natural symmetric three-conformer exchange model. A second transition after the central resonance becomes a trough shows that one cannot identify the number of environments by the number of observed local peaks. The two nontrivial algebraic thresholds and quartic-flat transition classification offer a complete, reusable ideal benchmark rather than an arbitrary isolated parameter calculation.

## Scope and residual risk

The result is for stationary equal-rate nearest-neighbor exchange, frequency offsets \(-\Delta,0,\Delta\), and no homogeneous linewidth. The inaccessible Kovrigin full text, specialized historical NMR coalescence studies and implicit consequences of the broad 2022 resolvent remain priority risks. Strict local maxima need not be experimentally resolvable. No independent scientific audit or novelty certification has been performed.

Self-review: passed. Independent audit: not yet performed.
