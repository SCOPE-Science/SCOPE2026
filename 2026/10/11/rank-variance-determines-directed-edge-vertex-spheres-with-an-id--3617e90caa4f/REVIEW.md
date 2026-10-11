# Same-model review

## Correctness
PASS. The primary source gives both the rank hyperplane and the exact affine dimension for connected rank-function quivers. Their intersection identifies the affine hull. Orthogonal projection of the origin gives
\[
c=-\frac r{\|r\|^2},
\]
and every arrow root then has squared distance
\[
2-\frac1{\|r\|^2}.
\]
The minimum-enclosing part is separate: a common vertex sphere is optimal exactly when its center lies in the vertex convex hull. Writing that barycentric condition as a nonnegative flow and applying max-flow/min-cut gives precisely the lower-ideal centered-rank inequalities.

## Originality
PASS. The exact directed-edge-polytope source was inspected at the vertex, dimension, rank-hyperplane, and graded-poset results, including the relevant PDF page. It contains no “circumradius”, “sphere”, “Euclidean”, or “radius” occurrence. The semi-balanced root-polytope and toric directed-edge literatures were inspected as broader same-object coverage; neither states the metric theorem. Published-result searches covered circumsphere, rank-variance, minimum-enclosing-ball, Chebyshev-center, and lower-ideal formulations. The closest prior own result is an Ehrhart theorem for oriented cycle root polytopes and does not imply this metric statement.

## Value
PASS. Rank-function directed edge polytopes are the dimension-deficient class singled out by the recent complete face theory. The theorem turns their rank data into an exact Euclidean vertex sphere and gives a sharp combinatorial criterion for when that sphere is the actual minimum enclosing sphere. The lower-ideal/flow equivalence is structurally meaningful and distinguishes graded quivers with the same ambient root-vector norm but different enclosing-ball behavior.

## Closest literature and limitations
The closest sources determine affine structure, faces, triangulations, and toric properties. They do not normalize the Euclidean metric or decide minimum-enclosing optimality. The theorem is specific to the standard incidence-vector realization, and it does not give the smaller minimum-enclosing radius when the ideal condition fails. A residual risk remains for an equivalent incidence-configuration theorem under different terminology.

Same-model review: passed. Independent audit: not yet performed.
