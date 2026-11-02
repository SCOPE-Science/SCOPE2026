# Scientific review

## Correctness — PASS

The conditional mean identity and its all-center uniqueness follow by matching coefficients of arbitrary component centers in affine resolvents. The common contraction guarantees the invariant law; a centered scalar random affine recurrence and an independent component draw give exact second moments. Conditional expectation propagates lag covariances, and a geometric sum yields the finite-\(N\) and limiting time-averaging coefficients. The two-component sign is an exact nonnegative square; the three-component derivative is a rational function times \(r-1\) with a strictly positive polynomial. An additional exact derivative shows the stationary single-iterate variance grows in that family. The included standalone verifier passes ten symbolic identity groups, 275 rational parameter cases, and three independent seeded trajectory checks. These experiments are secondary to the displayed proof.

## Originality — PASS, qualified

The motivating 2023 study [1] specifies the standard finite-sum stochastic proximal point iteration and its variance-reduced variants but, in the inspected algorithm, results, and derivation sections, does not establish curvature-dependent sampling that makes its conditional expectation equal the full proximal map. The 2024 random-resolvent generalization [2] permits arbitrary sampling and provides convergence bounds, but does not state the same calibrated identity and sharp step-size monotonicity reversal. Implicit stochastic-gradient estimator theory [3] operates in a different step-size framework, and Bregman proximal-average theory [4] generally gives a prox of a proximal average, not the original arithmetic-average objective. Prior random affine-recursion covariance identities are standard and are not claimed independently new. Publication-priority risk remains for an unlocated quadratic resolvent-averaging or Markov-chain-specialization result; this review does not establish global uniqueness in the literature.

## Value — PASS

The all-center calibration makes the conditional expected randomized update equal the desired deterministic update without correction vectors. Stationary precision is not captured by this mean equality: the exact long-run variance can improve or worsen under more aggressive implicit steps. The pairwise nondecreasing theorem establishes a minimal-component boundary, and three symmetric-offset components furnish a robust all-steps strict reversal, not just one numerical witness. The explicit formula and exact rational witness can guide interpretation of step-size robustness and trajectory averaging in finite-sum proximal methods.

## Closest literature and limitations

[1] Traoré et al., arXiv:2308.09310 (2023), relevant Sections 1–4 and algorithm descriptions. [2] Sadiev, Condat and Richtárik, arXiv:2405.14255 (2024), SPPM and SPPM-OC sections. [3] Toulis and Airoldi, arXiv:1408.2923 (2014), implicit stochastic gradient estimator analysis. [4] Bauschke and Wang, arXiv:2108.11440 (2021), introduction and proximal-average principle. [5] Bertsekas (2011), randomized incremental proximal-method analysis. Residual priority risk: generic random affine recursions and weighted proximal averages may simplify parts of the proof. The result is not extended beyond scalar quadratics or the stated iid choices.

Self-review: passed. Independent audit: not yet performed.
