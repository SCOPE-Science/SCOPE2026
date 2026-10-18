# Scientific assessment

## Correctness — PASS

The claim has the exact domain of a nondegenerate parallelogram with four independent uniform-arclength samples, one per side. Affine normalization is justified because each edge is traversed at constant speed. The square-minus-hull decomposition gives the exact four-corner coverage identity, and direct one-variable integration supplies the corner probability. Reflection/exchange symmetry reduces the full depth to one wedge. Explicit positive partial derivatives make the center the unique point with coverage one. A uniform second-order Taylor expansion establishes the upper-depth level-area asymptotic; a monotone slice-width argument with a separate shrinking-corner bound establishes the logarithmically corrected lower-depth level-area asymptotic. The constants are \(\pi/4\) and \(4\), respectively, for **the distribution of the coverage depth** at an independent area-uniform location.

A standalone checker passes 3000 formula comparisons, 330000 direct hull-containment trials (also under a skew affine map), and finite quadrature checks near both endpoints. Those checks support the derivation; they cannot prove its all-parameter identities or infinitesimal asymptotics.

## Originality — PASS, qualified

Maesumi's 2018 triangle paper examines the area distribution of a three-side sample and contains no parallelogram-specific pointwise coverage field or depth-level endpoint laws. Reitzner, Schütt and Werner's 2019 preprint studies pooled-boundary samples and asymptotic polytope volume/face counts; those statements do not imply the present stratified finite-four-point conditional coverage-depth distribution. Closest related calculations involving triangular inclusion depth reuse the same elementary corner probability; no novelty is attributed to that integration. Previously treated quadrilateral **area** mean, variance, and density also do not determine the distribution of pointwise conditional inclusion probabilities. Searches using spatial depth, corner probability, four independent side samples, level areas, and logarithmic lower-depth rates disclosed no equivalent statement. Exact publication priority remains uncertain because literature search is not exhaustive.

## Mathematical value — PASS

Pointwise convex-hull inclusion is a natural coverage diagnostic distinct from the area of a random hull. The theorem determines the whole spatial coverage field in an affine-invariant family, proves that only the center has certain inclusion, and resolves both extremes of the induced depth histogram. The lower tail has width \(\varepsilon/\log(1/\varepsilon)\) from host edges, whereas the near-certain superlevel region has area proportional to \(\varepsilon\) around the center. These quantitatively different regimes are not fixed by the known mean-area identity. The sharp coefficients are attached to a natural continuous coverage statistic, not to an arbitrary finite computation.

## Boundaries and residual risks

No assertion concerns general quadrilaterals, pooled-boundary independent samples, other densities, other dimensions, or the distribution of the hull's random area. Near-certain contours are circular only in affine coordinates. Unindexed equivalent literature and unexamined portions of less closely related sources remain originality risks. Independent review is needed before treating this as an externally certified new mathematical result.

Self-review: passed. Independent audit: not yet performed.
