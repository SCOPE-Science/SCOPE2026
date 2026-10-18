# Scientific review

## Correctness — PASS
The objective is strictly convex in the constant held control because its quadratic coefficient is the positive integral of \(e^{-\rho t}(t^2+r)\). Exact integration gives the sampled multiplier, whose condition \(-1<g<1\) reduces without discarded cases to \(r/h^2>\psi(\rho h)\). A sign-certified entire-function coefficient expansion proves the **unique** maximum of \(\psi\) and hence the complete reentrant stability classification, rather than extrapolating from a sampled graph. A separate sign/derivative argument proves the unique fixed-discount hold-time threshold. The exponential witness is exact. The reproduced symbolic and high-precision checks independently test key identities and estimates, but do not themselves prove the infinite sign pattern.

## Originality — PASS with residual literature uncertainty
The closest motivating source, Zhang–Hørsholt–Jørgensen (2024), establishes exact discounted running-cost discretization but not the stated one-step repeated-feedback universal stability band. Granzotto et al. (2021) prove sufficient/general finite-horizon discounted **discrete-time** stability properties, not a sharp within-hold discount bifurcation for one-interval exact continuous costs. Schwenkel et al. (2024) address economic MPC with differing discount objectives. Published-source text and mathematical-record comparisons identified no equivalent or stronger result that implies the complete statement. A negative search is not proof of novelty, and unindexed scalar receding-horizon literature is a residual priority risk.

## Mathematical value — PASS
The result gives a sharp design boundary and an analytically complete explanation of a counterintuitive phenomenon: increasing within-step discount can first destabilize and later restabilize a repeated optimal controller, even though each single-step problem is strongly convex and integrated exactly. Both the universal threshold and exact root classification are natural, testable invariants tied to stability of predictive sampled feedback, rather than arbitrary numerical slices. The result does not imply that longer-horizon or terminally stabilized controllers fail.

## Scope and verification
The theorem concerns the sampled scalar integrator only. The roots are defined exactly and checked numerically; their printed decimal expansions are not certified interval bounds. Comparison with source manuscripts is scientific, not an independent audit or definitive exhaustive priority determination.

Self-review: passed. Independent audit: not yet performed.
