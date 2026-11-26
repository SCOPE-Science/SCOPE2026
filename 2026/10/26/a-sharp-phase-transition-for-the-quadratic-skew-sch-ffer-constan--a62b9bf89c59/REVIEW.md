# Independent mathematical audit

## correctness

PASS

The six-edge isometries and the pair operation (x,y)↦(y,−x) induce j↦−j and j↦3−j on relative edge indices. The two orbits are {0,3} and {1,2,4,5}; the first-coordinate test gives the lower bound A=1+τ² in the first orbit. In the second orbit take x=(1,a), y=(-1+b,-1). For x+τy the two nonnegative candidates 1−τ+τb and 1−a+τb dominate |a−τ|, and for τx−y the two nonnegative coordinates dominate their absolute difference. This gives precisely the two maxima in the frozen proof and a convex squared objective. At a=τ, b=τ(1−τ), choosing the second-norm branch weight θ=τ(1−τ) zeros the b component; the required first-norm weight κ=τ(1−θ)/(1−τ) zeros the a component iff κ≤1, exactly the sign test for 1−2τ+τ²−τ³. This polynomial is strictly decreasing and changes sign. Above its root, the candidate a=(A²−τ)/(A²+τ²), b=τ(1−a) has a<τ, satisfies AU=τV for the two transformed norms U,V, and the ridge weight θ=τ²/A gives zero gradient of the squared objective in the subgradient sense. The candidates coincide at the transition. The first trial family is admissible on [0,1] and its squared objective is ≤A, with the stated nonnegative factorization; this closes the comparison with the other orbit. At τ=1 the second candidate gives (U,V)=(4/5,8/5) and squared value 8/5, while at τ=0 all pairs give 1. Norm symmetry proves reciprocity and the Taylor coefficients are 1, −1/2, 9/8. The active-facet description concerns a representative optimizer; the pair symmetry can exchange the two norms.

## originality

PASS

The general invariant and reciprocal identity are antecedents. The exact outer-quadratic profile on the stated real hexagon, including the active-set switch, is distinct from the inspected Hilbert and Lp formulas and from same-norm skew-James or skew-quartic supremum results. The cited outer-∞ record is the closest plausible overlap; its reported value at τ=1 is for a different objective, and its text could not be independently retrieved from the mirror. No priority is inferred from search misses.

## value

PASS

The affine-regular hexagon is a natural test space for the published Banach invariant because it has finitely many support directions without being Hilbert. The complete quadratic profile gives an explicit non-Hilbert example in which the active facets change at a nontrivial parameter and the small-skew decrease is linear. A user needing this exact value or its change under the skew parameter cannot obtain it by importing the Hilbert or outer-∞ value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
