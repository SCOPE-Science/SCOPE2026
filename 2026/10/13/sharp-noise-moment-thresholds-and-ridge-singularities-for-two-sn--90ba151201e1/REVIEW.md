# Self-review

## Correctness — PASS

The result applies to arbitrary deterministic, distinct input snapshots, independent isotropic Gaussian oracle errors, an affine scalar contraction and the displayed one-column Anderson projection. The update identity follows by substituting the one-column least-squares minimizer. The sum/difference Gaussian transform yields independent numerator and denominator vectors and a residual-difference density positive at zero. A polar lower/upper bound proves the strict moment cutoff \(q<d\), including divergence at equality. A separate polar integration of the squared ridge coefficient yields the exact leading \(\varepsilon^{-1/2}\) and \(\log(1/\varepsilon)\) constants. A uniformly bounded regular remainder controls cross terms; dominated convergence handles dimensions \(d\ge3\). The accompanying deterministic verifier cross-checks the algebra and numerically integrated leading constants, without using finite computations as an infinite proof.

## Originality — PASS, with residual risk

Wei–Bao–Liu (arXiv:2110.01543v1, sections 2 and 3 plus appendix) introduces stochastic Anderson mixing, damping and adaptive regularization, but does not state the displayed unsafeguarded two-noise moment threshold and ridge singularity coefficients. The inexact/approximate Anderson full-text treatments (arXiv:2206.03915 and arXiv:1909.03245) analyze perturbation bounds and regularization, not an equivalent probability-integrability law. Related indexed records found by searches address deterministic Aitken–Steffensen contraction or unrelated Gaussian laws, without an implication of this vector stochastic-ratio theorem. The 2017 inaccurate-function-evaluations paper is plausible and only an abstract could be examined; uncertainty about material inaccessible there and unindexed literature remains. General Gaussian-ratio tail phenomena are known background, not asserted novel.

## Value — PASS

The exact moment cutoff determines whether a basic noisy Anderson update has a meaningful mean-square performance metric, and the dimension-one square-root versus dimension-two logarithmic penalty laws quantify how regularization suppresses the singularity. This sharp boundary matters for interpreting small-dimensional noisy fixed-point acceleration and justifies ridge safeguards on a natural algorithmic model. It does not claim improvement in iteration complexity or universal instability of safeguarded stochastic Anderson methods.

## Sources and limitations

Relevant inspected full texts: F. Wei, C. Bao, Y. Liu, arXiv:2110.01543v1; D. Lupo Pasini, M. P. Laiu, arXiv:2206.03915; and H. Shi et al., arXiv:1909.03245. Abstract-only comparison: A. C. Toth et al., DOI:10.1137/16M1080677. Fixed externally specified snapshots, a scalar contraction, independent isotropic Gaussian noise, and one Anderson update are essential restrictions. Numerical cross-checks are corroborative only. The finding has no independent external assessment.

Self-review: passed. Independent audit: not yet performed.
