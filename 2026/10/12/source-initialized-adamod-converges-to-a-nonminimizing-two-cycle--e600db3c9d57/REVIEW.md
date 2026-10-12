# Review

## Correctness

PASS. The defining AdaMod update has been specialized without removing the moving-average rate state, clipping minimum, or source initialization. On the explicit parameter rectangle a rational derivative bound proves a \(24/25\) contraction of a forward-invariant square. The parameter changes sign at every step, and the deviation from its nonzero limiting alternating orbit is bounded for **every** positive integer. The small-positive-moment extension is proved using a local four-state contraction and summable bias-correction perturbations. Numeric iteration is supporting only, not a substitute for the infinite proof.

## Originality

PASS. Adam limit cycles and their bias-corrected attraction are prior (Bock–Weiß, arXiv:2210.02070v1), as is the elementary one-step startup attenuation of AdaMod. The new theorem specifically establishes the complete actual **AdaMod** source trajectory with an evolving and sometimes active minimum cap, an explicit open parameter rectangle, a rational invariant square, and persistence with strictly positive moments. The defining AdaMod paper, arXiv:1910.12249v1, does not provide these conclusions. The accessible excerpt of a broader optimizer comparison describes qualitative late deterioration only; its complete text was not inspected, and unindexed overlap remains a residual risk.

## Value

PASS. The exact two-cycle demonstrates that the smoothing safeguard can produce an initially safe descent while failing even asymptotic stationarity on a deterministic strongly convex quadratic. The geometric certificate and strictly positive-moment continuation separate this structural mechanism from both an initial-step toy calculation and an arbitrary simulation. The explicit smoothing interval does not cover the method's usual near-one memory parameter.

Self-review: passed. Independent audit: not yet performed.
