# Review

## Correctness

PASS. The first two source Apollo iterations are reconstructed exactly. Zero initialization forces \(B_1=0\), the bias-corrected momentum gives a closed form for \(m_2\), and substitution into the diagonal quasi-Newton update yields the exact \(B_2\) formula. Solving \(B_2>\sigma\) gives the sharp activation threshold and initialization boundary.

Risk: the theorem is limited to the first two informative iterations and constant learning rate.

## Originality

PASS. The defining paper discusses zero-initialization bias, rectification, learning-rate/floor coupling, and warmup; the official implementation stresses that warmup is important. Neither inspected source states the second-step estimate, its saturation ceiling, or the universal threshold \(q=1+\beta\). Focused published-record searches found no implication-equivalent Apollo result.

Residual risk: an equivalent short calculation may exist in unindexed optimizer notes.

## Value

PASS. Apollo's defining feature is learned diagonal curvature, yet its source initialization deliberately starts that state at zero and relies on a rectification floor. The finding gives an exact criterion for when the learned curvature can first matter, directly illuminating the optimizer's documented warmup sensitivity and providing a concrete diagnostic in the simplest curvature model.

Same-model review: passed. Independent audit: not yet performed.
