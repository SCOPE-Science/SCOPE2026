# Review — Sharp shortest-edge volume profile for diameter-bounded simplices

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the geometry to a square projected-coordinate matrix. After placing the distinguished edge symmetrically, the simplex determinant is exactly the distinguished-edge length times the determinant of the transverse coordinate matrix.

The diameter constraints imply two families of transverse inequalities: each projected vertex has squared norm at most \(D^2-s^2/4\), and each projected pair is at distance at most \(D\). A positive weighted sum of the corresponding rank-one matrices has a trace bounded by these inequalities. Its coefficient matrix is a shifted complete-graph Laplacian whose determinant is explicit. The trace-determinant inequality then gives the displayed sharp determinant bound.

The equality conditions were checked in both directions. Equality in the weighted trace bound forces every projected norm and every projected pair distance to saturate. Saturation of the two endpoint constraints then puts every remaining vertex in the perpendicular bisector hyperplane and makes every nondistinguished edge have length \(D\). Conversely, the resulting Gram matrix
\[
G_0=\alpha I+\beta J
\]
is positive definite for \(0<s\le D\), so the equality simplex exists. Its Gram matrix is unique, giving uniqueness up to isometry. The paired coefficient matrix satisfies \(QG_0=\alpha(\alpha+m\beta)I\), verifying equality in the trace-determinant step.

The normalized shortest-edge profile recovers the regular simplex at \(\mu=1\), the planar isosceles-triangle formula at \(n=2\), and collapses linearly as \(\mu\downarrow0\). Differentiation confirms strict monotonicity, and solving the resulting quadratic in \(\mu^2\) gives the stated inverse profile.

## Originality

**PASS, to the best of our knowledge.**

The classical largest-small-polytope literature was checked through Graham, Kind--Kleinschmidt, and Fejes Toth's survey. Those sources establish the diameter-constrained extremal setting and, in particular, the regular simplex as the \(d+1\)-vertex optimizer, but the located statements do not prescribe a distinguished or shortest edge and do not give the profile proved here.

Recent simplex inequalities based on vertex and edge frames were checked. They include aggregate volume bounds in terms of the sum of squared edge lengths, but the located results do not state the sharp one-edge-conditioned envelope, its equality family, or the inverse shortest-edge law. Recent Cech-complex work was also checked because it explicitly studies simplices with short and long edges; its relevant calculations concern circumradii and related geometric parameters, not this volume optimization.

Searches under "largest small simplex", "maximum volume simplex with prescribed edge", "shortest edge simplex volume", "minimum edge simplex maximum volume", "edge ratio simplex volume", "one short edge simplex", and equivalent diameter terminology did not locate an exact match or a stronger theorem implying the full statement.

The principal residual originality risk is that the result is elementary enough to have appeared in older distance-geometry, determinant-inequality, or mesh-quality literature under different terminology. No specific inaccessible paper was identified as especially likely to contain the same theorem.

## Value

**PASS.**

The result refines the classical regular-simplex diameter extremum into a complete one-parameter sharp profile. It identifies the unique optimizer at every prescribed shortest-edge ratio, not merely near the regular case, and it inverts the profile to give a best-possible quantitative edge-regularity statement from volume alone.

The formula is directly applicable to geometric arguments where simplex quality is measured by the longest-to-shortest edge ratio, and to settings in which near-maximal volume must be converted into explicit control of every edge.

## Scientific limitations

- The theorem is Euclidean and simplex-specific.
- The stability output controls edge lengths, not Hausdorff, Banach-Mazur, altitude, inradius, or circumradius distances to the regular simplex.
- Only one prescribed edge is optimized explicitly; simultaneous constraints on several short edges are not treated.
- Originality is to the best of our knowledge, with residual risk of an equivalent older distance-geometry or folklore formulation.
