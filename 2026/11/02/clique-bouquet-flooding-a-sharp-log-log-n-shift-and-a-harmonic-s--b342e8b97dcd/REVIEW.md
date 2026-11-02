# Scientific review

## Correctness — PASS

For each petal of \(m\) vertices and the common hub, exponential first-passage exploration is a pure-birth chain with exact rates \(k(m+1-k)\), \(k=1,\ldots,m\). Independent petals give the hub-source maximum. From a peripheral source, the uniform rank of the hub and the independent exponential holding times give the finite decomposition. The two slow terminal stages both have rate \(m\); the internal exponential moment telescopes to \((m-1)^2\), fixing the \(t e^{-mt}\) tail and hence the \(\log\log n\) correction. Tail integration establishes convergence of the centered maximum's mean. The exceptional petal's remaining completion time is negligible compared with the other petals' maximum, and its mean entry delay is exactly \(H_m/m\). The proof covers all finite \(n,m\) and the fixed-\(m\) limit. The independent checker passed 187 exact and numerical tests, including direct full-graph rational recurrences, but those tests are not used as a proof of the limit.

## Originality — PASS, qualified

The closest source is Leskelä and Ngo, arXiv:1806.09568 (first posted 2018-06-25), whose configuration-model assumptions require bounded \((2+\epsilon)\)-degree moments and thus exclude the hub's diverging degree. Mountford and Saliba, arXiv:1909.04563, study flooding in random configuration-model graphs, not this deterministic clique bouquet with exact finite laws. Van der Hofstad and Lodewijks, arXiv:2311.16088, study torus-embedded complete graphs. Public mathematical-record comparisons found related windmill graph structure and epidemic or FPP work, but no implication-equivalent finite classification, precise double-minimum-rate extreme-value center, and peripheral-source harmonic penalty. A failed search cannot prove absence from all literature, and historical priority remains uncertain. Standard pure-birth calculations and classical Gumbel max theory are acknowledged prior ingredients.

## Value — PASS

The generalized friendship/windmill graph models many small dense communities joined at a single articulation hub. Its flooding completion time has a \(\log\log n\) correction not predicted by a lone exponential tail and source placement changes the limiting distribution by a genuinely random additive delay, despite leaving its diverging leading term unchanged. The exact finite law and the \(H_m/m\) source penalty give an interpretable quantitative benchmark for rare slow communities and articulation-point influence. The comparison is structural and exceeds a routine finite-value computation.

## Scientific limits and risks

The asymptotic fixed-petal-size condition cannot be dropped without new arguments; nonexponential edge distributions and growing petal sizes are not classified. Novelty is a best-knowledge literature comparison, not a proof of worldwide uniqueness. No independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
