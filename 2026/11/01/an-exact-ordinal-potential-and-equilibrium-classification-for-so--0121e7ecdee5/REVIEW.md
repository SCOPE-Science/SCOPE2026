# Scientific review

## Correctness

**PASS.** The scope is restricted to finite connected simple cactus hosts and connected spanning states. In each cactus cycle at most one edge may be removed; the block-cut tree makes shortest-path increments from different removed cycle edges exactly additive, including at shared articulation vertices. The actual payoff changes at the two endpoints are the full-host distance shocks minus/plus the degree reward. These establish the proposed ordinal potential and the strict, tie-aware equilibrium tests. The same distance identity proves the welfare decomposition. The attachment-star family follows by direct finite distance counts. A deterministic executable has verified 1,093 parameterized instances and 26,710 state-level checks, with a separate exhaustive connected-state comparison of 1,526 small cases. Finite computation is supplemental, not substituted for the proof.

## Originality

**PASS, best-knowledge with residual bibliographic risk.** The primary 2022 source gives the game definition, general sufficient equilibrium regimes, some inefficiency examples and an improving-response cycle for the unrestricted model. It does not give an all-incentive cactus-host ordinal potential or the product classification of *all* equilibria. Searches for the exact source, cactus-host variants, potential formulations and equivalent distance/block decomposition formulations in published mathematical records and in accessible related research returned no stronger claim covering this one. The previously published isolated-cycle inefficiency is explicitly excluded from the new contribution. Unindexed or otherwise inaccessible specialized results remain a residual risk.

## Mathematical value

**PASS.** This identifies a natural structural boundary where the general game can cycle but the cactus-restricted game always converges. The explicit threshold product answers existence, counting, equilibrium selection and exact welfare optimization for every finite cactus and every incentive value. This goes beyond a small numerical example and supplies a complete polynomially computable classification with nonvanishing inefficiency witnesses.

## Limits and relation to prior work

The theorem assumes an undirected simple cactus host, one-edge unilateral deletion, strictly mutually beneficial single-edge addition, and connected spanning states. It does not address arbitrary host graphs or coalitional edge changes. Closest primary source: Friedrich et al., *Social Distancing Network Creation*, arXiv:2204.10423v1 (2022-04-21), ICALP 2022, and *Algorithmica* 85 (2023), particularly Theorems 4, 7, 9, 10 and 14–15. Their cycle-only special cases and general sufficient parameter bounds neither contradict nor imply this cactus-wide classification. No independent audit is reported.

Self-review: passed. Independent audit: not yet performed.
