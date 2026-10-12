# Self-review

## Correctness
**PASS.** The domain is finite and exhaustively parameterized. For each arm of size \(m\), positivity of all four stratum-by-outcome cells is exactly a positive composition of \(m\) into four parts, so the two-arm search has \(\binom{m-1}{3}^2\) tables. The verifier checks every table through \(m=11\) using exact cross multiplication, finding no reversal for \(m\le10\) and exactly four labeled reversals at \(m=11\). All four are reconstructed, grouped into two stratum-swap orbits, and rechecked by the binary cross-product association sign. The packaged verifier returns `VERIFY_OK`.

Risk: the cutoff is not universal once zero cells or unequal pooled arm sizes are allowed.

## Originality
**PASS.** Classical and modern literature already owns Simpson reversal, its causal/confounding interpretation, and general association-reversal characterizations. A Stanford Encyclopedia example even gives a balanced positive-cell reversal with 13 observations per group. An archived Brilliant challenge asks for the smallest strict Simpson example, but its formal domain permits zero cells and does not require equal pooled group totals. Searches for the constrained balanced positive-cell minimum, 11-per-arm formulation, exact witness rates, and first-layer census did not locate the 22-observation theorem.

Risk: the public smallest-example challenge is close in spirit, and an unindexed solution could have studied the balanced positive-cell specialization.

## Value
**PASS.** Equal pooled arm size is standard in comparative experiments, and positivity removes degenerate zero-rate examples. The result therefore answers a natural finite-design question: how small can a fully nondegenerate balanced dataset be before confounding can reverse every within-stratum treatment comparison? The complete first layer adds diagnostic value beyond a single example and improves the familiar balanced positive-cell example at 13 per group to the sharp 11-per-group boundary.

Self-review: passed. Independent audit: not yet performed.
