# Independent mathematical audit

## correctness

PASS

For three exact normalized planar rows, after a nonterminal projection the error lies on one row-orthogonal line; squared norm transition factors are x=cos²θ or y=(2x−1)² and greedy residual ranking uses complementary factors. The resulting 3x3 weighted transition matrices M1,M2,M3, with a conditional preference swap at x=1/4, were inspected and their characteristic roots checked symbolically. The Perron eigenvalues yield λ1=(2+y+√(y²+8x²))/6; λ2 piecewise (y+√(y²+24x²))/6 or (y+√(y²+3x²))/3; λ3=min(x,y). Exact resultant factorizations of 3t²−y t−2x² with t³−x² and 3t²−2y t−x² with t³−y² give P5 and P9; Sturm variation counts isolate roots in (1/12,1/8) and (1/4,1/3). The sample-budget quantities λβ^(1/β) are then compared, and exact singleton lower bounds exclude unique β=1. The tie at x=1/4 and finite termination x=1/2 are handled. Independent symbolic identities and finite exact projections corroborate but do not replace Perron/Sturm proof.

## originality

PASS

Haddock–Ma establish sample-size-dependent SKM bounds and explicitly leave precise tuning as a challenge; De Loera–Haddock–Needell supply the SKM method and empirical sample-size comparisons, not the special exact squared-error Markov exponents or two sharp algebraic cost crossovers. Related Resultary two-row Kaczmarz relaxation and residual-coherence notes concern different matrices/cost models. The new claim resolves a geometry-dependent exact three-size minimization with full ties in the smallest nontrivial three-row setting.

## value

PASS

The three-row planar SKM system is the first genuinely nontrivial geometry where each β in {1,2,3} can be chosen. The two sharp transitions show that maximum greed is not always optimal per charged residual, but it becomes optimal in two disjoint regimes; this mathematical rate-budget phase diagram is a useful exact benchmark, even though it does not predict implementation wall time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
