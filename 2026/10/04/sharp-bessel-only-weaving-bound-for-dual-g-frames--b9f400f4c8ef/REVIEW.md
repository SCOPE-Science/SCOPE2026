# Review: Sharp Bessel-only weaving bound for dual g-frames

## Correctness
PASS. For a unit vector, the four partial energies \(x,y,u,v\) are nonnegative and the dual reconstruction identity gives \(1\le\sqrt{xu}+\sqrt{yv}\). Substituting the two Bessel bounds and applying Cauchy-Schwarz yields the exact scalar constraint \(1\le\sqrt{E(S-E)}\). Since \(S\ge2\), solving the quadratic gives the claimed lower bound. The sharpness construction has trace \(S\), determinant \(1\), and therefore the same extremal root; its common index-space rotation preserves norms and the dual pairing. Boundary cases and the infinite-index convergence requirements are included.

## Originality
PASS with stated residual risk. The motivating 2024 paper materially states the weaker lower bound \(1/(2\max\{B_\Lambda,B_\Gamma\})\). The 2020 generalized-frame paper establishes that a g-frame and a dual g-frame are woven, while the 2019 duality paper treats sufficient conditions for selected duals. Targeted searches for the square-root formula, Bessel-only sharpness, one-dimensional extremizers, and operator-valued aliases returned no covering statement. A 2025 operator-valued weaving article is highly relevant but its theorem body was not materially available; its accessible abstract does not state the present two-parameter formula, so it remains the principal residual risk rather than evidence of coverage.

## Value
PASS. The result converts a qualitative dual-weaving theorem with a nonsharp universal lower estimate into the exact best guarantee obtainable from the two natural Bessel conditioning parameters. The extremizers are completely classified at the level needed for sharpness by a two-dimensional Gram/eigenvalue reduction and exist for every admissible parameter pair, so this is a structural improvement rather than a numerical example.

## Closest literature and limitations
The closest inspected statement is Corollary 5.2 of Xiao, Zhao and Zhou, which gives lower bound \(1/(2\max\{B_\Lambda,B_\Gamma\})\) under the same dual g-frame hypotheses. Deepshikha and Samanta supply the earlier qualitative dual g-frame weaving theorem. The result here does not determine the exact weaving bound for an individual pair from its full geometry and does not claim an extension to general \(K\)-g-frames.

Same-model review: passed. Independent audit: not yet performed.
