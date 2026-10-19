# Self-review

## Correctness — PASS

The five-input median is globally Lipschitz, so the dynamics have unique forward solutions. The reduction of cohesive sets to induced minimum-degree-two sets is exact for equal self-plus-four-neighbor weights; such sets are equivalent to cycles. An unpinned cycle traps a non-target high-opinion group for all time. When the unpinned graph is a forest, leaf peeling exposes three already controlled median inputs at each step, giving the displayed global convolution/error bound by induction. The squared-ring gap criterion excludes exactly the triangular gaps and the unbroken winding cycle. Its sharp threshold and the optimal-layout enumeration follow from explicit bounded compositions. Independent finite enumeration and numerical trajectory checks support, but do not replace, these arguments.

## Originality — PASS (best-knowledge comparison)

Han et al.'s Proposition 14 already supplies the general cohesive-set pinning condition; it is credited, not presented as a novel condition. The new mathematical content evaluates its exact optimal design on the natural uniform five-neighbor cyclic family, classifies **all** successful positions, counts optimal positions, and derives a global finite-time error bound. The full accessible primary text discusses random-network pinning counts but gives none of those ring-specific exact results. Zhang et al.'s distinct discrete-time control theorem explicitly flags minimum pin-set determination as future work. Searches for feedback-vertex/decycling results on squared cycles did not identify an implication covering the full stated result. Residual risk: unindexed exact graph-power formulas may exist, and this finding is not independently audited.

## Value — PASS

The exact number and complete location criterion solve a natural, explicitly motivated network-intervention design problem, not an arbitrary finite special case: they distinguish one pin every three sites (which can fail by leaving a cycle) from an adjacent-pin break that guarantees consensus. The exact count quantifies design flexibility, and the all-initial-data rate bound supplies a checkable transient guarantee absent from bare asymptotic controllability. The earlier discrete-time prejudice paper independently identifies minimal pinning as a problem of interest.

## Scientific limitations

Only unit-rate full pinning with a common fixed target and uniform five-neighbor weights is included. The universal error bound is not established to be sharp. Graph-power specialist literature remains a residual originality risk; no independent external audit or certification has been performed.

Self-review: passed. Independent audit: not yet performed.
