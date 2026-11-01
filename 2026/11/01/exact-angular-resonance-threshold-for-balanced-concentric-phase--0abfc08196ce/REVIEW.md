# Self-review

## Correctness — PASS

The root-of-unity DFT of the intensity trace has only the top harmonic aliased at two samples per degree. Its two real projections invert exactly when \(\sin(d(\phi_2-\phi_1))\ne0\); rational two-circle reflection then enforces constant phase. The explicit equal-radius linear-factor pair and resonant-angle degree-\(d\) binomials establish both necessary conditions. The standalone deterministic checker passes 6048 finite assertions; only the written algebraic proof justifies the all-degree quantifiers.

## Originality — PASS (historical priority provisional)

Pohl, Li, and Boche (2017, Theorem 7) already provide a \(4d\)-site design on two concentric circles, but with \(2d+1\) and \(2d-1\) sites rather than balanced regular \(2d\)-gons. Bodmann and Hammen (2013, §2.3) use intersecting circles. Grohs, Liehr, and Rathmair (2023) concern infinite-dimensional Fock-space sampling. The known degree-two balanced-orbit case is not presented as new. A complete equivalence, broader-coverage and result-index comparison found no all-degree balanced-grid resonance classification; an unindexed earlier result remains possible.

## Value — PASS

The result solves a natural exact classification problem at the established \(4d\)-measurement budget. It identifies precisely how a balanced pair of FFT-compatible regular polygon orbits can fail universally despite different radii, and which rotations restore universal injectivity. It does not depend on an artificial fixed-degree slice, claim a new measurement-count minimum, or infer noise stability.

## Scientific scope and limits

All degrees \(d\ge1\), arbitrary complex coefficients, positive known radii, noiseless point samples. No quantitative conditioning or arbitrary irregular-grid classification is proved; independent mathematical verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
