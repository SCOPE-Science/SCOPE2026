# Scientific assessment

## Correctness — PASS

For each integer \(1\le c<g\), each batch size \(1\le s\le g\), and every rank \(1\le j\le s\), the unit-row projection sends any input to one of the two observed right-hand sides. The hypergeometric count \(K\) gives two exact transition tails, and the rank-one nonconstant eigenvalue determines the invariant law and all stationary correlations. The strict rank monotonicity follows from a positive, increasing likelihood-ratio sequence; the sharp zero-error cutoff is the absence/presence of an all-corrupt batch. The even/odd correlation phase follows from complementarity or overlap of the count tails. The replacement variant follows independently by binomial counting. These are exact proofs for all admissible integer parameters, supplemented by 2,174 exact rational checks and exhaustive subset enumeration for small systems. The checks do not stand in place of infinite-parameter reasoning.

## Originality — PASS, with stated residual risk

The relevant small-sample algorithm is Section V-D/Algorithm 2 of Haddock–Ma–Rebrova (2023), which reports empirical sensitivity to the small-batch quantile and identifies exact optimal-sample/quantile theory as a future direction. Its main proportional-batch theorem does not state the two-level stationary chain, optimal rank, lag correlation, or with-/without-replacement boundary. Haddock–Needell–Rebrova–Swartworth (2020/2022) analyze different quantile-RK convergence hypotheses. Cai–Chen–Ma–Wu (2025/2026) give upper and lower sample-size orders for finite-horizon performance of a distinct scheme with an independently selected candidate update row, not the exact invariant laws of update-from-subset order-statistic selection. Direct statement-and-implication comparisons were made; similarity of quantile and corruption parameters alone was not treated as independent novelty. A specialized prior analysis of this two-state order-statistic process could still precede the classification, and no database partition proves novelty.

## Mathematical value — PASS

This is a natural complete classification of the smallest corrupted system possessing competing quantile-selected updates: it solves all ranks and sample sizes, identifies a sharp finite-population threshold for a truly absorbing exact solution, and exhibits a qualitative median-induced independence and high-quantile alternating-correlation regime. It also distinguishes without-replacement from with-replacement sampling, a consequential implementation choice. It is a nonasymptotic, exact benchmark motivated by the cited small-sample algorithm's quantile-selection problem; no broad multidimensional performance claim is needed or made. The elementary probabilistic ingredients are acknowledged as standard.

## Closest literature and limitations

- Haddock, Ma, Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, Section V-D, arXiv:2308.07987: primary algorithm and empirical observations; the exact two-level all-rank classification is not supplied there.
- Haddock, Needell, Rebrova, Swartworth, *Quantile-based Iterative Methods for Corrupted Systems of Linear Equations*, arXiv:2009.08089: quantile-based robust convergence theory, not the stated finite-state exact law.
- Cai, Chen, Ma, Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185: distinct update-sampling mechanism, finite-horizon high-probability bounds.

The result assumes identical one-dimensional unit rows, a common corruption amplitude, independent batches, and exact projections. Nothing here establishes optimal quantiles or robustness in high-dimensional applications. Specialized priority overlap remains possible. Finite exact checks corroborate but do not replace the analytic derivations.

Self-review: passed. Independent audit: not yet performed.
