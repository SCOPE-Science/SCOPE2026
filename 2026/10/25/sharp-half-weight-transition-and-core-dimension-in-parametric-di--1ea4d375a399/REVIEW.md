# Scientific review

## Correctness — PASS

The claim is quantified over all finite loopless directed graphs with nonnegative weights and all convex mixing coefficients. The co-singleton calculation is exact because outside the coalition containing every vertex except one, the external contribution is the sum of that vertex's outgoing weights. Adding the implied individual upper bounds forces an empty core below one half and pins all coordinates at the boundary. Above one half the explicit allocation has the exact nonnegative cut-slack decomposition shown in the proof; strictness identifies the active component-union constraints and yields the core dimension. Restricted core allocations are constructed directly for every player subset, proving total balancedness. The two-vertex case establishes sharpness. The exact-arithmetic checker returned PASS on 22,085 parameterized finite graph cases. Finite checks are not used as a proof of infinite-size assertions.

## Originality — PASS, with residual priority risk

The closest primary work is Ryzák and Kroupa (arXiv:2605.18157v1, Sections 2, 5, and 6). It solves the fixed unweighted-sum model and explicitly proposes studying convex combinations as future work. The earlier Bandhana–Kroupa–García AAMAS 2024 paper likewise concerns the original fixed sum. Neither inspected work states the three-phase empty/singleton/positive-dimensional classification, the exact weak-component dimension, or the all-coefficient total-balancedness criterion. General theory of internal edge-sum games gives a known endpoint but not the claimed parameter-wide converse. Targeted phrase and implication searches did not surface equivalent coverage. Equivalent material under alternative parametric cooperative-game terminology has not been exhaustively excluded.

## Mathematical value — PASS

The mixing coefficient is a natural model choice that governs whether coalitions value internal edges or external minimum trust. The theorem answers a research direction explicitly posed in the motivating paper. It shows a qualitative instability for even infinitesimal weight changes below one half, a unique stable allocation at equality, and an exact graph-topological dimension of bargaining freedom above one half. The sharp two-node example and total-balancedness classification make the transition structural rather than a numerical instance-specific observation.

## Scope and limitations

All claims use the stated zero-for-empty-minimum convention and nonnegative weights. The full core vertex and facet structure is not classified. The tests cover finite families only; independent validation and exhaustive bibliographic priority confirmation are not claimed.

Self-review: passed. Independent audit: not yet performed.
