# Scientific review: sharp hostile-degree preservation and finite stabilization

## Correctness — PASS

The fully receptive Kann--Feng update yields the exact rank-score identity \(x_i^+=\mu+(c/n)g_i(x)\). Hostile degrees bound every next-step gap, while choosing the top two hostile-degree vertices as the initial extremes proves the strict boundary is necessary. The convex total hostile-distance subgradient supports an increasing potential with strict gain \(n\|x^+-x\|_2^2/(2c)\); because the post-first-step scores are finite-valued, exact finite termination follows. The integer-score proof handles ties with the source's label-based convention. The standalone standard-library checker passed 2,800 exact direct-update cases, 231,388 finite exhaustive assertions, and 7,818 additional sampled checks. These checks corroborate, not replace, the universal proof.

## Originality — PASS (priority risk retained)

Kann and Feng, arXiv:2301.02210v1, define this model and prove a separate fully hostile clique result (Theorem 4.10), while leaving broader intuition in Theorem 4.11. Their inspected statements do not imply the sharp mixed-sign degree-sum criterion or finite-step termination with quantized states. Conventional HK finite-time convergence (Bernardo et al., DOI:10.1016/j.automatica.2023.111302; Li, arXiv:2112.13348v1) has different positive-only or mixed-averaging dynamics. He et al. (DOI:10.1016/j.neucom.2019.12.061) is a plausible earlier signed model, but the obtainable abstract describes sign-preserving dynamics, unlike the present update; its full paper remained inaccessible. Semantic mathematical-result and published-literature searches identified no directly covering claim, but failed retrieval is not proof of absence.

## Value — PASS

For any size of fully connected signed social network, the inequality \(d_{(1)}+d_{(2)}<n\) is a sharp topology-only guarantee against all future loss of influence from initially trusted pairs. It simultaneously gives exact finite-time stabilization and discrete possible equilibrium offsets. This addresses a motivated hostility-versus-confidence question and identifies a structural preservation boundary rather than providing a routine special-case computation.

## Scope and residual uncertainty

Conclusions do not cover trajectories starting outside full confidence, edge deactivation after the first update, incomplete signed graphs, asynchronous rules, or alternative hostile corrections. The step bound is not claimed sharp. Full-text publication-priority uncertainty persists for the earlier signed-model article.

Self-review: passed. Independent audit: not yet performed.
