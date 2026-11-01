# Scientific review

## Correctness — PASS

The domain is a fixed embedded \(C^8\) strictly convex arclength curve with positive curvature. Compact embeddedness ensures every sufficiently short ambient chord is local and lets midpoint-arclength coordinates parametrize exactly two nearby endpoints. The Frenet-frame expansion, fifth-order inversion, periodic integration by parts, strict cubic extremum, and closed harmonic examples all have self-contained proofs in RESULT.md. The executable verifier checks the algebra, exact circle law, harmonic averages and eight separate direct numerical chord integrals. All essential nonstandard coefficients are derived, not inferred from fitting data. The error term is fixed-curve \(O_\Gamma(t^7)\); no uniform high-frequency estimate is claimed.

## Originality — PASS, provisional priority

Hein and Audibert (2005; DOI `10.1145/1102351.1102388`) studied kernel-weighted correlation integrals on embedded manifolds and explicitly obtained a second-order curvature correction. That gives prior coverage of the cubic \(t\)-term after dimensional rescaling. Its stated remainder does not supply the relative fourth-order coefficient, hence cannot yield the present fifth-order formula. Bäsel (2012; arXiv `1204.2707`) studies random-line chords and interior point distances in regular polygons, with a different boundary measure and nonsmooth domain. Lellouche and Souris (2019; DOI `10.3390/stats3010001`) give a general compact-set distance framework but no identified exact formula for the curvature-gradient term. The indexed near-zero polygon-boundary result concerns corner angles instead of curvature derivatives. This review has not established unconditional historical priority: higher-order manifold kernel asymptotics remain a residual risk.

## Mathematical value — PASS

The negative \(\int(\kappa')^2\) energy has a genuine geometric consequence. Although the circle minimizes the cubic correction, the fifth correction is not bounded from below at fixed perimeter, and an explicit family of smooth strictly convex closed curves crosses from larger-than-circle to smaller-than-circle exactly at harmonic frequency five. This separates curvature magnitude from curvature variation using a measurable chord-proximity statistic; it is not a known-circle recomputation or an arbitrary finite benchmark.

## Limitations

All results are asymptotic as the threshold tends to zero for each fixed curve. The sampling law is arclength-uniform and the metric is ambient Euclidean. The work does not identify an arbitrary shape from a finite number of coefficients, address noisy samples, or certify global novelty. Some primary manuscript sections were inaccessible, as specified in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
