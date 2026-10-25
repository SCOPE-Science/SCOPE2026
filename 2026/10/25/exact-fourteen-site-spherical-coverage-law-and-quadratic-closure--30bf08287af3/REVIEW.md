# Self-review

## Correctness — PASS

The support expression is exactly \(\max(\|u\|_\infty,\|u\|_1/\sqrt3)\) for the fourteen declared sites. The 48-chamber spherical Jacobian is \(dx\,d\phi\); the ordering constraint and diagonal-cap constraint yield the integral with its correct probability normalization. An exact convex-polytope extremal argument finds all 24 gap directions and the prior-known covering radius. Local piecewise-linear expansion, coercivity and rescaling prove the coefficient \(6/(\pi q^5r^2(1-r))\) without extrapolating finite tests. A direct nearest-site distance argument supplies the independent high-threshold cap branch. The standalone checker reproduces the published numerical near-covering benchmark and samples 262144 spherical directions independently of the chamber integral.

## Originality — PASS relative to the material inspected

Fowler–Tarnai–Gáspár (2002), the principal source, already provides the equal-circumradius compound and its covering threshold; neither fact is presented as new. Its inspected discussion of numerical intermediate coverages and the covering graphs does not derive the exact sublevel integral for the *fixed* fourteen-site arrangement or the sharp quadratic uncovered-area coefficient. Bürgisser–Cucker–Lotz (2007) analyzes randomly sampled sites rather than the fixed fourteen-site law, and the general spherical Voronoi abstract alone does not establish equivalence. Several semantically related published research summaries concern unrelated Euclidean covering, polyhedral shadow, or distance distributions, and do not imply the present angular distribution. Full historical priority cannot be guaranteed; the potentially relevant inaccessible complete Voronoi-algorithm source remains a residual risk.

## Mathematical value — PASS

The question of uncovered *area* below the critical cap radius is the natural quantitative refinement of the classical fixed configuration's covering threshold. The exact integral gives all radii, and the universal leading-order leakage profile explains how the 24 Voronoi gap vertices open into small uncovered patches. It independently reproduces the 2002 published numerical coverage benchmark and provides a reusable analytical constant for fixed-covering tolerance calculations. The result is a motivated exact distribution and sharp edge law, not a restatement of the known optimal radius.

## Literature and limits

Closest primary literature: Fowler–Tarnai–Gáspár (2002), DOI `10.1098/rspa.2002.0990`, the explicit original compound and numerical coverage data; Bürgisser–Cucker–Lotz (2007), arXiv:`0712.2816`, random rather than fixed site centers; Na–Lee–Cheong (2002), DOI `10.1016/S0925-7721(02)00077-9`, spherical Voronoi algorithms, abstract-level comparison only. Definitive historical priority and independent validation are not established.

Self-review: passed. Independent audit: not yet performed.
