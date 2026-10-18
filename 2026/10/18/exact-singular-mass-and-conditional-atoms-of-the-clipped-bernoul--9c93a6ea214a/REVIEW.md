# Review of the singular-mass decomposition

## Correctness — PASS

The copula is fixed explicitly, with parameter and endpoint domains stated. For positive interior parameter, algebra gives the two exact clipping curves. The conditional CDF obtained by differentiating the joint CDF in its first coordinate jumps at each curve; its one-sided values yield the two displayed atom weights. The interior mixed derivative is nonnegative (a quantitative lower bound is proved) and integrates with those atoms to one. Uniformity of the first marginal allows exact integration of the two graph masses, proving a genuine Lebesgue decomposition rather than a merely formal density calculation. Reflection handles negative parameters, and the Fréchet/independence endpoint laws are explicit. The 20,814 reproducibility checks passed; the analytic proof, not finite sampling, establishes the universal claim.

## Originality — PASS, with residual priority uncertainty

The 2022 primary conference paper gives the copula and its clipping. The 2023 full copula-proof paper supplies the interior mixed derivative and boundary analysis, but the inspected text does not state a measure decomposition, conditional jump masses, or an integrated singular-mass formula. The 2017 transformed-copula study explicitly concerns singular components but has diagonal, not these two distinct non-diagonal, singular supports. General characterizations of bivariate copulas do not imply the model-specific integrated fraction without new calculation. Dedicated searches of research records under correlated Boolean operators, Lucas copula, clipped Fréchet bounds, Lebesgue decomposition, logistic support, and exact logarithmic mass identified no stronger covering theorem. Residual risk remains from uncatalogued or differently named earlier derivations; lack of matches is not a proof of novelty.

## Value — PASS

The measure's singular mass is not a negligible exceptional set: for \(|\rho|=1/2\), it is \(\frac23\log2\), over 46%. Any likelihood, simulation, or integration method that assumes a purely planar Lebesgue density loses this portion of probability. The exact conditional atoms, two support curves, and parameter-dependent mass split supply the missing information for rigorous distributional treatment of a natural previously published copula. This result does not claim a new copula or invalidate the original construction.

Self-review: passed. Independent audit: not yet performed.
