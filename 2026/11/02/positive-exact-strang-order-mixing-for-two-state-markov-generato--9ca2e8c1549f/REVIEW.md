# Scientific review

## Correctness — PASS

The binary statement follows from the exact affine form of a two-state Markov transition map. The two palindromic orders have the same contraction factor \(e^{-(s+t)h}\) and explicit distinct stationary intercepts. Strict convexity of \(\sinh\) brackets the exact equilibrium between them and proves strict mixing positivity. The combination consequently equals the entire exact transition matrix. For the three-state witness, direct finite matrix algebra yields the exact trace defect \((1-e^{-h})^4/4>0\), precluding even a signed affine mix. The verifier checks the identities independently on numerical rates and exact-rational polynomial data. It does not replace the universal proof.

## Originality — PASS (best-knowledge comparison)

Searches over the public mathematics record and published mathematical claims covered exact convex combinations, reverse Strang orders, two-state kinetic generators, rate-only weights, three-state trace obstructions, and alternative Markov splitting terminology. The closest accessible primary work (Battestini–Caliari–Cassini, arXiv:2610.07989v1) analyzes noncommuting splitting *errors* of fixed orders; Li–Liu–Wan (arXiv:2603.27654) randomize order for approximation; Eisenmann–Stillfjord (arXiv:2210.05375) analyze a different random subflow scheme. None of the inspected statements implies the rate-only exact matrix identity, its unique mixing probability, and a sharp dimension-three trace obstruction. published-finding corpus matches on two-state reversible chains, SSP-SDIRK2 positivity, and Crank–Nicolson positivity concern other algorithms and metrics. This supports novelty under the checked evidence, not exhaustive priority. Residual risk: a specialized historical two-state splitting formula not indexed in the searched materials.

## Mathematical value — PASS

The theorem gives an exact, *stochasticity-preserving* way of replacing an expensive coupled two-state generator exponential by a single randomly selected composition of split semigroups. Equal total relaxation scales yield a surprisingly simple fair randomization even when the generator components do not commute. The strict three-state obstruction identifies the first state dimension where the same two-order strategy can fundamentally fail, making the result a meaningful boundary for kinetic integrator design, not merely a renamed second-order error estimate. No cost optimality, nonlinear extension, or higher-dimensional impossibility is claimed.

## Source and scope limitations

Relevant primary materials were checked at the full HTML level where accessible; a broader archival survey is not exhaustive. The two-state exactness refers to transition matrices/expectations at step endpoints, not pathwise sample paths. The obstruction applies to the two particular reverse Strang orders, not arbitrary positive multi-product formulas. All results are in exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
