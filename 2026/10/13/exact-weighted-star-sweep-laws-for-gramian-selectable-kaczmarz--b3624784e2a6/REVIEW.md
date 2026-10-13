# Scientific review

## Correctness — PASS

The row construction has exactly a star nonorthogonality graph, and the published GSSRK update forces nonrepeating leaf draws between center resets. The episode probability follows from the conditional selection weights; its finite mean follows by renewal. A separately derived first-step recurrence reproduces both formulas with exact rational arithmetic for 54 parameter pairs, plus an explicit selectable-set-state check. For the IID comparison, exponential first-arrival order and the center-draw count identity prove the stated expression without numerical extrapolation. The full argument covers all integers \(m\ge2\) and real weights \(w>0\); numerical checks only supplement it.

## Originality — PASS, subject to residual priority uncertainty

The two most directly relevant freely accessible source papers were examined through their algorithm definitions, theory sections, and relevant appendices. Yaniv et al. give the GSSRK transition and bounds on expected-error contraction / selectable-set sizes, not the exact star sweep-certificate law; Nutini et al. give orthogonality-graph row selection, update implementation, and rate bounds, not the same renewal comparison. Searches for aliases and stronger coverage in published mathematical findings and accessible literature found no exact overlap. This is a priority assessment, not proof of uniqueness; a related dissertation was available only in abstract form and an unindexed prior treatment remains possible.

## Value — PASS

A structural exact-solution certificate is useful when residual inspections are expensive, and it permits a transparent comparison of two legitimate sampling schemes at the same target condition. The formulas reveal a non-obvious \(m^{w+1}\) expected-certificate scale that changes with a single row's norm even though that row's projector and Gramian sparsity graph do not change. In particular, the conditional selectable-set rule removes a sharp constant factor \((w+1)/w\) versus fresh IID row sampling, with an additional harmonic gap as \(w\downarrow0\) at fixed \(m\). The result does not establish an equal improvement in expected numerical error, actual first-solution time, or computational runtime.

## Closest literature and limitations

The closest primary work is Yaniv et al., *Selectable Set Randomized Kaczmarz* (arXiv:2110.04703; Algorithm 3 and Section 4), following Nutini et al., *Convergence Rates for Greedy Kaczmarz Algorithms...* (arXiv:1612.07838; Appendix L). The common underlying coupon-collection reduction is classical, and the claim is carefully limited to the structural certificate on an explicit weighted star. A 2024 dissertation on Kaczmarz variants was not available in full text during this comparison; no wider priority guarantee is claimed.

Self-review: passed. Independent audit: not yet performed.
