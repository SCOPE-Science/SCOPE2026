# Scientific review: activation transition in expanding-color reinforced trees

## Correctness — PASS

The exact one-dimensional reduction follows because an unchosen color is always represented by exactly one unit-weight ball; hence its total selection weight is the number of unchosen vertices. The mean and variance recursions follow by conditioning and the covariance identity. The divergence branch uses a predictable-variance-bounded martingale strong law and a triangular martingale central limit theorem with deterministically controlled weights. In the summable branch, the finite-activation conclusion follows from finite expected activation count, and the last-activation tail follows from a first/second Bonferroni comparison with the deterministic summable hazard. The proof explicitly identifies fixed positive reinforcement coefficients and exponents and excludes other feedback mechanisms. The supplied full-history checker independently validates 856 exact/numeric assertions; it is corroboration, not an infinite proof.

## Originality — PASS, qualified

The closest exact model source is Singh, Alajaji and Gharesifard (arXiv:2308.10197, first public 2023-08-20), whose Sections II–IV define the deterministic-new-color urn and establish *single-color* draw-count marginals, but not global parent-activation trichotomy, Gaussian fluctuations or last-activation timing. The mean count can be recovered by summing those marginals, so mean-only novelty is expressly not claimed. Sidorova (arXiv:1807.04844) treats a fixed two-color reinforced urn and its monopoly event. Sethuraman and Venkataramani (arXiv:1704.05568) obtain degree-count phenomena for degree-superlinear, rather than time-increment-reinforced, preferential attachment. Ruszel and Thacker (2024) treat finitely many colors. Bellina, De Marzo and Loreto (2025) treat novelty-triggered color introduction rather than exactly one new color at every step. Each is mathematically distinct at the transition law's essential assumptions. Research-record and prior research records alias searches did not disclose an implication-equivalent statement. General reinforced-urn and occupancy theory may contain an equivalent abstract result, and priority remains open to independent checking.

## Value — PASS

The activated-parent count is a natural measure of a growing network's structural diversity: it identifies how many vertices cease to be leaves and is different from the degree law of a typical named vertex. The theorem gives all three natural reinforcement regimes, the sharp finite-versus-infinite activation boundary, Gaussian fluctuations on the divergent side, a positive eternal-star probability on the finite side and a heavy-tail exponent for the final activation time. The tail predicts when a graph can continue growing for very long periods without creating a new parent and identifies a separate moment cutoff. These are structural statements for an infinite parameter family, not a small finite lookup or mere re-labeling.

## Scientific limitations and nearest prior work

The theorem does not cover random reinforcement, feedback on current degree, stochastic color birth, or a moving exponent. The claim of novelty is comparative, not an independent priority certificate. The original expanding-color paper's individual-color marginal result and its implications for the first moment remain prior work. The general prior literature may support further reductions that were not established in the completed comparisons.

Self-review: passed. Independent audit: not yet performed.
