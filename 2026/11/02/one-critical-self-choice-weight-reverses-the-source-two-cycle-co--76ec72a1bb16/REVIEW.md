# Scientific review

## Correctness: PASS
The distribution has independent source arrows, and the proof directly computes the one-vertex avoidance probability, the number and probability of marked directed cycles, and the mixed moment after separating vertices inside and outside a cycle. The covariance factorization and the strict sign comparisons follow algebraically; positivity of the prefactors is explicit for all \(n\ge3\), finite \(w\ge0\), and \(2\le r\le n\). The strict negative sign for longer cycles uses monotonicity in cycle length and weight, not extrapolation from experiments. The fixed-length expansion and moving-weight two-cycle window use controlled finite-order asymptotic expansions. Exact rational exhaustive checks corroborate all tested small parameters.

## Originality: PASS, with residual historical-priority risk
Tavaré (2020, arXiv:2006.04805v1) thoroughly studies the no-self-choice endpoint, its core cycles, and component-size distributions; its accessible text was compared for the full diagonal interpolation and no such covariance transition was identified. The classical uniform mapping model sits at the other endpoint. A known earlier loopless covariance classification covers the \(w=0\) endpoint; this endpoint is **not** claimed as new. The proposed statement is the exact finite-parameter crossover, strict global sign classification across weights, and boundary-layer asymptotics. Search and comparison did not identify a broader result expressly including this diagonal-weight crossover. The elementary event calculation makes independent prior derivation possible, and priority remains qualified rather than certified.

## Value: PASS
Loopless random mappings and classical uniform random mappings are standard neighboring models. Their natural one-parameter interpolation answers a structural question about whether incoming-degree-zero vertices and feedback cycles compete or coexist. The unique exact sign change for two-cycles, its microscopic cutoff, and the opposite rigid sign for all longer cycles provide a complete phase diagram; they are not a mere numeric instance or parameter relabeling. The exact critical window quantifies the passage between the distinct endpoint regimes.

## Limitations
The result is about covariances, not conditional independence, and applies only to independently sampled outgoing arrows with a common diagonal weight. A published equivalent derivation remains a real historical-priority risk. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
