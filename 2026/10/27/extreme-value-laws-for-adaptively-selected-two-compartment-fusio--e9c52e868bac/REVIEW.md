# Scientific review: adaptive complementary fusion

## Correctness — PASS

The claim is exact for independent, equally loaded Poisson A/B counts, complete local reaction and one adaptively selected pair. For each realized imbalance vector, the maximizing pair consists of the largest positive and the largest negative imbalance; hence its gain is the minimum of their magnitudes. Inclusion–exclusion over the three disjoint sign-threshold categories proves the finite-pool survival law. For fixed loading, a Poisson point-probability lower bound and a Chernoff upper bound sandwich the Skellam right tail at logarithmic scale, giving the sharp \(\log C/\log\log C\) probability and mean limits. The high-loading statement is explicitly sequential: a fixed-dimensional Poisson-difference central limit theorem, continuous mapping, and Mills' ratio give the two-independent-Gumbel minimum law. The 131-check standalone finite verifier executed successfully; it is corroboration, not a substitute for the proofs.

## Originality — PASS, subject to independent review

The closest source is Rubinovich–Polak, arXiv:2607.03549v1/v2. Their Eq. (7) gives hidden fusion capacity for a prescribed grouping; Eq. (4) and Supplement A give symmetric Poisson/Skellam moments, and Supplement F addresses equivalent Poisson-loaded compartments. These are explicitly used as known ingredients. The new question optimizes a single pair **after** observing the entire candidate pool and proves the resulting exact two-extreme finite law and separate pool-size/loading scaling regimes. Searches for adaptive opposite-sign Skellam pairing, optimal microreactor fusion, and its extreme-value limits did not identify a matching theorem. Classical Poisson/normal extremes and experimentally motivated active droplet sorting are acknowledged, not rebranded as new. The main text and visible portions of the supplement were read; some supplemental material and the full text of the experimental sorting article were unavailable, leaving possible implicit priority.

## Value — PASS

A restriction to one secondary fusion makes partner selection a meaningful scarce operation. The fixed-mean result proves that observant sorting yields an unbounded \(\log C/\log\log C\) expected burst advantage over a predetermined pair while selecting just two compartments, and the finite exact formula predicts nonzero-burst reliability for arbitrary pool size. The sequential high-loading law resolves how the limiting variability changes when molecular counts become Gaussian before extreme selection. The result is a motivated, quantified resource-selection law, not a recomputation of the mean capacity of a predetermined fusion tree.

## Relationship and limitations

The result relies on independent symmetric Poisson loading, ideal local completion, perfect measurement and a single selected pair. It makes no claim about finite-time kinetics, full experimental performance, simultaneous large-load/pool crossover, or optimal multi-pair matching. The published capacity identity and known extreme-value lemmas remain prior work. Primary prior work: L. Rubinovich and M. Polak, arXiv:2607.03549; active sorting context: DOI:10.1039/C7LC00745K; standard Gaussian maxima: arXiv:1308.5541.

Self-review: passed. Independent audit: not yet performed.
