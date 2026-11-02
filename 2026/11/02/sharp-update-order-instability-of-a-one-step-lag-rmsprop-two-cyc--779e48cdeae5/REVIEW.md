# Assessment of the one-step-lag RMSProp period-two theorem

## Correctness

**PASS.** The two spatial displacement equations enforce opposing signs, and the memory difference identity rules out unequal magnitudes; this completes, rather than assumes, the classification of all primitive two-cycles. At the unique symmetric orbit, the full two-state one-step Jacobians are related by reflection, yielding an exact quadratic characteristic polynomial for their signed product. Strict Schur conditions prove attraction exactly between the existence and crossing thresholds. Discriminant and determinant calculations prove the defective node-to-spiral transition and hyperbolic repulsion above the second threshold. The packaged SymPy verification recomputes these identities from the original map.

**Limits:** The finite rational tests corroborate only; the written proof gives the uniform quantifiers. At equality of the unit-circle threshold, no nonlinear conclusion is proved.

## Originality

**PASS under examined evidence.** The closest full primary text is Loh et al. (arxiv:2610.30078v1), which treats the immediate, newly updated RMSProp memory. Its antiphase-existence and near-onset-stability theorems do not cover the one-step-stale map. Li et al. (arxiv:2212.00309) and Tian Li's 2023 thesis develop delayed preconditioners using a different blockwise algorithm, without this exact two-cycle spectrum. The difference is in the update equations and the implications, not titles: a different Jacobian and a finite universal upper stability frontier are proved for the lagged recurrence. Related numerical and alternative optimizer thresholds do not entail this exact result.

**Residual risk:** Historical priority against specialized or unindexed optimization dynamics remains provisional; one related central-flow full text could not be fully accessed. This does not remove the need for human literature review prior to a publication claim.

## Mathematical value

**PASS.** A precise one-step lag in applying the adaptive memory is a motivated change to the optimizer, and the resulting sharp upper threshold (independent of memory decay) distinguishes delayed from immediately updated normalization. The complete pair classification, stability window, exact spectral crossover and post-threshold repelling regime provide a compact dynamical benchmark. The conclusion is local and does not imply general convergence or nonlinear invariant-circle birth.

Self-review: passed. Independent audit: not yet performed.
