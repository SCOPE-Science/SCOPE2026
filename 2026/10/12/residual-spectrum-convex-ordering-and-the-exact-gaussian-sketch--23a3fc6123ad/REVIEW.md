# Self-review

**Correctness — PASS.** The orthogonal Gaussian blocks are independent by rotational invariance, and the exact projection Pythagorean identity reduces the relative squared error to an exchangeable, positive weighted sum of Gaussian pseudoinverse energies. Majorization plus permutation Jensen proves convex order for finite-mean cases. Gaussian/Wishart integration derives the rank-one beta-prime law; comparison inequalities give the iff moment frontier for every nonzero residual. Conditional Gaussian variance decomposition gives the exact spectral variance formula. The packaged independent algebraic/sample diagnostics were replayed; simulations alone are not used as a proof.

**Originality — PASS, residual priority risk.** Tropp et al. (2017), Appendix A.3, explicitly gives the factor error decomposition and the exact first-moment multiplier; both are credited as known. Nakatsukasa (2020), Theorem 3.2, gives related two-sided Gaussian Nyström error estimates. The inspected papers and targeted published-index search do not establish the same distribution-level spectral convex order or universal sharp moment cutoff. The beta-prime mixture itself is standard probability, and a specialized unindexed sketch/regression treatment could reduce priority; independent literature audit has not occurred.

**Value — PASS.** The theorem replaces a spectrum-blind expected-error guarantee with a sharp order for convex tail-sensitive risk, identifies the precise oversampling needed for finite error variance, and provides an exact testable rank-one calibration law. These are meaningful sketch-quality and robustness distinctions, not a claim of a faster approximation algorithm.

The theorem is conditional on fixed, independent-Gaussian range/test subspaces and exact arithmetic; it does not give finite-precision stability or raw stochastic-quantile dominance.

Self-review: passed. Independent audit: not yet performed.
