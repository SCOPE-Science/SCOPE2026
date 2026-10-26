# Scientific review: sharp AdaSPS noninterpolation fluctuations

## Correctness
PASS. The source's exact AdaSPS minimum reduces to a loss-sum inverse-square-root step with positive nonvanishing gradients on the specified two-client problem. The proof controls the current-sample dependence by comparing to a predictable pre-update step, establishes second/fourth moments, derives quantitative self-normalization, and couples to deterministic-gain linear stochastic approximation. An explicit weighted-sign Lindeberg argument yields both the limiting Gaussian variance and the sharp second moment. The standalone finite checks confirm the precise source branch, but do not serve as an infinite proof.

## Originality
PASS under presently available comparisons, not independently certified. The source arXiv:2308.06058v1 proves rate bounds, not this unaveraged sharp constant and distribution; DecSPS (arXiv:2205.04583) is a different update; deterministic-gain stochastic approximation results (arXiv:2405.17834) do not directly handle the sample-dependent cumulative loss. Targeted published mathematical research records yielded no direct covering result. The primary outstanding priority risks are general adaptive-gain limit theorems under unsearched terminology and the limited accessible text of arXiv:2406.04142.

## Value
PASS. The result establishes that the noninterpolating \(n^{-1/2}\) last-iterate expected-objective rate cannot generally be sharpened for the actual AdaSPS rule at fixed scale, and specifies the nonzero leading constant and limiting random fluctuations. This is useful when interpreting algorithmic rate bounds, tuning fixed scales, and constructing reference tests for adaptive optimizers; it does not claim universality.

## Limitations
The exact conclusion is confined to two equiprobable equal-curvature scalar clients, a symmetric zero start and fixed \(c\ge1\). Generic central limit theorems supply the final deterministic-gain step; novelty is in rigorously reducing the original current-loss-adaptive rule to that limit and identifying the sharp algorithm-specific constant. No independent audit or proof of priority has occurred.

Self-review: passed. Independent audit: not yet performed.
