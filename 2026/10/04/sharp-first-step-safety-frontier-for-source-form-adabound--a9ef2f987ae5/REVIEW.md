# Review

## Correctness

PASS. The source first step is reconstructed exactly. Varying the nonzero scalar initialization makes the raw rate span all positive values, so the clip spans its entire interval. Universal objective monotonicity therefore reduces to the sharp endpoint condition \((1-\beta_1)h u_1\le2\), and failure creates an exact upper-clipped amplification plateau.

Risk: the theorem concerns the source theoretical recurrence without the bias correction and epsilon used by some software implementations.

## Originality

PASS. The defining paper gives dynamic clipping and the recommended schedule; the direct 2019 correction addresses the regret proof and arbitrarily slow convergence; later work qualitatively criticizes task-independent bounds. The inspected literature does not state the exact curvature-sensitive first-step frontier, upper-clipping plateau, or high-\(\beta_2\) amplification law.

Residual risk: an equivalent local observation may appear in unindexed optimizer discussions.

## Value

PASS. Dynamic clipping is AdaBound's defining response to extreme adaptive learning rates. The finding shows that a finite upper bound can itself be dynamically unsafe, quantifies the exact curvature limit, and demonstrates the effect at the paper's stated defaults. This gives a concrete safety diagnostic for the core mechanism.

Same-model review: passed. Independent audit: not yet performed.
