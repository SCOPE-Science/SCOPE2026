# Scientific assessment

## Correctness — PASS

Splitting a disconnected coalition strictly removes enemies without removing friends, so all positive-product optima have connected coalitions. The exact utilities for a proper arc give the product recurrence. The finite threshold is computed by exact integer arithmetic, while two explicit monotonic comparison functions handle all larger even and odd cycle lengths. The asymptotic inequality is proved from endpoint and interior utilities, and a near-balanced constructive partition gives the matching upper bound. An independent subset enumeration and full replay of the included verifier corroborate the finite cases, without being treated as an infinite proof.

## Originality — PASS, with residual priority risk

The closest primary source, Pagano and Schlenga, *Nash Welfare in Additively Separable Hedonic Games* (arXiv:2605.19030v1), investigates the exact same additive friend/enemy values and a general approximation algorithm. Its Section 4 and appendices do not derive this cycle-family sharp threshold, exact product formula or asymptotic coalition-size law. Elkind, Flammini and Varricchio (arXiv:2512.20261v1) optimize egalitarian welfare instead; earlier fractional-hedonic literature averages coalition utility and does not imply this unnormalized product statement. Published mathematical-record and targeted literature searches identified no exact counterpart. A relevant unindexed or differently formulated result remains possible.

## Value — PASS

The paper's general approximation guarantees leave open exact behavior even on highly structured friendship graphs. The smallest family where the grand coalition ceases to optimize Nash welfare, exact computability for the whole cycle family, and the emergent \(\sqrt n\)-scale coalition size give motivated structural and quantitative information, not a routine evaluation of one fixed finite instance.

## Limitations

No claim is made for arbitrary friendship graphs, other friend/enemy weights, or stability. The supporting finite verifier does not prove the full asymptotic formula. Independent validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
