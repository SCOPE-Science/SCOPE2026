# Self-review

## Correctness

PASS. Complete algebraic reconstruction establishes the exact transition from the full row projection, positivity of all row normalizers, reversibility and aperiodicity, Vandermonde factorization and eigenvalue inertia, squared-residual moment identities, and the compact-constraint sharp cubic-moment bound. All period-two exceptions and repeated data have been kept. `verify.py` passes 12,006 exact rational test cases and 54 exact outlier cases. The finite tests support but do not replace the general proof.

## Originality

PASS, with documented residual bibliographic uncertainty. The primary residual-power Kaczmarz paper proves convergence for consistent systems and explicitly asks about inconsistent equations. Other noise-tolerant/sparse Kaczmarz studies analyze alternative algorithms and convergence bounds rather than an exact row-index invariant law with the sharp bias and spectral-inertia classification. Closest indexed records concern cyclic under-relaxation bias, maximal-distance one-step residual spikes, and two-row cyclic finite-horizon rates. Classical Markov reversibility and distance-kernel inertia are acknowledged as inputs; neither alone states the full sharp residual-driven Kaczmarz classification. The nearest published comparison is algorithmically narrower; hidden/unindexed equivalent constructions remain possible. The no-covering assessment is not an independence or database-completeness claim.

## Value

PASS. The source explicitly motivates residual-weighted Kaczmarz as improving projection progress, making the inconsistent-system behavior a consequential algorithmic gap. The theorem proves an unambiguous design warning: for one outlier among arbitrarily many unit-row observations, pure residual weighting visits it in one half of stationary steps, rather than one over sample size; even away from this extremum, squared weighting never improves stationary least-squares error relative to uniform full projections. The exact maximum skewness-controlled bias and all-exponent spectral-sign change classify quantitative and qualitative failure mechanisms, not simply one numerical counterexample.

## Closest literature and limits

Steinerberger, arXiv:2007.02910v1 (original sampler and explicit inconsistent-system question); Zhang et al., arXiv:2306.06813v1 (related noisy weighted sparse Kaczmarz); Bogomolny--Bohigas--Schmit, arXiv:nlin/0301044v1 (distance-matrix spectral background); classical detailed-balance and inertia results. Scope is strictly exact full-step scalar projections, with no claim for higher-dimensional or damped variants. In the two-distinct-value zero-floor case, convergence is only Cesàro because the chain is periodic.

Self-review: passed. Independent audit: not yet performed.
