# Self-review

## Correctness — PASS
For the scalar repeated-row model, exact projection reduces to a two-value update. Conditioning on the hypergeometric number of corrupted sampled rows gives both transition probabilities without approximation. Comparing disjoint, partitioning and overlapping integer-tail events proves the rank-dependent correlation sign. The median depends only on the fresh subset majority, so its iterates are iid; geometric hitting times, the exact safe cutoff, and infinite-time recurrence follow. The asymptotic proof uses uniform finite-population-to-binomial reduction, Stirling's formula, and a geometrically dominated tail; this is not inferred from finite experiments. Reproducible finite enumerations and approximations provide additional checks.

## Originality — PASS (publication-priority risk remains)
Haddock–Ma–Rebrova (2023, Algorithm 2 and Section V-D) motivates precisely the constant-sized sample issue and remarks on occasional corrupt updates, but offers only a heuristic and experiments for that case. Their Algorithm 1 is materially different. The foundational 2020 quantile-based Kaczmarz paper, the Cai–Chen–Ma–Wu (2025) general sample-size analysis, and the Battaglia–Ma (2025) error-horizon analysis were compared at the level of row-selection mechanisms and claimed implications. None among the examined texts states the full sampled-row equality Markov law, odd-quantile serial-correlation phase, iid median property, or sharp hypergeometric observation horizon. Generic rare-event and logarithmic sample-size observations are acknowledged as prior; published literature outside the examined sources may contain equivalent special-case calculations. Searches do not prove uniqueness.

## Value — PASS
The 2023 paper explicitly identifies small-sample quantile and subset-size guidance as a future theoretical problem. The exact median iid law distinguishes short-run empirical robustness from almost-sure long-run failures; the rank correlation reversal and zero-risk cutoff are sharp structural information useful as a diagnostic benchmark. The sharp prefactor gives quantitative experiment-horizon planning in the stated scalar model; no practical high-dimensional convergence claim is made.

## Boundaries and remaining uncertainties
This classification is for identical scalar unit rows, binary corruption, fresh uniform subsets without replacement, exact projection, and rank-equality selection. It is not an analysis of the threshold-accepted algorithms or arbitrary nonlinear/nonscalar systems. The explicit large-sample limit requires fixed corruption fraction below one-half and negligible finite-population dependence. Publication-priority checks do not substitute for independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
