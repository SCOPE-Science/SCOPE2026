# Independent mathematical audit

## correctness

PASS

The frozen Markov calculation is correct: projection lands in {0,h}; the rank selects a corrupt row at 0 iff its corrupt-count tail begins at s−j+1, and selects a clean row at h iff the count is at most j−1. Since w₀>0, the balance equation determines the unique invariant law. Conditional iteration of the affine probability update gives both the time evolution and the stationary covariance. The two tails are disjoint, a partition, or overlapping according to 2j versus s+1, including vanishing middle mass. Identical rows of the matrix do give independent stationary draws beginning with the second update for arbitrary initial ties. The worked example uses exact probabilities. The repair restricts the Finding to optimization and makes the risk ordering complete: the denominator weights have positive support u=0,…,q with q=min(c,s), and the reflected weights first become positive at ℓ=s−q. On their common positive support the consecutive reflected odds ratio is (g−u)(g−s+u+1)/[(c−u)(c−s+u+1)]>1. Appending a weight at an index j≤q and j≥ℓ strictly raises the weighted average; after j>q the denominator is constant and the numerator strictly increases as soon as j≥ℓ. This includes ℓ>q, as well as singleton rank, denominator saturation and the exactly one-positive-rank case. The zero-risk ranks are absorbing with positive restart probability of reaching 0 from h; positive-risk ranks cannot retain 0 permanently, since the batches are independent and the exit probability is positive. With replacement all weights are positive and the reflected ratio multiplier is (g/c)^2>1; the rank-one odds use just (c/m)^s and (g/m)^s. `python3 /workspace/branches/frozen_replay.py 2` passed 105 exact rank cases for the original model. `cd /workspace/repairs/2 && python3 verify_rank.py` passed exact direct residual-sorting checks of the amended theorem in 100 sampling-design/size cases, including s>c, gaps between the two supports, and batch sizes exceeding g under replacement. The proofs, not the bounded tests, establish the universal statements.

## originality

PASS

This PASS is for the repaired result, not the original bundle. Earlier Resultary 2639ecb81dd1 directly states the same transition law, invariant mass, covariance/eigenvalue, correlation sign in its full-support regime and odd-median independence, and allows a broader range of subset sizes. The original stationary-error formula and existence of any absorbing rank are immediate from that earlier law. The repair explicitly credits these results, removes the correlation classification from the Finding, and proves the strict ordering of the whole positive risk range, including for s>c after the zero-risk plateau, with an optimized same-batch replacement comparison. Neither the prior transition law alone nor the inspected literature analyzes that ordering: the reflected hypergeometric ratios and the case where the denominator saturates are needed. The binomial evaluation alone is elementary and not credited as a separate major contribution.

## value

PASS

For the specific implementable same-batch rule, the rank decision affects the stationary risk, a natural optimization criterion that cannot be read off from the previously recorded median behavior or temporal correlation. Knowing the whole shape (an exact zero plateau if it exists, then strict growth) determines both the best choice and which suboptimal ranks are worse, including all finite-population truncations. Replacement removes the zero plateau even with optimized rank. This gives exact tuning guidance for the stated model, not an assertion that rank one is preferable on general Kaczmarz systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
