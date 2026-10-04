# Same-model review

## Correctness
PASS. The bounded monotone sample cone becomes a simplex after passing to nonnegative increments, so a linear quadrature functional is optimized exactly at step vectors. This proves that the image interval is governed by tail sums, and Newton–Cotes symmetry converts those tail sums into cumulative prefixes. Exact rational moment solving independently reproduces all weights through \(n=13\), the published \(n=12\) coefficient table, the exact defect \(147227/750750\), the strict monotone negative witness, and the positive cumulative minimum for \(n=13\).

## Originality
PASS with explicit residual risk. Classical sources derive Cotes numbers, tabulate high-order weights, and discuss negative coefficients, truncation error, and roundoff. A separate quadrature-monotonicity literature studies monotone convergence of refinement sequences for function classes. Searches under cumulative weights, monotone samples, range preservation, positive linear functionals, and Newton–Cotes negativity did not locate the statement that the monotone-data image is exactly controlled by cumulative Cotes numbers, nor the first-failure/restoration pattern at \(n=12,13\). An older ordered-functional formulation or an unindexed observation in quadrature literature remains possible.

## Value
PASS. High-order Newton–Cotes rules are commonly rejected once negative coefficients appear, but monotone sampled data form a much smaller and practically important cone. The theorem separates arbitrary-data negativity from monotone-data range failure, gives the first exact failure order and its nearly twenty-percent sharp defect, and identifies the immediate \(n=13\) recovery. The cumulative-weight criterion is simple enough to use as a deterministic safety test for any further rule.

Same-model review: passed. Independent audit: not yet performed.
