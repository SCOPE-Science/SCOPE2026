# Mathematical review: single-erasure Chebyshev–Lobatto interpolation

## Correctness

PASS. The rank-one cancellation of a full-grid cardinal polynomial eliminates the highest coefficient, identifies the reduced-grid basis, and gives the exact value at the missing node. The reverse triangle inequality and the classical Chebyshev cardinal trigonometric identity reduce the norm asymptotics to one cardinal supremum with a uniform logarithmic error. Concavity of sine proves the global factor bound used in both localization regimes, and the boundary-scaled sinc ratio gives the strict overshoot and its positive inverse-square correction. The accompanying checker passed 1242 finite consistency assertions. Numerical tests are supportive only; the mathematical limits are proved analytically.

## Originality

PASS within examined material, not an assertion of global historical uniqueness. Mascarenhas (arXiv:1309.7944) analyzes full-grid barycentric evaluation and numerical rounding; Xiang (arXiv:1411.7746) studies full-grid interpolation rates and fundamental-polynomial estimates; Wu (arXiv:2606.23409) studies same-size perturbed grids. None of the inspected statements establishes the one-deletion sharp normalized Lebesgue limits as a function of deletion position. Salzer's 1972 abstract concerns the full grid and barycentric evaluation; its full text was inaccessible and represents an acknowledged residual priority risk. Generic Lagrange identities give a reduction but do not themselves state or evaluate the asymptotic boundary-profile maximization.

## Value

PASS. Chebyshev–Lobatto grids are used precisely because ordinary interpolation amplification is only logarithmic. The theorem shows a single lost measurement creates a linear instability and resolves the sharp coefficient in the edge, fixed-distance, and moving-bulk regimes, uniformly over erasure positions. The nontrivial sinc-ratio boundary layer, with strictly positive overshoot and explicit inverse-square decay, quantifies how sensitivity depends on the erasure location and supplies useful guidance for interpolation with incomplete sampling.

## Limits and nearest literature

The result does not determine exact finite-degree global argmax locations, analyze multiple missing points, or certify historical priority. Nearest work: Salzer (1972), Mascarenhas (2013), Xiang (2014), and Wu (2026) as listed in `RESULT.md`. The 2026 paper is comparison literature only, not the historical anchor.

Self-review: passed. Independent audit: not yet performed.
