# Scientific review: induced matchings of cycle prisms

## Correctness — PASS
The graph-to-word bijection assigns each prism edge to exactly one column and one of three edge types. Endpoint inspection supplies complete nearest-column and distance-two exclusions. The seven-state closed-walk transfer enumerates precisely the permitted words; its determinant is an explicit exact integer-polynomial identity. The logarithmic derivative extracts all nontrivial trace coefficients. In the extremal proof, cyclic gaps force one three-gap in odd order, whereas even order forces one of two alternating supports, making the count a complete classification rather than interpolation. Replayed exact arithmetic in `verify.py` checks the determinant and all configurations of orders three to nine; the proof, not these finite checks, establishes the arbitrary-order claim. Restrictions: \(n\ge3\); no claim about other generalized Petersen graphs.

## Originality — PASS, with priority risk
The exact open-ladder enumeration by Mathar (arXiv:2404.18806, pp. 6–7, Eq. (8), Table 2) is **prior**; it does not impose cyclic longitudinal closure or state these prism counts. Joos–Rautenbach–Sasse (arXiv:1312.1110, pp. 1–2, Theorems 1–2) prove size lower bounds for all subcubic graphs, not the full prism polynomial or maximum-set multiplicities. Chen–Miao–Zhou (2020) concern strong edge-coloring numbers. The 2025 *Symmetry* prism matching-polynomial tables enumerate ordinary matchings, not induced matchings. An exact equivalent under cylindrical domino or generalized Petersen terminology might exist and would supersede the novelty claim; the literature searches did not locate one.

## Value — PASS
Cycle prisms are canonical cubic graphs with closure that changes the open-ladder enumeration; the complete induced-matching polynomial records the full size distribution. The sharp \(n^2\)/\(6\)/\(2\) maximum-set multiplicity dichotomy is a structural consequence of the cyclic topology, not a routine shift of the open-board formula. It provides an exact benchmark for strong-matching enumeration beyond universal cubic size bounds.

## Verification limits
The exhaustive test has finite scope. No independent mathematical audit or earlier-priority guarantee is claimed; the complete theorem rests on the included combinatorial argument. Any equivalent uncatalogued cyclic-cylinder formula would require a fresh priority comparison.

Self-review: passed. Independent audit: not yet performed.
