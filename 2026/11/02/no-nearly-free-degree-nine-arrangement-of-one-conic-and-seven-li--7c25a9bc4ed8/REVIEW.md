# Independent mathematical audit

## correctness

PASS

The degree-nine syzygy bounds force (4,5), hence τ=47. Subtracting the pair-intersection and Tjurina counts gives t+n₃=12 and n₂=6−s for s=7−t; Gałecka's inequality restricts s to 3–6. Independently enumerated pair-disjoint line triples first, then chose the unused secant pairs for conic triples with degree at most two. Replay: python3 /workspace/branches/independent-check-3.py; labelled counts 54,24,0,60, with orbit sizes (18,36),(24),(),(60). These are four orbits, not the incidental word ‘five’ in the frozen text; its listed sizes and geometry treat all four. For s=3 the two surviving lists force two diagonal secants of a circumscribed quadrilateral to intersect on the conic. In the normalization with tangent parameters 0,1,∞,x, the conic equation XZ−Y² at the three diagonal intersections is proportional respectively to x²(x−1)³, x³(x−1)², x³(x−1)³, all nonzero. For s=4 the inscribed vertices avoid the three tangencies, so the finite chord equations are legitimate; the remaining collinearity determinant is 4(2v−1)(v²−v+1), nonzero modulo the incidence condition v²−v−1=0. For s=6 the representative is a hexagon with alternate concurrences. The two chord involutions compose to a projectivity cycling three distinct points, hence of order three; normalizing it and either involution gives the alternating parametrization. The opposite chord intersections all satisfy X=ω² Z (their products are 1 and ω, and the corresponding chord sums differ by a factor ω²). This line meets Q at ±ω, so cannot be the last tangent. The search exhausts necessary combinatorial constraints only; the projective arguments exclude realization over ℂ. The frozen scripts were inspected but not executed.

## originality

PASS

A distinct later-indexed record does make the exact same nonexistence assertion; critically, its purported proof does not establish it. In its Hirzebruch step, the conic triples become ordinary double points after the conic is removed, so they must be included in t₂ for the line arrangement. With u triple points among the lines, the correct value is 21−3u, not 21−3u−v. The corrected inequality is 9u≤56, which admits the candidate u=5 and u=6, so its decisive contradiction disappears. Gałecka's earlier valid inequalities likewise do not exclude all cases. The supported distinct contribution here is a complete valid obstruction using actual incidence geometry, not the first appearance of the nonexistence wording or a priority claim.

## value

PASS

The one-conic case is the first nonlinear component composition in the expressly motivated degree-nine existence problem. Excluding the full composition over the complex numbers goes beyond a list of admissible singularity counts and requires actual realization obstructions. It does not rule out the other conic counts or higher singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
