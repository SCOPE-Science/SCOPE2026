# Review: Exact minimum-width directions of the sharp lattice-width simplex

## Correctness

**PASS.** The vertex evaluations reduce width to half the integer range of \(\{0,x_1,x_2,x_3\}\) on the congruence sublattice \(x_1+x_2+x_3\equiv0\pmod4\). If that range is below two, all entries lie in \(\{0,1\}\) or \(\{-1,0\}\), forcing the zero vector. The range-two cases are exhausted by the three sign patterns in the proof and map to exactly 18 vectors. The edge determinant is \(1/2\), so the volume is exactly \(1/12\).

## Originality

**PASS, with residual bibliographic risk.** Aliev’s 2023 paper states the sharp volume–lattice-width inequality and supplies the equality simplex, but the inspected text does not list its minimum-width directions. Draisma–McAllister–Nill give a universal count bound of \(3^3-1=26\) and characterize the equality case for that count; this does not imply the exact 18-vector set for \(\Delta\). Exact and alias-oriented literature searches found related general results but no matching classification. Search failure is not treated as proof of novelty.

## Value

**PASS.** The result gives the complete active-direction set for a canonical sharpness witness in a three-dimensional geometry-of-numbers inequality. This finite contact structure is a natural exact invariant of the equality example and is useful for comparing it with the universal direction-count theorem; no broader stability or equality-classification consequence is claimed.

## Closest literature and limits

- Aliev, arXiv:2306.14576: the sharp inequality and the equality simplex.
- Draisma, McAllister, and Nill, DOI 10.1137/120877635: the general lattice-width-direction count and extremal cross-polytope case.

Self-review: passed. Independent audit: not yet performed.
