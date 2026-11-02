# Scientific assessment — parity-split majority cycles on wheels

## Correctness — PASS

The claim covers every integer rim length \(n\ge3\), uses labelled graph states, and counts each temporal two-cycle once. The proof is reconstructed from the explicit majority update: fixed-hub cycles force distance-two parity-class constancy, while hub-flipping cycles have a unique hub-zero representative satisfying the necessary and sufficient no-isolated-one condition together with the two strict half-density inequalities. The step-two graph has either one or two cyclic components, and the three-state transfer and cyclic run-composition formula count them without normalization ambiguities. The classical finite-graph period-two property is additionally re-proved by a symmetric integer potential. Exact code checks cover all \(262{,}128\) configurations at rim lengths three through sixteen; these finite checks supplement rather than replace the proof.

## Originality — PASS, with residual search risk

The closest early results are Goles–Olivos's period-at-most-two theorem and Agur–Fraenkel–Klein's enumeration of fixed cyclic one-dimensional majority strings. Full inspection of the eight-page Agur–Fraenkel–Klein article confirms its graph has no hub and its counting problem is fixed cyclic strings, not wheel primitive two-cycles. Benjamini et al. (arXiv:1405.2486v1) prove convergence phenomena, and Kaaser et al. (arXiv:1508.03519v1) study convergence time and hardness; neither supplies the wheel orbit-count polynomial in the inspected full-text sections and searches. Turau's later arXiv:2202.01580 classification is for trees. Aledo et al. (2020) treat a different maxterm/minterm Boolean update family. A distinct same-rule formula for open ladders concerns a different graph and transfer structure. Queries of mathematical literature and published-finding corpus did not identify an equivalent wheel count, but absence from indexed results cannot exclude a little-known preprint or alternate terminology. The assessed novelty is the complete wheel-specific two-cycle phase classification and exact count, not the previously available potential argument or run-composition technique.

## Value — PASS

Wheel graphs are the simplest cyclic networks with a global neighbour interacting simultaneously with locally constrained rim vertices. Their behaviour is not captured by the cycle-only fixed-point census: every wheel has just two steady configurations, yet exponentially many distinct oscillatory attractors, with a sharp parity split depending on whether the hub alternates. The exact binary-polynomial formula and proven exponential lower bound quantify this qualitative difference for all wheel sizes. It is an intrinsically useful recurrent-orbit classification rather than a single ad hoc value. Attraction basins and an exact exponential growth constant remain open within this result.

## Scientific limits and closest references

The work does not count transient states or their basins and does not claim independent certification. The most relevant primary references are Agur–Fraenkel–Klein (1988), Benjamini et al. (2014, arXiv:1405.2486v1), Kaaser et al. (2015, arXiv:1508.03519v1), Turau (2022, arXiv:2202.01580), Aledo et al. (2020, DOI:10.1155/2020/9708347), and Goles–Olivos (1980). Residual risk: an overlooked same-rule wheel enumeration may exist under a different name.

Self-review: passed. Independent audit: not yet performed.
