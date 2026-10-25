# Scientific assessment

## Correctness — PASS
The specified fifteen-category Dirichlet prior has independent-gamma representation. Partitioning into five ballot types per first-choice candidate, and then into the \(C\)-first continuation categories, gives the independent \(\operatorname{Dirichlet}(2,2,1)\) transfer law. A direct two-variable Jacobian calculation yields the density \(1-3d^2+2|d|^3\) for the transfer difference, whose tail integrates to the claimed quartic. The posterior limiting claim follows from exact grouped Dirichlet conjugacy and concentration. The included checker verifies exact polynomial identities and Monte Carlo diagnostics. The mathematical proof, not simulation, establishes the infinite claim.

## Originality — PASS (qualified)
The closest source, Rosenman and Liang (2026, arXiv:2606.31022, Sections 2.1, 4.2–4.6), specifies the fifteen ballot types and flat Dirichlet model, then estimates outcomes by simulation using complete poll responses. Its inspected text does not state the first-choice-only conditional Dirichlet transfer law, quartic risk, nonzero infinite-poll residual or complete-versus-truncated cubic/linear frontier. The classic RangeVoting catalog gives unconditional plurality/IRV discordance under a different random model. Targeted published-web and mathematical-result searches found no statement implying the complete present claim. Ordinary Dirichlet-neutrality calculations could make an equivalent formula derivable and unindexed precedent remains an originality risk.

## Value — PASS
The work answers a directly motivated decision quantity for the new Bayesian instant-runoff polling model: what win confidence can an arbitrarily large but less detailed first-choice-only poll support? Its positive Bayes-error floor is quantitatively sharp, has an exact cubic majority-frontier rate, and contrasts with a full-ranking ballot-universe model. This is more than a generic conjugacy example because the exhaustions, three-way grouping, explicit winner rule, and asymptotic observational information limit are all essential to the resulting law. Practical calibration is entirely conditional on the stated prior; no universal empirical reliability is claimed.

## Main remaining risks
A previously unindexed conditional ranked-choice calculation or a broad explicit Dirichlet order-statistic theorem may already imply the quartic. The flat prior's weighting of truncated ballots is context dependent, as the motivating paper itself emphasizes.

Self-review: passed. Independent audit: not yet performed.
