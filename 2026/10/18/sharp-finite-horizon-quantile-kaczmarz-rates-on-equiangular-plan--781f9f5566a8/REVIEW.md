# Mathematical review

## Correctness — PASS

The exact row definition, order-statistic selection, and tie inclusion are specified. The single-step orthogonal-projection identity reduces the risk to the mean of the least \(r\) squared residuals. A finite trigonometric progression bounds that average sharply, with explicit worst-orientation equality. After a projection every nonzero error is perpendicular to an original row, so each future acceptance set contains \(r\) members for odd \(r\) and all-row selection, or \(r+1\) for even nonterminal \(r\). This yields one exact conditional post-first-step risk factor, proving the all-horizon equality and sharp supremum. The rank-one absorbing state, geometric decay for higher rank, and stated asymptotics follow directly. The standalone verifier reproduces 39,420 deterministic numerical checks; the analytic proof carries the infinite and all-horizon claims.

## Originality — PASS under the presently accessible record

Steinerberger's original quantile rule already chooses uniformly from all residuals at or below a quantile; it also anticipates slow progress when residuals are small and identifies tight frames and spherical designs as natural deterministic instances. Lok–Rebrova's constrained quantile formulation is a relevant structured extension; Coria–Haddock–Pacheco's analysis concerns perturbations and high-level error rates. Their inspected original statements do not furnish the exact regular-frame trigonometric first-step optimum, parity-sensitive after-first law, or equality at every finite horizon. An accessible mathematical-record comparison and the available prior-claim record uncovered no stronger covering claim. This is a priority assessment, **not** an independence or exhaustive-publication certificate. A concealed formulation in older cyclic-projection or trigonometric-design literature remains possible.

The closest mathematical-record entries describe two-row deterministic cyclic Kaczmarz and maximal-residual Kaczmarz. Neither has the minimum-residual order-statistic mechanism or a random update among tied least-residual rows. The related prior-claim record involving quantile rank selection acts on a sampled subset and establishes a different rank-statistical property, not the present equiangular full-frame finite-horizon law.

## Value — PASS

The result gives the exact worst-risk function for **every** finite horizon of a natural existing algorithm on a family with condition number one. It separates (i) a pathological permanent rank-one stalling threshold, (ii) an exact one-time parity correction induced by cutoff ties, and (iii) a quadratic-in-frame-size convergence slowdown for any fixed accepted rank. These structural distinctions are invisible to estimates based solely on global frame conditioning, and the exact benchmark is useful for interpreting quantile cutoff choices. The claim's value is the algorithmic structural characterization, not the underlying elementary sine-sum identity alone.

## Scope and risks

Two real coordinates, equally spaced projective row normals, consistent data, exact orthogonal projections and inclusive quantile ties only. No independently performed audit, no claim about corruption resilience, no novelty proof from unsuccessful searches. Possible equivalent forms under older geometric Kaczmarz terminology remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
