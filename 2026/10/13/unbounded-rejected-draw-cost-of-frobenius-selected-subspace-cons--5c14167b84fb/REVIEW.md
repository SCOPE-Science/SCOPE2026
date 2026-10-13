# Scientific review

**Correctness — PASS.** A direct projector computation gives all three Frobenius criteria and proves unique selection for \(0<t\le1/2\). The two active-row proposal probabilities follow from squared projected norms, and a geometric waiting-time calculation yields exact means. Both accepted projections were reconstructed analytically; rational instances independently checked by `verify.py`. There is no inference from a finite experiment to the universal claim.

**Originality — PASS, qualified.** The 2026 primary work gives the rejection rule, the row-norm distribution and the Frobenius surrogate separately, but neither the concrete family nor a uniform raw-proposal comparison with an alternative row selection. The 2023 SCRK paper gives a projected-row method and spectral convergence theory, but it does not compare the surrogate's proposal cost. The 2025 SC-RCD paper addresses a different coordinate/PSD setting. published-finding corpus similarity searches returned related Kaczmarz, row-coherence and pivoting results, but no statement implying this same-system unbounded selection regret. A rediscovery under alternate sampling-cost terminology remains a risk; literature search is not proof of uniqueness.

**Value — PASS.** The Frobenius selection surrogate is motivated by the cited work as a practical proxy for solver acceleration. The counterexample identifies a concrete computational cost not measured by accepted-iteration convergence bounds. It compares a globally optimal surrogate decision against an explicit alternative on the identical system and right-hand side, and the overhead ratio diverges despite identical accepted iteration counts. It exposes a structural design choice rather than a mere numerical failure.

**Scope and residual risks.** Exact arithmetic, singleton constraints, independent raw samples, unit relaxation, and zero-residual rejection. Dynamic residual-aware sampling would change the cost model. Other row distributions and numerical thresholds are not covered.

Self-review: passed. Independent audit: not yet performed.
