# Independent mathematical audit

## correctness

PASS

The three incident faces have intrinsic shortest paths equal to Euclidean straight segments; a shortest route to the opposite face crosses some edge, and unfolding gives the minimum of distances from three reflected vertex images. Their Voronoi cells partition the opposite equilateral face into three congruent centroidal triangles, giving unique farthest point G at 2/sqrt(3). Polar integration of the three incident wedges and three opposite Voronoi wedges yields disk area pi*r²/2 for r<=1 and 3[r²(pi/6-acos(1/r))+sqrt(r²-1)] for 1<r<2/sqrt(3); divide by surface area sqrt(3). Differentiation gives perimeter r*(pi-6acos(1/r)). Independent sympy Puiseux expansion proved disk-area defect -4sqrt(2)(r-1)^(3/2)+O((r-1)^(5/2)), and independent partitioned numerical polar integrations matched at eight radii (including both endpoints) to <1e-10. The auxiliary checks confirm, not replace, exact unfolding and integration.

## originality

PASS

The accessible Fontenot et al. full paper develops nearest-path formulas and polyhedral unfoldings for tetrahedra and cubes, not the distribution of intrinsic distance from a fixed vertex to an area-uniform point, complete disk-area profile, level-set-length law or C1/non-C2 transition. Davis et al. treat geodesic trajectories, and Davis 2023 the cut locus; neither inspected statement explicitly integrates the radial area distribution.

## value

PASS

Vertex-centered metric balls are a natural and independently useful intrinsic metric-measure invariant of an elementary curved-by-cones surface. The complete probability/length law, exactly identified farthest point and fractional-power singularity sharpen pointwise geodesic formulas without claiming broader polyhedral classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
