# Mathematical assessment

**Correctness — PASS.** The exact Gaussian second moments imply the covariance map in the proof. Splitting it into a positive two-by-two Perron block and a smaller antisymmetric mode yields the spectral radius and the unique sharp noise threshold by a characteristic-polynomial calculation. Both endpoint asymptotics follow from elementary expansions, and the continuous-time covariance generator establishes the genuine stability-gap interval. A standalone checker passed 185 independent deterministic identities and matrix tests. No finite simulation is offered as an infinite-horizon proof.

**Originality — PASS, subject to residual bibliographic uncertainty.** The motivating 2026 paper and Bréhier–Cohen–Ulander 2024 were examined at the actual splitting definitions and stability results. Those prove positivity and finite-horizon accuracy or moment bounds; such estimates do not imply the precise two-site infinite-horizon mean-square threshold. Published mathematical-record searches found no equivalent calculation and found several different stochastic stability and positivity results that are not implication-dominating. The exact Gaussian moment mechanism itself is classical. The uninspected 2022 almost-sure-stability finite-difference paper and other implicit-scheme works leave a named overlap risk, but they concern different methods and/or different stability notions.

**Value — PASS.** Even a positive method that accurately approximates a stable continuous-time system for small steps can destabilize mean-square behavior on long horizons. The sharp closed-form frontier and explicit nonempty noise band quantify the gap between pathwise positivity and long-time numerical stability, giving a stringent two-node regression test for stochastic-heat splitting implementations rather than an arbitrary finite numerical exercise.

The theorem is confined to symmetric coupled two-site systems with independent equal linear noise, and does not establish general mesh-level stability or almost-sure growth. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
