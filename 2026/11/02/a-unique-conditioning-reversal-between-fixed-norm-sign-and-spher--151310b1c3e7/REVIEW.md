# Review

## Correctness — PASS

The fixed-norm definitions are explicit, and for each distribution the single-node Lanczos formula is the actual Rayleigh-log rule. For Rademacher the estimator is constant; for spherical sampling its Fourier logarithm has an absolutely convergent expansion, giving mean and variance exactly. The resulting difference is a one-variable scalar function whose derivative numerator is strictly increasing with opposite endpoint signs. This proves precisely one interior crossing and all strict comparisons. The exact rational root bracket and independent angular quadrature checks in `verify.py` support the algebra but are not substituted for the proof. Risks: no inference is made for additional nodes or unrestricted matrices.

## Originality — PASS, with priority risk

The inspected full texts [1]–[3] define the broader stochastic trace/log-determinant Lanczos context, supply distributional concentration and complexity results, and include Gaussian/Rademacher comparisons. They do not present the exact one-node, two-dimensional, norm-matched spherical-versus-sign expected squared error formulas or the unique crossover classification. The known sphere sampling distribution and elementary Fourier identities are acknowledged, and their separate existence is not construed as novelty. Published-results-index searches using the exact estimator, both probe laws and their reformulations did not yield a covering record. A specialized prior calculation is still possible and should be independently checked. This is a self-review, not independent, priority assessment.

## Value — PASS

Finite-budget SLQ error consists of random-direction variability and deterministic quadrature bias, so comparing only variances or trace-probe guarantees can misrank two choices. The natural single-matrix-vector-product case exhibits an exact, unexpectedly **reversed** MSE ranking despite the sign probe having zero variance on this diagonal input. The complete crossover and explicit risks quantify the mechanism rather than asserting general superiority. The narrow model is mathematically motivated by the lowest SLQ budget and the simplest genuinely anisotropic spectrum.

## Closest literature and limitations

[1] Cortinovis and Kressner, arXiv:2005.10009, Sections 1, 3 and 4: unnormalized Gaussian/Rademacher high-probability logdet estimation. [2] Chen, Trogdon, Ubaru, arXiv:2204.01941, sphere sampling and randomized matrix-free quadrature. [3] Li, Huang, Zhu, arXiv:2307.00847, stochastic Lanczos error-budget allocation and probe comparisons. Their actual statements do not imply the sharp fixed-norm one-node reversal. The claim is specific to a diagonal two-dimensional matrix, and no independent validation or comprehensive priority certificate is claimed.

Self-review: passed. Independent audit: not yet performed.
