# Self-review

**Claim.** The precise two-zone splitting law and the unique speed-induced capture-side reversal condition stated in `RESULT.md`; no broader claims about other active-particle models.

**Correctness: PASS.** The left/right effective boundary impedances follow from the exact matrix exponential for the backward telegraph-and-killing ODE. The particle is eventually captured almost surely by one-dimensional recurrence plus a uniform positive chance of killing during inward interval crossings. The strict monotonicity of the impedance ratio, and the signs of its two endpoint limits, prove the iff criterion and exclude additional crossings and nontrivial equality. The independently implemented transfer system agreed in 400 randomized cases within \(1.62	imes10^{-13}\); 300 derivative and 110 crossover tests independently corroborated the analysis. The infinite-scope conclusions rely on the displayed analytic proof, not finite experiments.

**Originality: PASS.** Angelani (arXiv:2303.03078) handles symmetric finite reaction regions and the trapped-position distribution; its reflection symmetry cannot prove unequal-site velocity reversal. Bressloff (arXiv:2302.01158) treats inequivalent sticky boundary absorbers, not finite traversable reactive strips. Angelani's generic boundary formulation and Jeon--Go--Kim's one-target velocity optimum were also compared by full text. The new contribution is only the precise finite-zone, two-label split and all-parameter one-crossing theorem; not the pre-existing backward generator or transfer method. Semantic research-record searches and the accessible relevant earlier findings showed no covering claim, but unavailable or unindexed equivalences remain a risk.

**Mathematical value: PASS.** The theorem identifies which of two partially reactive zones captures a self-propelled searcher, giving a complete decision criterion depending only on the ordering of local rates and rate-times-width strengths, with explicit asymptotics and a unique reversal in speed. It offers a nontrivial physical threshold rather than a routine special-function rearrangement.

**Scientific limitations.** The model requires two finite penetrable zones in an unbounded line, constant hazards, constant speed, homogeneous symmetric flipping, and unbiased central release for the crossover theorem. No experiment, arbitrary multiple traps, or general stochastic-control optimality is claimed; independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
