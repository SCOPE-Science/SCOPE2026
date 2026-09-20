# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The stagewise norm condition is exactly \(0\le\tau_i\le2/L\) for symmetric positive-definite matrices with spectrum in \([\mu,L]\). After normalization, the two-stage problem becomes a constrained minimax problem for \((1-ux)(1-vx)\) with \(u,v\in[0,2]\). In the well-conditioned branch, the ordinary degree-two Chebyshev roots satisfy the constraint exactly up to \(\kappa=1+\sqrt2\). In the other branch, an endpoint lower bound proves that every feasible pair has norm at least \((1-2a)/(1+2a)\), while the explicit pair \(u=2\), \(v=2/(1+2a)\) attains that bound; its only interior extremum stays below the endpoint level precisely for \(a\le\sqrt2-1\). Equality conditions give uniqueness up to permutation.

The general \(m\)-stage lower bound is immediate at the smallest curvature: if every step is individually nonexpansive and \(\kappa\ge2\), then each factor at \(\mu\) is at least \(1-2/\kappa\). Repeated optimal fixed-step Richardson supplies the matching-order upper bound. Deterministic checks reproduce the piecewise closed form, the phase-transition continuity, the comparison identities, and representative interval sup norms.

## Originality

**PASS, to the best of our knowledge.** Classical Golub--Varga Chebyshev semi-iteration provides the unconstrained minimax baseline. Axelsson explicitly records that the factorized one-step Chebyshev form can have individual iteration matrices with norm much larger than one and discusses permutation/stable-recurrence remedies. Manteuffel treats optimal stationary second-degree methods. Sambharya--Stellato study learned finite step sequences for a mean-square parametric objective. General restricted-zero approximation problems also exist.

No checked source stated the present constrained result: the exact two-stage uniform minimax value under the requirement that every Richardson factor be a Euclidean nonexpansion, its transition at \(\kappa=1+\sqrt2\), the unique boundary pair \(\{2/L,2/(L+2\mu)\}\), or the resulting all-\(m\) obstruction to Chebyshev-order acceleration under the same factorwise constraint. The result is elementary enough that independent rediscovery is plausible. The full theorem-level text of the 1961 Golub--Varga papers was not inspected, leaving the main residual historical-coverage risk.

## Value

**PASS.** The result converts the familiar internal-instability issue of factorized Chebyshev iteration into a sharp optimization frontier. It identifies exactly when two-step Chebyshev acceleration is compatible with per-step nonexpansiveness, gives the optimal replacement once that compatibility fails, and shows more generally that insisting on individually safe first-order factors destroys the square-root condition-number acceleration order. The theorem also separates this strict factorwise notion from more permissive stabilization by parameter ordering or three-term recurrences.

## Scientific limitations

- Exact arithmetic and SPD matrices only.
- The robust objective is over a full continuous spectral interval; a particular discrete spectrum can admit better tailored parameters.
- Euclidean factorwise nonexpansiveness is a deliberately strong stability condition, not a claim about the weakest sufficient notion of numerical stability.
- No floating-point error-growth, backward-stability, or implementation-performance theorem is asserted.
- Stable three-term Chebyshev recurrences and factor orderings that permit temporary amplification are outside the constraint.
- Nonsymmetric, indefinite, nonlinear, stochastic, adaptive, momentum, conjugate-gradient, and line-search methods are outside the claim.
- Full theorem-level text of the 1961 Golub--Varga papers was not inspected, leaving residual originality uncertainty.
