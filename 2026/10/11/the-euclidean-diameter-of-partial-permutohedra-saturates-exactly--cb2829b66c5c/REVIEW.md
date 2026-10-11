# Same-model review

## Correctness
PASS. Euclidean diameter endpoints of a polytope are extreme. The published vertex theorem says that a vertex with \(k\) nonzero coordinates uses the prefix \(n,n-1,\ldots,n-k+1\). For each coordinate, \((u_i-v_i)^2\le\max\{u_i^2,v_i^2\}\), so any squared distance is bounded by the sum of the largest \(s=\min\{m,2n\}\) entries of two copies of \(n^2,(n-1)^2,\ldots,1\). Disjoint supports with balanced prefix lengths attain that bound. Equality is strict at any coordinate where both endpoints are positive, and the strict square ordering then forces exactly the stated prefix sizes and value sets.

## Originality
PASS. The primary full text was inspected at the definition, exact vertex theorem, anti-blocking realization, and its stated face/volume/Ehrhart program. The earlier full paper introducing partial permutohedra was also inspected. Neither contains a Euclidean-diameter theorem; targeted published-result, literature, and research-record searches covered partial permutations, parking functions, anti-blocking permutohedra, stellohedra, and both Euclidean- and graph-diameter terminology. No statement was located that implies the formula, equality classification, or \(m=2n\) saturation threshold.

## Value
PASS. The theorem computes a fundamental realization-sensitive metric invariant over the entire two-parameter partial-permutohedron family, not a fixed small example. It also classifies all extremal pairs and identifies a qualitative phase change: the Euclidean diameter becomes completely dimension-independent once two disjoint supports can each carry every allowed positive value. This complements existing face, volume, Ehrhart, and inradius information rather than repeating it.

## Closest literature and limitations
The closest papers determine the vertex/facet/face structure, volume, Ehrhart data, and anti-blocking realization. Existing inradius results for the same family optimize supporting-hyperplane clearances and do not imply a farthest-vertex-pair theorem; graph-diameter results for related polytopes concern a different metric. The theorem is specific to the standard coordinate realization and does not determine enclosing spheres, widths, or arbitrary generalized-permutohedron diameters.

Same-model review: passed. Independent audit: not yet performed.
