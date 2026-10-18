# Scientific assessment: exact rate for discrete martingale entropy projections

**Correctness — PASS.** The exact rowwise KL projection is uniquely characterized by the row mean and the invariant endpoint-product ratio. The target rescaling yields a closed scalar recurrence; differentiating it establishes strict monotonicity and the exact local factor. A second-order expansion of conditional KL yields the squared entropy factor. The boundary expansion is an algebraic identity. The accompanying independent-formula finite tests agree on 15,316 checks, while the proof does not rely on those finite checks.

**Originality — PASS, with remaining overlap risk.** Examined primary martingale Sinkhorn convergence sources provide abstract rates or numerical examples, not the exact projective factor for the symmetric two-by-three support, nor the derived boundary coefficient. The closest general theorem assumes a convex terminal support that fails for three separated atoms. An abstract information-projection theorem may imply qualitative exponential convergence without specifying this exact factor. Unindexed equivalent two-by-three calculations or a stronger local linearization result could still subsume the finding; searching does not establish absolute priority.

**Mathematical value — PASS.** The first nontrivial support cardinalities already exhibit a precise degeneration of entropy iteration speed as convex-order slack vanishes. The exact coefficient turns a qualitative convergence guarantee and previously observed dependence on marginal separation into a reproducible benchmark for exact martingale-constraint enforcement. The distinct local plan and KL multipliers matter for interpreting numerical iteration histories.

**Boundaries and verification.** Only the zero-cost symmetric finite model with positive weights and exact alternating projections is covered; no broad-support or runtime estimate is claimed. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
