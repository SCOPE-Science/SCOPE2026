# Scientific review

## Correctness — PASS

The theorem is proved for an increasing two-sided filtration, adapted variables bounded by one, and deterministic positive integer horizons. Interval coloring yields at most \(\Delta\) classes of disjoint windows. Within each class the centered terms are martingale differences bounded by two. Conditional Hoeffding, generalized Hölder, Cauchy–Schwarz, and Chernoff optimization give the displayed constant \(8\). The proof covers arbitrary finite \(N\); no finite experiment is used to support a universal statement.

## Originality — PASS

The closest inspected primary result is Vovk's fixed-horizon law of large numbers, which assumes a single common horizon \(K\). The present statement handles arbitrary deterministic \(K_n\) through maximum window overlap \(\Delta\). The example with one horizon equal to \(N\) and all remaining horizons equal to one shows why the maximum horizon can be an unnecessarily coarse parameter. Searches did not locate a statement-level equivalent, but they cannot prove absolute novelty.

## Value — PASS

The overlap parameter measures how many forecast windows can be active at one information time. The resulting finite-sample inequality gives a useful criterion, \(\Delta_N=o(N)\), for asymptotic unbiasedness even when the largest individual horizon is not sublinear. The theorem is a sufficient bound; no universal sharpness claim is made.

## Closest literature and limitations

V. Vovk, “A law of large numbers for predicting several steps ahead,” arXiv:2508.17507, first posted 24 August 2025; later published in *Statistics and Probability Letters* 236 (2026), article 110785. Its theorem concerns a common horizon and does not state the variable-horizon overlap bound. A general dependent-risk aggregation paper was located through its metadata and abstract, but its full text was not accessible; it remains a residual literature risk. Random or data-adaptive horizons and unbounded variables are not covered.

Self-review: passed. Independent audit: not yet performed.
