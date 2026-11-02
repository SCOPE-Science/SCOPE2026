# Scientific review

## Correctness — PASS

The new theorem concerns two rate-\(\lambda_i\) irreversible competing infections from distinct peripheral seeds on \(K_{2,n}\). Conditional on the first infected hub, the opposite-color seed clock races one winner-color seed clock and \(n-2\) independent two-stage exponential sums. This gives the exact integral and finite rational series for core coexistence. A uniform Laplace expansion gives \(\sqrt{\pi/(2n)}\) and the second-order rate-dependent correction. Conditioning on a rare core split yields a half-normal bridge time, \(o(n)\) early peripheral infections, and independent binomial late infection types, proving the conditional fractions and minority moment growth. An independently implemented four-count Markov-chain recurrence matched the closed-law calculation in all supplied exact finite tests. Numerical asymptotic diagnostics are not substituted for the all-order proof.

## Originality — PASS, with residual historical risk

Deijfen, van der Hofstad and Sfragara (arXiv:2204.04125, 2022) prove winner-takes-all-but-one for a heavy-tailed random configuration model, whereas this theorem provides a fixed deterministic two-hub graph's *exact finite-size probability*, sharp second-order expansion, and anomalous minority moments. Ahlberg, Deijfen and Janson (arXiv:1711.02902, 2017) assume a sparse finite-variance-degree configuration model; Deijfen and van der Hofstad (arXiv:1306.6467, 2013) study a distinct infinite-variance random-graph regime. Their actual statements and hypotheses do not imply the present formula. Directed searches for two-type biclique competition, equivalent loser-size/core-split events, and related tables found no dominating result. This is a best-knowledge scientific comparison, not a proof of historical priority; a not-indexed exact calculation remains possible.

## Value — PASS

The statement resolves a naturally measurable probability of two-type core coexistence on a simple heterogeneous network, explaining exactly how a rare successful minority bridge occurs. It shows the surprising rate-universality of the leading square-root probability and its failure one order lower. It also establishes that a minority outbreak which almost surely reduces to one seed can nevertheless have expected size diverging as \(\sqrt n\) and variance growing as \(n^{3/2}\). This distinguishes typical and rare-event epidemic risk in a way not captured by a limit asserting only winner-takes-all.

## Sources and limitations

Primary literature: Deijfen, van der Hofstad and Sfragara, *The winner takes it all but one*, https://arxiv.org/abs/2204.04125 (first public version 8 April 2022). Supporting comparisons: https://arxiv.org/abs/1711.02902 and https://arxiv.org/abs/1306.6467. The theorem does not cover changing rates, recovery, more than two hubs, other source placements, or random graph models. The computation is independently structured but does not constitute an independent human mathematical audit.

Self-review: passed. Independent audit: not yet performed.
