# Scientific assessment

## Correctness — PASS
The argument proves a Borel-measure identity, not merely finite moments: acute geometry partitions each target side into two nonoverlapping projection intervals; their incoming constant densities coincide exactly when \(p_i\cos A_i/\ell_i\) is constant. A two-step synchronous coupling has a strict common squared contraction factor, proving finite-moment existence, uniqueness, and quantitative \(W_2\) convergence; a pathwise coupling extends invariant uniqueness without moment assumptions. An exact SymPy checker tests twelve rational density constraints and 72 polynomial identities on two nonsymmetric acute triangles. The checker is supplementary to the analytic result.

## Originality — PASS, qualified
Relevant full-text comparisons include Zeng et al. (arXiv:2301.00176), whose adaptive-step algorithm targets least-squares convergence, and Hermer–Luke–Sturm (arXiv:2205.15897), whose general invariant-measure theory covers broad nonexpansive random iterations but does not state the explicit triangle uniform-density sampling classification. Li–Wu (arXiv:2310.14175) uses an augmented update, not this chain. Related work on deterministic farthest-line triangle projection maps does not imply a law for iid random line selection. Targeted title/claim/equivalence searches found no dominating exact statement. This is evidence for originality, not proof of universal publication priority: Butnariu's earlier expected-projection theory and specialized geometric random-iteration literature remain a residual risk.

## Value — PASS
The complete, geometrically natural classification of **which sampling probabilities make an inconsistent randomized Kaczmarz problem sidewise uniform** provides an exact benchmark for stochastic projection stationary behavior. It ties row probability to an observable invariant density, separates per-side from global perimeter uniformity, and supplies a quantitative convergence bound even though individual iterates cannot solve the inconsistent equations. The result is not a routine change of variables in the cited general convergence statements.

## Scope and verification limitations
The acute assumption is essential to the two-interval proof; right and obtuse triangles are unclassified here. The Wasserstein contraction constant is sufficient rather than proved optimal. Exact polynomial tests are finite corroboration, not the source of the all-triangle proof. Specialized earlier literature is not exhaustively accessible and independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
