# Review

## Correctness

PASS. The proof exactly expands the quadratic LARS step, reduces the worst trust limit to a spectral-moment ratio, uses convexity to restrict the extremum to endpoint spectra, and solves the remaining scalar maximization. The two-dimensional diagonal witness attains equality.

Risk: the claim is one-step and excludes momentum.

## Originality

PASS. The defining source specifies the norm-ratio trust rule; the closest direct theory analyzes one-dimensional quadratics; the later layer-wise theory gives sufficient stochastic bounds. Focused comparisons found no statement implying the sharp SPD formula or its extremizer.

Residual risk: the moment inequality may be known abstractly outside LARS terminology.

## Value

PASS. The trust ratio is LARS's defining mechanism. The exact frontier gives a mathematically actionable safety law, shows the naive worst-curvature bound is substantially conservative, and identifies the precise spectral mixture that exhausts the margin.

Same-model review: passed. Independent audit: not yet performed.
