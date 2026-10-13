# Review

## Correctness

PASS. Solving the source pseudo-count recurrence under exact inliers gives its fixed point, and substituting a single outlier into the source Student-\(t\) first-momentum update yields the stated rational attenuation exactly. The Mahalanobis displacement has one critical point at \(D=\nu/\beta\), which is its global maximum. The sparse-support dimension law follows directly from \(D=kz^2\).

Risk: the result isolates first-momentum influence at a calibrated state; the second-moment and subsequent parameter trajectory are not classified.

## Originality

PASS. The source papers already state continuous outlier down-weighting and qualitatively warn that large whole-vector blocks can under-detect sparse aberrations. Those facts are treated as prior. The inspected literature does not state the exact beta-dependent calibrated influence curve, its sharp maximum, or the \(\sqrt{d/k}\) half-attenuation threshold.

Residual risk: a short equivalent calculation may exist in unindexed robust-optimizer notes.

## Value

PASS. Robustness and block granularity are central to TAdam's design. The theorem supplies an exact worst-case influence bound and quantifies the source's qualitative block-size warning, showing precisely how sparse-outlier detectability degrades with dimension under the recommended \(\nu=d\).

Self-review: passed. Independent audit: not yet performed.
