# Mathematical review

## Correctness
**PASS.** The original all-pairs support constraints reduce to exactly two inequalities per cyclic neighboring normal by a monotone-turn polygon projection argument. The edge-tangent coordinate map is invertible on each neighbor pair (the angular gaps are strictly below half a turn); its closure equation has rank two. A strictly positive reference configuration supplies the full dimension and a transfer-of-duplicate-columns argument certifies every proposed facet. Minimal positive circuits of a rank-two matrix give a complete pair/triple classification and the combinatorial counting proof handles odd and even regular grids separately. The standalone checker independently verifies all proposed rays and original inequalities for dimensions three through twelve; those finite tests are supporting evidence rather than the infinite proof.

## Originality
**PASS, with residual priority risk.** Rieger (arXiv:2608.26615v1, 27 August 2026) supplies the motivating vertex-normal cone and some redundancy analysis. Those antecedents and classical positive-circuit theory are not claimed as new. Inspected corresponding sections do not supply a complete explicit H/V classification or the parity-sensitive extreme-ray sequence. Poullot's graphical-zonotope deformation cones (arXiv:2404.02669) and Padrol–Pilaud–Poullot's deformation-cone H-description concern non-equivalent parameter spaces; the cone dimensions and ray counts already differ for a regular hexagon. The recorded semantic searches did not find a covering statement. A possible earlier equivalent treatment under oriented-matroid or cyclic-cone terminology cannot be fully excluded.

## Mathematical value
**PASS.** The theorem provides the full irredundant inequality structure and generating-ray list for a geometrically motivated class of cones, then a closed cubic ray formula revealing an arithmetic odd/even change in canonical regular grids. It is a complete structural classification with a natural finite-dimensional optimization interpretation, rather than a bare collection of finite computations.

## Scientific boundaries
Consecutive angular gaps must be strictly between zero and a half turn. Ray classification is modulo translations. Uniform closed counts require equally spaced normals, although the geometric circuit classification covers all admissible grids. Floating-point checks are auxiliary only; no formal or independent verification is asserted.

## Sources considered
J. Rieger, *Galerkin approximations to the space of convex bodies by polytopes in nondegenerate V-representation*, arXiv:2608.26615v1 (2026). G. Poullot, *Rays of the deformation cones of graphical zonotopes*, arXiv:2404.02669 (2024). A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, DOI:10.1007/s00454-023-00586-x. Standard rank-two nonnegative-kernel circuit theory.

Self-review: passed. Independent audit: not yet performed.
