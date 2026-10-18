# Scientific review

## Correctness — PASS
The proof starts from an explicit finite cyclic resolvent and checks all quantifiers: \(n\ge3\), all strictly positive rates, all \(\theta\in[0,1]\), and all \(h\ge0\). The controlling fastest-state return diagonal is strictly decreasing even without reversibility; its endpoints give all finite/infinite threshold cases. The theta endpoints and critical equality are handled separately. Strict Karamata yields the global majorization order and budget optimizer classification. The standalone code verifies 1,065 exact-rational configurations but is not substituted for the infinite-family argument.

## Originality — PASS, residual risk stated
Horváth (1998, 2005) provides general RK positivity radii; Fallat–Tsatsomeros (2002) and a public 2026 Markov-return theorem provide known Cayley/resolvent algebra, acknowledged as prior work. Hadjimichael–Ketcheson–Lóczi (2021) analyzes centered/higher-order periodic advection semidiscretizations, not positive heterogeneous one-way cyclic generators. None of these inspected sources implies the derived strict nonreversible return monotonicity, all-real-rate theta horizon, and majorization optimizer transition. The risk of an equivalent unindexed theorem remains; negative searches are not uniqueness proof.

## Value — PASS
The theorem settles a naturally motivated numerical positivity-design question for heterogeneous directed transport: sharp feasible timestep, exact all-rate comparison, and whether uniformly allocating fixed throughput is the uniquely best design. The rate-budget uniqueness transition is structural, rather than a routine formula for one chosen finite matrix.

## Closest literature and limits
The 2026 reversible-chain criterion is closest at the algebraic level, but its monotonicity theorem assumes reversibility. The result does not cover additional directed edges, reverse edges, zero rates, internal stages, or nonlinear positivity. No independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
