# Independent mathematical audit

## correctness

PASS

For k-token C_n with uniform positive clockwise gap cap U, the lifted feasible coordinate set with all consecutive cyclic differences in [1,U] is closed under coordinatewise min/max. If k<n<kU and U>=2, an attempt to increase a maximal-deficit coordinate can be blocked only by a neighboring equal-deficit site across a gap saturated at 1 or U; any obstruction directed cycle forces every gap to equal 1 or U, contradicting strict slack. Hence ordered feasible lifts admit L1-length monotone interpolations. Every ambient cycle token path preserves cyclic token order, so replacing its lifted displacement by this admissible path proves isometry. Edge-flow conservation yields f_j=s_j-c; minimizing sum|f_j| over integers uses a median and is attainable by cutting at zero flow. For k=3 mutual visibility iff all gaps<=floor(n/2); the n=3 singleton case is handled separately. Saturated n=6,k=3,U=2 has two isolated vertices. Independent full-graph BFS compared 8983 ordered visible-pair distances through n=11 and the median formula.

## originality

PASS

Fresán-Figueroa, Goldfeder and Lozano-Piña (2026), Section 6, give the same cycle mutual-visibility gap criterion and token-layer connectivity. These are prior. The inspected proof does not give isometric inclusion or the exact pairwise ambient median-flow metric, nor the general gap cap U isometry theorem.

## value

PASS

Exact shortest permitted token-routing distances strengthen mere connectivity for a natural constrained reconfiguration graph, support optimal routing algorithms, and expose the strict-slack obstruction and difference between isometry and convexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
