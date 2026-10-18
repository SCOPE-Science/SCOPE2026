# Scientific review

## Correctness — PASS

The stated theorem has two independently verifiable parts. For each unordered pair of positions the randomized product has one of three second moments according to whether two graph edges are equal, incident, or disjoint. Counting these overlaps, exploiting the deterministic sum of all lag classes, and diagonalizing the resulting two-block matrix yields every displayed covariance and both parity spectra. The nonnegative scale \(\Lambda\) is one-quarter of a squared four-position difference expectation times \(n\); it vanishes exactly when all but at most one fixed sample value agree. The generic support theorem follows from algebraic independence, graph-edge polynomial coefficients, the disjoint-cycle structure of each lag graph, and exact automorphism-group orders. The executed verifier passed 737 exact arithmetic assertions; infinite cases rest on the proofs rather than enumeration.

## Originality — PASS on inspected evidence, with risks

The qualifying Romano–Tirlea 2020 preprint concerns exchangeability-based time-series permutation tests and ordinary endpoint-truncated lag correlations. Zhou et al. (2013) already derive general quadratic-form permutation moments, so the raw existence and computation of the covariance entries are **not** claimed novel. The mathematical distinction here is the simultaneous explicit parity-dependent all-lag spectrum and, particularly, a generic exact gcd-sensitive support census showing that equal variance need not mean equal permutation tail resolution. The cited general moment results do not establish the atom support, and no inspected record supplies the combined theorem. Older Daniels and Hallin–Puri material was only partly accessible, and related stabilizer orbit formulae may be known elsewhere. Independent historical priority is unverified.

## Value — PASS

Circular lag-product scores are natural randomization statistics. The exact finite-sample covariance modes determine multivariate second-order calibration, while the generic orbit counts determine the size of the exact p-value grid for every lag, irrespective of any normal approximation. The length-nine factor-72 difference between supports of lags one and three, despite identical variance, is a substantive statistical boundary that motivates retaining the support theorem rather than presenting another generic moment computation.

## Scope and evidence

The covariance applies to any fixed real observations for \(n\ge4\). The orbit law applies only under algebraic independence, almost surely for absolutely continuous observations. The verifier checks finite examples through eight positions; exact general proofs are explicit in `RESULT.md`. Source inspections and unresolved coverage risks appear in `AUDIT.json`. No independent mathematical audit or global historical-priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
