# Scientific review: forced four-colouring of wheel graphs

## Correctness — PASS
The exact if-and-only-if classification separates the initially seeded hub from the unseeded hub, rules out adjacent unseeded rim vertices by a first-move argument, and derives the correct three-colour compressed-cycle count. Inclusion–exclusion enforces three distinct visible colours before the hub can force. The cycle independent-set formula and a minimum-seed construction prove the infinite result. The standalone standard-library verifier independently simulates the original forcing rule for all partial assignments of wheels with five through seven rim vertices and checks coefficient formulas against cyclic patterns and bitmask counts up to twelve rim vertices. It returned `VERIFY_OK (64 independently cross-checked identities)`.

## Originality — PASS, with historical-priority limits
G. E. Farr's 2026 foundational forced-colouring article introduces the general function and discusses its complexity; the inspected accessible full-text sections do not give this complete wheel-four polynomial or the minimum-witness count. Searches across descriptions 'wheel', 'cone over cycle', 'partial four-colouring', and 'forced colouring' returned related exact results for three-colour paths/cycles and complete multipartite graphs, but not a directly equivalent wheel statement. The all-order wheel structural decomposition adds a hub-unseeded surjectivity requirement not in those closest statements. Unlocated older equivalent enumerations remain possible; search absence is not uniqueness proof.

## Value — PASS
This is a full size-refined enumeration and exact optimizer classification for a natural infinite family central to graph colouring, answering a graph-specific instance of the 2026 forced-colouring probability problem. The hub-first obstruction and compressed-cycle bijection account for both degree distribution and parity dependence of minimum seeds; the result is not only a numeric threshold.

The palette is fixed at four named colours, the rim length is at least five, and no independent external validation is asserted.

Self-review: passed. Independent audit: not yet performed.
