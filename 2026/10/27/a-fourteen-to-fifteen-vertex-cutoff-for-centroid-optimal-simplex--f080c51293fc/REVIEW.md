# Independent mathematical audit

## correctness

PASS

A quotient right inverse lifts uniquely to an extension agreeing at every vertex by choosing the output representative that agrees at one fixed vertex. Each lifted evaluation has mass 1 and may have signed coefficients. On the equilateral vertices a zero-mass difference has norm equal to its positive mass: the vertex data 1 on positive coordinates, 0 on the rest attain it. For the unit-edge simplex, embed vertices as e_i/√2 up to isometry and translation; barycentric differences therefore have squared distance (k+l−2t)/(2kl). Averaging preserves the right inverse and cannot increase norms, and forces the full-centroid measure to be uniform. The vertex-to-full-centroid pair gives C_n=√(2(n−1)/n). At a seven-face the inside coefficient a is common; the two indicator tests give 1−a≤||E||√(3/7) and 7a−7/n≤||E||√((n−7)/(14n)), regardless of signs. Adding after dividing the second by 7 yields B_n. With y=√(1−7/n), B_n/C_n=√(6+y²)/(√6+y/7), greater than 1 exactly when y²>49/96, or n>672/47. This proves strict failure for all integers n≥15, without asserting the exact value there. For 3≤n≤14 I independently replayed the exact finite upper certificate with /workspace/branches/replay_simplex.py, taking the path to the frozen verify_barycentric.py as its argument. It parses only the literal weight data, does not execute the supplied checker, and constructs actual barycentric vectors and evaluation vectors on all stabilizer representatives, choosing the second subset by its counts inside and outside the first. The exact squared inequalities passed in all 1,489 unordered pair orbits, with exactly the 12 vertex–full-centroid equalities and strictly positive other slack (minimum 200006288271/1225000000000000). The intermediate-rank weights are strictly positive and normalized; the singleton weights are the required point masses. This proves the full-set upper bound, not just separate bounds at different ranks.

## originality

PASS

The supported contribution is the sharp all-face cutoff for a single common linear extension, not the older relative projection framework, edge-midpoint or fixed-k formulas, or the full-centroid bound in isolation. The strongest indexed overlap has exact fixed-k simultaneous interpolation, but that quantifier is over all faces of one rank; the mixed-rank inequalities are absent and explicitly excluded. No inspected more general theorem entails the frozen cutoff.

## value

PASS

The geometry and benchmark are canonical: compare a global interpolation on the full barycentric subdivision with the exactly forced cost for the full centroid alone. The first incompatibility is not visible from individual face ranks. The finite positive result certifies simultaneous compatibility through fourteen vertices, and the two explicit witnesses exclude it for every larger size, locating a mathematically meaningful first failure without an all-dimensional numerical sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
