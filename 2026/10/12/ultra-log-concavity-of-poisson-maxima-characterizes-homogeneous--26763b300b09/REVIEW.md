# Scientific review: Poisson-maximum ultra-log-concavity rigidity

## Correctness — PASS

The exact event \(M\le k\) gives a product of Poisson CDFs. For equal rates the mass factors as a Poisson pmf times a log-concave synchronized sum, proving every ultra-log-concavity inequality. For unequal rates, the product-difference telescoping formula yields a normalized pmf consisting of a constant contribution from the largest rate and an exponentially small positive contribution from the second-largest distinct rate. Squaring consecutive terms gives a rigorously negative limiting curvature. Finite exact-rational checks independently corroborate cases but are not used as proofs of asymptotic or infinite-domain claims.

## Originality — PASS (subject to independent priority review)

The most directly relevant source, Badiella, del Castillo, and Puig (2023, Theorem 2), proves ultra-log-concavity preservation for i.i.d. discrete order statistics. It covers exactly the homogeneous sufficiency direction but not the heterogeneous necessity statement or asymptotic constant. Chowdhury, Kundu, and Mishra (2021, Theorem 3.1) compare heterogeneous Poisson maxima via majorization and ordinary stochastic order, which does not imply the asserted curvature conclusion. Yu (2009) studies relative log-concavity to compare distributions and mixtures, without analyzing heterogeneous Poisson sample maxima. Searches under terms including relative log-concavity, Poisson maximum, independent nonidentical order statistics, mixed-rate extrema, and the second-largest-rate correction did not reveal a stronger covering result. This search is not a proof of novelty; older work using different terminology remains a residual risk.

## Value — PASS

The result resolves a structural classification across **all** positive finite intensity vectors, showing that the well-known i.i.d. ultra-log-concavity phenomenon is rigid: any nontrivial rate heterogeneity eventually destroys it. The exact leading negative curvature identifies its scale and which rate levels control it. This is relevant to the use of Poisson order statistics and shape-constrained count modeling, without implying any unproved claim about ordinary log-concavity or dispersion.

## Limitations and reproducibility

Only finite samples with independent, fixed-rate Poisson coordinates are covered. The theorem does not supply a uniform first failing index or extend to a varying-rate triangular array. The reported rational cases were reproduced by `python3 verify.py`; the proof establishes the infinite claims independently. No independent audit or external priority certification was performed.

Self-review: passed. Independent audit: not yet performed.
