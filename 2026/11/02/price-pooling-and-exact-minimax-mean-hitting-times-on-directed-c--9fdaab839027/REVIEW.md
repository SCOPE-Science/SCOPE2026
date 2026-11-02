# Scientific review: price-pooled minimax hitting-time design

## Correctness — PASS

The model specifies all distinct ordered start–target pairs and the positive-rate budget. Every hitting expectation is a sum of forward-arc reciprocal rates, so the worst arc has length \(n-1\). The unique price root exists by strict monotonicity. A dual convex average of omitted-edge sums and Cauchy–Schwarz give the universal sharp bound \(M^2/B\), attained by the displayed positive allocation. Equality forces proportional holding times and exact budget use, proving uniqueness including price ties. The explicit three-state and single-expensive-edge cases follow by solving the level equation. `verify.py` supplies 6,393 supporting deterministic checks; finite experiments are not infinite proofs.

## Originality — PASS on inspected evidence; priority risk retained

The source full text of Roch (2004) addresses reversible spectral mixing rather than directed first-hitting minimax design. Aldous–Fill gives general hitting identities, not a price-allocation formula. The Berman (1964) PERT model is a broad convex resource-allocation predecessor, so the present optimization is connected to that framework. Its accessible abstract does not exhibit the price threshold or complete closed-form optimizer, but full-text comparison is incomplete; it is the largest priority risk. The Best–Chakravarti–Ubhaya (2000) published abstract describes prespecified monotone-chain constraints, not endogenous cheapest-price pooling. No equivalent exact result was identified in the actual semantic source and formula searches; a negative search does not prove uniqueness in literature. Kemeny-type stationary-target averages differ from the maximum over all ordered pairs and cannot directly imply the transition at \(Q=2\).

## Mathematical value — PASS

Worst-case pairwise first-hitting delay is a natural robust performance criterion for a unidirectional stochastic communication cycle. The all-price threshold turns a nonsmooth minimax allocation into an exact, sorted-price computation; the unique pooled versus square-root regimes show which transitions should share equal service rates. The sharp price tie cases, explicit three-state breakpoint, and expensive-edge budget-concentration law are useful structural consequences beyond a mere numerical optimizer.

## Remaining limitations

The result is restricted to one-way exponentially held directed cycles and expected first hitting times. It does not determine stationary-target Kemeny or spectral convergence optima. The full text for the broad PERT predecessor was inaccessible at review; no independence, formal validation, or publication priority is certified by this review.

Self-review: passed. Independent audit: not yet performed.
